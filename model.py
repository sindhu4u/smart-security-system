import os
import cv2
import torch
import numpy as np
import matplotlib.pyplot as plt
from torchvision import transforms
from transformers import AutoImageProcessor, AutoModelForImageClassification
from pathlib import Path
from collections import Counter

# Device configuration
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def get_transform(processor):
    return transforms.Compose([
        transforms.ToPILImage(),
        transforms.Resize((processor.size["height"], processor.size["width"])),
        transforms.CenterCrop((processor.crop_size["height"], processor.crop_size["width"])),
        transforms.ToTensor(),
        transforms.Normalize(mean=processor.image_mean, std=processor.image_std),
    ])

# Load trained DeiT model
def load_model(model_path: str, num_labels: int):
    model = AutoModelForImageClassification.from_pretrained(
        "facebook/deit-base-distilled-patch16-384",
        num_labels=num_labels,
        ignore_mismatched_sizes=True
    )
    state_dict = torch.load(model_path, map_location=device)
    model.load_state_dict(state_dict)
    model.to(device)
    model.eval()
    return model

def predict_image(model, image_path, transform):
    image = cv2.imread(image_path)
    if image is None:
        print("Failed to load image:", image_path)
        return None, None
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    tensor = transform(image_rgb).unsqueeze(0).to(device)
    with torch.no_grad():
        outputs = model(tensor).logits
        pred_class = outputs.argmax(dim=1).item()
    return pred_class, image_rgb

def predict_video(model, video_path, transform):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error opening video.")
        return None, None, []

    results = []
    display_frame = None
    frame_interval = 5
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_count += 1
        if frame_count % frame_interval != 0:
            continue

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        tensor = transform(frame_rgb).unsqueeze(0).to(device)
        with torch.no_grad():
            outputs = model(tensor).logits
            pred_class = outputs.argmax(dim=1).item()

        results.append(pred_class)

        if display_frame is None:
            display_frame = frame_rgb

    cap.release()

    if not results:
        return None, None, []

    # Detect consistent class appearance
    threshold = 5
    max_label = None
    max_count = 0
    current = results[0]
    count = 1

    for i in range(1, len(results)):
        if results[i] == current:
            count += 1
            if count >= threshold and count > max_count:
                max_label = current
                max_count = count
        else:
            current = results[i]
            count = 1

    if max_label is None:
        max_label = Counter(results).most_common(1)[0][0]

    return max_label, display_frame, results

# 🔸 New function: Just returns the predicted class
def predict_class(video_path: str):
    model_path = "rained_deit_distilled_best (1).pth"
    num_classes = 6  # Update based on your dataset

    processor = AutoImageProcessor.from_pretrained("facebook/deit-base-distilled-patch16-384")
    model = load_model(model_path, num_labels=num_classes)
    transform = get_transform(processor)

    final_pred, _, _ = predict_video(model, video_path, transform)
    return final_pred

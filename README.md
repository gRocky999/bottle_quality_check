# **_Bottle Quality Control using YOLOv8_**

This project uses a **YOLOv8 object detection model** to analyze video footage from a juice/bottle production line and classify the liquid levels in bottles as:
- **underfilled**
- **normal**
- **overfilled**

Optionally, it also detects:
- **cap damaged or missing**
- **label damage**

## **_Features_**

- Trained **YOLOv8n** model for efficient and accurate detection
- Video-based inference on `.avi` files
- Beautified bounding boxes and smart label placement using OpenCV
- Output video with annotated predictions


## **_How to Use_**

### _Google Colab_

1. Upload your `.avi` input video and your own trained weights file (e.g., `best.pt`)  
2. Open and run `inference.ipynb`  
3. The output video will be saved and automatically downloaded as `output.mp4`

> **Note:** The trained weights file (`best.pt`) is not included in this repository. You can train your own using the instructions below or download from your own training output.

## **_Training a YOLOv8 Model_**

```python
from ultralytics import YOLO

model = YOLO('yolov8n.pt')
model.train(data='data.yaml', epochs=50, imgsz=640, batch=16)
```

## **_Dataset_**

The dataset was annotated using **Roboflow** and includes the following classes:
- underfilled
- normal
- overfilled
- cap_damaged / cap_missing
- label_damaged

The dataset was exported in **YOLOv8 format** and referenced in `data/data.yaml`.

## **_Resources_**

- [YOLOv8 Documentation](https://docs.ultralytics.com/)
- [Roboflow](https://roboflow.com)

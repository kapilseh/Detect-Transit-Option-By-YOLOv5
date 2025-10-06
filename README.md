# Detect-Transit-Option-By-YOLOv5

Step1 - Prepare data (prepareData.ipynb)

Step2 - Train/detect using YOLO  (detect.ipynb)

**Outputs Metrics**
Precision (P) - of all the predicted boxes, how many are correct?

Recall (R)    - of all the actual objects, how many were detected?

mAP50         - mean Average Precision at IoU* threshold 0.50

mAP50-95      - averages precision across IoU thresholds from 0.50 to 0.95 in steps of 0.05 - a more rigorous metric

* Intersection over Union - Measures overlap between predicted and ground truth boxes.

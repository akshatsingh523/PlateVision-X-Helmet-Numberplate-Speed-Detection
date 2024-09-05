
---

# **Helmet-Numberplate-Speed Detection System**

## Project Overview

**Helmet-Numberplate-Speed Detection** is an advanced system designed to detect helmets, recognize vehicle number plates, and measure speed, ensuring traffic safety and law enforcement compliance. This system leverages state-of-the-art object detection models (YOLOv7, YOLOv8, and YOLOv9) and integrates the Deepsort algorithm for accurate speed detection. Tesseract OCR is used for number plate recognition, and the system's frontend and backend are built with HTML, CSS, and Django.

## Key Features

- **Helmet Detection**: Detects whether a rider is wearing a helmet using YOLOv7, YOLOv8, and YOLOv9.
- **Number Plate Recognition**: Employs Tesseract OCR to extract and recognize text from number plates for easy identification of vehicles.
- **Speed Detection**: Utilizes the Deepsort algorithm to accurately track and measure the speed of vehicles.
- **Frontend & Backend Development**: Designed with HTML and CSS for the frontend, while Django powers the backend for seamless performance and scalability.

## Performance Metrics

- **YOLOv7**:
  - Precision: 87%
  - Recall: 90.1%
  - mAP@50: 90.4%

These metrics showcase the system's effectiveness in detecting helmets, recognizing number plates, and tracking vehicle speeds with high accuracy.

## Technology Stack

- **YOLOv7, YOLOv8, YOLOv9**: Used for helmet and number plate detection.
- **Deepsort Algorithm**: Tracks vehicle movement and calculates speed.
- **Tesseract OCR**: Extracts and recognizes number plate text for vehicle identification.
- **Django**: Backend framework for server-side logic and database management.
- **HTML & CSS**: Frontend design for a user-friendly interface.

## Use Cases

- **Traffic Law Enforcement**: Automatically detect helmet usage, recognize number plates, and measure vehicle speeds for monitoring traffic violations.
- **Safety Compliance**: Ensure compliance with road safety rules by monitoring helmet use and speed limits.
- **Automated Surveillance**: Deploy in smart city surveillance systems for real-time traffic monitoring and enforcement.

---


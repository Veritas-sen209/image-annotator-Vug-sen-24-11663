# Image Annotator & Measurement Tool

Matric no: vug-sen-24-11663
name: NTAH CHIDERA ISAAC

## Course
SEN 281 – Computer Vision (Theory and Practical)

## Description
This project is a simple Windows desktop application that allows users to load images,
annotate them using shapes and text, measure distances, and save the annotated image.
It is designed to be lightweight, easy to use, and offline.

## Features
- Load image from computer
- Draw rectangle annotation
- Draw circle annotation
- Draw line and measure distance (pixel-based)
- Add text labels
- Save annotated image

## Tools and Technologies
- Python
- OpenCV (cv2)
- Tkinter
- NumPy
- Windows OS

## How to Run the Project
1. Install Python 3.10 or higher
2. Install required libraries:
   pip install opencv-python numpy
3. Run the application:
   python main.py

## Controls
- L → Line / Measure
- R → Rectangle
- C → Circle
- T → Text
- S → Save Image
- ESC → Exit

## Screenshots
All screenshots are available in the screenshots folder.

## Limitations
- Distance measurement is in pixels only
- No undo/redo feature
- Limited annotation tools

## Future Improvements
- Add real-world measurement calibration
- Add undo/redo functionality
- Add more annotation shapes

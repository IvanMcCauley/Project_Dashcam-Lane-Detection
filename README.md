# 🚗 Dashcam Lane Detection - Computer Vision for Autonomous Driving (Python + OpenCV)

A real-time lane detection system built using Python and OpenCV, designed to process my personal dashcam footage and overlay detected lane lines on the road. This project replicates core visual perception logic used in autonomous vehicles.

---

## 🎯 Project Motivation

Autonomous vehicles rely heavily on robust lane detection as part of their perception stack. As a Mechatronic Engineering graduate passionate about self-driving tech, I built this project to:

- Demonstrate computer vision skills for AV perception
- Build a clean, realistic implementation suitable for GitHub/portfolio
- Prepare for roles in ADAS/autonomy at companies like BMW, Waymo, Mobileye, etc.
- Most importantly - to learn as much as I can

---

## ✨ Key Features

- Canny edge detection and Gaussian blur preprocessing  
- Region of Interest (ROI) masking to focus on the drivable lane  
- Probabilistic Hough Line Transform for robust line detection  
- Automatic separation of left/right lane candidates by slope  
- Least-squares line fitting with color-coded overlay  
- Semi-transparent lane fill polygon for clear visualization  
- Real-time video processing with frame-by-frame output  
- Modular, clean Python code ready for extension

---

## 🛠️ How It Works

1. **Video Input**  
   Load dashcam footage using `cv2.VideoCapture`.
   ![image](https://github.com/user-attachments/assets/5a602e42-a657-408f-9447-d0eac736162d)

3. **Preprocessing**  
   Convert to grayscale → blur → edge detect using Canny.
   ![image](https://github.com/user-attachments/assets/34c6b3f5-4297-4ba0-9fb4-d48c47707c07)


5. **Apply Region of Interest**  
   Use a trapezoidal mask to isolate the road region.
![image](https://github.com/user-attachments/assets/1e105ad3-8a72-4554-a36a-5371b49a3b86) 

6. **Detect Lines**  
   Run `cv2.HoughLinesP` to extract line segments.
![image](https://github.com/user-attachments/assets/2cb4cf1f-30e3-4731-b1d9-7f2d3c6ea933)


7. **Classify Lines**  
   Separate segments by slope into left/right categories.
![image](https://github.com/user-attachments/assets/5a21f7d9-dcd1-4405-b7dc-403094d011a2)


8. **Line Fitting**  
   Use `np.polyfit` to fit a clean single line to each side.
![image](https://github.com/user-attachments/assets/31e659f4-b0c2-4532-8082-83e4f260e2f6)

9. **Draw Overlay**  
   - Draw left (yellow) and right (green) lines  
   - Fill polygon between them using `cv2.fillPoly`  
   - Blend with alpha transparency
![image](https://github.com/user-attachments/assets/34bfbc4f-458d-425a-83c6-e5571e8e825d)

---

## 📷 Demo

### 🎞️ Input Clip (Dashcam Footage)
*Add input video*


### 🧠 Lane Detection Output
*Add output video*

---

## 🖥️ Source Code
## 📂 Source Code

| File | Description |
|------|-------------|
| [`main.py`](main.py) | Main entry point — loads video, runs frame-by-frame lane detection, saves output |
| [`lane_detector.py`](lane_detector.py) | Core logic for detecting lanes, classifying line segments, and rendering overlays |
| [utils.py`](utils.py) | Helper functions for masking the region of interest and (optional) line drawing |
| [`test_video.py`](test_video.py) | Lightweight debugging script for testing raw video playback without processing |




### 🚀 Example Usage
If you want to try the program yourself:
- Clone the files above and place them according to the following structure:
```
lane_detection_dashcam/
├── data/
│   └── raw/
│       └── lane_test_clip.mp4       # Input video file
├── output/
│   └── processed_video.mp4          # Output video (this auto-saved when the program runs, you don't need to put this in manually)
├── src/
│   ├── main.py                      # Main runner
│   ├── lane_detector.py             # Detection logic
│   └── utils.py                     # Region of Interest, helpers
└── test_video.py                    # Quick video viewer (initial test)
```
- Install the required Python libraries by opening a terminal and running:
```
pip install opencv-python numpy
```
Run the lane detection pipeline with:
```
python -m src.main
```
This will:
- Load your input dashcam video from data/raw/lane_test_clip.mp4
- Process each frame to detect and overlay lane lines
- Fill the drivable area with a transparent color
- Save the final result to output/processed_video.mp4
- Show a real-time preview window (press q to exit)

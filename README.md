# 🚗 Dashcam Lane Detection - Computer Vision for Autonomous Driving (Python + OpenCV)

A real-time lane detection system that I built using Python and OpenCV, designed to process my personal dashcam footage and overlay detected lane lines on the road. This project replicates core visual perception logic used in autonomous vehicles.

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

<table>
<tr>
  <td><strong>1. Video Input</strong><br>Load dashcam footage using <code>cv2.VideoCapture</code>.<br>
    <img src="https://github.com/user-attachments/assets/5a602e42-a657-408f-9447-d0eac736162d" width="250">
  </td>
  <td><strong>2. Preprocessing</strong><br>Convert to grayscale → blur → edge detect using Canny.<br>
    <img src="https://github.com/user-attachments/assets/34c6b3f5-4297-4ba0-9fb4-d48c47707c07" width="250">
  </td>
  <td><strong>3. Apply ROI</strong><br>Use a trapezoidal mask to isolate the road.<br>
    <img src="https://github.com/user-attachments/assets/1e105ad3-8a72-4554-a36a-5371b49a3b86" width="250">
  </td>
</tr>
<tr>
  <td><strong>4. Detect Lines</strong><br>Run <code>cv2.HoughLinesP</code> to extract segments.<br>
    <img src="https://github.com/user-attachments/assets/f7c1aaa7-59e0-48a5-8ef6-9613ad166947" width="250">
  </td>
  <td><strong>5. Classify Lines</strong><br>Split into left/right lines based on slope.<br>
    <img src="https://github.com/user-attachments/assets/5a21f7d9-dcd1-4405-b7dc-403094d011a2" width="250">
  </td>
  <td><strong>6. Line Fitting</strong><br>Use <code>np.polyfit</code> to fit straight lines.<br>
    <img src="https://github.com/user-attachments/assets/31e659f4-b0c2-4532-8082-83e4f260e2f6" width="250">
  </td>
</tr>
<tr>
  <td colspan="3"><strong>7. Draw Overlay</strong><br>Final step: Format lane line colour and fill lane area using <code>cv2.fillPoly</code> and alpha blending.<br>
    <img src="https://github.com/user-attachments/assets/34bfbc4f-458d-425a-83c6-e5571e8e825d" width="700">
  </td>
</tr>
</table>



---

## 📷 Demo

### Input Clip (Dashcam Footage)
[Click here to see the input dashcam clip](https://drive.google.com/file/d/1ibkRtDaTSSNpaCJ08TMMahfGAoRvLXVw/view?usp=sharing)


### Lane Detection Output
[Click here to see the result](https://drive.google.com/file/d/1GWE1YMmQjrz3NEOppxTaMh8bqTneD93G/view?usp=sharing)

---

## 📂 Source Files

| File | Description |
|------|-------------|
| [`main.py`](main.py) | Main entry point - loads video, runs frame-by-frame lane detection, saves output |
| [`lane_detector.py`](lane_detector.py) | Core logic for detecting lanes, classifying line segments, and rendering overlays |
| ['utils.py`](utils.py) | Helper functions for masking the region of interest and line drawing |
| [`test_video.py`](test_video.py) | Lightweight debugging script for testing raw video playback without processing |
| [`lane_test_clip`](https://drive.google.com/file/d/1ibkRtDaTSSNpaCJ08TMMahfGAoRvLXVw/view?usp=sharing) | Input dashcam video file (google drive link - download) |
| [`requirements.txt`](requirements.txt) | List of required Python libraries for quick setup |



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
├── requirements.txt                 # Lists Python libraries needed to run the project
└── test_video.py                    # Quick video viewer (initial test)
```
- Install the required Python libraries by opening a terminal and running:
```
pip install -r requirements.txt

```
Run the lane detection pipeline with:
```
python -m src.main
```
This will:
- Load the input dashcam video from data/raw/lane_test_clip.mp4
- Process each frame to detect and overlay lane lines
- Fill the drivable area with a transparent color
- Save the final result to output/processed_video.mp4
- Show a real-time preview window (press q to exit)


---

## 📚 What I Learned

- How to build a real-time lane detection pipeline from scratch
- Practical experience tuning Hough Transform and ROI masks
- Clean modular coding with NumPy + OpenCV
- Debugging common CV pipeline issues (e.g., jitter, over-detection)
- Importance of parameter tuning, masking, and visualization in AV pipelines
- *...and most importantly, patience*

  ---

## 🔭 Next Steps / Possible Improvements

- Add curve handling with polynomial fitting (for winding roads)
- Temporal smoothing across frames to reduce jitter
- Extend to multi-lane roads and markings
- Export path trajectory coordinates for downstream use (trajecory planning, control etc)


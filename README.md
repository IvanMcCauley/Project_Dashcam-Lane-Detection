# 🚗 Dashcam Lane Detection - Computer Vision for Autonomous Driving

This is a personal side project focused on building a basic perception pipeline for autonomous vehicles. The goal is to detect lane lines and overlay projected paths on dashcam video footage using Python and OpenCV.

---

## 🎯 Project Goal

The purpose of this project is to:

- Build a real-time computer vision pipeline for lane detection using dashcam footage
- Understand and apply fundamental techniques like edge detection, masking, and line detection
- Develop hands-on experience with OpenCV and video processing
- Demonstrate relevant skills for autonomous driving roles at companies like BMW, CARIAD, ZF, and Aptiv

---

## 🛠️ Current Progress (08 June 2025)

✅ Went for an early morning drive for minimal traffic and recorded dashcam footage  
✅ Trimmed raw video to usable clip  
✅ Set up folder structure for code and data  
✅ Installed Python + OpenCV + NumPy  
✅ Ran first Python test script to confirm video can load with OpenCV  

🔜 Next step: Implement basic Canny edge detection + region of interest masking

---

## 🗂️ Planned Folder Structure
lane-detection-dashcam/ - Root project folder

data/ - Contains all project data

raw/ - Holds the raw dashcam .mp4 footage

output/ - Folder where processed video clips will be saved

src/ - Source code files for the lane detection pipeline (e.g. main.py, lane_detector.py, utils.py)

test_video.py - A simple test script to verify video playback using OpenCV


- ## 🧠 Learning Focus

This project is being built incrementally with the intention of fully understanding each part of the pipeline. I will be documenting and revisiting areas like:

- Canny edge detection parameters
- Region masking logic
- Hough Transform tuning
- Polynomial curve fitting for curved lanes
- Path overlay visualization

- ## 🧾 License

This is an open personal learning project. You're welcome to reference or adapt it, but please build your own understanding - just like I am.

# 📝 TODO — Lane Detection Dashcam Project

This file tracks planned features, progress, and milestones as I build a real-time lane detection system from dashcam footage using Python and OpenCV.

---

## ✅ Setup & Preparation

- [x] Record dashcam video using
- [x] Trim video to ~50 sec clip and store in `data/raw/`
- [x] Create project folder structure
- [x] Install Python, OpenCV, NumPy
- [x] Run basic script (`test_video.py`) to verify video loads

---

## 🚧 In Progress

- [ ] Implement Canny edge detection
- [ ] Apply region of interest (ROI) masking
- [ ] Use Hough Transform to detect line segments
- [ ] Overlay detected lines on video frames
- [ ] Save processed output to `output/processed_video.mp4`

---

## 🔮 Planned Enhancements

- [ ] Classify left and right lane lines
- [ ] Smooth/average lane lines across frames
- [ ] Fit polynomial curves to curved lanes
- [ ] Project driving path between lane boundaries
- [ ] Add transparency mask to visualize lane region
- [ ] Create `demo.mp4` for GitHub preview

---

## 🧠 Learning Focus

- Understand edge detection and tuning Canny thresholds
- Practice defining effective ROI for camera perspective
- Learn how Hough Transform parameters affect detection
- Explore curve fitting and path prediction logic

---

## 📦 Final Deliverables

- [ ] Clean, modular codebase (`main.py`, `lane_detector.py`, `utils.py`)
- [ ] Requirements file for dependencies
- [ ] Video demo (.mp4 or .gif) in `/output`
- [ ] Well-written `README.md` with visuals
- [ ] Optional `notebooks/` folder for experiments

---

*Last updated: June 2025*

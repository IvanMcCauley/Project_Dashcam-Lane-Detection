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

## 🚧Step 2

- [x] Implement Canny edge detection
- [x] Apply region of interest (ROI) masking
- [x] Use Hough Transform to detect line segments
- [x] Overlay detected lines on video frames
- [x] Save processed output to `output/processed_video.mp4`

## Next Steps
- [ ] Filter out short or horizontal lines (bottom-edge false positives)
- [ ] Separate left and right lane lines using slope and position
- [ ] Average lane lines for smoother tracking
- [ ] Extrapolate lines to extend full lane boundaries
- [ ] Start working on path prediction overlay (optional)


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

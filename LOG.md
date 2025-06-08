## ✅ June 8, 2025 — Step 2 Complete

- Implemented Canny edge detection after blurring grayscale frames
- Applied region of interest (ROI) masking to focus on road lanes
- Detected lines using Hough Transform
- Drew line overlays on original video
- Saved results to `output/processed_video.mp4`
![image](https://github.com/user-attachments/assets/83a67911-b16c-4344-9427-f162cb612284)
**Current Issues:**
- Only detects part of the lane (sometimes left only)
- Bottom of the frame (edge of ROI) is mistakenly detected as a strong line

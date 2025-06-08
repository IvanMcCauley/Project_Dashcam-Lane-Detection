# Dashcam Lane Detection Build Log

## ✅ 09:30 June 8, 2025 
- Recorded dashcam video during early morning hours for minimal traffic
- Trimmed to 51 second clip
- Set up basic folder structure
- Installed OpenCV + NumPy
- Planning next step: write minimal script to play back video


## ✅ 14:00 June 8, 2025 — Step 2 Complete
- Implemented Canny edge detection after blurring grayscale frames
- Applied region of interest (ROI) masking to focus on road lanes
- Detected lines using Hough Transform
- Drew line overlays on original video
- Saved results to `output/processed_video.mp4`
![image](https://github.com/user-attachments/assets/83a67911-b16c-4344-9427-f162cb612284)
**Current Issues:**
- Only detects part of the lane (sometimes left only)
- Bottom of the frame (edge of ROI) is mistakenly detected as a strong line
  

## ✅ 15:20 June 8, 2025 — Debugging Truncated Lane Lines
- Issue: Detected lane lines were short and jittery — they barely extended upward, making the output look poor and incomplete.
  ![image](https://github.com/user-attachments/assets/6672ff3a-cb37-409c-9c60-45c0ef4e24f2)
- Investigation: Suspected Hough parameters at first (minLineLength, maxLineGap), but they weren’t the actual cause. Realized the issue was in the line drawing logic.
- Root Cause: In the _fit_line() method, the top y-coordinate y2 was hardcoded as int(y1 * 0.45), which limited how far the line could stretch upward in the frame.
- Fix: Replaced the line with y2 = int(frame.shape[0] * 0.45) so the line could reach up to a more realistic vanishing point.
- Result: Lines now extend much further up the road, improving realism and visual quality. This change made a major difference in the clarity and usefulness of the lane visualization.
  ![image](https://github.com/user-attachments/assets/abd80046-8797-41c5-b956-9da945d9eefd)

  
## ✅ 21:45 June 8, 2025 — Lane Stability + Visual Enhancements
- Cleaned up unnecessary code (removed smoothing, averaging) to simplify final structure
- Improved overall visual clarity:
- Left lane now colored yellow
- Right lane colored green
- Polygonal lane fill added with semi-transparent overlay to highlight drivable path
- ROI outline was commented out to reduce clutter in final video output
- Settled on using a single fitted line per side after testing multi-segment and full-segment draw modes
- Lines are now smooth, consistently track the road ahead, and remain stable across most frames

### What’s next:
- Consider minor fine-tuning of ROI shape or thresholds if needed
- Begin writing project README.md and prepping final demo video for GitHub






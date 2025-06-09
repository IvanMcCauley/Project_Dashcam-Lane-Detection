import cv2
import numpy as np
from src.utils import region_of_interest

class LaneDetector:
    def process(self, frame):
        # Convert to grayscale for simplicity
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Blur helps reduce noise and small details
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        # Detect edges using Canny
        edges = cv2.Canny(blur, 50, 150)
        # Apply trapezoidal mask to focus on road/lane area
        roi = region_of_interest(edges)
        # Detect line segments using probabilistic Hough Transform
        lines = cv2.HoughLinesP(
            roi, 1, np.pi / 180,
            threshold=30,
            minLineLength=10,
            maxLineGap=200
        )

        # Separate line points into left and right based on slope
        left_pts, right_pts = [], []
        if lines is not None:
            for line in lines:
                for x1, y1, x2, y2 in line:
                    if x2 == x1:
                        continue  # vertical line, skip
                    slope = (y2 - y1) / (x2 - x1)
                    if not (0.4 <= abs(slope) <= 1.2):
                        continue  # ignore too flat or too steep
                    # Sort into left or right side
                    if slope < 0:
                        left_pts.extend([(x1, y1), (x2, y2)])
                    else:
                        right_pts.extend([(x1, y1), (x2, y2)])

        def fit_line(points):
            # Return None if not enough points
            if len(points) < 2:
                return None
            x, y = zip(*points)
            slope, intercept = np.polyfit(x, y, 1)
            y1 = frame.shape[0]              # bottom of frame
            y2 = int(y1 * 0.45)              # approx. middle height
            x1 = int((y1 - intercept) / slope)
            x2 = int((y2 - intercept) / slope)
            return (x1, y1), (x2, y2)

        # Fit lines for each side
        left_line = fit_line(left_pts)
        right_line = fit_line(right_pts)

        # Draw left and right lines
        if left_line:
            cv2.line(frame, left_line[0], left_line[1], (0, 200, 255), 6)
        if right_line:
            cv2.line(frame, right_line[0], right_line[1], (0, 255, 0), 6)

        # If both lines are found, draw a filled polygon between them
        if left_line and right_line:
            polygon = np.array([[left_line[0], left_line[1], right_line[1], right_line[0]]], dtype=np.int32)
            overlay = frame.copy()
            cv2.fillPoly(overlay, [polygon], (0, 255, 0))  # fill with green
            # Blend it onto the original frame with transparency
            cv2.addWeighted(overlay, 0.3, frame, 0.7, 0, frame)

        return frame

from src.lane_detector import LaneDetector
import cv2
import os

# Paths to input and output video files
VIDEO_PATH = 'data/raw/lane_test_clip.mp4'
OUTPUT_PATH = 'output/processed_video.mp4'

def main():
    print("Starting Lane Detection Pipeline")

    # Check if video file exists
    if not os.path.exists(VIDEO_PATH):
        print(f"Video file not found at: {VIDEO_PATH}")
        return
    
    # Load video file
    cap = cv2.VideoCapture(VIDEO_PATH)
    if not cap.isOpened():
        print("Failed to load video.")
        return
    print("Video opened successfully.")

    detector = LaneDetector() # Initialize my lane detector class
    out = None # This will hold the output video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Code for .mp4 format

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break # No more frames left
        
        # Run lane detection on current frame
        processed = detector.process(frame)

        # Initialize output writer once we know the frame size
        if out is None:
            h, w = processed.shape[:2]
            out = cv2.VideoWriter(OUTPUT_PATH, fourcc, 20.0, (w, h))

        out.write(processed) # Save processed frame to output
        cv2.imshow('Lane Detection', processed) #Show live preview

        # Press 'q' to stop video early
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    # Clean up everything
    cap.release()
    if out: out.release()
    cv2.destroyAllWindows()
    print(f"Done. Output saved to: {OUTPUT_PATH}")

if __name__ == "__main__":
    main()

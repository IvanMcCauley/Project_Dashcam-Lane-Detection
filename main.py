from src.lane_detector import LaneDetector
import cv2
import os

VIDEO_PATH = 'data/raw/lane_test_clip.mp4'
OUTPUT_PATH = 'output/processed_video.mp4'

def main():
    print("Starting Lane Detection Pipeline")

    if not os.path.exists(VIDEO_PATH):
        print(f"Video file not found at: {VIDEO_PATH}")
        return

    cap = cv2.VideoCapture(VIDEO_PATH)
    if not cap.isOpened():
        print("Failed to load video.")
        return
    print("Video opened successfully.")

    detector = LaneDetector()
    out = None
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        processed = detector.process(frame)

        if out is None:
            h, w = processed.shape[:2]
            out = cv2.VideoWriter(OUTPUT_PATH, fourcc, 20.0, (w, h))

        out.write(processed)
        cv2.imshow('Lane Detection', processed)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    if out: out.release()
    cv2.destroyAllWindows()
    print(f"Done. Output saved to: {OUTPUT_PATH}")

if __name__ == "__main__":
    main()

import cv2
import os

VIDEO_PATH = 'data/raw/lane_test_clip.mp4'
absolute_path = os.path.abspath(VIDEO_PATH)
print(f"Looking for video at: {absolute_path}")
print(f"File exists? {os.path.isfile(absolute_path)}")

cap = cv2.VideoCapture(VIDEO_PATH)
if not cap.isOpened():
    print("Could not open video. Check the file path and file type.")
else:
    print("Video opened successfully!")

while True:
    ret, frame = cap.read()
    if not ret:
        print(" No more frames or video ended.")
        break

    cv2.imshow('Test Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

import cv2

for i in range(4):
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f"✅ Webcam index {i} is working!")
        ret, frame = cap.read()
        if ret:
            print("✅ Frame read successfully.")
            cv2.imwrite("test_image.jpg", frame)
        else:
            print("❌ Failed to read frame.")
        cap.release()
        break
    else:
        print(f"❌ Webcam index {i} not available.")

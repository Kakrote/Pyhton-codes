import cv2

def main():
    # Create a VideoCapture object
    cap = cv2.VideoCapture(0)  # 0 for the default camera, you can change it if you have multiple cameras

    if not cap.isOpened():
        print("Error: Couldn't access the camera.")
        return

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the resulting frame
        cv2.imshow('Camera', frame)

        # Press 'q' to close the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the VideoCapture object and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    main()

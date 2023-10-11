import cv2
import os
import time

IMAGE_FILE_PATH = os.path.join("Capture", "BoardPictures")

# Create directory to save pictures if it doesn't exist
if not os.path.exists(IMAGE_FILE_PATH):
    os.makedirs(IMAGE_FILE_PATH)

# Start the video capture
vid = cv2.VideoCapture(1)  # ID 1 assumes a second camera (like your Orbbec Astra). Use 0 for default camera

is_automatic = False

try:
    while True:
        ret, frame = vid.read()
        if not ret:
            print("Failed to grab frame")
            break
        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1)
        if key == ord("c") or is_automatic:
            timestamp = time.time()
            filename = os.path.join(IMAGE_FILE_PATH, f"Picture_{timestamp}.png")
            cv2.imwrite(filename, frame)
            if not is_automatic:
                print(f"Saved: {filename}")

            #I'm nearly out of storage space so this will have to save me...
            time.sleep(0.5)
            
        # Switch to automatic mode
        if key == ord("a"):
            is_automatic = not is_automatic
            if is_automatic:
                print("Automatic capture mode enabled")
            else:
                print("Manual capture mode enabled")
            
        # Quit on 'q' key press
        if key == ord("q"):
            break
            
finally:
    vid.release()
    cv2.destroyAllWindows()

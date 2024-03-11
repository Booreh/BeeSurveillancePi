import cv2
import os
from datetime import datetime
from domain.image import Image
import time

class Webcam:
    def __init__(self, device_id=0):
        self.device_id = device_id
        self.capture = cv2.VideoCapture(self.device_id)
        if not self.capture.isOpened():
            raise ValueError("Unable to connect to webcam. Please check the device ID.")

    def capture_image(self, folder_path):
        ret, frame = self.capture.read()
        if ret:

            os.makedirs(folder_path, exist_ok=True)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

            file_name = f"image_{timestamp}.jpg"
            

            file_path = os.path.join(folder_path, file_name)
            
            
            time.sleep(1)

            cv2.imwrite(file_path, frame)
            print(f"Image captured and saved as {file_name}")
            return Image(file_path)
        else:
            print("Failed to capture image.")

    def release(self):
        self.capture.release()

if __name__ == "__main__":
    # Example usage
    webcam = Webcam()
    webcam.capture_image("image.jpg")
    webcam.release()

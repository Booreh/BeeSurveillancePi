import cv2
import os
from datetime import datetime
from domain.image import Image

class Webcam:
    def __init__(self, camera_id):
        self.camera_id = camera_id
        self.capture = cv2.VideoCapture(self.camera_id)
        if not self.capture.isOpened():
            raise ValueError("Unable to connect to webcam. Please check the camera ID.")

    def capture_image(self, folder_path, width, height, rotation):
        
        ret, frame = self.capture.read()
        if ret:

            os.makedirs(folder_path, exist_ok=True)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

            file_name = f"image_{timestamp}.jpg"
            file_path = os.path.join(folder_path, file_name)
            
            captured_image = Image(frame)
            resized_image = captured_image.resize(width, height)
            rotated_image = resized_image.rotate(rotation)

            rotated_image.save(file_path)
            print(f"Image captured and saved as {file_name}")

            return rotated_image
        else:
            print("Failed to capture image.")

    def release(self):
        self.capture.release()



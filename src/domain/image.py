import cv2

class Image:
    def __init__(self, image_data):
        self.image_data = image_data
        self.file_path = None
        

    
    def resize(self, width, height):
        resized_img = cv2.resize(self.image_data, (width, height))
        return Image(resized_img)

    def rotate(self, angle):
        if angle == 0:
            return self
        rotated_img = cv2.rotate(self.image_data, angle)
        return Image(rotated_img)
    
    def save(self, file_path):
        cv2.imwrite(file_path, self.image_data)
        self.file_path = file_path

    def getFilePath(self):
        return self.file_path
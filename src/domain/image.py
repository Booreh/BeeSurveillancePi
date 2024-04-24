import cv2

class Image:
    def __init__(self, image_data):
        self.image_data = image_data
        

    
    def resize(self, width, height):
        resized_img = cv2.resize(self.image_data, (width, height))
        return Image(resized_img)

    def rotate(self, angle):
        if angle == 0:
            return self
        rotated_img = cv2.rotate(self.image_data, angle)
        return Image(rotated_img)
    
    def zoom(self, scale):
        if scale == 0:
            return self

        height, width, _ = self.image_data.shape

        new_width = int(width / scale)
        new_height = int(height / scale)

        crop_x = (width - new_width) // 2
        crop_y = (height - new_height) // 2

        crop_x = max(0, crop_x)
        crop_y = max(0, crop_y)

        cropped_img = self.image_data[crop_y:crop_y + new_height, crop_x:crop_x + new_width]
        zoomed_img = cv2.resize(cropped_img, (width, height))

        return Image(zoomed_img)
    
    def save(self, file_path):
        cv2.imwrite(file_path, self.image_data)
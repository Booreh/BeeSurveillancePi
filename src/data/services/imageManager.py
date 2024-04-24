import os

class ImageManager:
    def __init__(self, image_folder):
        self.image_folder = image_folder



    def countImages(self):
        if os.path.exists(self.image_folder):
            return len(os.listdir(self.image_folder))
        else:
            return 0
        
    
    
    def deleteExcessImages(self, num_to_delete):
        images = os.listdir(self.image_folder)
        if len(images) < num_to_delete:
            print("Number of images to delete exceeds total number of images.")
            return
        
        for i in range(num_to_delete):
            os.remove(os.path.join(self.image_folder, images[i]))

        print(f"{num_to_delete} images deleted.")

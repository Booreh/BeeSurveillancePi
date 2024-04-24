from presentation.console import Console
from data.camera import Webcam
from data.api_client import APIClient
from data.services.setupProcedure import SetupProcedure
from data.services.imageManager import ImageManager
import time
import cv2

image_folder = "images"
api_client = APIClient(base_url="http://example.com/api")
console = Console("Main Console")
setupProcedure = SetupProcedure()
imageManager = ImageManager(image_folder)




def main():
    console.printWelcomeMessage()
    
    start = console.inputStartProcess()
    if start.lower() == 'y':
        console.runningSetupProcedures()

        if setupProcedure.runAllSetupProcedures():
            webcam = Webcam(setupProcedure.getDeviceData()["camera_id"])
            
            try:
                while True:
                    console.statusRunning()  
                    webcam.capture_image(image_folder, 1280, 720, 0, 0)
                    
                    imagecount = imageManager.countImages()
                    if imagecount >= 10:
                        imageManager.deleteExcessImages(10)
            
                    time.sleep(3600)  #interval pr.photo
            except KeyboardInterrupt:
                #  handle Ctrl+C (KeyboardInterrupt)
                webcam.release()
        else: 
            console.errorSetupFailed()
            
    else:
        console.statusExiting()
        

if __name__ == "__main__":
    main()



#api_client.upload_image(image_path)
    
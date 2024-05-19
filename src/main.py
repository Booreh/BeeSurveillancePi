from presentation.console import Console
from data.camera import Webcam
from data.api_client import APIClient
from data.services.setupProcedure import SetupProcedure
from data.services.imageManager import ImageManager
import time

image_folder = "images"
console = Console("Main Console")
setupProcedure = SetupProcedure()
imageManager = ImageManager(image_folder)
api = APIClient("http://158.39.162.139:8006")



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
                    image_capture = webcam.capture_image(image_folder, 1280, 720, 0)
                    current_image = image_capture.getFilePath()
                    api.upload_image(setupProcedure.getUserData()["user_id"], setupProcedure.getDeviceData()["device_id"], current_image)

                    imagecount = imageManager.countImages()
                    if imagecount >= 50:
                        imageManager.deleteExcessImages(50)


                    setupProcedure.shutDownSchedule()
                    time.sleep(720)  
            except KeyboardInterrupt:
                webcam.release()
        else: 
            console.errorSetupFailed()
            
    else:
        console.statusExiting()
        

if __name__ == "__main__":
    main()

    
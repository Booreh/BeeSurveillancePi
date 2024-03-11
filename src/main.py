from presentation.console import Console
from data.camera import Webcam
from data.api_client import APIClient
from data.services.setupProcedure import SetupProcedure
import time

webcam = Webcam()
api_client = APIClient(base_url="http://example.com/api")
console = Console("Main Console")
setupProcedure = SetupProcedure(0)

def main():
    console.printWelcomeMessage()
    
    start = console.inputStartProcess()
    if start.lower() == 'y':
        console.runningSetupProcedures()

        if setupProcedure.runAllSetupProcedures():
            
            try:
                while True:
                    console.statusRunning()
                    image_path = "images"  
                    webcam.capture_image(image_path)
                    
                    
            
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
    
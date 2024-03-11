import subprocess
import cv2
class SetupProcedure:
    def __init__(self, device_id):
        self.device_id = device_id



    def checkCameraConnection(self):
        
        try:
            capture = cv2.VideoCapture(self.device_id)
            if not capture.isOpened():
                print(f"Unable to connect to camera ({self.device_id}). Please check the device for issues.")
                return False
            else:
                print("Camera Found")
                capture.release()
                return True
        except Exception as e:
            # Handling for any exceptions (e.g., OpenCV errors)
            print(f"Error while checking camera connection: {e}")
            return False


    #Run IDE as admin, may also need to turn of firewall
    def checkInternetAccess(self):
        try:
            subprocess.check_output(["ping", "-c", "1", "8.8.8.8"])
            return True
        except subprocess.CalledProcessError:
            print("No internet access!")
            return False
    
    

    def checkServerConnection(self):
        return True
    


    def runAllSetupProcedures(self):
        """
        Runs all setup procedures.
        
        Returns:
            bool: True if all setup procedures succeed, False otherwise.
        """
        camera_connected = self.checkCameraConnection()
        internet_access = self.checkInternetAccess()
        # Add more setup procedures here
        
        # Return True if all setup procedures succeed, False otherwise
        return camera_connected and internet_access

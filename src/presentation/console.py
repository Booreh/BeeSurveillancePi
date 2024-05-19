
class Console:
    def __init__(self, name):
        self.name = name


    def printWelcomeMessage(self):
        print(f"RPi Bee Surveilance System - {self.name}")

    def inputStartProcess(self):
        return input("Do you want to start the process? (y/n): ")

    def loggingCameraStatus(self):
        print("Camera has status: x")

    def statusRunning(self):
        print("Running...")


    def statusExiting(self):
        print("Exiting...")

    def runningSetupProcedures(self):
        print("Running setup procedures...")

    def statusImageSaved(self, image_path):
        print(f"Image captured and successfully saved to {image_path}.")

    def errorSetupFailed(self):
        print("Setup procedure failed, please check logs for details.")




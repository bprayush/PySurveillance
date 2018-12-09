#! /usr/bin/python3
from drive import Drive
from capture import Capture
from threading import Thread
import time

capture = Capture()
appDrive = Drive()
path = ""

def cam_capture():
    while True:
        capture.setFilePath()
        if capture.captureReady():
            print("Capture")
            filename = capture.captureVid()
            appDrive.enQueue(filename)
        global path
        path = capture.filePath
        print("Working...")


def drive_upload():
    print("inside drive_upload")
    while True:
        global path
        appDrive.path = path
        print("waiting inside drive_upload")
        # time.sleep(30*60)
        time.sleep(120)
        connection = False
        print("waiting finished")
        while not connection:
            try:
                appDrive.authenticate()
                appDrive.uploadFile()
                connection = True
                print("Upload success")
            except:
                print("Connection error")
                connection = False
                time.sleep(10)
        # appDrive.delete()


if __name__ == "__main__":
    print("Surveillance Started")
    camera_thread = Thread(target=cam_capture)
    camera_thread.setName("Camera Thread")

    drive_thread = Thread(target=drive_upload)
    drive_thread.setName("Google Drive Thread")

    camera_thread.start()
    drive_thread.start()

    camera_thread.join()
    drive_thread.join()
    print("Surveillance Ended")

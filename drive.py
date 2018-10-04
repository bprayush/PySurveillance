from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from datetime import datetime
import os


class Drive:
    gauth = []
    drive = []
    path = "videos/"
    folderId = "1Axb2yk26lcL5BOncsRAwQKfGdL1YLN0I"
    uploadKind = "drive#childList"
    queue = []

    def authenticate(self):
        self.gauth = GoogleAuth()
        self.gauth.LocalWebserverAuth()
        self.drive = GoogleDrive(self.gauth)

    def uploadFile(self):
        while len(self.queue):
            print("uploading...")

            newFile = self.drive.CreateFile({
                "parents": [{
                    "kind": self.uploadKind,
                    "id": self.folderId
                }],
                "title": self.top()
            })

            newFile.SetContentFile(self.path + self.top())
            newFile.Upload()

            if newFile.uploaded:
                print("Uploaded")
                self.deQueue()
            else:
                print("Not Uploaded")

    def top(self):
        return self.queue[0]

    def enQueue(self, file):
        self.queue.append(file)

    def deQueue(self):
        self.queue.pop(0)

    def getQueue(self):
        return self.queue

    def getFileName(self):
        return str(datetime.now()) + '.avi'


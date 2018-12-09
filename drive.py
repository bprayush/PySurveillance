from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from datetime import datetime
import os


class Drive:
    gauth = []
    drive = []
    rootPath = "videos/"
    path = ""
    folderId = "1Axb2yk26lcL5BOncsRAwQKfGdL1YLN0I"
    uploadKind = "drive#childList"
    queue = []
    uploadedFiles = []

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
                self.uploaded(self.top())
                self.deQueue()
            else:
                print("Not Uploaded")

    def top(self):
        return self.queue[0]

    def enQueue(self, file):
        print("Adding to upload list")
        self.queue.append(file)
        print(self.queue)

    def deQueue(self):
        self.queue.pop(0)

    def getQueue(self):
        return self.queue

    def getFileName(self):
        return str(datetime.now()) + '.avi'

    def uploaded(self, file):
        self.uploadedFiles.append(file)

    def delete(self):
        # for file in self.uploadedFiles:
        #     os.remove(self.path + file)
        #     print("Deleting file ...")

        self.uploadedFiles = []

    def setPath(self, path):
        self.path = path




import cv2
import datetime
import os


class Capture:
    flag = True
    first = True
    fileRoot = "videos/"
    filePath = ""
    length = 59
    fps = 60.0
    width = 320
    height = 240
    startTime = 0
    endTime = 0
    recording = False

    def captureVid(self):
        self.recording = True
        self.setStartEnd()
        cap = cv2.VideoCapture(1)
        cap.set(cv2.CAP_PROP_FPS, self.fps)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        name = str(datetime.datetime.now().strftime("%H-%M")) + '.avi'
        full_path = self.filePath + name
        out = cv2.VideoWriter(full_path, fourcc, self.fps, (self.width, self.height))
        font = cv2.FONT_HERSHEY_SIMPLEX

        while True:
            ret, frame = cap.read()
            time = datetime.datetime.now()
            cv2.putText(frame, str(time), (10, 20), font, 0.8, (0, 0, 0), 1, cv2.LINE_AA)
            out.write(frame)
            if self.stopRecording():
                self.recording = False
                print("Recording stopped")
                break

        cap.release()
        cv2.destroyAllWindows()

        return name

    def captureReady(self):
        # end = datetime.datetime.now().minute
        #
        # if end % self.length == 0:
        #     self.flag = True
        # else:
        #     self.flag = False
        #
        # return self.flag
        return not self.recording

    def setStartEnd(self):
        self.startTime = datetime.datetime.now().minute
        self.endTime = (self.startTime + self.length) % 60

    def stopRecording(self):
        if datetime.datetime.now().minute == self.endTime:
            return True
        else:
            return False

    def setFilePath(self):
        self.filePath = self.fileRoot + str(datetime.datetime.now().strftime("%d-%B-%Y")) + "/"
        if not os.path.exists(self.filePath):
            os.mkdir(self.filePath)

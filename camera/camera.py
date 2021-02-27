import cv2 as cv

face_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_alt2.xml")
eye_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')
ds_factor = 0.6


class VideoCamera(object):
    def __init__(self):
        self.video = cv.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        image = cv.flip(image, 1)
        image = cv.resize(image, None, fx=ds_factor, fy=ds_factor, interpolation=cv.INTER_AREA)
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        face_rects = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in face_rects:
            cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            roi_gray = gray[y:y + w, x:x + w]
            roi_color = image[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
            for(ex, ey, ew, eh) in eyes:
                cv.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 2)
            break

        ret, jpeg = cv.imencode('.jpg', image)
        return jpeg.tobytes()

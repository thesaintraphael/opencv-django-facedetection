from django.shortcuts import render
from django.views import View
from django.http import StreamingHttpResponse
from .camera import VideoCamera


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def camera_live(request):
    try:
        return StreamingHttpResponse(gen(VideoCamera()), content_type="multipart/x-mixed-replace;boundary=frame")
    except Exception as e:
        print(e)


def close_camera(request, camera):
    VideoCamera().__del__()


class Camera(View):
    template_name = 'home.html'
    # template_name = 'camera.html'
    word = 'Face-Eye Detection'

    def get(self, request):
        context = {
            'data': self.word
        }
        return render(request, self.template_name, context)

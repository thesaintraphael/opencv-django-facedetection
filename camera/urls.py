from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.Camera.as_view(), name='camera'),
    path('video_feed/', v.camera_live, name='camera_live'),
    path('close-camera/', v.camera_live, name='close_camera')
]

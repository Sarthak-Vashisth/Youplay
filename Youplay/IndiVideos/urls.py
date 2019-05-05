from django.conf.urls import include, url
from . import individual_videos_playlist

app_name = "IndiVideos"

urlpatterns = [
    url(r'^create_playlist/$', individual_videos_playlist.CreateAndPlayPlaylist.as_view(), name='CreateAndPlayPlaylist'),
]

from mixer.youtube.searching import YouTubeClient, QueryOptions
from mixer.browsers.player import *

yt_client = YouTubeClient()

example = 'Bracia Figo Fagot'

videos = yt_client.youtube_search(QueryOptions(example, 5))

player = FirefoxPlayer()

player.play_video(videos[3].song_id)
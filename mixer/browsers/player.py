from selenium import webdriver
import os
from time import sleep

class WebBrowserPlayer:
    def __init__(self):
        raise NotImplemented()

    def _build_url(self, video_id):
        base_url = 'https://www.youtube.com/watch?v='
        return base_url + video_id

    def play_video(self, video_id):
        self.driver.get(self._build_url(video_id))


class FirefoxPlayer(WebBrowserPlayer):
    # todo: add existing profile file from OS
    # todo: or change selenium for something else
    def __init__(self):
        import os
        gecko_path = os.path.abspath('mixer/browsers/geckodriver')
        print gecko_path
        self.driver = webdriver.Firefox(executable_path=gecko_path)

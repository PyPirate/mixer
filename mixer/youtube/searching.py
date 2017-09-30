from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
from collections import namedtuple

QueryOptions = namedtuple('QueryOptions', ['band', 'max_results'])
QueryResult = namedtuple('QueryResult', ['song_name', 'song_id'])


class YouTubeClient:
    # Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
    # tab of
    #   https://cloud.google.com/console
    # Please ensure that you have enabled the YouTube Data API for your project.
    def __init__(self):
        self._DEVELOPER_KEY = "AIzaSyCG6uGNl6FKqwXqszqeEttXVNFiuieOWzo"
        self._YOUTUBE_API_SERVICE_NAME = "youtube"
        self._YOUTUBE_API_VERSION = "v3"
        self.client = build(self._YOUTUBE_API_SERVICE_NAME, self._YOUTUBE_API_VERSION,
                        developerKey=self._DEVELOPER_KEY)

    def get_video_duration(self, video_id):
        """
        :param video_id: unique id of yt video
        :return: duration in seconds
        """
        response = self.client.videos().list(
            part='contentDetails',
            id=video_id,
            maxResults=1
        ).execute()

        duration = response['items'][0]['contentDetails']['duration']

        # convert duration from ISO 8601 str to integer amount of seconds

        duration = duration.replace('PT', '').replace('M', ':').replace('S', '')
        minutes, seconds = duration.split(':')
        return int(minutes)*60 + int(seconds)

    def youtube_search(self, options):
        """
        :param options: Namedtuple with band name and maximum amount of search results
        :return: list of Namedtuples (song_name, song_id)
        """

        # Call the search.list method to retrieve results matching the specified
        # query term.
        search_response = self.client.search().list(
            q=options.band,
            part="id,snippet",
            maxResults=options.max_results,
            type='video'
        ).execute()

        results = [QueryResult(search_result["snippet"]["title"], search_result["id"]["videoId"]) for search_result in
                   search_response.get("items", [])]

        return results


if __name__ == "__main__":
    seeker = YouTubeClient()
    id = seeker.youtube_search(QueryOptions('REM', 5))[0].song_id
    print seeker.get_video_duration(id)

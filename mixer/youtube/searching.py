from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
from collections import namedtuple

QueryOptions = namedtuple('QueryOptions', ['band', 'max_results'])
QueryResult = namedtuple('QueryResult', ['song_name', 'song_id'])


class YouTubeMusicSeeker:

    # Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
    # tab of
    #   https://cloud.google.com/console
    # Please ensure that you have enabled the YouTube Data API for your project.
    def __init__(self):
        self._DEVELOPER_KEY = "AIzaSyCG6uGNl6FKqwXqszqeEttXVNFiuieOWzo"
        self._YOUTUBE_API_SERVICE_NAME = "youtube"
        self._YOUTUBE_API_VERSION = "v3"

    def youtube_search(self, options):
        """
        :param options: Namedtuple with band name and maximum amount of search results
        :return: list of Namedtuples (song_name, song_id)
        """
        youtube = build(self._YOUTUBE_API_SERVICE_NAME, self._YOUTUBE_API_VERSION,
                        developerKey=self._DEVELOPER_KEY)

        # Call the search.list method to retrieve results matching the specified
        # query term.
        search_response = youtube.search().list(
            q=options.band,
            part="id,snippet",
            maxResults=options.max_results
        ).execute()

        results = []

        for search_result in search_response.get("items", []):
            if search_result["id"]["kind"] == "youtube#video":
                results.append(QueryResult(search_result["snippet"]["title"], search_result["id"]["videoId"]))

        return results

if __name__ == "__main__":
    seeker = YouTubeMusicSeeker()
    for el in seeker.youtube_search(QueryOptions('REM', 5)):
        print el
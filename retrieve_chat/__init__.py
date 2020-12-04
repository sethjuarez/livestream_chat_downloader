import logging
import azure.functions as func
from ..shared.chat_replay_downloader import *


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    post = req.get_json()
    logging.info(post['video'])
    # get messages via url
    youtube_messages = get_chat_replay('https://www.youtube.com/watch?v=xxxxxxxxxxx')
    twitch_messages = get_chat_replay('https://www.twitch.tv/videos/xxxxxxxxx')

    # get messages via id
    youtube_messages = get_youtube_messages('xxxxxxxxxxx')
    twitch_messages = get_twitch_messages('xxxxxxxxx')

    
    return func.HttpResponse(
        "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
        status_code=200
    )

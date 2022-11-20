"""This module contains functions for downloading videos from youtube."""
import logging
import youtube_dl  # type: ignore
from typing import Union
from .config import settings

logger = logging.getLogger(settings.PROJECT_SLUG)
YDL_OPTS = {
    'outtmpl': '%(title)s',
    'quiet': False
}


def download_clip(url: str) -> Union[str, None]:
    """Download video from the given youtube URL.

    Args:
        url (str): url to the video in youtube, you can get it through copying
          the url in address bar.

    Returns:
        str: Downloaded youtube video file.
    """
    output_file = None
    try:
        with youtube_dl.YoutubeDL(YDL_OPTS) as ydl:
            ydl.cache.remove()
            info_dict = ydl.extract_info(url, download=False)
            output_file = ydl.prepare_filename(info_dict) + '.' + info_dict['ext']
            ydl.download([url])
    except Exception as e:
        error_msg = "The error [{}] occurred during downloading " \
                    "the video from URL [{}]".format(str(e), url)
        logger.error(error_msg)
    return output_file

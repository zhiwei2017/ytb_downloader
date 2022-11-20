"""This module contains functions for downloading videos from youtube."""
import logging
import youtube_dl  # type: ignore
from typing import List, Dict
from .config import settings
from .file_name_collector import FilenameCollectorPP

logger = logging.getLogger(settings.PROJECT_SLUG)
YDL_OPTS = {
    'outtmpl': '%(title)s',
    'quiet': False
}


def download_videos(urls: List[str], ydl_opts: Dict = YDL_OPTS) -> List[str]:
    """Download videos from the given youtube URLs.

    Args:
        urls (List[str]): urls to the videos in youtube, you can get it through
          copying the url in address bar.
        ydl_opts (dict): youtube download options.

    Returns:
        List[str]: Downloaded youtube video file.
    """
    output_files = []
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            filename_collector = FilenameCollectorPP()
            ydl.cache.remove()
            ydl.add_post_processor(filename_collector)
            ydl.download(urls)
            output_files = filename_collector.filenames
    except Exception as e:
        error_msg = "The error [{}] occurred during downloading " \
                    "the videos.".format(str(e))
        logger.error(error_msg)
    return output_files

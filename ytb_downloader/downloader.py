"""This module contains functions for downloading videos from youtube."""
import logging
import youtube_dl  # type: ignore
from typing import List, Dict, Optional
from .config import settings
from .file_name_collector import FileNameCollectorPP

logger = logging.getLogger(settings.PROJECT_SLUG)
YDL_OPTS = {
    'outtmpl': '%(title)s',
    'quiet': False
}


def download_videos(urls: List[str],
                    ydl_opts: Optional[Dict] = None) -> List[str]:
    """Download videos from the given youtube URLs.

    Args:
        urls (:obj: of list of str): urls to the videos in youtube, you can get it
          through copying the url in address bar.
        ydl_opts (dict|None): youtube download options.

    Returns:
        :obj: of list of str: Downloaded youtube video file names.
    """
    ydl_opts = ydl_opts or YDL_OPTS
    output_files = []
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            filename_collector = FileNameCollectorPP()
            ydl.cache.remove()
            ydl.add_post_processor(filename_collector)
            ydl.download(urls)
            output_files = filename_collector.file_names
    except Exception as e:
        error_msg = "The error [{}] occurred during downloading " \
                    "the videos.".format(str(e))
        logger.error(error_msg)
    return output_files

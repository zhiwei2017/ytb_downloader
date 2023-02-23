"""This module contains functions for downloading videos from youtube."""
import logging
import yt_dlp  # type: ignore
from typing import List, Dict, Optional
from .config import settings
from .file_name_collector import FileNameCollectorPP

logger = logging.getLogger(settings.PROJECT_SLUG)
YDL_VIDEO_OPTS = {
    'outtmpl': '%(title)s',
    'quiet': False
}
YDL_AUDIO_OPTS = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s',
    'quiet': False
}


def download(urls: List[str], ydl_opts: Optional[Dict] = None) -> List[str]:
    """Download videos/audios from the given youtube URLs.

    Args:
        urls (:obj:`list` of :obj:`str`): urls to the videos in
          youtube, you can get it through copying the url in address bar.
        ydl_opts (:obj:`dict`): yt_dlp's options.

    Returns:
        :obj:`list` of :obj:`str`: Downloaded youtube video file names.
    """
    ydl_opts = ydl_opts or YDL_AUDIO_OPTS
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            filename_collector = FileNameCollectorPP()
            ydl.cache.remove()
            ydl.add_post_processor(filename_collector)
            ydl.download(urls)
            return filename_collector.file_names
    except Exception as e:
        error_msg = "The error [{}] occurred during downloading " \
                    "the videos.".format(str(e))
        logger.error(error_msg)
        raise e

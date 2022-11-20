"""This module contains functions for converting the downloaded youtube video
file to the given format."""
import os
import logging
import moviepy.editor as mp  # type: ignore
from typing import Optional, Union
from .config import settings

logger = logging.getLogger(settings.PROJECT_SLUG)


def convert_to(downloaded_file: str, conversion_format: str = 'mp3',
               t_start: int = 0, t_end: Optional[int] = None,
               bitrate: str = '3000k') -> Union[str, None]:
    """Convert the downloaded youtube video file to the given format.

    Args:
        downloaded_file (str): path to the download youtube video file.
        conversion_format (str): format of the output file, mp3, avi etc.
        t_start (int): starting point for cutting the video.
        t_end (int): ending point for cutting the video, if not provided, the
          whole video will be converted.
        bitrate (str): Audio bitrate, given as a string like '50k', '500k', '3000k'.
          Will determine the size and quality of the output file.
          Note that it mainly an indicative goal, the bitrate won't
          necessarily be the this in the output file.

    Returns:
        str: the converted file path.
    """
    if not os.path.exists(downloaded_file):
        logger.error("The given downloaded file path doesn't exist.")
        return None
    filename, _ = os.path.splitext(downloaded_file)
    output_file = "{}.{}".format(filename, conversion_format)
    clip = mp.VideoFileClip(downloaded_file).subclip(t_start, t_end)
    clip.audio.write_audiofile(output_file, bitrate=bitrate)
    return output_file

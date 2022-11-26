"""This module contains functions for converting the downloaded youtube video
file to the given format."""
import logging
import moviepy.editor as mp  # type: ignore
import os
from typing import Optional, Union
from .config import settings
from .constants import Media

logger = logging.getLogger(settings.PROJECT_SLUG)


def convert_to(downloaded_file: str,
               media_format: Media = Media.AUDIO,
               conversion_format: str = 'mp3',
               t_start: int = 0, t_end: Optional[int] = None,
               fps: int = 44100, bitrate: str = '3000k') -> Union[str, None]:
    """Convert the downloaded youtube video file to the given format.

    Args:
        downloaded_file (:obj:`str`): path to the download youtube video file.
        media_format (:obj:`Media`): the original file's format.
        conversion_format (:obj:`str`): format of the output file, mp3, avi etc.
        t_start (:obj:`int`): starting point for cutting the video.
        t_end (:obj:`int`, optional): ending point for cutting the video, if
          not provided, the whole video will be converted.
        fps (:obj:`int`): Frames per second. It will default to 44100.
        bitrate (:obj:`str`): Audio bitrate, given as a string like '50k', '500k',
          '3000k'. Will determine the size and quality of the output file.
          Note that it mainly an indicative goal, the bitrate won't
          necessarily be the this in the output file.

    Returns:
        :obj:`None` or :obj:`str`: the converted file path, if conversion
        succeed, otherwise None.
    """
    if not os.path.exists(downloaded_file):
        logger.error("The given downloaded file path doesn't exist.")
        return None
    filename, _ = os.path.splitext(downloaded_file)
    output_file = "{}.{}".format(filename, conversion_format)
    if media_format == Media.VIDEO:
        clip = mp.VideoFileClip(downloaded_file).subclip(t_start, t_end).audio
    else:
        clip = mp.AudioFileClip(downloaded_file).subclip(t_start, t_end)
    clip.write_audiofile(output_file, fps=fps, bitrate=bitrate)
    return output_file

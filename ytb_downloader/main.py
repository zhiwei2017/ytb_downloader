import click
import logging
import os
from typing import Optional
from .config import settings
from .converter import convert_to
from .downloader import download, YDL_AUDIO_OPTS, YDL_VIDEO_OPTS
from .file_loader import load_file
from .constants import Media


logger = logging.getLogger(settings.PROJECT_SLUG)


@click.command()
@click.option('--video-only', is_flag=True)
@click.option('--format', '-f', default="mp3", required=False, type=str,
              show_default=True, help='Output file format, like mp3, avi etc.')
@click.option('--time-start', '-ts', default=0, required=False, type=int,
              show_default=True, help='Start time for converting the video.')
@click.option('--time-end', '-te', required=False, type=int, show_default=True,
              help='End time for converting the video. If not provided, the '
                   'whole video will be converted')
@click.option('--fps', '-fs', default=44100, required=False,
              type=int, show_default=True,
              help="Frames per second. It will default to 44100.")
@click.option('--bitrate', '-br', default='3000k', required=False,
              type=str, show_default=True,
              help="Audio bitrate, like '50k', '500k', '3000k'.")
@click.argument("url")
def download_single(video_only: bool, format: str, time_start: int,
                    time_end: Optional[int], fps: int, bitrate: str, url: str):
    """CMD function for downloading a video from given URL and convert it to the
    audio with given format and other converting params.

    \f

    Args:
        video_only (:obj:`bool`): flag, to indicate whether to convert the video
          or not.
        format (:obj:`str`): audio format for the conversion.
        time_start (:obj:`int`): starting time for cutting the video.
        time_end (:obj:`int`, optional): end time for cutting the video.
        bitrate (:obj:`str`): bitrate of the audio.
        url (:obj:`str`): url of the video to download and convert.
    """
    ytb_opts = YDL_VIDEO_OPTS if video_only else YDL_AUDIO_OPTS
    tmp_output_file = download([url], ytb_opts)[0]
    if video_only:
        msg = "The video from [{}] is downloaded " \
              "in file [{}].".format(url, tmp_output_file)
        logger.info(msg)
        return
    output_file = convert_to(tmp_output_file, Media.AUDIO, format,
                             time_start, time_end, fps, bitrate)
    os.remove(tmp_output_file)
    msg = "The video from [{}] is downloaded and converted to [{}] format " \
          "in file [{}].".format(url, format, output_file)
    logger.info(msg)


@click.command()
@click.option('--video-only', is_flag=True)
@click.argument("file")
def download_bulk(video_only: bool, file: str):
    """Download videos in bulk and convert them to audios.

    \f

    Args:
        video_only (:obj:`bool`): flag, to indicate whether to convert the video or
          not.
        file (:obj:`str`): path to the csv file containing all the information for
        downloading and converting.
    """
    urls, info_dicts = load_file(file)
    ytb_opts = YDL_VIDEO_OPTS if video_only else YDL_AUDIO_OPTS
    tmp_output_files = download(urls, ytb_opts)
    if not video_only:
        output_files = []
        for i, info_dict in enumerate(info_dicts):
            output_file = convert_to(tmp_output_files[i], **info_dict)
            os.remove(tmp_output_files[i])
            output_files.append(output_file)
        msg = "The videos are downloaded and converted to files {}.".format(str(output_files))
    else:
        msg = "The videos are downloaded in files {}.".format(str(tmp_output_files))
    logger.info(msg)

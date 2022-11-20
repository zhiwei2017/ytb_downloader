import logging
import click
import os
from .downloader import download_clip
from .conversion import convert_to
from .config import settings

logger = logging.getLogger(settings.PROJECT_SLUG)


@click.command()
@click.option('--format', '-f', default="mp3", required=False, type=str, show_default=True,
              help='Output file format, like mp3, avi etc.')
@click.option('--time-start', '-ts', default=0, required=False, type=int, show_default=True,
              help='Start time for converting the video.')
@click.option('--time-end', '-te', required=False, type=int, show_default=True,
              help='End time for converting the video. If not provided, the '
                   'whole video will be converted')
@click.option('--bitrate', '-br', default='3000k', required=False, type=str,
              show_default=True, help="Audio bitrate, like '50k', '500k', '3000k'.")
@click.argument("url")
def main(format, time_start, time_end, bitrate, url):
    """Main function for accepting url for downloading."""
    tmp_output_file = download_clip(url)
    output_file = convert_to(tmp_output_file)
    os.remove(tmp_output_file)
    msg = "The video from [] is downloaded and converted to [] format " \
          "in file [].".format(url, format, output_file)
    logger.info(msg)

"""Extracting downloaded files' names."""
import yt_dlp  # type: ignore
from typing import Tuple, Dict, List


class FileNameCollectorPP(yt_dlp.postprocessor.common.PostProcessor):
    """Collect file names from the yt_dlp for downloaded videos as an post
    processing step.

    Attributes:
        file_names (:obj:`list` of :obj:`str`): file names of the downloaded videos in sequence.

    """
    def __init__(self):
        super(FileNameCollectorPP, self).__init__(None)
        self.file_names = []

    def run(self, information: Dict) -> Tuple[List, Dict]:
        """Interface function for adding the last downloaded video's file name
        in the class attribute `filenames`.

        Args:
            information (:obj:`dict`): last downloaded video's information.

        Returns:
            :obj:`tuple` (:obj:`list` and :obj:`dict`): last downloaded
            video's information.
        """
        self.file_names.append(information["filepath"])
        return [], information

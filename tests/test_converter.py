import os
import pytest
from ytb_downloader.converter import convert_to


@pytest.mark.parametrize("file_path, format, time_start, time_end, bitrate, expected_result",
                         [("Dummy", "mp3", 0, None, "500k", None),
                          (os.path.join(os.getcwd(), "tests/resources/Shortest_Video_on_Youtube.mkv"),
                           "mp3", 0, None, "500k",
                           os.path.join(os.getcwd(), "tests/resources/Shortest_Video_on_Youtube.mp3")),
                          (os.path.join(os.getcwd(), "tests/resources/Shortest_Video_on_Youtube_Part_922.mp4"),
                           "mp3", 0, 4, "500k",
                           os.path.join(os.getcwd(), "tests/resources/Shortest_Video_on_Youtube_Part_922.mp3")),
                          (os.path.join(os.getcwd(), "tests/resources/Shortest_Video_on_Youtube_Part_922.mp4"),
                           "mp3", 2, 4, "500k",
                           os.path.join(os.getcwd(), "tests/resources/Shortest_Video_on_Youtube_Part_922.mp3")),
                           (os.path.join(os.getcwd(), "tests/resources/Shortest_Video_on_Youtube_Part_922.mp4"),
                            "wav", 2, 4, "500k",
                            os.path.join(os.getcwd(), "tests/resources/Shortest_Video_on_Youtube_Part_922.wav"))])
def test_convert_to(file_path, format, time_start, time_end, bitrate, expected_result):
    result = convert_to(file_path, format, time_start, time_end, bitrate)
    assert result == expected_result
    if expected_result:
        os.remove(expected_result)

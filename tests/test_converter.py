import os
import pytest
from ytb_downloader.converter import convert_to, Media


@pytest.mark.parametrize("file_path, media_format, format, time_start, time_end, fps, bitrate, expected_result",
                         [("Dummy", Media.AUDIO, "mp3", 0, None, 44100, "500k", None),
                          (os.path.join(os.getcwd(), "tests/resources/Shortest_Video_on_Youtube.mkv"),
                           Media.VIDEO, "mp3", 0, None, 3000, "150k",
                           os.path.join(os.getcwd(), "tests/resources/Shortest_Video_on_Youtube.mp3")),
                          (os.path.join(os.getcwd(), "tests/resources/Shortest_Video_on_Youtube"),
                           Media.AUDIO, "mp3", 0, None, 3000, "500k",
                           os.path.join(os.getcwd(), "tests/resources/Shortest_Video_on_Youtube.mp3")),
                          (os.path.join(os.getcwd(), "tests/resources/Shortest_Video_on_Youtube_Part_922.mp4"),
                           Media.VIDEO, "mp3", 0, 4, 300, "300k",
                           os.path.join(os.getcwd(), "tests/resources/Shortest_Video_on_Youtube_Part_922.mp3")),
                          (os.path.join(os.getcwd(), "tests/resources/Shortest_Video_on_Youtube_Part_922.mp4"),
                           Media.VIDEO, "mp3", 2, 4, 1, "220k",
                           os.path.join(os.getcwd(), "tests/resources/Shortest_Video_on_Youtube_Part_922.mp3")),
                          (os.path.join(os.getcwd(), "tests/resources/Shortest_Video_on_Youtube_Part_922.mp4"),
                           Media.VIDEO, "wav", 2, 4, 100, "400k",
                           os.path.join(os.getcwd(), "tests/resources/Shortest_Video_on_Youtube_Part_922.wav")),
                          (os.path.join(os.getcwd(), "tests/resources/Shortest_Video_on_Youtube_Part_922"),
                           Media.AUDIO, "wav", 2, 4, 100, "100k",
                           os.path.join(os.getcwd(), "tests/resources/Shortest_Video_on_Youtube_Part_922.wav")),
                          (os.path.join(os.getcwd(), "tests/resources/Shortest_Video_on_Youtube_Part_922"),
                           Media.AUDIO, "mp3", 2, 4, 100, "200k",
                           os.path.join(os.getcwd(), "tests/resources/Shortest_Video_on_Youtube_Part_922.mp3"))])
def test_convert_to(file_path, media_format, format, time_start, time_end, fps, bitrate, expected_result):
    result = convert_to(file_path, media_format, format, time_start, time_end, fps, bitrate)
    assert result == expected_result
    if expected_result:
        os.remove(expected_result)

import os
import pytest
from ytb_downloader.file_loader import columns_validation, load_file


@pytest.mark.parametrize("columns, expected_result",
                         [([], None),
                          (["nothing"], None),
                          (["url"], []),
                          (["url", "nothing"], []),
                          (["url", "format"], ["format"]),
                          (["url", "format", "nothing"], ["format"]),
                          (["url", "format", "time_start", "time_end", "bitrate"], ["format", "time_start", "time_end", "bitrate"]),
                          (["url", "format", "time_start", "time_end", "fps", "bitrate"], ["format", "time_start", "time_end", "fps", "bitrate"]),
                          (["url", "format", "time_start", "time_end", "bitrate", "nothing"], ["format", "time_start", "time_end", "bitrate"])])
def test_columns_validation(columns, expected_result):
    result = columns_validation(columns)
    if expected_result is None:
        assert result == expected_result
    else:
        assert set(result) == set(expected_result)


@pytest.mark.parametrize("file_name, expected_result",
                         [(os.path.join(os.getcwd(), "tests/resources/example.csv"),
                           (["https://www.youtube.com/watch?v=WqkjYKUXERQ",
                             "https://www.youtube.com/watch?v=nOubjLM9Cbc"],
                            [dict(format="mp3", time_start=0, time_end=None, fps=44100, bitrate="3000k"),
                             dict(format="wav", time_start=4, time_end=1000, fps=200, bitrate="200k")])),
                          (os.path.join(os.getcwd(), "tests/resources/example_only_url.csv"),
                           (["https://www.youtube.com/watch?v=WqkjYKUXERQ",
                            "https://www.youtube.com/watch?v=nOubjLM9Cbc"],
                            [])),
                          (os.path.join(os.getcwd(), "tests/resources/example_no_time_end.csv"),
                           (["https://www.youtube.com/watch?v=WqkjYKUXERQ",
                             "https://www.youtube.com/watch?v=nOubjLM9Cbc"],
                            [dict(format="mp3", time_start=0, fps=44100, bitrate="3000k"),
                             dict(format="wav", time_start=4, fps=200, bitrate="200k")]))])
def test_load_file(file_name, expected_result):
    result = load_file(file_name)
    assert result == expected_result


def test_load_file_failure():
    with pytest.raises(ValueError) as e:
        load_file(os.path.join(os.getcwd(), "tests/resources/example_wrong_col.csv"))
    assert str(e.value) == "Missing column [url] in csv file."

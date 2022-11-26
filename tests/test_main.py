import os
from unittest import mock
from click.testing import CliRunner
from ytb_downloader.main import (
    download_single, download_bulk, YDL_AUDIO_OPTS, YDL_VIDEO_OPTS, Media
)


@mock.patch("ytb_downloader.main.logger")
@mock.patch("ytb_downloader.main.os")
@mock.patch("ytb_downloader.main.convert_to", return_value="dummy/path/file/converted")
@mock.patch("ytb_downloader.main.download", return_value=["dummy/path/file"])
def test_download_single(mocked_download, mocked_convert_to, mocked_os, mocked_logger):
    runner = CliRunner()
    result = runner.invoke(download_single, ['dummy'])
    assert result.exit_code == 0
    mocked_download.assert_called_once_with(['dummy'], YDL_AUDIO_OPTS)
    mocked_convert_to.assert_called_once_with("dummy/path/file", Media.AUDIO, "mp3", 0, None, 44100, "3000k")
    mocked_os.remove.assert_called_once_with("dummy/path/file")
    mocked_logger.info.assert_called_once_with("The video from [dummy] is downloaded and converted to [mp3] format in file [dummy/path/file/converted].")


@mock.patch("ytb_downloader.main.logger")
@mock.patch("ytb_downloader.main.os")
@mock.patch("ytb_downloader.main.convert_to", return_value="dummy/path/file/converted")
@mock.patch("ytb_downloader.main.download", return_value=["dummy/path/file"])
def test_download_single_video_only(mocked_download, mocked_convert_to, mocked_os, mocked_logger):
    runner = CliRunner()
    result = runner.invoke(download_single, ["--video-only", 'dummy'])
    assert result.exit_code == 0
    mocked_download.assert_called_once_with(['dummy'], YDL_VIDEO_OPTS)
    mocked_convert_to.assert_not_called()
    mocked_os.remove.assert_not_called()
    mocked_logger.info.assert_called_once_with("The video from [dummy] is downloaded in file [dummy/path/file].")


@mock.patch("ytb_downloader.main.logger")
@mock.patch("ytb_downloader.main.os")
@mock.patch("ytb_downloader.main.convert_to", return_value="dummy/path/file/converted")
@mock.patch("ytb_downloader.main.download", return_value=["dummy/path/file"])
def test_download_single_fail(mocked_download, mocked_convert_to, mocked_os, mocked_logger):
    runner = CliRunner()
    result = runner.invoke(download_single, [1])
    assert result.exit_code == 1

    result = runner.invoke(download_single, ["--dummy-flag", "dummy"])
    assert result.exit_code == 2

    result = runner.invoke(download_single, [])
    assert result.exit_code == 2


@mock.patch("ytb_downloader.main.logger")
@mock.patch("ytb_downloader.main.os")
@mock.patch("ytb_downloader.main.convert_to", return_value="dummy/path/file/converted")
@mock.patch("ytb_downloader.main.download", return_value=["dummy/path/file1", "dummy/path/file2"])
def test_download_bulk(mocked_download, mocked_convert_to, mocked_os, mocked_logger):
    file_path = os.path.join(os.getcwd(), "tests/resources/example.csv")
    runner = CliRunner()
    result = runner.invoke(download_bulk, [file_path])
    assert result.exit_code == 0
    mocked_download.assert_called_once_with(["https://www.youtube.com/watch?v=WqkjYKUXERQ",
                                             "https://www.youtube.com/watch?v=nOubjLM9Cbc"],
                                            YDL_AUDIO_OPTS)
    assert mocked_convert_to.call_count == 2
    assert mocked_os.remove.call_count == 2
    mocked_logger.info.assert_called_once_with("The videos are downloaded and converted to files ['dummy/path/file/converted', 'dummy/path/file/converted'].")


@mock.patch("ytb_downloader.main.logger")
@mock.patch("ytb_downloader.main.os")
@mock.patch("ytb_downloader.main.convert_to", return_value="dummy/path/file/converted")
@mock.patch("ytb_downloader.main.download", return_value=["dummy/path/file1", "dummy/path/file2"])
def test_download_bulk_video_only(mocked_download, mocked_convert_to, mocked_os, mocked_logger):
    file_path = os.path.join(os.getcwd(), "tests/resources/example.csv")
    runner = CliRunner()
    result = runner.invoke(download_bulk, ["--video-only", file_path])
    assert result.exit_code == 0
    mocked_download.assert_called_once_with(["https://www.youtube.com/watch?v=WqkjYKUXERQ",
                                             "https://www.youtube.com/watch?v=nOubjLM9Cbc"],
                                            YDL_VIDEO_OPTS)
    mocked_convert_to.assert_not_called()
    mocked_os.remove.assert_not_called()
    mocked_logger.info.assert_called_once_with("The videos are downloaded in files ['dummy/path/file1', 'dummy/path/file2'].")


@mock.patch("ytb_downloader.main.logger")
@mock.patch("ytb_downloader.main.os")
@mock.patch("ytb_downloader.main.convert_to", return_value="dummy/path/file/converted")
@mock.patch("ytb_downloader.main.download", return_value=["dummy/path/file"])
def test_download_bulk_fail(mocked_download, mocked_convert_to, mocked_os, mocked_logger):
    runner = CliRunner()
    result = runner.invoke(download_bulk, [1])
    assert result.exit_code == 1

    result = runner.invoke(download_bulk, ["--dummy-flag", "dummy"])
    assert result.exit_code == 2

    result = runner.invoke(download_bulk, [])
    assert result.exit_code == 2

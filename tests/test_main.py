import os
from unittest import mock
from click.testing import CliRunner
from ytb_downloader.main import download_audio, download_audios


@mock.patch("ytb_downloader.main.logger")
@mock.patch("ytb_downloader.main.os")
@mock.patch("ytb_downloader.main.convert_to", return_value="dummy/path/file/converted")
@mock.patch("ytb_downloader.main.download_videos", return_value=["dummy/path/file"])
def test_download_audio(mocked_download_videos, mocked_convert_to, mocked_os, mocked_logger):
    runner = CliRunner()
    result = runner.invoke(download_audio, ['dummy'])
    assert result.exit_code == 0
    mocked_download_videos.assert_called_once_with(['dummy'])
    mocked_convert_to.assert_called_once_with("dummy/path/file", "mp3", 0, None, "3000k")
    mocked_os.remove.assert_called_once_with("dummy/path/file")
    mocked_logger.info.assert_called_once_with("The video from [dummy] is downloaded and converted to [mp3] format in file [dummy/path/file/converted].")


@mock.patch("ytb_downloader.main.logger")
@mock.patch("ytb_downloader.main.os")
@mock.patch("ytb_downloader.main.convert_to", return_value="dummy/path/file/converted")
@mock.patch("ytb_downloader.main.download_videos", return_value=["dummy/path/file"])
def test_download_audio_video_only(mocked_download_videos, mocked_convert_to, mocked_os, mocked_logger):
    runner = CliRunner()
    result = runner.invoke(download_audio, ["--video-only", 'dummy'])
    assert result.exit_code == 0
    mocked_download_videos.assert_called_once_with(['dummy'])
    mocked_convert_to.assert_not_called()
    mocked_os.remove.assert_not_called()
    mocked_logger.info.assert_called_once_with("The video from [dummy] is downloaded in file [dummy/path/file].")


@mock.patch("ytb_downloader.main.logger")
@mock.patch("ytb_downloader.main.os")
@mock.patch("ytb_downloader.main.convert_to", return_value="dummy/path/file/converted")
@mock.patch("ytb_downloader.main.download_videos", return_value=["dummy/path/file"])
def test_download_audio_fail(mocked_download_videos, mocked_convert_to, mocked_os, mocked_logger):
    runner = CliRunner()
    result = runner.invoke(download_audio, [1])
    assert result.exit_code == 1

    result = runner.invoke(download_audio, ["--dummy-flag", "dummy"])
    assert result.exit_code == 2

    result = runner.invoke(download_audio, [])
    assert result.exit_code == 2


@mock.patch("ytb_downloader.main.logger")
@mock.patch("ytb_downloader.main.os")
@mock.patch("ytb_downloader.main.convert_to", return_value="dummy/path/file/converted")
@mock.patch("ytb_downloader.main.download_videos", return_value=["dummy/path/file1", "dummy/path/file2"])
def test_download_audios(mocked_download_videos, mocked_convert_to, mocked_os, mocked_logger):
    file_path = os.path.join(os.getcwd(), "tests/resources/example.csv")
    runner = CliRunner()
    result = runner.invoke(download_audios, [file_path])
    assert result.exit_code == 0
    mocked_download_videos.assert_called_once_with(["https://www.youtube.com/watch?v=WqkjYKUXERQ",
                                                    "https://www.youtube.com/watch?v=nOubjLM9Cbc"],)
    assert mocked_convert_to.call_count == 2
    assert mocked_os.remove.call_count == 2
    mocked_logger.info.assert_called_once_with("The videos are downloaded and converted to files ['dummy/path/file/converted', 'dummy/path/file/converted'].")


@mock.patch("ytb_downloader.main.logger")
@mock.patch("ytb_downloader.main.os")
@mock.patch("ytb_downloader.main.convert_to", return_value="dummy/path/file/converted")
@mock.patch("ytb_downloader.main.download_videos", return_value=["dummy/path/file1", "dummy/path/file2"])
def test_download_audios_video_only(mocked_download_videos, mocked_convert_to, mocked_os, mocked_logger):
    file_path = os.path.join(os.getcwd(), "tests/resources/example.csv")
    runner = CliRunner()
    result = runner.invoke(download_audios, ["--video-only", file_path])
    assert result.exit_code == 0
    mocked_download_videos.assert_called_once_with(["https://www.youtube.com/watch?v=WqkjYKUXERQ",
                                                    "https://www.youtube.com/watch?v=nOubjLM9Cbc"],)
    mocked_convert_to.assert_not_called()
    mocked_os.remove.assert_not_called()
    mocked_logger.info.assert_called_once_with("The videos are downloaded in files ['dummy/path/file1', 'dummy/path/file2'].")


@mock.patch("ytb_downloader.main.logger")
@mock.patch("ytb_downloader.main.os")
@mock.patch("ytb_downloader.main.convert_to", return_value="dummy/path/file/converted")
@mock.patch("ytb_downloader.main.download_videos", return_value=["dummy/path/file"])
def test_download_audios_fail(mocked_download_videos, mocked_convert_to, mocked_os, mocked_logger):
    runner = CliRunner()
    result = runner.invoke(download_audios, [1])
    assert result.exit_code == 1

    result = runner.invoke(download_audios, ["--dummy-flag", "dummy"])
    assert result.exit_code == 2

    result = runner.invoke(download_audios, [])
    assert result.exit_code == 2

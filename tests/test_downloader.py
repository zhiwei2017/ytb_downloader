import pytest
from unittest import mock
from ytb_downloader.downloader import (
    download, YDL_VIDEO_OPTS, YDL_AUDIO_OPTS
)


@pytest.mark.parametrize("ydl_opts, expected_ydl_opts",
                        [(None, YDL_AUDIO_OPTS),
                         (YDL_AUDIO_OPTS, YDL_AUDIO_OPTS),
                         (YDL_VIDEO_OPTS, YDL_VIDEO_OPTS)])
@mock.patch("ytb_downloader.downloader.logger")
@mock.patch("ytb_downloader.downloader.yt_dlp")
def test_download_fail(mocked_yt_dlp, mocked_logger, ydl_opts, expected_ydl_opts):
    mocked_yt_dlp.YoutubeDL.side_effect = ValueError("dummy")
    with pytest.raises(ValueError) as e:
        download(["dummy"], ydl_opts)
    assert str(e.value) == "dummy"
    mocked_logger.error.assert_called_once_with('The error [dummy] occurred during downloading the videos.')
    mocked_yt_dlp.YoutubeDL.assert_called_once_with(expected_ydl_opts)


@pytest.mark.parametrize("ydl_opts, expected_ydl_opts",
                         [(YDL_VIDEO_OPTS, YDL_VIDEO_OPTS),
                          (YDL_AUDIO_OPTS, YDL_AUDIO_OPTS),
                          (None, YDL_AUDIO_OPTS)])
@mock.patch("ytb_downloader.downloader.FileNameCollectorPP")
@mock.patch("ytb_downloader.downloader.logger")
@mock.patch("ytb_downloader.downloader.yt_dlp")
def test_download_success(mocked_yt_dlp, mocked_logger, mocked_fnc, ydl_opts, expected_ydl_opts):
    mocked_fnc.return_value = mock.MagicMock(file_names=["1", "2"])
    result = download(["dummy"], ydl_opts)
    assert result == ["1", "2"]
    mocked_logger.assert_not_called()
    mocked_yt_dlp.YoutubeDL.assert_called_once_with(expected_ydl_opts)


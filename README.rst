Youtube Downloader
==================

Introduction
------------
Download youtube videos and convert them to mp3.

User Guide
----------

How to Install
++++++++++++++

To install `ytb_downloader` by running::

    $ pip install ytb_downloader

How to Use
++++++++++

You can use the command line tool from `ytb_downloader` to download audios or videos
from Youtube.

Download Audio
~~~~~~~~~~~~~~
Start downloading a single audio by calling::

    $ ytb_downloader "<your youtube video url>"

If you want to specify the format of the downloaded video, you can use the option
`--format` or `-f` with the format as string, such as::

    $ ytb_downloader --format "mp3" "https://www.youtube.com/watch?v=nOubjLM9Cbc"

For more details, please execute::

    $ ytb_downloader --help

Download Video
~~~~~~~~~~~~~~
Start downloading a single video by calling::

    $ ytb_downloader --video-only "<your youtube video url>"

Download in bulk
~~~~~~~~~~~~~~~~
If you want to download audios in bulk, please prepare a *csv* file containing all
the urls of the audios. Here is an example about how does this csv file look like.

.. list-table:: example-url-only.csv
   :widths: 25
   :header-rows: 1

   * - url
   * - https://www.youtube.com/watch?v=WqkjYKUXERQ
   * - https://www.youtube.com/watch?v=nOubjLM9Cbc

Here is the content of the example-url-only.csv file::

    url
    https://www.youtube.com/watch?v=WqkjYKUXERQ
    https://www.youtube.com/watch?v=nOubjLM9Cbc

In the csv file, you can also specify the *format*, *time_start*, *time_end* and *bitrate*
for each audio, such as

.. list-table:: example.csv
   :widths: 50 25 25 25 25 25
   :header-rows: 1

   * - url
     - format
     - time_start
     - time_end
     - fps
     - bitrate
   * - https://www.youtube.com/watch?v=WqkjYKUXERQ
     - mp3
     - 0
     -
     - 44100
     - 3000k
   * - https://www.youtube.com/watch?v=nOubjLM9Cbc
     - mp3
     - 3
     - 100
     - 200
     - 500k

Here is the content of the example.csv file::

    url,format,time_start,time_end,fps,bitrate
    https://www.youtube.com/watch?v=WqkjYKUXERQ,mp3,0,,44100,3000k
    https://www.youtube.com/watch?v=nOubjLM9Cbc,mp3,3,100,200,500k

To download all the audios from the urls listed in this file by calling::

    $ ytb_downloader_bulk example.csv

If you want to download the videos only, you need to provide a csv file with
one column *url*, and list all the urls you want to download in that column. Then
execute::

    $ ytb_downloader_bulk --video-only example.csv

Maintainers
-----------

..
    TODO: List here the people responsible for the development and maintaining of this project.
    Format: **Name** - *Role/Responsibility* - Email

* **Zhiwei Zhang** - *Maintainer* - `zhiwei2017@gmail.com <mailto:zhiwei2017@gmail.com?subject=[GitHub]Youtube%20Downloader>`_

.. _bandit: https://bandit.readthedocs.io/en/latest/
.. _mypy: https://github.com/python/mypy
.. _flake8: https://gitlab.com/pycqa/flake8
.. _pytest: https://docs.pytest.org/en/stable/
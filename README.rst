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

Download Audio
~~~~~~~~~~~~~~
Start downloading audio by calling::

    $ ytb_downloader "<your youtube video url>"

If you want to specify the format of the downloaded video, you can use the option
`--format` or `-f` with the format as string, such as::

    $ ytb_downloader --format "mp3" "https://www.youtube.com/watch?v=nOubjLM9Cbc"

For more details, please execute::

    $ ytb_downloader --help


Download Video
~~~~~~~~~~~~~~
Start downloading video by calling::

    $ ytb_downloader --video-only "<your youtube video url>"

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
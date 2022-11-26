import os
from distutils.text_file import TextFile
from pathlib import Path
from importlib import import_module
from setuptools import setup, find_packages

# Package meta-data.
NAME = 'ytb_downloader'
SHORT_DESCRIPTION = "Download youtube videos and convert them to mp3"
URL = "https://github.com/zhiwei2017/ytb_downloader"
AUTHOR = 'Zhiwei Zhang'
EMAIL = 'zhiwei2017@gmail.com'
LICENSE = 'MIT'


def _parse_requirements(filename):
    """Return requirements from requirements file."""
    setup_path = Path(__file__).resolve().parent.joinpath(filename)
    requirements = TextFile(filename=str(setup_path)).readlines()
    return [p for p in requirements if "-r" not in p]


try:
    VERSION = import_module(NAME+".version").__version__
except Exception as e:
    print("Version information cannot be imported using "
          "'importlib.import_module' due to {}.".format(e))
    about = dict()
    version_path = Path(__file__).resolve().parent.joinpath(NAME, "version.py")
    exec(version_path.read_text(), about)
    VERSION = about["__version__"]


try:
    # Load README as description of package
    with open('README.rst', encoding="utf-8") as readme_file:
        LONG_DESCRIPTION = readme_file.read()
except FileNotFoundError:
    LONG_DESCRIPTION = SHORT_DESCRIPTION


# Requirements
INSTALL_REQUIRED = _parse_requirements(os.path.join("requirements", "base.txt"))
# Optional requirements
DEV_REQUIRED = _parse_requirements(os.path.join("requirements", "dev.txt"))
DOC_REQUIRED = _parse_requirements(os.path.join("requirements", "doc.txt"))

# What packages are optional?
EXTRAS = {"docs": DOC_REQUIRED}


setup(name=NAME,
      version=VERSION,
      author=AUTHOR,
      author_email=EMAIL,
      description=SHORT_DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type='text/x-rst',
      license=LICENSE,
      url=URL,
      packages=find_packages(include=["ytb_downloader*"],
                             exclude=["tests*", "docs*"]),
      entry_points={
          'console_scripts': [
              'ytb_downloader = ytb_downloader.main:download_single',
              'ytb_downloader_bulk = ytb_downloader.main:download_bulk',
          ],
      },
      include_package_data=True,
      install_requires=INSTALL_REQUIRED,
      tests_require=DEV_REQUIRED,
      extras_require=EXTRAS,
      setup_requires=['wheel'])
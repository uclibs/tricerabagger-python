from glob import glob
from os import chdir, getcwd, remove
from re import sub
from drc.zipfix import ZipFix
import zipfile
import logging
import subprocess


class Unzip:
    """unzip all of the contents within the target folder"""

    def __init__(self, directory):
        self.target_directory = directory
        self.starting_directory = getcwd()

    def unzip(self):
        chdir(self.target_directory)

        zip_files = [file for file in glob("*.zip")]
        for zip_file in zip_files:
            self._unzip(zip_file)
        chdir(self.starting_directory)

    def _unzip(self, zip_file):
        directory = zip_file.split(".zip")[0]
        try:
            with zipfile.ZipFile(zip_file, "r") as zip_reference:
                logging.info(f"Unzipping {zip_file}")
                zip_reference.extractall(directory)
        except zipfile.BadZipFile:
            logging.warning(f"Bad file {zip_file} - fixing")
            ZipFix(zip_file).fix_file()

            with zipfile.ZipFile(zip_file, "r") as zip_reference:
                zip_reference.extractall(directory)
        remove(zip_file)

    def _fix_zip(self, zip_file):
        file_name = sub("\.zip$", ".fixed.zip", zip_file)
        subprocess.run(["zip", "-F", zip_file, "--out", file_name])
        return file_name

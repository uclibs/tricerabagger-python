from glob import glob
from os import chdir, getcwd, remove
import zipfile


class Unzip:
    """unzip all of the contents within the target folder"""

    def __init__(self, directory):
        self.target_directory = directory
        self.starting_directory = getcwd()

    def unzip(self):
        chdir(self.target_directory)

        zip_files = [file for file in glob("*.zip")]
        for zip_file in zip_files:
            with zipfile.ZipFile(zip_file, "r") as zip_reference:
                directory = zip_file.split(".zip")[0]
                zip_reference.extractall(directory)
            remove(zip_file)

        chdir(self.starting_directory)

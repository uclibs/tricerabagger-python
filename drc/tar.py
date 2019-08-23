import tarfile
from shutil import rmtree
from os.path import basename
import logging


class Tar:
    """tar and compress all of the contents of the target folder"""

    def __init__(self, directory, tarfile_name):
        self.target_directory = directory
        self.tarfile_name = tarfile_name
        self.basename = self.tarfile_name.split(".tar")[0]

    def tar(self):

        logging.info(f"Adding {self.target_directory} to {self.tarfile_name}")
        with tarfile.open(self.tarfile_name, "w") as tar:
            tar.add(self.target_directory, arcname=basename(self.basename))

        rmtree(self.target_directory)

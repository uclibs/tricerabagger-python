import zipfile
import subprocess
from os import rename


class ZipFix:
    """recursively fix a zip file until it is fixed"""

    def __init__(self, filepath):
        self.filepath = filepath
        self.zip_file = zipfile.ZipFile(self.filepath)

    def fix_file(self):
        while self._check_if_file_is_bad():
            self._zip_ff()

    def _check_if_file_is_bad(self):
        """test whether the zip is valid - returning False if it isn't, True if it is"""
        if self.zip_file.testzip() is None:
            return False
        else:
            return True

    def _zip_ff(self):
        tmppath = "tmp.zip"
        subprocess.run(["zip", "-FF", self.filepath, "--out", tmppath])
        rename(tmppath, self.filepath)
        self.zip_file = zipfile.ZipFile(self.filepath)

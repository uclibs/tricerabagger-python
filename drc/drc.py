from drc import unzip, bag, tar, push
from datetime import date
from os.path import dirname
from os import chdir, remove
from time import time
import logging


class Drc:
    """

    Accepts a DSpace 1.8 AIP export directory path
    
    * unzips the content
    * bags the content
    * tars the content
    * pushes it to AP Trust

    """

    def __init__(self, path, clean=False, production=False, push=True):
        today = str(date.today())
        timestamp = int(time())

        self.working_directory = dirname(path.rstrip("/"))
        self.identifier = path.rstrip("/").split("/")[-1]
        self.clean = clean
        self.production = production
        self.push = push
        self.tarfile_name = f"cin.dspace.{self.identifier}.{today}.tar"
        self.tarfile_path = f"{self.working_directory}/{self.tarfile_name}"

        logging.basicConfig(
            filename=f"./cin.dspace.{self.identifier}.{today}.{timestamp}.log",
            level=logging.INFO,
        )

    def run(self):
        chdir(self.working_directory)
        self._unzip()
        self._bag()
        self._tar()
        self._push()
        self._clean()

    def _unzip(self):
        unzip.Unzip(self.identifier).unzip()

    def _bag(self):
        bag.Bag(self.identifier).bag()

    def _tar(self):
        tar.Tar(self.identifier, self.tarfile_name).tar()

    def _push(self):
        if self.push:
            push.Push(self.tarfile_name, self.production).push()

    def _clean(self):
        if self.clean:
            remove(self.tarfile_path)

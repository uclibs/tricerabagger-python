from drc import unzip, bag, tar, push
from datetime import date
from os.path import dirname
from os import chdir, remove, getcwd
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

    def __init__(self, path, production=False, unzip=True, push=True, clean=False):
        today = str(date.today())
        timestamp = int(time())

        self.production = production
        self.push = push
        self.unzip = unzip
        self.clean = clean

        cwd = getcwd()
        self.config_paths = {
            "baginfo": f"{cwd}/drc/xsl/bagInfo.xsl",
            "aptrustinfo": f"{cwd}/drc/xsl/aptrustInfo.xsl",
        }
        self.working_directory = dirname(path.rstrip("/"))
        self.identifier = path.rstrip("/").split("/")[-1]
        self.tarfile_name = f"cin.dspace.{self.identifier}.{today}.tar"
        self.tarfile_path = f"{self.working_directory}/{self.tarfile_name}"

        logging.basicConfig(
            format="%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
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
        if self.unzip:
            unzip.Unzip(self.identifier).unzip()
        else:
            logging.info("Skipping unzip")

    def _bag(self):
        bag.Bag(self.identifier, self.config_paths).bag()

    def _tar(self):
        tar.Tar(self.identifier, self.tarfile_name).tar()

    def _push(self):
        if self.push:
            push.Push(self.tarfile_name, self.production).push()
        else:
            logging.info("Skipping push")

    def _clean(self):
        if self.clean:
            logging.info(f"Deleting {self.tarfile_path}")
            remove(self.tarfile_path)

from drc import unzip, bag, tar, push
from datetime import date
from shutil import rmtree


class Drc:
    """

    Accepts a DSpace 1.8 AIP export identifier
    
    * unzips the content
    * bags the content
    * tars the content
    * pushes it to AP Trust

    The identifier *must* be in the same directory as the script running this class

    """

    def __init__(self, identifier, clean=False, production=False):
        self.identifier = identifier
        self.clean = clean
        self.production = production
        today = str(date.today())
        self.tarfile_name = f"cin.dspace.{identifier}.{today}.tar"

    def run(self):
        self._unzip()
        self._bag()
        self._tar()
        self._push()

        if self.clean:
            rmtree(identifier)

    def _unzip(self):
        unzip.Unzip(self.identifier).unzip()

    def _bag(self):
        bag.Bag(self.identifier).bag()

    def _tar(self):
        tar.Tar(self.identifier, self.tarfile_name).tar()

    def _push(self):
        push.Push(self.tarfile_name, self.production).push()

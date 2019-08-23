from drc import drc
from shutil import copytree

copytree("./702759.backup", "./702759")
d = drc.Drc("./702759", push=True, clean=True)
d.run()
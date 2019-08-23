from drc import drc
import sys

d = drc.Drc(sys.argv[1], production=True, push=True, clean=True)
d.run()

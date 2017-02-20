import os
import glob

# Detect all modules
for fullname in glob.glob(os.path.dirname(__file__) + "/*.py"):
    name = os.path.basename(fullname)
    if name[:-3] == "__init__" or name[:-3] == "feature":
        pass
    else:
        __import__("hashdd.features." + name[:-3])


import os, shutil, re
from pathlib import Path
source1 = "C:/Users/alex"
source = os.path.join(source1,"aboba.txt")
dest = "C:/Users/alex/Desktop"
destination = shutil.move(source,dest)

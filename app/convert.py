import os
import zipfile
from shutil import rmtree


def unzip(file, dest):
    zip = zipfile.ZipFile(file)
    if os.path.isdir(dest):
        rmtree(dest)
    os.mkdir(dest)
    zip.extractall(dest)

    zip.close()

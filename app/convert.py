import os
import zipfile
from shutil import rmtree

def zipdir(file, dest):
    fantasty_zip = zipfile.ZipFile(file)
    dir = f'C:\\Users\\Александр\\PycharmProjects\\GoToHack_20_2\\tmp\\{dest}'
    if os.path.isdir(dir):
        rmtree(dir)
    os.mkdir(dir)
    fantasty_zip.extractall(dir)

    fantasty_zip.close()

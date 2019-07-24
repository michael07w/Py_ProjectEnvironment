import os

class Directory(object):

    def __init__(self, dir_name):
        self.dir_name = dir_name

    def createDir(self):
        path = "./" + self.dir_name
        print(path)
        os.mkdir(path)



class File(object):

    def __init__(self, file_name):
        self.file_name = file_name

    # Creates file and allows a path to be passed for creating file in subdir
    def createFile(self, path=""):
        f = open(path + self.file_name + ".py", "w+")
        f.close()

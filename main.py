import classes

def main():

    print("Please enter your desired project name:")
    proj_name = input("> ")

    # Creates necessary directories
    bin = classes.Directory("bin")
    bin.createDir()

    docs = classes.Directory("docs")
    docs.createDir()

    name = classes.Directory(proj_name)
    name.createDir()

    tests = classes.Directory("tests")
    tests.createDir()


    # Creates necessary files
    setup = classes.File("setup")
    setup.createFile()

    proj_init = classes.File("__init__")
    proj_init.createFile(proj_name + "/")

    tests_init = classes.File("__init__")
    tests_init.createFile("tests/")

    test_file = classes.File(proj_name + "_tests")
    test_file.createFile("tests/")


if __name__ == '__main__':
    main()

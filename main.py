import classes

def main():

    print("Please enter your desired project name:")
    proj_name = input("> ")

    # Creates necessary directories
    print("Creating Directories...")

    bin_dir = classes.Directory("bin")
    bin_dir.createDir()

    docs_dir = classes.Directory("docs")
    docs_dir.createDir()

    name_dir = classes.Directory(proj_name)
    name_dir.createDir()

    tests_dir = classes.Directory("tests")
    tests_dir.createDir()


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

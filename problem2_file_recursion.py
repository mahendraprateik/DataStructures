"""
Finding Files:
For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"
Here is an example of a test directory listing, which can be downloaded here:
./testdir ./testdir/subdir1 ./testdir/subdir1/a.c ./testdir/subdir1/a.h ./testdir/subdir2 ./testdir/subdir2/.gitkeep ./testdir/subdir3 ./testdir/subdir3/subsubdir1 ./testdir/subdir3/subsubdir1/b.c ./testdir/subdir3/subsubdir1/b.h ./testdir/subdir4 ./testdir/subdir4/.gitkeep ./testdir/subdir5 ./testdir/subdir5/a.c ./testdir/subdir5/a.h ./testdir/t1.c ./testdir/t1.h Python's os module will be useful—in particular, you may want to use the following resources:
os.path.isdir(path)
os.path.isfile(path)
os.listdir(directory)
os.path.join(...)
Note: os.walk() is a handy Python method which can achieve this task very easily. However, for this problem you are not allowed to use os.walk().
Here is some code for the function to get you started:
"""

import os


def main():
    files = find_files_root("/Users/prateikmahendra/Downloads/testdir/")
    print("Files with suffix \".c\" are: ", files)


def find_files_root(root):
    """
    Function that calls the recursive function find_files

    Parameters:
    root (str): The root dir to begin with

    Returns:
    A list of paths with the suffix ".c"
    """
    if not os.path.isdir(root):
        return -1
    files = find_files(".c", root)
    return files


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    if type(path) != str:
        print("Please enter a valid path in the form of string")
        return

    if not os.path.isdir(path):
        print("Please enter a valid path")
        return

    contents = os.listdir(path)

    if not contents:
        return

    li = list()

    for content in contents:
        content_path = os.path.join(path, content)

        if os.path.isfile(content_path) and content.endswith(suffix):
            li.append(content_path)

        elif os.path.isdir(content_path):
            #Recusrion happens when we hit a subdirectory
            files = find_files(suffix, content_path)
            li.extend(files)

        else:
            pass

    return li


if __name__ == "__main__":
    main()


# Test cases - Regular

print(find_files('.c', '/Users/prateikmahendra/Downloads/testdir/'))
"""
['/Users/prateikmahendra/Downloads/testdir/subdir3/subsubdir1/b.c',
'/Users/prateikmahendra/Downloads/testdir/t1.c',
'/Users/prateikmahendra/Downloads/testdir/subdir5/a.c',
'/Users/prateikmahendra/Downloads/testdir/subdir1/a.c']
"""

print(find_files('.c', '/Users/prateikmahendra/Downloads/testdir/subdir3'))
# ['/Users/prateikmahendra/Downloads/testdir/subdir3/subsubdir1/b.c']

print(find_files('.c', '/Users/prateikmahendra/Downloads/testdir/t1.c'))
# None

print(find_files('.c', '/Users/prateikmahendra/Downloads/testdir/subdir2'))
# []

# Test cases - Edge

# Empty path string
print(find_files('.c', ''))
# None

print(find_files('.c', 'gibberish'))
# None

# Random int instead of path
print(find_files('.c', 12345))

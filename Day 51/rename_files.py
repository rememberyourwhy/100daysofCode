import os
import glob
import re

FOLDER = r'C:\Users\Hii\Downloads\lwt\To_import\English\LingQ\A1\Who_is_she\Audio\\'


def mass_rename():

    count = 1
    # count increase by 1 in each iteration
    # iterate all files from a directory
    for file_name in sorted(os.listdir(FOLDER), key=lambda x: int(re.search("[0-9]+", x).group())):
        # Construct old file name
        source = FOLDER + file_name

        # Adding the count to the new file name and extension
        destination = FOLDER + str(count) + ".mp3"

        # Renaming the file
        print(f"SOURCE: {source}")
        print(f"DESTINATION: {destination}")
        os.rename(source, destination)
        count += 1
    print('All Files Renamed')

    print('New Names are')
    # verify the result
    res = sorted(os.listdir(FOLDER), key=lambda x: int(re.search("[0-9]+", x).group()))
    print(res)


# def test_glob():
#     print(sorted(glob.glob(r'C:\Users\Hii\Downloads\lwt\To_import\Korean\LingQ\A1\Who_is_she\Audio\*')))


mass_rename()


#
# filenames = [
#     "1.txt",
#     "2.123131.txt",
#     "40_123123.txt",
#     "4.txt",
#     "3.txt",
#     "10.df232297b785.txt"
#
# ]
# new_filenames = list()
# count = 1
# for file_name in sorted(filenames, key=lambda x: int(re.search("[0-9]+", x).group())):
#     new_name = f"{count}.txt"
#     new_filenames.append(new_name)
#     count += 1
# print(new_filenames)


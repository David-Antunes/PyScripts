import os
import sys


# Obtains the name of all the files where this program is present, then cleans the array leaving only directories
def getSubDirectory():
    #Gets all the file names
    list = os.listdir()

    # Cleans the array leaving only the name of the directories in them
    folder = []

    for file in list:

        if os.path.isdir(file):
            folder.append(file)

    return folder
# Verifies if the first 3 characters of the string correspond to numbers. Returns True if there is 2 numbers and a space. False otherwise.
def verifyNumber(number):
    try:
        int(number[0])
        int(number[1])
        if number[2] != " " and number[3] != "-" and number[4] != " ":
            return False

        return True
    except ValueError:
        return False
    except IndexError:
        return False

def  main():

    if len(sys.argv) > 1 and sys.argv[1] == "update":

        folders = getSubDirectory()
        if len(folders) <= 99:
            i = [0,0]
            for dir in folders:
                num_tag = dir[0:5]

                new_name = ""
                if verifyNumber(num_tag):
                    new_name = dir[5:]
                else:
                    new_name = dir
                os.rename(dir, str(i[0]) + str(i[1]) + " - " + new_name)

                i[1] += 1
                if i[1] == 10:
                    i[1] = 0
                    i[0] += 1
                if i[0] == 10:
                    i[0] = 0
                    i[1] = 0
        print("Done.")
    else:
         print("Miss click.")

if __name__ == "__main__":
    main()

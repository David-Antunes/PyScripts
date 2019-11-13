import os
import sys
import shutil

def isInt(value):
    try:
        int(value)
        return True
    except:
        return False

def searchOutputNum(value, output):
    position = 0

    for file in output:
        fileNum = file[len("output"):]
        if value == int(fileNum):
            break
        else:
            position += 1

    return position

def main():

    files = os.listdir()

    inputs = []
    outputs = []

    for file in files:
        if "input" in file:
            if isInt(file[len("input")]):
                inputs.append(file)
        elif "output" in file:
            if isInt(file[len("output")]):
                outputs.append(file)

    if len(inputs) > 0 and len(outputs) > 0 and len(inputs) == len(outputs):
        pos = 0
        for file in inputs:
            fileNum = file[5:]
            dirName = "test" + fileNum
            os.mkdir(dirName)
            shutil.move(file, dirName)
            shutil.move(outputs[pos], dirName)
            pos += 1


if __name__ = "__main__":
    main()
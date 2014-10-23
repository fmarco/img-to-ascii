# -*- coding: utf-8 -*-

# Author: Marco Federighi


import argparse

from PIL import Image

mode = ["1", "L"]

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help='filename')
    parser.add_argument("scale", help='grayscale or black-and-white')
    args = parser.parse_args()
    try:
        if not args.scale in mode:
            raise Exception("Wrong scale!")
        im = Image.open(args.filename)
        pix = im.load()
        im = im.convert(str(args.scale))
        res = ""
        for i in range(0, im.size[1]):
            for j in range(0, im.size[0]):
                if pix[j, i][1] != 0:
                    res = "".join((res, "*"))
                else:
                    res = "".join((res, "0"))
                if j == im.size[0] - 1:
                    res = "".join((res, "\n"))
        with open("output.txt", "w") as f:
            f.write(res)
            print "Output created!"
    except IOError:
        print "The file doesn't exist!"


if __name__ == "__main__":
    main()
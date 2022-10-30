from Utilities import *

import argparse, os
import zlib

from dat import *

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--Input")
    parser.add_argument("-o", "--Output")
    parser.add_argument("-d", "--Decompression", action="store_true")
    parser.add_argument("-c", "--Compression", action="store_true")

    args = parser.parse_args()

    if args.Input:

        path_to_file =  args.Input.split("\\")[-1]
        filename = os.path.splitext(path_to_file)[0]
        file_size = os.path.getsize(args.Input)

        try:
            with open(args.Input, "rb") as f_in:
                br = BinaryReader(f_in, "<")

                if args.Decompression : 

                    data = br.readBytes(file_size)
                    data = crypt(bytearray(data), file_size)
                    data = zlib.decompress(data)

                    if args.Output == None:
                        f_out = open(filename + "_decompressed.dat", "wb")
                    else:
                        f_out = open(args.Output + "//" + filename + "_decompressed.dat", "wb")

                elif args.Compression :

                    data = br.readBytes(file_size)
                    data = zlib.compress(data)
                    data = crypt(bytearray(data), len(data))

                    if args.Output == None:
                        f_out = open(filename + "_compressed.dat", "wb")
                    else:
                        f_out = open(args.Output + "//" + filename + "_compressed.dat", "wb")

                else :
                    pass

                f_out.write(data)
                f_out.close()

                print("Done")

        except IOError:
            print('Error While Opening the file!')


if __name__ == "__main__":
    main()
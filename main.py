from Utilities import *

import argparse, os
import zlib

from dat import *

def main():

    """
    path_to_file =  "E:\\MODDING\\Archive\\_Ace Combat\\Ace Combat 7\\Localization\\_Game\\C.dat"
    filepath = os.path.splitext(path_to_file)[0]
    filename = os.path.basename(filepath)
    file_size = os.path.getsize(path_to_file)
    if len(filename) == 1:
        file_size_for_crypt = file_size + ord(filename) - 65 
    else:
        file_size_for_crypt = file_size

    f_in = open(path_to_file, "rb")
    
    br = BinaryReader(f_in, "<")
    data = br.readBytes(file_size)
    data = crypt(bytearray(data), file_size_for_crypt)
    
    f_in.close()

    f_out  = open(filepath + "_decrypt.dat", "wb")
    f_out.write(data)
    f_out.close()
    """
    
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
                    if "Cmn" not in filename:
                        file_size_for_crypt = file_size + ord(filename[0]) - 65
                    else:
                        file_size_for_crypt = file_size
                    data = crypt(bytearray(data), file_size_for_crypt)
                    data = zlib.decompress(data)

                    if args.Output == None:
                        f_out = open(filename + "_decrypted.dat", "wb")
                    else:
                        f_out = open(args.Output + "//" + filename + "_decrypted.dat", "wb")

                elif args.Compression :

                    data = br.readBytes(file_size)
                    data = zlib.compress(data)
                    if "Cmn" not in filename:
                        file_size_for_crypt = len(data) + ord(filename[0]) - 65
                    else:
                        file_size_for_crypt = len(data)
                    data = crypt(bytearray(data), file_size_for_crypt)

                    if args.Output == None:
                        f_out = open(filename + "_crypted.dat", "wb")
                    else:
                        f_out = open(args.Output + "//" + filename + "_crypted.dat", "wb")

                else :
                    pass

                f_out.write(data)
                f_out.close()

                print("Done")

        except IOError:
            print('Error While Opening the file!')


if __name__ == "__main__":
    main()
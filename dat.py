from Utilities import *

def crypt(data, file_size):

    eax = file_size
    ebx = 0
    ecx = 0
    edi = file_size
    position = 0 # r12d
    r15 = 0

    while position < file_size:
        
        ecx = ebx * 8
        position += 1
        ecx ^= ebx
        eax = ebx + ebx
        ecx = ~ecx
        edi = edi + edi * 4
        ecx >>= 7
        r15 += 1
        ecx &= 1
        edi += 1
        ebx = ecx

        ebx |= eax

        eax = ebx

        eax = ToUnsignedByte(eax) + ToUnsignedByte(edi & 0xFF)
        data[r15 - 1] = data[r15 - 1] ^ ToUnsignedByte(eax)
        #print(data[r15 - 1])

        eax = file_size
        ecx = position

    return data


        
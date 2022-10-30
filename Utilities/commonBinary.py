def ToSignedByte(byte):
    if byte > 127:
        return -(256 - byte) & 0xFF
    else:
        return byte

def ToUnsignedByte(byte):
    if byte > 255:
        return byte - 256 & 0xFF
    else:
        return byte

def ToUnsignedInt(integer):
    if integer > 4294967295:
        return integer - 4294967296 & 0xFF
    else:
        return integer
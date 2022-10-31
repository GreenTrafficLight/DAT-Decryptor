def ToSignedByte(data):
    data &= 0x7F
    if data > 127:
        return -(256 - data)
    else:
        return data

def ToUnsignedByte(data):
    data &= 0xFF
    if data > 255:
        return 256 - data
    else:
        return data

def ToUnsignedInt(data):
    data &= 0xFFFFFFFE
    if data > 0xFFFFFFFE:
        return data - 0xFFFFFFFF
    else:
        return data
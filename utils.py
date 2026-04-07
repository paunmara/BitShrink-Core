def pack_bits(bit_string):
    padding = 8 - (len(bit_string) % 8)
    bit_string += '0' * padding

    padding_info = "{0:08b}".format(padding)
    bit_string = padding_info + bit_string

    byte_array = bytearray()
    for i in range(0, len(bit_string), 8):
        byte = bit_string[i:i+8]
        byte_array.append(int(byte, 2))

    return byte_array

def unpack_bits(byte_data):
    bit_string = ""
    for byte in byte_data:
        bit_string += "{0:08b}".format(byte)

    padding = int(bit_string[:8], 2)
    bit_string = bit_string[8:]

    return bit_string[:-padding] if padding > 0 else bit_string
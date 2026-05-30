def caesar_ch(alphabet, shift):
    ascii_val = ord(alphabet)
    if 65 <= ascii_val <= 90:
        return chr((ascii_val - 65 + shift) % 26 + 65)
    elif 97 <= ascii_val <= 122:
        return chr((ascii_val - 97 + shift) % 26 + 97)
    else:
        return alphabet


def caesar_encode(text, shift=3):
    result = ""
    for c in text:
        result += caesar_ch(c, shift)
    return result


def caesar_decode(text, shift=3):
    result = ""
    for c in text:
        result += caesar_ch(c, -shift)
    return result


def main():
    original = "ABCdef, World!"
    encoded = caesar_encode(original, 3)
    decoded = caesar_decode(encoded, 3)

    print(encoded)
    print(decoded)


if __name__ == '__main__':
    main()
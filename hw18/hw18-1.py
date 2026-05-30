def toggle_ch(alphabet):
    ascii_val = ord(alphabet)
    if 65 <= ascii_val <= 90:
        return chr(ascii_val + 32)
    elif 97 <= ascii_val <= 122:
        return chr(ascii_val - 32)
    else:
        return alphabet

def toggle_text(text):
    result = []
    for c in text:
        result.append(toggle_ch(c))
    return "".join(result)

def main():
    print(ord("a"))
    print(ord("A"))
    print(ord("z"))
    print(ord("Z"))
    print(chr(65))
    print(toggle_ch("A"))
    print(toggle_ch("b"))
    print(toggle_text("Hello, World!"))

if __name__ == '__main__':
    main()
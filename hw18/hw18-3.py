import random


def get_chosung_ch(char):
    chosung_list = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    if '가' <= char <= '힣':
        unicode_val = ord(char) - 44032
        chosung_index = unicode_val // 588
        return chosung_list[chosung_index]
    else:
        return char


def get_chosung(text):
    result = ""
    for c in text:
        result += get_chosung_ch(c)
    return result


def main():
    words = ["사과", "바나나", "파이썬", "노트북", "자동차"]
    target_word = random.choice(words)
    chosung = get_chosung(target_word)

    print(f"[초성 게임 시작] 제시어: {chosung}")
    user_answer = input("정답을 입력하세요: ")

    if user_answer == target_word:
        print("정답입니다!")
    else:
        print(f"틀렸습니다. 정답은 [{target_word}]입니다.")


if __name__ == '__main__':
    main()
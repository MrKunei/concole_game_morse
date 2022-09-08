import random

english_to_morse = {
  "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
  "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
  "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.",
  "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
  "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
  "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
  "y": "-.--", "z": "--..", ".": ".-.-.-", ",": "--..--", "?": "..--..",
  "!": "-.-.--", "-": "-....-", "/": "-..-.", "@": ".--.-.", "(": "-.--.",
  ")": "-.--.-"
}
eng_words = ['python', 'code', 'study', 'list', 'snake', 'word', 'brainstorm']
answers = []

def morse_encode(word):
    morse = []
    for letter in word:
        if letter in english_to_morse:
            morse.append(english_to_morse[letter])
    return ''.join(morse)

def get_word():
    word = random.sample(eng_words, 1)[0]
    return word


def print_statistics(answers):
    all_answers = len(answers)
    true_answers = answers.count(True)
    false_answers = answers.count(False)
    print(f"\n")
    print(f'Всего ответов: {all_answers}')
    print(f"Отвечено верно: {true_answers}")
    print(f"Отвечено неверно: {false_answers}")


def start_game():
    print("Добро пожаловать в игру!")
    name = input("Введите имя ")
    print(f"Привет, {name.upper()}! "
          f"Сегодня мы потренируемся расшифровывать морзянку.")
    input("Нажмите Enter и начнем")

    i = 1

    while True:
        word = get_word()
        print(f"Слово {i}: {morse_encode(word)}")
        answer = input("Введите перевод: ")
        answer = answer.replace(" ", "")
        if answer != "stop":
            if answer.lower() == word:
                answers.append(True)
                print(f"Верно, {word}!")
            else:
                answers.append(False)
                print(f"Неверно, {word}!")
            i += 1
        else:
            break
    print_statistics(answers)

start_game()



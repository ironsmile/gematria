#!/usr/bin/env python

import argparse
import math
import sys

alphabets = {
    "he": {
        "א": 1,
        "ב": 2,
        "ג": 3,
        "ד": 4,
        "ה": 5,
        "ו": 6,
        "ז": 7,
        "ח": 8,
        "ט": 9,
        "י": 10,
        "כ": 11,
        "ל": 12,
        "מ": 13,
        "נ": 14,
        "ס": 15,
        "ע": 16,
        "פ": 17,
        "צ": 18,
        "ק": 19,
        "ר": 20,
        "ש": 21,
        "ת": 22,
        "ך": 23,
        "ם": 24,
        "ן": 25,
        "ף": 26,
        "ץ": 27,
    },

    "bg": {
        "а": 1,
        "б": 2,
        "в": 3,
        "г": 4,
        "д": 5,
        "е": 6,
        "ж": 7,
        "з": 8,
        "и": 9,
        "й": 10,
        "к": 11,
        "л": 12,
        "м": 13,
        "н": 14,
        "о": 15,
        "п": 16,
        "р": 17,
        "с": 18,
        "т": 19,
        "у": 20,
        "ф": 21,
        "х": 22,
        "ц": 23,
        "ч": 24,
        "ш": 25,
        "щ": 26,
        "ь": 27,
        "ъ": 28,
        "ю": 29,
        "я": 30,
    },

    "en": {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
    },
}

def letterToNumber(x):
    return (math.pow(10, math.floor((x-1)/9))) * (((x-1) % 9) + 1)

def nameToNumber(name, language):
    sum = 0
    for letter in name.lower():
        if letter in [' ', '']:
            continue
        sum += int(letterToNumber(alphabets[language][letter]))
    return sum

def main():
    parser = argparse.ArgumentParser(description='Show gematria or a name in some languages.')
    parser.add_argument('names', metavar='N', type=str, nargs='*',
                    help='names to be converted')
    parser.add_argument('--lang',
                    help='possible languages: ' + ",".join(alphabets.keys()),
                    default="bg")

    args = parser.parse_args()

    if not args.lang in alphabets:
        print('Language {} is not supported.'.format(args.lang))
        sys.exit(1)

    if len(args.names) > 0:
        for name in args.names:
            print("{}: {}".format(name, nameToNumber(name, args.lang)))
        sys.exit(0)

    lang = args.lang

    selectedLang = None

    while not selectedLang in alphabets:
        if selectedLang == '':
            break
        selectedLang = input("Select language. possible [{}] default [{}]: ".format(
            ",".join(alphabets.keys()), lang))

    if selectedLang is not None and selectedLang != '':
        lang = selectedLang

    name = None

    while True:
        name = input("input name: ")
        if name == '':
            break
        print("{}: {}".format(name, nameToNumber(name, lang)))

if __name__ == "__main__":
    main()

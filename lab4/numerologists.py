converter = {
    "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10,"k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26
}
def word_to_value(word):
    word = word.lower()
    value = 0
    letters = [letter for letter in word] # adds each letter to a list
    for letter in letters:
        if letter in converter:
            value += converter[letter] # flips the value from a char to a int given in the converter dictionary and adds it to the value
    return value

print(word_to_value(input("Enter a word and convert it to a value: ")))

# Does the same thing asked in 1.3 numerologists-extended
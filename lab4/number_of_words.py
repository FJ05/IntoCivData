def word_counter(sentence):
    sentence = sentence.lower()
    count = 0
    
    index = 0
    letters = [letter for letter in sentence] # adds each letter to a list
    for letter in letters:
        if index == 0 and letter in list("abcdefghijklmnopqrstuvwxyz"):
            count += 1 # adds 1 if the there exists a letter in the begining of the sentence
        if letters[index - 1] == " ":
            count += 1
        index += 1
    
    return count

print(word_counter(input("Enter a sentence: ")))
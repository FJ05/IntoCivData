def average_length_calc(sentence):
    sentence = sentence.lower()
    word_count = 0
    valid_letter_count = 0
    
    sentence_list = list(sentence)
    if sentence_list[0] in list("abcdefghijklmnopqrstuvwxyz"):
        word_count += 1 # gives +1 to word_count of the first word is valid
    word_count += sentence_list.count(" ") # detects the amount of words dependning on spaces
    
    letters = [letter for letter in sentence] # adds each letter to a list
    for letter in letters:
        if letter in list("abcdefghijklmnopqrstuvwxyz"):
            valid_letter_count += 1
            
    return valid_letter_count / word_count
print("Average letters is: ", average_length_calc(input("Enter a sentence: ")))
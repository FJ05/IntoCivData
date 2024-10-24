def convert_to_acronym(word):
    
    res = [] # This will be the result that we later convert to a string
    index = 0
    res.append((list(word)[0])) # Adds the first letter in the word to res
    
    letters = [letter for letter in word] # converts string into a char list
    for letter in letters:
        if letter == ' ':
            res.append(letters[index + 1]) # If there is a space add the index after the space to res
        index += 1
    result = (''.join(res)).upper() # Joins the list and converts it to uppercase
    return result
print(convert_to_acronym(input("Write your word that's going to be converted into an acronym: ")))
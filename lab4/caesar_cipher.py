converter = {
    "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10,"k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26
}
reverse_converter = {v: k for k, v in converter.items()} # Will be used for getting the keys from converter

def caesar_ciper(word:str, key:int):
    word = word.lower()
    output_list = [] # this is the array that will store the chars of the output. this will later be converted into a string at the return
    letters = [letter for letter in word] # adds each letter to a list
    for letter in letters:
        if letter in converter:
            index = converter[letter] + key
            
            if index > 26: # makes sure that the index is in the range of 26 
                while index > 26:
                    index -= 26
                    
            output_list.append(reverse_converter[index])
        else:
            output_list.append(letter) # if the letter is outside of the converter it will still be outputet. stuff like spaces and !,?.åäö will still count twoards the output
        
    
    return ''.join(output_list)

print(caesar_ciper(input("input your word: "), int(input("input your key [int]: "))))
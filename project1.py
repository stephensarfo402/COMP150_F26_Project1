# Project 1 Template Code
# Written by Jasmine Lu 2026


import sys
cipher = { 
    'A': 'P',
    'B': 'A',
    'C': 'N',
    'D': 'D',
    'E': 'Z',
    'F': 'Y',
    'G': 'X',
    'H': 'W',
    'I': 'V',
    'J': 'U',
    'K': 'T',
    'L': 'S',
    'M': 'R',
    'N': 'Q',
    'O': 'O',
    'P': 'M',
    'Q': 'L',
    'R': 'K',
    'S': 'J',
    'T': 'I',
    'U': 'H',
    'V': 'G',
    'W': 'F',
    'X': 'E',
    'Y': 'C',
    'Z': 'B'
} # Our cipher dictionary, created using the keyword PANDA. 
# Duplicate letters were removed from PANDA and the remaining unused letters were added in reverse alphabetical order.

def encode(message): # The function we use to encode the message 
    encoded_message = '' # Where we are going to store the encoded message 

    for letter in message: # Looks throgh each character(letter) of the message one at a time
        if letter == ' ': # Checks to see if that character(letter) is a space 
            encoded_message += ' ' # If it is a space, it adds a space to the encoded message
        else: # If its not a space
            encoded_message += cipher[letter] # Turns the original letter of the message into the encoded letter EX. will turn 'A' to 'P'

    return encoded_message # Returns the encoded message 
	

def decode(encoded_msg, cipher):  # Decodes an encoded message using our cipher dictionary
    decoded_message = ''  # Empty string where we will build and store the decoded message

    for letter in encoded_msg:  # Looks at each character in the encoded message one at a time
        if letter == ' ':  # Checks whether the current character is a space
            decoded_message += ' '  # If it is a space, keep the space in the decoded message
        else:
            found = False  # Keeps track of whether the encoded letter was found as a value in our cipher

            for key, val in cipher.items():  # Looks through each key-value pair in our cipher dictionary
                if letter == val:  # Checks whether the encoded letter matches a value in the dictionary
                    decoded_message += key  # If it does, add the corresponding original letter (key)
                    found = True  # Records that we successfully decoded the letter using a value

            if found == False:  # If the letter was not found as a value, check whether it is a key
                if letter in cipher.keys():  # Checks whether the encoded letter is a key in the dictionary
                    decoded_message += cipher[letter]  # Adds the value associated with that key

    return decoded_message  # Returns the complete decoded message



def helpus(encoded_msg):  # Counts how many times each letter appears in an encoded message
    letter_count = {}  # Empty dictionary where each letter will be stored with its count

    for letter in encoded_msg:  # Looks at each character in the encoded message one at a time
        if letter != ' ':  # Ignores spaces because we only want to count letters
            if letter in letter_count.keys():  # Checks whether we have already seen this letter
                letter_count[letter] += 1  # If we have, increase its count by 1
            else:  # If this is the first time we have seen the letter
                letter_count[letter] = 1  # Add the letter to the dictionary with a starting count of 1

    return letter_count  # Returns the dictionary of letters and how many times each one appears

def double_letters(encoded_msg):  # Finds identical letters that appear directly next to each other
    doubles = []  # Empty list where we will store any double-letter combinations we find

    for i in range(len(encoded_msg) - 1):  # Looks through the message while stopping before the final character
        if encoded_msg[i] != ' ':  # Makes sure the current character is not a space
            if encoded_msg[i] == encoded_msg[i + 1]:  # Checks whether the current letter matches the next letter
                doubles.append(encoded_msg[i] + encoded_msg[i + 1])  # Adds the double-letter pair to the list

    return doubles  # Returns all double-letter combinations found in the encoded message

def word_pattern(word):  # Shows the repeated-letter pattern of an encoded word
    pattern_dict = {}  # Stores each new letter and the number assigned to it
    pattern = []  # Empty list where we will build the word pattern
    next_number = 1  # Number that will be assigned to the next new letter we find

    for letter in word:  # Looks at each letter in the word one at a time
        if letter not in pattern_dict.keys():  # Checks whether we have seen this letter before
            pattern_dict[letter] = next_number  # Gives a new number to a letter we have not seen yet
            next_number += 1  # Increases the number so the next new letter gets a different number

        pattern.append(pattern_dict[letter])  # Adds the letter's assigned number to the pattern

    return pattern  # Returns the completed repeated-letter pattern



# No need to change these last sections. They are just for easily running your functions via the command line.
if __name__ == "__main__":
    if sys.argv[1] == 'encode':
    	print(encode(sys.argv[2]))
    elif sys.argv[1] == 'decode':
    	print(decode(sys.argv[2], eval(sys.argv[3])))

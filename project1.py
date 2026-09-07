# Project 1 Template Code
# Written by Jasmine Lu 2026

import sys

'''
 Takes a message and uses a ‘secret’ cipher to encode the message

 Parameters: message - a String message of your choosing
 Returns: an encoded String message
'''
def encode(message):
	# Write your code here
	return message

'''
Takes an encoded_msg and uses a cipher to decode the message

Parameters: encoded_msg - a String message that has been encoded with a cipher
			cipher - a dict that scrambles the cipher message. Note: This should come in the format of {'A': 'Z', 'B': 'Y', 'C': 'X'} and so on.
Returns: a decoded message (in normal English)
'''
def decode(encoded_msg, cipher):
	# Write your code here
	message = ''
	return message


# Below you should write functions to help you during class time decode your team's messages.
# Consider what letters might be the most common in messages and might be easy to identify even when in a secret code
# Feel free to look up strategies that help with these cipher puzzles
# Make sure to write a comment explaining how your helper functions work
# Feel free to create functions other than helper() (like a helper1, helper2, etc. and name them whatever you want)

def helper(encoded_msg):
	print("Modify this function to actually be helpful in decoding this message: " + encoded_msg)


# No need to change these last sections. They are just for easily running your functions via the command line.
if __name__ == "__main__":
    if sys.argv[1] == 'encode':
    	print(encode(sys.argv[2]))
    elif sys.argv[1] == 'decode':
    	print(decode(sys.argv[2], eval(sys.argv[3])))
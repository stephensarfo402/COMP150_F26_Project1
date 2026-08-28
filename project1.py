# Project 1 Template Code
# Written by Jasmine Lu 2026


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

def helper(encoded_msg):
	print("Modify this function to actually be helpful in decoding this message: " + encoded_msg)
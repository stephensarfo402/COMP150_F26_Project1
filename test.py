# Project 1 Test Code
# Written by Jasmine Lu 2026


# Run these tests on the terminal with python3 test.py

from project1 import *

'''
	Tests to make sure your encode function isn't just returning the same message. Returns T/F based on test success.
'''
def test0_encode():
	msg = 'THIS IS A TEST MESSAGE'
	enc_msg = encode(msg)

	if enc_msg == msg:
		return False
	else:
		return True

'''
	Tests to make sure every time you run the encode function on a message, you get the same output. Returns T/F based on test success.
'''
def test1_encode():
	msg = 'THIS IS A TEST MESSAGE'
	enc_msg0 = encode(msg)
	enc_msg1 = encode(msg)

	if enc_msg0 != enc_msg1:
		return False
	else:
		return True


'''
	Tests to make sure your encode function isn't just returning an empty message (template code). Returns T/F based on test success.
'''
def test0_decode():
	msg = 'KILUVHHLI OF SZH GDL XZGA'
	cipher = {'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V', 'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q', 'K': 'P', 'L': 'O', 'M': 'N', 'N': 'M'}
	enc_msg = decode(msg, cipher)

	if enc_msg == '':
		return False
	else:
		return True

'''
	Tests to make sure your decode function works for the example cipher in the project 1 specifications. Returns T/F based on test success.
'''

def test1_decode():
	msg = 'KILUVHHLI OF SZH GDL XZGA'
	cipher = {'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V', 'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q', 'K': 'P', 'L': 'O', 'M': 'N', 'N': 'M'}
	enc_msg = decode(msg, cipher)

	if enc_msg == 'PROFESSOR LU HAS TWO CATS':
		return True
	else:
		return False


passed_tests = 0
total_tests = 4

if test0_encode():
	passed_tests += 1
	print('Passed Test 0 Encode')
else:
	print('test0_encode failed. Check your project1.py encode function and make sure you are not returning the same message as the input message.')

if test1_encode():
	passed_tests += 1
	print('Passed Test 1 Encode')
else:
	print('test1_encode failed. Make sure that your encode function is deterministic - there cannot be a random element to your cipher')

if test0_decode():
	passed_tests += 1
	print('Passed Test 0 Decode')
else:
	print('test0_decode failed. Check your project1.py encode function and make sure you are not returning the same message as the input message.')

if test1_decode():
	passed_tests += 1
	print('Passed Test 1 Decode')
else:
	print('test1_decode failed. Check to make sure you swap letters according to the given cipher correctly')






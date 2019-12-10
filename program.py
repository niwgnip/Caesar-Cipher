
import string
#deciding what to do
def decideMode():
	print ("\nWhat do you want to do?")
	print ("0. Code message.")
	print ("1. Decode message.")
	print ("2. Brute force message.")
	print ("3. Exit")
	while True:
		try:
			decision = int(input())
			if decision > -1 and decision <4:
				break
		except ValueError:
			print("Invalid input - must be integer")
		else:
			print ("Invalid - must be between 0-2")
	return decision
#taking message to code/decode
def user_message():
	print("Please provide your sentence:\n")
	return str(input())
# taking the key from user
def input_key():
	print("Please provide a caesar_key (int number between 1-25)")
	# While loop to check if ceasar key value is correct
	while True:
		try:
			caesar_key = int(input())
			if caesar_key > 0 and caesar_key < 26:
				break
		except ValueError:
			print("Invalid input - must be integer")
		else:
			print ("Invalid - must be between 1 and 25")
	return caesar_key

#fuction for coding word with Caesar Cipher - by me
def translateMyWay(mode,message,input_key):
	#dictionary for alphabet -> [1:a, 2:b..... 26:z]
	dict_values = list(string.ascii_lowercase)
	dict_keys = (range(1,27,1))
	dictionary = dict(zip(dict_keys,dict_values))
	coded_message =''
	#checking position (key and value) for each letter of word
	for x in message.lower():
		for key, letter in dictionary.items():
			#if letter is not alphabetical, then just rewrite it
			if x.isalpha() == False:
				coded_message += x
				break
			#if letter is alphabetical and the mode is CODING, then change it to letter that corresponds to key + input number value
			elif x == letter and mode == 0:
				check = key + input_key
				if check <27:
					new_key = key + input_key
				# if key is > 27, substract 26 so the change from  'z' -> 'a' will happen
				else:
					new_key = key + input_key - 26
				coded_message += dictionary[new_key]
			#if letter is alphabetical and the mode is DECODING, then change it to letter that corresponds to key - input number value
			elif x == letter and mode == 1:
				check = key - input_key
				if check > 0:
					new_key = key - input_key
				else:
					# if key is < 0, add 26 so the change from  'a' -> 'z' will happen
					new_key = key - input_key + 26
				coded_message += dictionary[new_key]
					
	return (coded_message)

#Second way to encrypt/decrypt - based on materials found on the web, more advanced and with using ord() chr()
#Saved in order to have both ways in one place for future
def translateOtherWay(mode, message,input_key):
	if mode == 1 or mode == 2:
		input_key = -input_key
	coded = ''

	for x in message:
		if x.isalpha():
			letter = ord(x)
			letter += input_key

			if x.islower():
				if letter > ord ('z'):
					letter -=26
				elif letter < ord('a'):
					letter += 26
			elif x.isupper():
				if letter > ord('Z'):
					letter -=26
				elif letter < ord('A'):
					letter +=26

			coded += chr(letter)
		else:
			coded += x
	return coded
		
#start of code
run = True
while run:
	x = decideMode()
	
	if x == 0 or x == 1:
		m = user_message()
		k = input_key()
		p = translateMyWay(x,m,k)
		if x == 0:
			print("\nCoded message:")
			print(p + '\n')
		else:
			print("\nDecoded message: ")
			print("My way:")
			print(p + '\n')
	elif x == 2:
		m = user_message()
		for i in range(1,26,1):
			brute = translateMyWay(1,m,i)
			print(str(i) + ". " + brute)

	elif x == 3:
		print ("Shutting down.")
		run = False
	else:
		continue

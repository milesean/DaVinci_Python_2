#!/user/bin/python

# MadLibs Generator

'''
Mad Libs Generator
Takes .txt file with the type of words needed wrapped in {}, reads the file and pulls
words wrapped in {} into a list.  Asks user to enter corresponding words then relaces {}
with new words from user.
'''

def madLibs():
	play = raw_input("Enter Y to play, anything else to quit: ")

	while play.upper() == 'Y':
		f_name = raw_input("Enter the file name: ")

		if f_name.endswith('.txt'):    # tests to make sure file has .txt extension
			text = format(readFile(f_name))    # format allows the string to have embeded dict references
			listA = findWords(text)
			listB = newWords(listA)
			newDictionary = newDict(listA, listB)
			finalStory = newStory(newDictionary, text)
			print finalStory
		else:
			print "Please enter the correct file format, .txt."
			f_name = raw_input("Enter the file name: ")

		play = raw_input("Enter Y to play, anything else to quit: ")



# reads file and returns a string
def readFile(filename):

	text = ""    # new empty string to hold text from the text file

	# opens file and reads file to text variable
	with open(filename, 'r') as f:
		text = f.read()

	return text


# findWords reads through the string to find the place holders and returns a list of the placeholders
def findWords(string):

	# sepetates words inside {} from string variable
	replaceList = list()
	end = 0
	repetitions = string.count('{')    # counts the number of { in the list to use as range in for loop
	for i in range(repetitions):
		start = string.find('{', end) + 1 # pass the '('
		end = string.find('}', start)
		key = string[start : end]
		replaceList.append(key)

	wordList = set(replaceList)    # set removes diplicates from the list

	return wordList


# takes list of needed words and asks user to enter that type of word
def newWords(wordList):
	newList = [""] * len(wordList)    # new empty list with the same lenght as the passed in list
	i = 0    # counter

	# loop adds user inputs into new list
	for words in wordList:
		newList[i] = raw_input("Enter a {}: ".format(words))
		i += 1

	return newList


# combines the two lists into one dictionary, values from file are keys and user input are values
def newDict(keys, values):
	dictionary = dict(zip(keys, values))

	return dictionary


# replaces words wrapped in {} in the text with values from dictionary
def newStory(dictionary, text):

	story = text.format(**dictionary)

	return story
	

madLibs()


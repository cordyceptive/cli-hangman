from random import randrange

guesses = []
with open('/usr/share/dict/words') as f:
	words = f.read()
	words = words.split('\n')
f.close()

def checkLetter(word, letter):
	# Check whether the guessed letter is in the word
	# Case-insensitive, aka do everything in lowercase
	# Return True/False
	if (letter.lower() not in word.lower()):
		return False
	return True

def generateWord():
	# Get two random words from /usr/share/dict/words
	# Return them joined together with a space
	i = words[randrange(len(words))]
	j = words[randrange(len(words))]
	return str(i + " " + j)

def validateLetter(guess):
	# Return True if input is exactly one letter
	# Return False if anything else
	letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	if (len(guess) == 1 and guess in letters and guess not in guesses):
		return True
	return False

def returnOutput(currentWord, word, letter):
	# TESTING
	# guessed: t
	# T__T___
	# next guess: e
	# TE_T___
	for i, ltr in enumerate(word.lower()):
		if (ltr == letter.lower()):
			currentWord[i] = letter.upper()

def findSpaces(currentWord, word):
	for i, letter in enumerate(word):
		if (letter == " "):
			currentWord[i] = letter

def main():
	# Generate target word
	word = generateWord()
	tries = 5
	gameFinished = False
	currentWord = ["_"] * len(word)
	findSpaces(currentWord, word)

	while (tries > 0):
		# Take letters from stdin
		ltr = input("Guess a letter: ")
		while (not validateLetter(ltr)):
			ltr = input("Guess a letter: ")

		# Compare letter to actual word
		if (checkLetter(word, ltr)):
			# If correct, print a version of the word
			returnOutput(currentWord, word, ltr)
			print(''.join(currentWord))
		else:
			tries -= 1
			print(f'You have {tries} lives remaining.')
		guesses.append(ltr.lower())

		if ('_' not in currentWord):
			gameFinished = True
			break
	if (tries == 0):
		print(f'The word was {word}. Thanks for playing!')

while True:
	try:
		main()
	except KeyboardInterrupt as e:
		print('\nThanks for playing!')
		break

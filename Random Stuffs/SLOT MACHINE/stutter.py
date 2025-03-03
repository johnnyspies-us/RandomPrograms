
word = str(input("What's your name traveler?"))


def stutter(word):
	return str(word[0:2] + '...' + word[0:2] + '...' + word + '?')


print(stutter(word))

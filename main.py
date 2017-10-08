import pymorphy2
import random
import os

def randomPhrase(nounList, adjList, count=1):
	# Load morph analyzer
	mp = pymorphy2.MorphAnalyzer()
	phrases = []

	for cnt in range(0, count):
		# Found random adj and noun from lists
		randNoun = random.choice(nounList)
		randAdj  = random.choice(adjList)

		for i in mp.parse(randNoun):
			# Choose definition
			if i.tag.POS == "NOUN" and i.tag.case == "nomn":
				# Only plural number
				if ("Pltm" in i.tag) == True:
					number = "plur"
				# Only single number
				elif ("Sgtm" in i.tag) == True:
					number = "sing"
				# Randomize noun number
				else:
					number = random.choice(("sing", "plur"))

				# Change only gender on adj
				if number == "sing":
					gender = i.tag.gender
					if gender == None: gender = "masc"
					inflectVal = {gender}
				# Change only number on noun and adj
				else:
					inflectVal = {number}
					# Change number of noun
					randNoun = i.inflect(inflectVal).word
				
		for i in mp.parse(randAdj):
			# Choose definition
			if i.tag.POS == "ADJF" and i.tag.case == "nomn":
				# Change number or gender of adj
				randAdj = i.inflect(inflectVal).word

		phrases.append("{} {}".format(randAdj, randNoun))

	return phrases

if __name__ == '__main__':
	# Script directory
	main_dir = os.path.split(os.path.abspath(__file__))[0]

	# Load nouns to list
	with open(os.path.join(main_dir, 'noun'), 'r', encoding='utf-8') as f:
		nouns = f.read().splitlines()

	# Load adjectives to list
	with open(os.path.join(main_dir, 'adj'), 'r', encoding='utf-8') as f:
		adjectives = f.read().splitlines()

	phrase = randomPhrase(nouns, adjectives, 10)
	print(phrase)
# Task: Christmas Tree 2
# We need to draw a tree. Input argument - height of the tree. Let's draw only the right side.
# For the symbols, we should repeat the letters from the word: CAR. The cented of the tree is a start of the word.
# Example input:
#	4
# Example output:
#	C
#	C A
#	C A R
#	C A R C

import math

def ChristmasTree(height):
    wordToCompleteTree = 'CAR'
    phraseToUse = GetThePhraseToUse(wordToCompleteTree, height)
    for i in range(height):
        wordToPrint = ''
        for h in range(i+1):
            wordToPrint = wordToPrint + phraseToUse[h]
        print(wordToPrint)

def GetThePhraseToUse(wordToCompleteTree, height):
    lenOfTheWord = len(wordToCompleteTree)
    if (height <= lenOfTheWord):
        return wordToCompleteTree
    lenNeeded = float(height) / float(lenOfTheWord)
    timesToUseTheWord = int(math.ceil(lenNeeded))
    completePhrase = wordToCompleteTree * timesToUseTheWord
    return completePhrase

ChristmasTree(1)
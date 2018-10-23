# how many times does a letter appear in a string?

# how many times does a word appear in a sentence?

sentance = input("enter a word: ")

words = sentance.split(" ")
wordCount = {} # dictionary

for word in wordCount:
    if(words in wordCount):
        wordCount[words] += 1
    else:
        wordCount[words] = 1
print(wordCount["t"])
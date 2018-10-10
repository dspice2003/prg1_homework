b_sentence = " "

sentence = "The quick brown fox jumped over the lazy dog"
words = sentence.split(" ")
for x in words:
    backwards = x[::-1]
    b_sentence = b_sentence + " " + backwards
print(b_sentence)
    
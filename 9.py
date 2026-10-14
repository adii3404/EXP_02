#Take a sentence from from the user,split it into words ,and store then in list .print the longest word.
sentence = input("Enter a sentence: ")

words = sentence.split()

longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("Longest word:", longest_word)
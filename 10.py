"""4 Read a file,split its contents into words, and store them in a list
  1 , print the total number of words.
2 ,print all unique words.  """
f = open("file.txt", "r")

content = f.read()

words = content.split()

print("Total number of words:", len(words))

unique_words = set(words)

print("Unique words:", unique_words)

f.close()
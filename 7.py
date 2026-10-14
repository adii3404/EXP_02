#write a program to read a file and count how many vowels are present in content
f = open("file.txt", "r")
content = f.read()

vowel_count = 0
vowels = "aeiouAEIOU"

for char in content:
    if char in vowels:
        vowel_count += 1

print("Number of vowels in the file:", vowel_count)

f.close()
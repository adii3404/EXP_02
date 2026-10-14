# Read all lines from a file into a list .print the total number of lines and dispaly the 2nd and 4th line.
f = open("file.txt", "r")

lines = f.readlines()

print("Total number of lines:", len(lines))

if len(lines) >= 4:
    print("2nd line:", lines[1])
    print("4th line:", lines[3])

f.close()
# Open the file and turn the words into a list while removing special characters.
f = open("text.txt", "r")
x = f.read()
specChar = ['.', ',', '!', '?', '/']
for i in specChar:
    x = x.replace(i, '')
x = x.split()

# Settings up a few lists to work with later
maxwords = []
num = []

# Making a list of all the different character lengths
for i in x:
    num.append(len(i))

# Now that we have a list of the lengths, target only the highest one
maxnum = max(num)

# If the length of a word matches the max number, add it to the list "Maxwords"
for i in x:
    length = len(i)
    if length == maxnum:
        maxwords.append(i)

# Print different results based on if there is only 1 result or multiple results
if len(maxwords) == 1:
    print("This word is the largest word containing " + str(maxnum) + " characters")
    print(maxwords[0])
else:
    print("These words are the largest words, each containing " + str(maxnum) + " characters")
    for i in maxwords:
        print(i)









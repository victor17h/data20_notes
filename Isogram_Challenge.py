word = input("Enter a word: ")
count = {}
for letter in word:
    if letter in count:
        count[letter] += 1
    else:
        count[letter] = 1

for key in count:
    if count[key] > 1:
        print("Not Isogram")
        break
    else:
        print("Isogram")
        break

#####

def isogram(string):
    for letter in string:
        if string.count(letter) > 1:
            return False
    return True

print(isogram("Hello"))
print(isogram("bye"))
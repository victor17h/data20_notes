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


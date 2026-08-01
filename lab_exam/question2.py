
text = input("Enter a string: ")

vowels = 0
for character in text:
    if character.lower() in "aeiou":
        vowels += 1

reverse = ""
for character in text:
    reverse = character + reverse

print("Total characters: " + str(len(text)))
print("Number of vowels: " + str(vowels))
print("Uppercase: " + text.upper())
print("Reverse: " + reverse)

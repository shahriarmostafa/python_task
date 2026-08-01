

text = input("Enter a string: ")

total_characters = len(text)
print("\nTotal number of characters :", total_characters)

vowels = "aeiouAEIOU"
vowel_count = 0

for ch in text:
    if ch in vowels:
        vowel_count = vowel_count + 1

print("Number of vowels           :", vowel_count)

print("Uppercase string           :", text.upper())

print("Reversed string            :", text[::-1])

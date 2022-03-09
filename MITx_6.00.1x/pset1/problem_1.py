s = "azcbobobegghakl"

VOWELS = "aeiou"
vowel_counter = 0

for letter in s:
    if letter in VOWELS:
        vowel_counter += 1

print("Number of vowels: ", vowel_counter)

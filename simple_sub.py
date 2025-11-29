"""
Problem 1: Break Simple Substitution

Sources: 

import string: https://www.geeksforgeeks.org/python/alphabet-range-in-python/

"""
import string

ciphertext = input("Enter the ciphertext: ")

ciphertext = ciphertext.replace(" ", "")

# print(ciphertext)

letter_dict = {}

for letter in ciphertext:
  letter_dict[letter] = letter_dict.get(letter, 0) + 1

sorted_letter_dict = {k: v for k, v in sorted(letter_dict.items(), key = lambda item: item[1], reverse=True)}

print("Letter Frequency Counts:")

for letter, freq in sorted_letter_dict.items():
  print(letter + ": " + str(freq))

while True:
  key = input("Guess a key (type exit to quit): ")
  if key == 'exit':
    break
  elif len(key) == 26:
    alphabet = string.ascii_lowercase # library from https://www.geeksforgeeks.org/python/alphabet-range-in-python/
    mapping = {c: p for (c, p) in zip(key, alphabet)}
    # print(mapping)
    decrypted_plain = ""
    for c in ciphertext:
      if c in mapping:
        decrypted_plain += mapping[c]
      else:
        decrypted_plain += c
    print(decrypted_plain)
  else:
    print("Enter a valid key that is exactly 26 characters long")

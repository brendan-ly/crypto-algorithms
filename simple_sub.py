"""
Problem 1: Break Simple Substitution

Sources: 
https://www.geeksforgeeks.org/python/alphabet-range-in-python/

KEY=KFAZSROBCWDINUELTHQGXVPJMY
"""
import string

ciphertext = input()

ciphertext = ciphertext.replace(" ", "")

# print(ciphertext)

letter_dict = {}

for letter in ciphertext:
  letter_dict[letter] = letter_dict.get(letter, 0) + 1

sorted_letter_dict = {k: v for k, v in sorted(letter_dict.items(), key = lambda item: item[1], reverse=True)}

for letter, freq in sorted_letter_dict.items():
  print(letter + ": " + str(freq))

while True:
  key = input("Guess a key (type exit to quit): ")
  if key == 'exit':
    break
  elif len(key) == 26:
    alphabet = string.ascii_lowercase
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

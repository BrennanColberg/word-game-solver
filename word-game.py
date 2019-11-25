import sys
import json


def count_letters(word):
  # init letter counter
  letter_count = [0] * 26
  # goes through each letter and counts occurences in the given word
  for letter_index in range(0, 26):
    letter = chr(97 + letter_index)
    for word_letter in word:
      if (word_letter == letter):
        letter_count[letter_index] += 1 
  return letter_count


# get word from input
input_characters = ''
try:
  input_characters = sys.argv[1]
  print(input_characters)
except:
  print("you need to add letters as an argument")

# count letters from it
usable_letters = count_letters(input_characters)
  
# prints letters in alphabetical order
alphabetical_letters = ''
for i in range(0, 26):
  count = usable_letters[i]
  alphabetical_letters += chr(97 + i) * count
print('Input characters (alphabetical):', alphabetical_letters)

# sets up dictionary
dictionary = []
with open('six_letter_dict.json') as file:
  dictionary = json.load(file)
print('loaded', len(dictionary), 'words from dictionary')

# filters dictionary to valid, make-able words
words = []
for dict_word in dictionary:
  # count letters in word
  dict_word_letters = count_letters(dict_word)
  # check if it's composable of the given letters
  usable = True
  for i in range(0, 26):
    if dict_word_letters[i] > usable_letters[i]:
      usable = False
      break
  # add to usable words if it is!
  if usable:
    words.append(dict_word)

# print usable words to console
for word in words:
  print(word)



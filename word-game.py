import sys
import json


# loading dictionary
dict_full = []
dict_10k = []
dict_20k = []
with open('comprehensive.json') as file:
  dict_full = json.load(file)
with open('top-10000.json') as file:
  dict_10k = json.load(file)
with open('top-20000.json') as file:
  dict_20k = json.load(file)


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

def alphabetize(letter_count):
  alphabetical_letters = ''
  for i in range(0, 26):
    count = letter_count[i]
    alphabetical_letters += chr(97 + i) * count
  return alphabetical_letters


def get_input_letters():
  # prompt for letters
  input_characters = input('What letters are on the wheel (all together, any order)? ')
  input_characters = input_characters.lower()
  # count occurences
  usable_letters = count_letters(input_characters)
  # reprint in alphabetical order
  print('Your letters (in alphabetical order):', alphabetize(usable_letters))
  return usable_letters

# filters dictionary to valid, make-able words
# returns a list of tuples in form (string word, int rank)
def filter_words(usable_letters):
  words = []
  for word in dict_full:
    # count letters in word
    word_letters = count_letters(word)
    # check if it's composable of the given letters
    usable = True
    for i in range(0, 26):
      if word_letters[i] > usable_letters[i]:
        usable = False
        break
    # add to usable words if it is!
    if usable:
      if word in dict_10k:
        words.append({"text": word, "rank": 10000})
      elif word in dict_20k:
        words.append({"text": word, "rank": 20000})
      else:
        words.append({"text": word, "rank": 40000})
  return words

def print_words(words):
  print()
  for length in range(3,7):
    selected_words = []
    for word in words:
      if (len(word['text']) == length):
        selected_words.append(word)
    sorted_words = sorted(selected_words, key=lambda x: x['rank'])
    for word in sorted_words:
      prefix = ''
      if word['rank'] <= 20000:
        prefix = '[' + str(word['rank']).zfill(5) + ']'
      else:
        prefix = '[#####]'
      print(prefix, word['text'])
    print()


while True:
  usable_letters = get_input_letters()
  valid_words = filter_words(usable_letters)
  print_words(valid_words)
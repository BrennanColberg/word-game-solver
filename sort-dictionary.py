import json

potential_words = []
invalid_words = []

with open('dictionary.json') as dictionary:
  data = json.load(dictionary)
  for word in list(data.keys()):
    if len(word) >= 3 and len(word) <= 6:
      potential_words.append(word)
    else:
      invalid_words.append(word)

print('there are', len(potential_words), 'potential words')
print('there are', len(invalid_words), 'invalid words')

with open('six_letter_dict.json', 'w') as file:
  json.dump(potential_words, file, indent=2)
      
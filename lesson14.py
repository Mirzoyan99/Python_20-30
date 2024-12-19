
# import random

# students = {
#     f"Student {i+1}": random.randint(1, 10) for i in range(10)
# }

# print(students)
# points = {
#     'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
#     'D': 2, 'G': 2,
#     'B': 3, 'C': 3, 'M': 3, 'P': 3,
#     'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
#     'K': 5,
#     'J': 8, 'X': 8,
#     'Q': 10, 'Z': 10
# }

# word = input("Enter some text: ").upper()

# score = 0
# for i in word:
#     score += points.get(i, 0)

# print(f"points '{word}': {score}")





























# 7 from slide

# s = 'a,2,b,5,c,8,a,4,e,11'
# s = s.split(',')

# result = {}

# for i in range(0, len(s), 2):
#     if s[i] not in result:
#         result[s[i]] = int(s[i + 1])
#     else:
#         result[s[i]] += int(s[i + 1])

# print(result)


# 8 from slide
# word = input('Enter text: ')

# result = {}

# for letter in word:
#     if letter not in result:
#         result[letter] = 1
#     else:
#         result[letter] += 1

# print(result)


# 137
# from random import randint

# dice_dict = {
#     2: 0,
#     3: 0,
#     4: 0,
#     5: 0,
#     6: 0,
#     7: 0,
#     8: 0,
#     9: 0,
#     10: 0,
#     11: 0,
#     12: 0,
# }


# for _ in range(1000):
#     a = randint(1, 6)
#     b = randint(1, 6)

#     dice_dict[a + b] += 1


# for key in dice_dict:
#     dice_dict[key] /= 10

# print(dice_dict)



# 139

# morse_code = {
#     'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',     'F': '..-.', 
#     'G': '--.',   'H': '....',  'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..', 
#     'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',  'Q': '--.-',  'R': '.-.',  
#     'S': '...',   'T': '-',     'U': '..-',   'V': '...-', 'W': '.--',   'X': '-..-', 
#     'Y': '-.--',  'Z': '--..', 

#     '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', 
#     '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
# }

# sentence = input('Enter some text: ').upper()
# encoded_sentence = ""

# for letter in sentence:
#     encoded_sentence += morse_code.get(letter, '')

# print(encoded_sentence)



# 142
# H, e, l, o, ',', ' ', W, r, d, !
# sentence = "Hello, World!"
# counts = {}

# for letter in sentence:
#     counts[letter] = 0

# print(len(counts))



# 143
# word1 = input('Enter first  word: ')
# word2 = input('Enter second word: ')

# counts1, counts2 = {}, {}

# for letter in word1:
#     if letter not in counts1:
#         counts1[letter] = 1
#     else:
#         counts1[letter] += 1

# for letter in word2:
#     if letter not in counts2:
#         counts2[letter] = 1
#     else:
#         counts2[letter] += 1


# print(counts1 == counts2)

# 144
# sentence1 = "William Shakespeare".lower().replace(' ', '')
# sentence2 = "I am a weakish speller".lower().replace(' ', '')

# print(sentence1)
# print(sentence2)

# counts1, counts2 = {}, {}

# for letter in sentence1:
#     if letter not in counts1:
#         counts1[letter] = 1
#     else:
#         counts1[letter] += 1

# for letter in sentence2:
#     if letter not in counts2:
#         counts2[letter] = 1
#     else:
#         counts2[letter] += 1

# print(counts1 == counts2)

# scores_dict = {
#     1  :"AEILNORSTU",
#     2  :"DG",
#     3  :"BCMP",
#     4  :"FHVWY",
#     5  :"K",
#     8  :"JX",
#     10 :"QZ",
# }

# word = input('Enter a word: ').upper()
# score = 0

# for letter in word:
#     for key in scores_dict:
#         if letter in scores_dict[key]:
#             score += key

# print(score)


# dct = {
#     1: 'AEILNORSTU',
#     2: 'DG',
#     3: 'BCMP',
#     4: 'FHVWY',
#     5: 'K',
#     8: 'JX',
#     10:'QZ'
# }

# text = input('Enter text: ').upper()
# count = 0

# for i in text:
#     for j in dct:
#         if i in dct[j]:
#             count += j
# print(count)


# 146
# from random import sample

# LOTO = {
#     'B': sorted(sample(range(1 , 16), k=5)),
#     'I': sorted(sample(range(16, 31), k=5)),
#     'N': sorted(sample(range(31, 46), k=5)),
#     'G': sorted(sample(range(46, 61), k=5)),
#     'O': sorted(sample(range(61, 76), k=5)),
# }

# s = "Price is %4d" % 50
# s = 'Price is {:4d}'.format(50)



# for key in LOTO:
#     print(end=f"{key:>4}")
# print()


# values = list(LOTO.values())

# for j in range(len(values)):
#     for i in range(len(values)):
#         print(end=f"{values[i][j]:>4}")

#     print()


# x = 1.98765456789
# y = 2.00
# print(f"{y:.2f}")]

# a = {1:'A', 2:'B', 3:'C'}
# print(a.setdefault(3))

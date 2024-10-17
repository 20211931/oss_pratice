#10
# open('cafe.txt', 'w', encoding = 'utf8').write('cafe')
# open('cafe.txt').read()


#11
# import sys,locale
# expressions = """
#         locale.getpreferrendencoding()
#         type(my_file)
#         my_file.encoding
#         sys.stdout.isastty()
#         sys.stdout.encoding
#         sys.stdin.isatty()
#         sys.stdin.encoding
#         sys.getdefaultencoding()
#         sys.getfilesystemencoding()
#     """

# my_file = open('dummy', 'w')

# for expression in expressions.split():
#   value = eval(expression)
#   print(expression.rjust(30), '-->', repr(value))


# 12
# from unicodedate import normalize
# len(normalize('NFC',s1)), len(normalize('NFC', s2))
# len(normalize('NFD',s1)), len(normalize('NFD', s2))
# normalize('NFC',s1), normalize('NFC', s2)
# normalize('NFD',s1), normalize('NFD', s2)
# normalize('NFC',s1) == normalize('NFC', s2)
# normalize('NFD',s1) == normalize('NFD', s2)



# 13
# from unicodedate import normalize, name
# ohm = 'u\2126'
# name(ohm)

# ohm_c = normalize('NFC', ohm)
# name(ohm_c)

# ohm, ohm_c, ohm == ohm_c

# normalize('NFC', ohm) == normalize('NFC', ohm_c)


# 14
# eszett = 'ß'
# name(eszett)

# eszett_cf = eszett.cafefold()
# eszett_cf2 = eszett.lower()
# eszett, eszett_cf, eszett_cf2


# 15
# s1 = 'café'
# s2 = 'cafe\u0301'
# s1 == s2

# from unicodedata import normalize

# def nfc_equal(str1, str2):
#     return normalize('NFC', str1) == normalize('NFC', str2)

# def fold_equal(str1, str2):
#     return (normalize('NFC', str1).casefold() == normalize('NFC', str2).casefold())

# nfc_equal(s1, s2)

# nfc_equal('A', 'a')

# s3 = 'StraBe'
# s4 = 'strasse'
# s3 == s4

# nfc_equal(s3, s4)

# fold_equal(s3, s4)

# fold_equal(s1, s2)

# fold_equal('A', 'a')



# 16
# import unicodedata
# import string

# def shave_marks(txt):
#     norm_txt = unicodedata.normalize('NFD', txt)
#     shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c))
#     return unicodedata.normalize('NFC', shaved)

# order = "Herr Voß: • 1 cup of Çtker™ caffè latte • bowl of acai."
# shave_marks(order)

# Greek = 'Ζέφυρος, Ζέφυρο'
# shave_marks(Greek)

# shave_marks('Straße')
# shave_marks('café')



# 17
# def shave_marks_latin(txt):
#   norm_txt = unicodedata.normalize('NFD', txt)
#   latin_base = False
#   keepers = []

#   for c in norm_txt:
#       if unicodedata.combining(c) and latin_base:
#           continue
#       keepers.append(c)
#       if not unicodedata.combining(c):
#           latin_base = c in string.ascii_letters

#   shaved = ''.join(keepers)
#   return unicodedata.normalize('NFC', shaved)



# 18
# single_map = str.maketrans("", "f", "‘’“”•˜")
# multi_map = str.maketrans({
#     '€': '<euro>',
#     '…': '...',
#     'Œ': 'OE',
#     '™': '(TM)',
#     'œ': 'oe',
#     '%': '<per mille>',
#     '+': '**',
# })

# multi_map.update(single_map)

# def dewinize(txt):
#     return txt.translate(multi_map)

# def asciize(txt):
#     no_marks = shave_marks_latin(dewinize(txt))
#     no_marks = no_marks.replace('ß', 'ss')
#     return unicodedata.normalize('NFKC', no_marks)

# order = "Herr Voß: • ½ cup of Øtker™ caffè latte • bowl of açaí."
# dewinize(order)
# asciize(order)


# 19
# fruits = ['caju', 'atemoia', 'caja', 'acai', 'acerola']
# sorted(fruits)


# 20
# !pip install pyuca

# import pyuca

# coll = pyuca.Collator()
# fruits = ['caju', 'atemoía', 'cajá', 'açaí', 'acerola']
# sorted_fruits = sorted(fruits, key=coll.sort_key)
# sorted_fruits



# 21
# import unicodedata
# import re

# re_digit = re.compile(r'\d')
# sample = '\x1b\xbc2\u0966\u216b\u2466\u2480\u3285'

# for char in sample:
#     print('U+%04x' % ord(char),
#           char.center(6),
#           're_dig' if re_digit.match(char) else
#           'isdig' if char.isdigit() else
#           'isnum' if char.isnumeric() else
#           format(unicodedata.numeric(char), '5.2f'),
#           unicodedata.name(char),
#           sep='\t')



# 22
# import re

# re_numbers_str = re.compile(r'\d+')
# re_words_str = re.compile(r'\w+')
# re_numbers_bytes = re.compile(rb'\d+')
# re_words_bytes = re.compile(rb'\w+')

# text_str = ("Ramanujan saw \u0be7\u0bed\u0be8\u0bef"
#             " as 1729 = 1³ + 12³ = 9³ + 10³.")

# text_bytes = text_str.encode('utf_8')

# print('Text', repr(text_str), sep='\n ')
# print('Numbers')
# print(' str :', re_numbers_str.findall(text_str))
# print(' bytes:', re_numbers_bytes.findall(text_bytes))
# print('Words')
# print(' str :', re_words_str.findall(text_str))
# print(' bytes:', re_words_bytes.findall(text_bytes))


# 23
# import os
# os.listdir('.')
# os.listdir(b'.')


# 24
# os.listdir('./fluent_python')
# os.listdir(b'./fluent_python')

# pi_name_bytes = os.listdir(b'.')[1]
# pi_name_str = pi_name_bytes.decode('ascii', 'surrogateescape')
# pi_name_str
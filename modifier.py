import re

def general_pattern(input_string):
    return bool(re.search(r'\=\+?\d\.\d', input_string))

def pattern_with_plus_sign(input_string):
    return bool(re.search(r'\+\d\.\d', input_string))

def pattern_without_plus_sign(input_string):
    return bool(re.search(r'\d\.\d', input_string))

content = []
with open("xplayersL1.upl", "r") as file:
    content = file.readlines()
content = [x.strip() for x in content]

iterator = 0
for row in content:
    if row != "":
        words = row.split(",")
        for word in words:
            if general_pattern(word):
                sub_words = word.split("=")
                for sub_word in sub_words:
                    if pattern_with_plus_sign(sub_word):
                        content[iterator] = content[iterator].replace(sub_word, '+9.9')
                    elif pattern_without_plus_sign(sub_word):
                        content[iterator] = content[iterator].replace(sub_word, '9.9')
    iterator += 1

# printing to console
for row in content:
    if row != "":
        words = row.split(",")
        for word in words:
            if general_pattern(word):
                print(word)

# writing to file
with open("xplayersL1.upl", "w") as file:
    for row in content:
        file.write(row + "\n")

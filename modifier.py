import re

def general_pattern(input_string):
    return bool(re.search(r'\=\+?\-?\d\.\d', input_string))

def pattern_with_plus_sign(input_string):
    return bool(re.search(r'\+\d\.\d', input_string))

def pattern_with_minus_sign(input_string):
    return bool(re.search(r'\-\d\.\d', input_string))

def pattern_without_sign(input_string):
    return bool(re.search(r'\d\.\d', input_string))

def modify_file(filename):
    try:
        content = []
        # open file
        with open(filename, "r") as file:
            content = file.readlines()
        content = [x.strip() for x in content]
        
        # build up new content
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
                            elif pattern_with_minus_sign(sub_word):
                                content[iterator] = content[iterator].replace(sub_word, '+9.9')
                            elif pattern_without_sign(sub_word):
                                content[iterator] = content[iterator].replace(sub_word, '9.9')
            iterator += 1

        # printing to console
        """
        for row in content:
            if row != "":
                words = row.split(",")
                for word in words:
                    if general_pattern(word):
                        print(word)
        """

        # writing to file
        with open(filename, "w") as file:
            for row in content:
                file.write(row + "\n")
                
        return bool(True)
    except:
        return bool(False)

if not modify_file("xplayersL1.upl"):
    print("Failed to open xplayersL1.upl\nMake sure you execute the program in the \"Unreal Tournament 2004\System\" directory")
if not modify_file("xplayersL2.upl"):
    print("Failed to open xplayersL2.upl\nMake sure you execute the program in the \"Unreal Tournament 2004\System\" directory")
if not modify_file("xaplayersl3.upl"):
    print("Failed to open xaplayersl3.upl\nMake sure you execute the program in the \"Unreal Tournament 2004\System\" directory")

input("Press Enter to close the application")

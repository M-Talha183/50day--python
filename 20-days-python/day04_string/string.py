# 🌕 You are an extraordinary person and you have a remarkable potential. You have just completed day 4 challenges and you are four steps a head in to your way to greatness. Now do some exercises for your brain and muscles.

# 💻 Exercises - Day 4

# Declare a variable named company and assign it to an initial value "Coding For All".
company = "coding for all"
# Print the variable company using print().
print(company)
# Print the length of the company string using len() method and print().
print(len(company))
# Change all the characters to uppercase letters using upper() method.
print(company.upper())
# Change all the characters to lowercase letters using lower() method.
print(company.lower())
# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())
# Cut(slice) out the first word of Coding For All string.
print(company[0:8])
# Check if Coding For All string contains a word Coding using the method index, find or other methods.
sub_word = "coding"
print(company.index(sub_word))
# Replace the word coding in the string 'Coding For All' to Python.
# Change Python for Everyone to Python for All using the replace method or other methods.

print(company.replace("coding","Coding for all"))

# Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
company_02 = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(company_02.split(","))
# What is the character at index 0 in the string Coding For All.
print(company_02[0])
# What is the last index of the string Coding For All.
print(company_02[-1])

# Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index("o"))
# Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index("f"))
# Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.rfind("l"))
# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence
# : 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"

print(sentence.index("because"))
print(sentence.find("because"))
# Use rindex to find the position of the last occurrence of the word because in the following 
# sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex("because"))

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
word = '   Coding For All      '
print(word.strip())

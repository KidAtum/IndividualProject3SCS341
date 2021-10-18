# Lucas Weakland
# SCS 341 01
# Individual Project 3

#imports
from pyexpat import model
import difflib
from PyDictionary import PyDictionary
from difflib import get_close_matches
import numpy as np
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

#Read file
my_file = open("Words", "r")
content = my_file.read()
# printing words from file
#print(content) # commented out so its a surprise
# making words from file into list
content_list = content.split(",")


# using closematches lib from difflib
def closeMatches(patterns, word):
    # driver for lib
    print(get_close_matches(word, patterns))

# Make file into array
array_from_file = np.loadtxt("Words", dtype=str)
# print array of words (commented out for surprise sack)
#print(array_from_file)
# testing popping out first element if needed
#first_element = array_from_file[0]
#print(first_element)

# Driver program
if __name__ == "__main__":
    # user input
    userWord = input("Enter a word:")
    print("The word you entered is: " + userWord)
    print("The most similar word in the file compared to yours is: ")
    # users input word that we will compare
    word = userWord
    # making the patterns be the items in array from file
    patterns = array_from_file
    closeMatches(patterns, word)


#test (might use this to compare similarity unless i find a diff way)
# rest of the files words (how similar in rank)
similarity0 = difflib.SequenceMatcher(None, userWord, "python").ratio()
#print(similarity0)

similarity1 = difflib.SequenceMatcher(None, userWord, "monkey").ratio()
#print(similarity1)

similarity2 = difflib.SequenceMatcher(None, userWord, "grape").ratio()
#print(similarity2)

similarity3 = difflib.SequenceMatcher(None, userWord, "teach").ratio()
#print(similarity3)

similarity4 = difflib.SequenceMatcher(None, userWord, "ape").ratio()
#print(similarity4)

similarity5 = difflib.SequenceMatcher(None, userWord, "water").ratio()
#print(similarity5)

# Using Bio method
# Defining the sequences to be aligned
A = userWord
B = "python"
C = "monkey"
D = "grape"
E = "teach"
F = "ape"
G = "water"
# Note - 2 points are rewarded for matching, 1 point is deducted for each mismatching and .5 deducted for gap
# 1st round of "comparing"
# using this to show difference / compare
alignments = pairwise2.align.globalms(A, B, 2, -1, -0.5, -0.1) # change the second letter(B) to the next letter in list

# Using the format_alignment method that's imported to align the list
for a in alignments:
    print(format_alignment(*a))
# !! repeat this step for all 6 file words !!

# 2nd round of "comparing"
alignments = pairwise2.align.globalms(A, C, 2, -1, -0.5, -0.1) # changed letter

# Using the format_alignment method that's imported to align the list
for a in alignments:
    print(format_alignment(*a))

# 3rd round of "comparing"
alignments = pairwise2.align.globalms(A, D, 2, -1, -0.5, -0.1) # changed letter

# Using the format_alignment method that's imported to align the list
for a in alignments:
    print(format_alignment(*a))

# 4th round of "comparing"
alignments = pairwise2.align.globalms(A, E, 2, -1, -0.5, -0.1) # changed letter

# Using the format_alignment method that's imported to align the list
for a in alignments:
    print(format_alignment(*a))

# 5th round of "comparing"
alignments = pairwise2.align.globalms(A, F, 2, -1, -0.5, -0.1) # changed letter

# Using the format_alignment method that's imported to align the list
for a in alignments:
    print(format_alignment(*a))

# 6th round of "comparing"
alignments = pairwise2.align.globalms(A, G, 2, -1, -0.5, -0.1) # changed letter

# Using the format_alignment method that's imported to align the list
for a in alignments:
    print(format_alignment(*a))

# i cant figure out how to rank them in order, ive been on this step for like hours
# could hard code it by renaming each "for 'a' in alignments" and then compare each one of those like -
# if a > b then put a at the top of the list and etc, but that's a lot of hard coded bullshizzz

print("Here are the words from the list: ")
print(array_from_file)
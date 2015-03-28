# File:        hw4.py
# Written by:  Kyle Fritz
# Date:        10/2/2013
# Lab Section: 10
# UMBC email:  fritzk1@umbc.edu
# Description: HW4, English to Pig Latin
############### USE WITH PYTHON 3 ###########
# scl enable python33 bash


print("This program will change any English sentence into Pig Latin")
# Function to find vowels
def fvowel(word):
    Vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
  # This finds the vowels in each word  
    for i in range(len(word)):
        if word[i] in Vowels:
            return i
  # If there are no vowels, fvowel will return -1 so that no "ay" is added   
    return -1

def main():
    E =input("Type in your English sentence: \n")
  # This splits the words up 
    EL = E.split()
    for word in EL:
        vowel = fvowel(word)
      # For when no vowel occurs 
        if vowel == -1:
            print(word.capitalize(), end= " ")
      # For when the vowel is at the start of the word     
        elif vowel == 0:       
            print(word.capitalize() + "ay", end= " ")
      # For when a vowel are inside the word      
        else:
          # This capitalizes the word correcttly  
            W = word[vowel:] + word[:vowel] + "ay"
            print(W.capitalize(), end = " ")
    print()
main()

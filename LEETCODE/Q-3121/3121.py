## QUESTION
"""You are given a string word. A letter c is called special if it appears both in lowercase and uppercase in word, and every lowercase occurrence of c appears before the first uppercase occurrence of c.
Return the number of special letters in word"""

## INTUITION
"""Track First and Last Occurrences:

The code uses two dictionaries: foreChar to store the first occurrence of each letter (when converted to lowercase) that appears in uppercase in the word, and lastChar to store the last occurrence of each letter (in lowercase) that appears in lowercase in the word.
Iterate Through the Word:

For each character in the word, it checks if it is uppercase or lowercase.
If the character is uppercase, it converts it to lowercase and records its first occurrence index in foreChar.
If the character is lowercase, it records its last occurrence index in lastChar.
Count Special Characters:

After processing the word, the code iterates through all lowercase letters.
For each letter, it checks if both its first occurrence as an uppercase letter and its last occurrence as a lowercase letter are recorded.
It then checks if the last occurrence index of the lowercase letter is less than the first occurrence index of the uppercase letter.
If the condition is met, the letter is counted as a special character. """

## CODE:
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        #storing first and last occurence of each lowercase letter converted from uppercase
        foreChar = {}
        lastChar = {}

        #iterating through each character in the word alongside the index
        for index, i in enumerate(word):
            if i.isupper():
                i = i.lower()
                if i not in foreChar:
                    foreChar[i] = index
            else:
                i = i.lower()
                lastChar[i] = index
            #tallying up the number of special characters    
        tally = 0
        for i in string.ascii_lowercase:
            if i in foreChar and i in lastChar and lastChar[i] < foreChar[i]:
                tally += 1
        return tally
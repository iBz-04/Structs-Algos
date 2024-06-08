##Q: 
"""You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.
Return the number of special letters in word"""

## INTUITION:
"""i used two sets (upCase and lowCase) to track characters that appear in uppercase and lowercase.
If the character is is uppercase (i.isupper()), we add its lowercase version (i.lower()) to the upCase set.
If it is lowercase, we add its lowercase version to the lowCase set."""

## CODE:
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        upCase = set()
        lowCase = set()
        for i in word:
            if i.isupper():
                upCase.add(i.lower())
            else:
                lowCase.add(i.lower())
        return len(upCase & lowCase)
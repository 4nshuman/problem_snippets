# problem_snippets
various competitive problem solutions

1. next_palindrome.py :
    Given a palindrome number find the next smallest number which is a palindrome. A palindrome number is a sequence of digits     that reads the same forward and reverse. For e.g. 121 is a palindrome.
    Input
    The input number will contain 2 to 15 digits.
    Output
    Output should be a number which is the next palindrome.
    
    Sample Input
    22,12321,12344321
    
    Sample Output
    33,12421,12355321
    
2. morse_code.py :
    In Morse code, each letter of the alphabet is represented by a sequence of dots and dashes. For example, “eta” would be: “.
    - .-“. If the spaces between letters are omitted, codes can be ambiguous. For example,”.-.-“ could be ‘eta’, ‘ent’, or
    ‘aet’ based on the location where a space is inserted.
    
    Write a program which reads a word and determines how many words, with the same number of letters as the input, it might
    represent. In the above example, the answer is 3 as ‘.-.-‘ can represent ‘eta’, ‘ent’, or ‘aet’.
    Input
    Input is a string representing a word. The number of characters will be at most 10.
    Output
    Output should be the number of words with the same number of letters that can be interpreted if
    spaces in the Morse code of the input are removed.
    
    Sample Input & Output
    Eta 3
    Infy 25

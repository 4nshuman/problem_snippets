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
    In Morse code, each letter of the alphabet is represented by a sequence of dots and dashes. For example, “eta” would be: “. - .-“. If the spaces between letters are omitted, codes can be ambiguous. For example,”.-.-“ could be ‘eta’, ‘ent’, or
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

3. hungry_fish.py :
    An evil scientist has developed an injection that induces insatiable hunger in a fish. On giving this injection, a fish
    of size x can eat another fish of smaller size y (y < x) and become a fish of size x + y retaining this hunger. An
    aquarium has a number of fishes of various sizes. The scientist introduces an injected fish into this aquarium with an
    objective that eventually only 1 fish remains. In order to achieve this, the scientist is allowed only two types of
    moves: either add a normal fish of any size or remove an existing normal fish from the aquarium. Given the sizes of other
    fishes in the aquarium and the size of injected fish, write a program to determine the minimum number of moves needed by 
    the scientist to achieve his objective. For example, suppose there are 5 fishes in the aquarium, the injected fish is of
    size 10 and the other fishes are of sizes 9, 20, 25, and 100. To ensure that only 1 fish remains in the aquarium the
    scientist needs to remove the fish of size 100 and add a fish of size 3. So the output is 2. The sequence of steps is 
    shown below. The sizes of fishes in the aquarium at each step are shown in curly braces. The quoted number is the
    size of the injected fish.
    
    Step-0: initial state - {'10',9,20,25,100}
    Step-1: eats 9 - {'19',20,25,100}
    Step-2: add normal fish of size 3 - {'19',3,20,25,100} [1st move]
    Step-3: eats 3 - {'22',20,25,100}
    Step-4: eats 20 - {'42',25,100}
    Step-5: eats 25 - {'67',100}
    Step-6: remove fish of size 100 - {'67'} [2nd move]
    
    Alternatively the scientist can also choose to introduce any fish of size 2 to size 18 in step 2 instead of the fish of
    size 3 to achieve the same objective. Similarly, adding a fish of size 36 in step 6 instead of removing fish of size 100
    is also a valid solution. In all these solutions 2 moves are required.
    
    Constraints
    The sizes of the fishes in the tank can range from 1 to 1000000.
    
    Input
    Input is a string containing two parts separated by ‘#’. The first part is an integer representing the size of the 
    injected fish and the second part is a sequence of integer sizes of the other fishes separated by comma. The sizes of the
    fishes need not be in sorted order.
    The input to the above example would be represented as: 10#9,20,25,100.

    Output
    A string containing an integer representing the minimum number of moves.
    
    Sample Input
    10#9,20,25,100
    3#25,20,100,400,500
    50#25,20,9,100
    
    Sample Output
    2
    5
    0

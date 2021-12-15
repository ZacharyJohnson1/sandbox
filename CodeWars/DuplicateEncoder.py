
'''The goal of this exercise is to convert a string to a new string where each character in the new string is 
"(" if that character appears only once in the original string, or ")" if that character appears more than once
 in the original string. Ignore capitalization when determining if a character is a duplicate.
Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))((" 
Notes
Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX", the "XXX" is the expected result, not the input!'''

def duplicate_encoder(word):
    
    word = word.lower()
    unique_letter_code = '('
    duplicate_letter_code = ')'
    encoded_str = ''
    letter_map = {}

    for letter in word:
        if letter not in letter_map:
            letter_map[letter] = 0
        else:
            letter_map[letter] = 1

    for letter in word:
        if letter_map[letter] == 0:
            encoded_str += unique_letter_code
        else:
            encoded_str += duplicate_letter_code

    return encoded_str

print(duplicate_encoder('din'))
print(duplicate_encoder('recede'))
print(duplicate_encoder('Success'))
print(duplicate_encoder('(( @'))
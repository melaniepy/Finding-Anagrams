# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram():
    # [assignment] Add your code here
    word = input("Enter the first string: ")
    anagram = input("Enter the second string: ")
    while len(word) != len(anagram):
        print("\nStrings do not match in length. Try again\n")
        word = input("Enter the first string: ")
        anagram = input("Enter the second string: ")

    str1 = word.lower()
    str2 = anagram.lower()

    sort_str1 = sorted(str1)
    sort_str2 = sorted(str2)

    if sort_str1 == sort_str2:
        print(True)
    else:
        print(False)
    
    
    return False

find_anagram()

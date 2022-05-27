# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagrams(word, anagram):
    # [assignment] Add your code here
    wList = []
    aList = []

    for x in word:
        wList.append(x)
        wList.sort()

    for y in anagram:
        aList.append(y)
        aList.sort()

    if wList == aList:
        return True
    else:
        return False

print(find_anagrams("hello", "check"))
print(find_anagrams("below", "elbow"))
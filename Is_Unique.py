#Python code that determines whether a given string is made up of a unique set of characters
#It checks for strings of length 0 and strings consisting of only spaces
#The space complexity is O(n) where n is the length of the string
#The time complexity is O(n) where n is the length of the string, this cannot be improved as every character must be checked

def is_unique(a):
    s = set()
    if (len(a) != 0) :   
        for x in range(0, len(a)) :
            if (a[x] in s) : return False
            if (a[x] not in s) : s.add(a[x])
        return True

def test(a):
    if (len(a) == 0) :
        print("The string is of length 0.")
        return
    if (not a or not a.strip()) :
        print("The string contains only spaces.")
        return    
    if (isUnique(a) == True) : 
        print("{} is a string of unique characters.".format(a))
        return
    if (isUnique(a) == False) : 
        print("{} is not a string of unique characters.".format(a))
        return

test("aab")
test("abc")
test("")
test("  ")

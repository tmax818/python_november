# /* case insensitive string compare */

strA1 = "ABC"
strB1 = "abc"
expected1 = True


strA2 = "ABC"
strB2 = "abd"
expected2 = False

strA3 = "ABC"
strB3 = "bc"
expected3 = False

strA4 = "123"
strB4 = "abc"
strDict = {'a': 1, 'b': 2, 'c': 3}
expected1 = False

#  * Determines whether or not the strings are equal, ignoring case.
#  * - Time: O(?).
#  * - Space: O(?).
#  * @param {string} strA
#  * @param {string} strB
#  * @returns {boolean} If the strings are equal or not.
def caseInsensitiveStringCompare(strA, strB):
    if len(strA) != len(strB):
        return False
    if strA.upper() == strB.upper():
        return True
    else:
        return False


print(caseInsensitiveStringCompare(strA1, strB1))
print(caseInsensitiveStringCompare(strA2, strB2))
print(caseInsensitiveStringCompare(strA3, strB3))
print(caseInsensitiveStringCompare(strA4, strB4))
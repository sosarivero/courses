def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Base case for empty strings
    if len(aStr) == 0:
        return False

    # Get the index of the letter in the middle
    mid_index = len(aStr) // 2

    if len(aStr) == 1:
        return char == aStr[mid_index]

    if char == aStr[mid_index]:
        return True
    elif char > aStr[mid_index]:
        return isIn(char, aStr[mid_index:])
    elif char < aStr[mid_index]:
        return isIn(char, aStr[0:mid_index])

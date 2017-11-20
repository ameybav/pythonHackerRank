def isBalanced(s):
    # Complete this function
    dict_bracket={"{":"}",
                  "(":")",
                  "[":"]"}
    openingBracket = "({["
    stackOf=[]
    for i in s:
        #print ("i:",i)
        if i in openingBracket:
            stackOf.append(i)
        elif not stackOf or i != dict_bracket[stackOf.pop()]:
            return "NO"
    if stackOf:
        return "NO"
    return "YES"

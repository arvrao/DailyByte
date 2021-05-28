''' This question is asked by Facebook. Given two strings s and t return whether or not s is an anagram of t.
Note: An anagram is a word formed by reordering the letters of another word. '''

def anagram(s1,s2):
    if(sorted(s1) == sorted(s2)):
        print('true')
    else:
        print('false')
    return 1
print(anagram('listen','silent'))

def areAnagram(str1, str2):
    # Get lengths of both strings
    n1 = len(str1)
    n2 = len(str2)
  
    # If length of both strings is not same, then
    # they cannot be anagram
    if n1 != n2:
        return 0
  
    # Sort both strings
    str1 = sorted(str1)
    print(str1) #list form
    str2 = sorted(str2)
  
    # Compare sorted strings
    for i in range(0, n1):
        if str1[i] != str2[i]:
            return 'false'
    
    # Other way around
    # if(str1!=str2):
    #     return 'false'
    
    return 'true'
    
    
print(areAnagram('listen','silent'))
  
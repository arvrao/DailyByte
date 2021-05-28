'''  Given a string representing your stones and another string representing a list of jewels, 
return the number of stones that you have that are also jewels.

Ex: Given the following jewels and stones...

jewels = "abc", stones = "ac", return 2
jewels = "Af", stones = "AaaddfFf", return 3
jewels = "AYOPD", stones = "ayopd", return 0 '''

def jewelsNstones(s1,s2):
    s1 = list(s1)
    res=0
    for s in s2:
        if s in s1: res+=1
    return res

print(jewelsNstones('Af','AaaddfFf'))
# print('gev')
    

'''  This question is asked by Microsoft. Given a string, return the index of its first unique
 character. If a unique character does not exist, return -1.
 '''
# "abcabd", return 2
# "thedailybyte", return 1
# "developer", return 0

def func(s):
    frequency = {}
    for i in s:
        if i not in frequency:
            frequency[i] = 1    # counts the times it occurred
        else:
            frequency[i] +=1    # times any given letter is printed
        print(frequency)
    for i in range(len(s)):
        if frequency[s[i]] == 1:
            return(i)
    return(-1)

print(func('abcabdaa'))

def f1(s):
    if s == '':
        return -1
    for item in s:
        if s.count(item) == 1:
            return s.index(item)
            break
    return -1
        
print(f1('arvinda'))
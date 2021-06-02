Given two strings representing sentences, return the words that are not common to both strings (i.e. the words that only appear in one of the sentences). You
may assume that each sentence is a sequence of words (without punctuation) correctly separated using space characters.

Ex: given the following strings...

sentence1 = "the quick", sentence2 = "brown fox", return ["the", "quick", "brown", "fox"]
sentence1 = "the tortoise beat the haire", sentence2 = "the tortoise lost to the haire", return ["beat", "to", "lost"]
sentence1 = "copper coffee pot", sentence2 = "hot coffee pot", return ["copper", "hot"]

def uncommon(s1,s2):
    lookup = set(s1.split()) and set(s2.split())
    return [w for w in s1.split()+s2.split() if w not in lookup]

  
print(uncommon("the quick", "brown fox"))

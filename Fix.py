'''
Created on 6 sep. 2017

@author: ruben
'''
phrase = "If Pickford's packers packed a packet of crisps would the packet of crisps that Pickford's packers packed survive for two and a half years? "

dictionary = {}

for word in phrase.split():
    if word not in dictionary:
        dictionary[word] = 1
    else:
        dictionary[word]+=1
    print(dictionary)
    

phrase = "How much wood would a woodchuck chuck if a woodchuck could chuck wood? " 

for word in phrase.split():
    if word not in dictionary:
        dictionary[word] = 1
    else:
        dictionary[word]+=1
    print(dictionary)
    
    
phrase = "Can you can a can as a canner can can a can?? " 
for word in phrase.split():
    if word not in dictionary:
        dictionary[word] = 1
    else:
        dictionary[word]+=1
    print(dictionary)
    


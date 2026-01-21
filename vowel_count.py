def count_vowels(word): 
    v={'a','e','i','o','u'} 
    c=0

    for ch in word.lower():
        if ch in v: 
            c+=1 

    print("no. of vowels:",c) 
        
count_vowels(input())
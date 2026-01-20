#text analyzer tool

#input text
text=input("Enter text:")

#word count
word_count=len(text.split())

#vowel set
vowels={'a','e','i','o','u'}
v=0
d=0

#analyze text
for i in text.lower():
    if i in vowels:
        v+=1
    if i.isdigit():
        d+=1

#display analysis
print("Total no. of characters:", len(text))
print("Total no. of words:",word_count)
print("No. of vowels:",v)
print("No. of digits:",d)

#palindrome check
new_text=text.lower().replace(" ", "")
if new_text==new_text[::-1]:
    print("The sentence is a Palindrome!")
else:
    print("The sentence is not a Palindrome!")
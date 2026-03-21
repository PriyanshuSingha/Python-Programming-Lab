para=input("enter the paragraph:")
words=para.split()
print("Number of words:",len(words))
palindrome_count=0
for word in words:
    if word.lower()==word[::-1].lower():
        palindrome_count+=1
        
print("the no of palindromes:",palindrome_count)
print("words in reverse order:")
for word in words:
    print(word[::-1])        
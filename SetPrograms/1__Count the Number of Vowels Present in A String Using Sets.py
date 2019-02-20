element=input("Enter the String::")
count=0
vowels=set("aeiou")
for letter in element:
    if letter in vowels:
        count=count+1
print("Count The Number of Vowels::",count)

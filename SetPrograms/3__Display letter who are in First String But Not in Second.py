element1=input("Enter the 1st String::")
element2=input("Enter the 2nd String::")
common=list(set(element1)-(set(element2)))
print(common)

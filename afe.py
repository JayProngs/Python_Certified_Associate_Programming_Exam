from math import ceil

strng = input("Enter your string:")
strng=strng.lower()
lst = list(strng)

list1=[]
for ch in lst:
    if not ch.isspace():
        list1.append(ch)

lst=list1

l1 = len(lst)


flag = True
for i in range(ceil(l1 / 2)):
    if lst[i] != lst[l1 - i-1]:
        flag = False
        break
    else:
        flag = True
if flag:
    print("Palindrome")
else:
    print("Not Palindrome")

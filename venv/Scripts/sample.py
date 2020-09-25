#Input: s = "abcabcdbb"
#Output: 4
#Explanation: The answer is "abc", with the length of 3.
#input:-bbbbb
#output-b
s='ababcd'
substring=''
l1=[]
d={}
if s=='':
    num=0
elif s==' ':
    num=1
else:
    for i in range(len(s)):
        if s[i] not in d:
            substring=substring+s[i]
            d[s[i]]=i
        else:
            l1.append(len(substring))
            substring=s[i]
            d.clear()
            d[s[i]]=i
    print(l1)
    maximum = 0
    for i in l1:
        if i > maximum:
            maximum = i
    num=maximum
print(num)

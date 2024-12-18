# wap to check how many elements are present in colelection data type?
cdt=eval(input('enter a cdt'))   # take cdt as input from the user
c=0              #by assume given cdt is empty so assigning c=0
for i in cdt:    # by using for loop fetching each and every element for cdt
    c+=1         # adding 1 to c for every element of cdt
print(f' number of elements in given cdt is{c}') # atlast after complete the iteration of loop print c value
ITERATION
iteration1:it will fetch the first element from the cdt then it will increment c from 0 to 1
iteration2: it will fetch the second  element from the cdt then it will increment c from 1 to 2
iteration3: it will fetch the third element from the cdt then it will increment c from 2 to 3
iteration4: it will fetch the fourth element from the cdt then it will increment c from 3 to 4
iteration5: it will fetch the fourth element from the cdt then it will increment c from 4to 5





# wap to print how many times a given substring present in given string?
ms=input() #main string as input from the user
ss=input()# take sub string as another input from the user
c=0        # by assume sub string is not present in ms
for el in ms:  #by using for loop fetching each and every element for ms
    if el==ss:   #compare each element with substring
        c+=1    #adding 1 to c for every element of ms
print(c)        
Iterations
iteration1:it will fetch 'h' so el='h'
           check 'h'=='o' false so still c=0
iteration2: it will fetch 'e' so el='o'
            check 'e'=='o' false so still c=0
iteration3:it will fetch 'l' so el='l'
            check 'l'=='o' false so still c=0
iteration4:it will fetch 'l' so el='l'
            check 'l'=='o' false so still c=0
iteration5:it will fetch 'o' so el='o'
            check 'o'=='o' false so increment c from 0 to 1       
# wap to print how many numbers are present in string?
str =input() # string as input from the user
c=0     #by assume given str is empty so assigning c=0
for i in str:     #by using for loop fetching each and every element for str
    if i.isdigit():    # checking the characters i.e integers or not 
        c+=1   #adding 1 to c for every element of str
print(c)
iterations:
iteration1: it will fetch 'h' so i='h'
            check 'h'== digit  false so still c=0
iteration2: it will fetch 'a' so i='a'
            check 'a'== digit false so still c=0
iteration3:it will fetch 'i' so i='i'
            check 'i'== digit false  so still c=0
iteration4:it will fetch 1 so i= 1
            check 1==digit true so increment c from 0 to 1
iteration5: it will fetch 2  so i=2 
            check 2== digit  true so increment c from 1 to 2
iteration6:  it will fetch 3 so i=3 
            check 3 == digit  true so increment c from 2 to 3
                      


# wap to find the sum of digits present in a given string?
a=input()    #string as input from the
sum=0        #by assume given str is empty so assigning c=0
for k in a:        #by using for loop fetching each and every element for str
    if k.isdigit():        #checking the characters i.e integers or not 
        l=int(k)            # use type cast for convert int type
        sum+=l
print(sum)
ITERATIONS:
iteration1: it will fetch 'r' so k='r'
            check 'r'== digit false so still sum=0
iteration2: it will fetch '2' so k=2
            check 2 == digit true  so increment sum from 0 to 1
iteration3: it will fetch 'e' so k='e'
            check 'e'== digit false so still sum=1
iteration4: it will fetch '3' so k=3
            check 3 == digit True  so increment sum from 1 to 2            
            

# wap to find the sum of even digits present in a given string?
b=input()   #string as input from the user
sum=0       #by assume given str is empty so assigning c=0
for i in b:  #by using for loop fetching each and every element for str
    if i.isdigit():   #checking the characters i.e integers or not 
        k=int(i)       # use type cast for convert int type
        if k%2==0:       # compare the even or not 
            sum+=k        #adding 1 to sum  for every element of b
print(sum)
Iterations:
iteration1:it will fetch 'b'  so i='b'
          check 'b'== integer false so still sum=0
iteration2: it will fetch 'y' so k='y'
            check 'y'== integer false so still sum=0
iteration3: it will fetch 'e' so  k='y'
            check 'e'== integer false so still sum=0
iteration4: it will fetch '1' so k='y'
            check '1'== integer true and it must 1%2==0 false so still sum=0 
iteration5: it will fetch '4' s k='4'
            check '4'== integer and it must be 4%2==0 true  so increment  sum  from 1 to 2
            
# wap to count how many even and odd digits are present in a given string?
s=input()    #string as input from the user
ec=0         # if even numbers are empty in string
oc=0          # if odd  numbers are empty in string
for i in s:
    if i.isdigit():
        k=int(i)
        if k%2==0:
            ec+=1
        else:
            oc+=1
print(ec)
print(oc)            
Iterations:
iteration1: it will fetch '1' so i='1'
              check'1'== digit and  1%2==0 false  so odd count increment from 0 to 1
iteration2: it will fetch '2' so i='2'
            check '2'== digit and  2%2==0 true so even count increment from 0 to 1
iteration3: it will fetch '3' so i='3'
              check'3'== digit and  3%2==0 fasle so odd count increment from 1 to 2
iteration4: it will fetch '4' so i='4'
            check '4'== digit and  4%2==0 true  so even count increment from 1 to 2
# wap to find  sum of even digits are present and sum of even digits are present in a given string?
a=input()
esum=0
osum=0
for k in a:
    if k.isdigit():
        l=int(k)
        if l%2==0:
            esum+=l
        else:
            osum+=l
print(esum)
print(osum)
Iterations:
iteration1: it will fetch '5' so k ='5'
            check '5' == digtit true and '5'%2==0 false so odd sum increment osum from o to 1
iteration2: it will fetch '2' so k ='2'
            check '2' == digtit true and '5'%2==0 true  so even sum increment esum from 0 to 1
iteration3: it will fetch '7' so k ='7'
            check '7' == digtit true and '7'%2==0 false so odd sum increment osum from 1 to 2
iteration4: it will fetch '6' so k ='6'
            check '6' == digtit true and '6'%2==0 true  so even sum increment esum from 1 to 2
# wap to print how many vowels are present in a given string?
str=input()
vc=0
vowels='aeiouAEIOU'
for i in str:
    if i in vowels:
        vc+=1
print(vc)
ITERATIONS:
iteration1: it will fetch 'p' so i='p'
            check 'p'== vowel false so still vc=0
iteration2: it will fetch 'a' so i='a'
            check 'a'== vowel true so vc increment from 0 to 1
iteration3: it will fetch 'v' so i='v'
            check 'v'== vowel false so still vc=1
iteration4: it will fetch 'a' so i='a'
            check 'a'== vowel true so vc increment from 1 to 2
iteration5: it will fetch 'n' so i='n'
            check 'n'== vowel false so still vc=2
#wap to print how many consonants are present in given string??
a=input()
cc=0
vowels='aeiouAEIOU'
for l in a:
    if l.isalpha():
        if i not in vowels:
            cc+=1
print(cc)            
ITERATIONS:
iteration1:it will featch 'r'  so l='r'
            chech 'r'==alpha and that 'r'== vowel false so still cc=0            
iteration2:it will featch 'o'  so l='o'
            chech 'o'==alpha and that 'o'== vowel true so cc increment from 0 to 1
iteration3:it will featch 'y'  so l='y'
            chech 'y'==alpha and that 'y'== vowel false so still cc=1
iteration4 :it will featch 'a'  so l='a'
            chech 'a'==alpha and that 'a'== vowel true so cc increment from 1 to 2
iteration5:it will featch 'l'  so l='l'
            chech 'l'==alpha and that 'r'== vowel false so still cc=2          
  # wap to print how many alphanumercal values present in string?
 b=input()
 alnum=0
 for i in b:
     if i.isalnumeric():
         alnum+=1
print(alnum)
ITERATIONS:
iteration1: it will fetch '1' so i='1'
            check '1'== alnumeric true so alnum increment from 0 to 1
iteration2: it will fetch 'a' so i='a'
            check 'a'== alnumeric true so alnum increment from 1 to 2
iteration3: it will fetch '@' so i='@'
            check '@'== alnumeric false so alnum=2
iteration4: it will fetch '3' so i='3'
            check '3'== alnumeric true so alnum increment from 2 to 3
# wap to print how many special characters are present in given string??
c=input()
sc=0
for i in c:
    if not i.isalnum():
        sc+=1
print(sc)
# Iterations
iteration1: it will fetch 'p' so i ='p'
            check 'p'=! alnum false so still sc=0
iteration2:it will fetch '@' so i ='@'
            check '@'=! alnum true  so sc increment from 0 to 1
iteration3:it will fetch 'v' so i ='v'
            check 'v'=! alnum false  so still sc=1
iteration4:it will fetch '#' so i ='#'
            check '#'=! alnum true  so sc increment from 1 to 2
# wap to print sum of  digits present in the given list?
l=eval(input('enter the cdt'))
sum=0
for i in l:
    if type(i)==int:
        sum+=i
print(sum)l=eval(input('enter the cdt'))
sum=0
for i in l:
    if type(i)==int:
        sum+=i
print(sum)
# Iterations
iteration1: it will fetch 'p' so i='p'
           check 'p'==int false so sill sum =0
iteration2: it will fetch '2' so i='2'
           check '2'==int true so sum increment from 0 to 1
iteration3: it will fetch '123' so i='123'
            check '123'== int type so increment will be add 123 and 1
iteration4: it will fetch '3' so i='3'
           check '3'==int true so sum increment will be add 124 and 3

# wap to find the maximum number in a given list?
n=eval(input('enter the list'))
max=n[0]
for i in n:
    if i>max:
        max=i
print(max)        
           
Iterations:
iteration1:it will fetch '20'so i='20'
            check '20' > 0 true so max=20
iteration2: it will fetch '12'so i='12'
             check '12' > 20 false so still  max=20
iteration3:it will fetch '30'so i='30'
            check '30' > 20 true so max increment from 20 to 30
iteration4:it will fetch '50'so i='50'
            check '50' > 30 true so max increment from 30 to 50          
# wap to print each and every element how many times present in the cdt?
a=eval(input('enter cdt'))
d={}
for i in a:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
print(d)
# Iterations
iteration1: it will fetch 'h' so i 'h' it check in dictionary 'h' fale it add 1 to dictionary
iteration2: it will fetch 'a' so i 'a' it check in dictionary 'a' fale it add 1 to dictionary
iteration3: it will fetch 'i' so i 'i' it check in dictionary 'i' fale it add 1 to dictionary
iteration4: it will fetch 'h' so i 'h' it check in dictionary 'h' true it increment from 1 to 2
# wap to find most repeated character in a given string?
s=input()
mrc=0
c=0
for i in s:
    if s.count(i)>c:
        mrc=i
        c=s.count(i)
print(mrc)        
    
# Iterations:
iteration1: it will fetch 'p' so i='p' it check greater than 0 true so c increment from 0 to 1
iteration2: it will fetch 'a' so i='a' it check greater than 1 false so c still 1
iteration3: it will fetch 'v' so i='v' it check greater than 1 false so c still 1
iteration4: it will fetch 'a' s i='a' it check greater than 1 true so c increment from 1 to 2
iteration5:it will fetch 'n' so i='n' it check greater then 2 so c still 2

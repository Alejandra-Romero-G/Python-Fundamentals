#String Class

txt = "Hi python"
length =len(txt) #9
print(length)
# letter Position
txt[0]#H
txt[5]#t
txt[9]#Error
txt[-1]#n
txt[1:5]#i py

txt.upper()#HI PYTHON
txt.lower()#hi python
txtl="i'm the smallest"
txtl.capitalize()#I'm the smallest

txt.startswith("a")#False
txt.startswith("H")#True
txt.endswith("a")

#txt='Hi python'
txt.isdigit()#False
txt.isalnum()#False
txt.isalpha()#False
txt1='HiPython' 
txt1.isdigit()#False
txt1.isalnum()#True
txt1.isalpha()#True
txt1='1324'
txt1.isdigit()#True
txt1.isalnum()#True
txt1.isalpha()#False

txt.replace('i','o')#Ho python
txt = txt.replace('i','o')
txt.find("o")#1
txt.rfind("o")#7
txt.find("w")#-1
txt.find('o',2)#7 This searches after position 2
print("*******************************")
#EXAMPLE TO USE
x = 0
for i in txt:
    x += 1
    print( f'position: {x} = {i} ' )
print("*******************************")
#Example tu use
print('Introduce a number:')
num = input()
sum=0
if(num.isdigit()):
    for i in num:
        sum+=int(i)
else:
    print('You need to introduce only numbers')
print(f'The number is :{num} and the sum is: {sum}')

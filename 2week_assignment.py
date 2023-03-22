
def sum(a,b):
    return a+b
print (sum(1,1))

def sub(a,b):
    return a-b
print (sub(1,1))

def mul(a,b):
    return a*b
print (mul(1,2))

def div(a,b):
    return a/b
print (div(1,2))

def distance(x1,y1,x2,y2):
    return ((x1-x2)**2 + (y1-y2)**2)**(0.5)
print (distance(2,2,1,1))

def title():
    lyrics = "Switch sides and I'm beside you"
    return lyrics[20:]
print (title())

def reverseStr(string):
    return string[::-1]
print (reverseStr("Hello"))

def introduce():
    name = input("이름을 입력하세요 : ")
    hobby = input("취미를 입력하세요 : ")
    school = input("재학 중인 학교를 입력하세요 : ")
    birthday = input("생일을 입력하세요 : ")
    print("제 이름은 %s입니다. 취미는 %s입니다. 저는 %s를 다니고 있습니다. 제 생일은 %s월 %s일 입니다." %(name,hobby,school,birthday[2:4],birthday[4:6]))
print (introduce())

def calc():
    a = input("첫 번째 수를 입력하세요")
    b = input("두 번째 수를 입력하세요")
    print("두 수의 합 : ",a+b)
    print("두 수의 차 : ",a-b)
    print("두 수의 곱 : ",a*b)
    print("두 수의 몫 : ",a//b)
print (calc())

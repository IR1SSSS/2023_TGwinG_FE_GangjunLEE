# 1번
def grade(score):
    if score>=90 and score<=100: 
        return "A"
    elif score<=89 and score>=80:
        return "B"
    elif score<=79 and score>=70:
        return "C"
    elif score<=69 and score>=60:
        return "D"
    else:
        return "F"



# 2번
def quadrant(x, y):
    if x>0 and y>0:
        return "제 1사분면"
    elif x < 0 and y > 0:
        return "제2사분면"
    elif x < 0 and y < 0:
        return "제3사분면"
    elif x > 0 and y < 0:
        return "제4사분면"
    else:
        return "원점"

# 3번
def leapYear(year):
    if int((year)%4==0 and year%100 !=0) or int(year%400==0):
        return "윤년입니다."
    else:
        return "윤년이 아닙니다."


# 4번
def dice(a, b, c):
    if a==b and b==c:
        return 10000+1000*a
    elif a==b:
        return 1000+100*a
    elif b==c:
        return 1000+100*b
    elif a==c:
        return 1000+100*a
    elif a!=b and b!=c and c!=a:
        return max(a, b, c)*100

# 5번
def alarm(time):
    hour = time//100
    min = time%100

    if min>=45:
        min -= 45
    else:
        min+=15
        if hour == 0:
            hour = 23
        else:
            hour-= 1
    return str(hour)+"시 " + str(min)+"분"
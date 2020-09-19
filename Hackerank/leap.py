def leap(a):
    if a%4 ==0:
        if a%100==0 and a%400!=0:
            # print(False)
            return False
        elif a%100==0 and a%400==0:
            # print(True)
            return True
        else:
            # print(True)
            return True
    else:
        return False
        # print(False)

A=int(input())
leap(A)
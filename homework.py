list1 = [1,1]
time = 25
for i in range(2,time):
    new = list1[i-2]+list1[i-1]
    list1.append(new)
print("費氏數列1:",list1)
ans1 = sum(list1)
print("第一題答案總合:{:d}".format(ans1))
list2 = []
num1 = 1
num2 = 2
for i in range(time):
    num = num2/num1
    list2.append(num)
    num3 = num2
    num2 = num2 + num1
    num1 = num3
print("費氏數列2:",list2)
ans2 = sum(list2)
print("第二題答案總合:{:f}".format(ans2))
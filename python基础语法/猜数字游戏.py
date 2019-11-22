import random;
answer = random.randint(1,10)
count = 5
while(count > 0):
    temp = input("猜数字是多少：")
    guess = int(temp)
    if(guess==answer):
        print("rigtht")
        break
    else:
        if(guess > answer):
            print('bigger')
        else:
            print('smaller')
        count = count -1
print("end")

import random

def randomNumber():
    number = random.randint(1, 100)
    
    while True:
        try:
            print("********************************************")
            user = int(input("ทายตัวเลขที่มีค่าอยู่ที่ 1-100: "))
            print("********************************************")
            if user == number:
                print("********************************************")
                print("ยินดีด้วยคุณทายถูก!")
                print("********************************************")
                break
            elif user < number:
                print("คุณทายผิดตัวเลขที่ป้อนน้อยไป")
            else:
                print("คุณทายผิดตัวเลขที่ป้อนมากไป")
        except ValueError:
            print("กรุณาป้อนตัวเลขเท่านั้น")

randomNumber()
import random


def level1():
    print("Which level do you want? Enter a number:\n 1-simple operations with number 2-9\n 2-integral squares of 11-29")
    t = 0
    choose = int(input())
    if choose == 1:
        for i in range(5):
            symbol = ['-', '+', '*']
            ind = random.randint(0, 2)
            num_1 = random.randint(2, 10)
            num_2 = random.randint(2, 10)
            print(num_1, symbol[ind], num_2)
            while True:
                try:
                    gamer = int(input())
                    break
                except:
                    print("Incorrect format")

            if symbol[ind] == '-':
                n = num_1-num_2
                if gamer == n:
                    print("Right!")
                    t += 1
                elif gamer != n:
                    print("Wrong!")
                else:
                    print("Error")
            elif symbol[ind] == '+':
                b = num_1+num_2
                if gamer == b:
                    print("Right!")
                    t += 1
                elif gamer != b:
                    print("Wrong!")
                else:
                    print("Error")
            elif symbol[ind] == '*':
                m = num_1*num_2
                if gamer == m:
                    print("Right!")
                    t += 1
                elif gamer != m:
                    print("Wrong!")
                else:
                    print("Error")
            else:
                print("Error")
            print("Your mark is "+str(t)+"/5")
    elif choose == 2:
        for i in range(5):
            numb = random.randint(11,30)
            numb_s = numb**2
            print(numb,'** 2')
            while True:
                try:
                    gamer_2 = int(input())
                    break
                except:
                    print("Incorrect format")
            if gamer_2 == numb_s:
                print("Right!")
                t += 1
            elif gamer_2 != numb_s:
                print("Wrong!")
            else:
                print("Error")
            print("Your mark is " + str(t) + "/5")
    else:
        print("Only 1 or 2")
        while True:
                choose = input()
                if choose == '1' or choose == '2':
                    return level1()
                print("Incorrect format")
    print("Would you like to save your result to the file? Enter yer or no.")
    v = input()
    if v == 'yes':
        print("What is your name?")
        name = input()
        my_file = open("results.txt", "w+")
        my_file.write(name + ": Your mark is " + str(t) + "/5 in level " + str(choose))
        print("The results are saved in 'results.txt'")

level1()



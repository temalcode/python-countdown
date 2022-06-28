import time

def countdown(userInput):
    while(userInput != 0):
        minutes, seconds = divmod(userInput, 60)
        count = '{:02d}:{:02d}'.format(minutes, seconds)
        print(count)
        userInput -= 1
        time.sleep(1)
    print('count finished !')

userInput = int(input('Enter number of seconds: '))
countdown(userInput)

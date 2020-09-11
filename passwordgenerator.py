import random
from time import sleep

print('PASSWORD GENERATOR')
while True:
    input('Hit ENTER to run.')


    loop = 0
    while loop != 20:
        
        

        loop += 1

        char1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u',
                 'v', 'x', 'y', 'z']
        char2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u',
                 'v', 'x', 'y', 'z']

        char3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u',
                 'v', 'x', 'y', 'z']
        char4 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u',
                 'v', 'x', 'y', 'z']

        char5 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u',
                 'v', 'x', 'y', 'z']
        char6 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u',
                 'v', 'x', 'y', 'z']

        char7 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u',
                 'v', 'x', 'y', 'z']
        char8 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u',
                 'v', 'x', 'y', 'z']

        realchar9 = random.randrange(10, 1000)
        char10 = ['.', ':', '#', '/', ';', '$', '|', ',']

        realchar1 = char1[random.randrange(0, 25)]
        realchar2 = char2[random.randrange(0, 25)]
        realchar3 = char3[random.randrange(0, 25)]
        realchar4 = char4[random.randrange(0, 25)]
        realchar5 = char5[random.randrange(0, 25)]
        realchar6 = char6[random.randrange(0, 25)]
        realchar7 = char7[random.randrange(0, 25)]
        realchar8 = char8[random.randrange(0, 25)]
        # char 9 needs no randomizer
        realchar10 = char10[random.randrange(0, 7)]

        re = 1
        randompassword = (str(realchar1) + str(realchar2) + str(realchar3) + str(realchar4) + str(realchar5) + str(realchar6) + str(realchar7) + str(realchar8) + str(realchar9) + str(realchar10))

        sleep(0.5)
        print('.')
        sleep(0.5)
        print('..')
        sleep(0.5)
        print('...')

        print(str(randompassword))



















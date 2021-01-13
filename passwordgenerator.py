import random
from time import sleep

print('PASSWORD GENERATOR')
while True:
    input('Hit ENTER to run.')

        

    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u',
                 'v', 'x', 'y', 'z', '.', ':', '#', '/', ';', '$', '|', ',']
    pwstring = ""
    pw = []
    for i in range(20):
        pw.append(random.choice(chars))
      

        


    sleep(0.5)
    print('.')
    sleep(0.5)
    print('..')
    sleep(0.5)
    print('...')
    sleep(0.5)
    print(pwstring.join(pw))



















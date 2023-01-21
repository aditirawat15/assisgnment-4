import random

listt = []
for i in range(0, 10):
    listt.append(i)
for i in range(0,10):
    a = random.choice(listt)
    b = random.choice(listt)
    print("Question ", i+1 ,": ", a, 'x', b, ' = ', end = '')
    answer = int(input(''))
    if answer == round(a*b): print(' Right!')
    else: print('Wrong!. The answer is ', round(a*b))

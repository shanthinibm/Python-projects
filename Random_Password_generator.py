

import random

UC1 = chr(random.randint(65, 90))
UC2 = chr(random.randint(65, 90))
LC1 = chr(random.randint(97, 122))
LC2 = chr(random.randint(97, 122))
SC1 = chr(random.randint(33, 47))
SC2 = chr(random.randint(58, 64))
d1 = random.randint(0, 9)
d2 = random.randint(0, 9)
#print(d1,d2)
str1 = str(d1)+str(d2)
password =UC1+UC2+LC1+LC2+str1+SC1+SC2
#print(password)
temp = list(password)
#print(temp)
random.shuffle(temp)
#print(temp)
t1=''.join(temp)
print(t1)



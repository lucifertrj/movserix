from time import sleep
import random
import string
while True:
 username=input('Enter your name:')
 if username!='Tarun':
  continue
 print()
 password=input('Enter your password:')
 if password!='123':
  print('**Invalid Password**')
  continue
 else:
  break

print('Loading..............................................................................')
sleep(0.7)
for i in range(300000):
 k=random.choice(string.ascii_letters)
 print(k,end='')
 if i in (30,70,100,130,170,200,230,250,290,320,350,380):
  print('')
sleep(1)
for j in range(200000):
 l=random.choice(string.ascii_letters)
 print(l,end='')
 if i in (30,70,100,130,170,200,230,250,290,320,350,380):
  print('')
sleep(0.8)
for p in range(200000):
 u=random.choice(string.ascii_letters)
 print(u,end='')
 if i in (30,70,100,130,170,200,230,250,290,320,350,380):
  print('')

print('\n')
print()
print('Access granted!') 
sleep(0.2)
input('Press Enter!')
print('')
print('   Follow   ')
print('Movserix Studio')

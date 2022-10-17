from os import lseek


for i in range(10):
  if i % 5 ==0:
    print('ham')
  elif i % 3 ==0:
    print('eggs')
  else:
    print('spam')
print('Finish!')
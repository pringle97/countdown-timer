import time

#defining the amount of seconds as t
def countdown(t):
  while t:
    mins, secs = divmod(t, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end="\r")
    time.sleep(1)
    t -= 1

  print('Time is up!')

#grabbing user input
t = input('Enter the amount of time in seconds: ')

#calling function
countdown(int(t))


try:
    input = raw_input
except NameError:
    pass
  
####

import random

def main():
    range_min = 1
    range_max = 100
    answer = random.randint(range_min+1, range_max-1)
    guess_count = 0
    
    while True:
        print('Range %d ~ %d' % (range_min, range_max))
        guess = input('Input your %dth guess: ' % (guess_count+1))
        guess = int(guess)
        if guess <= range_min or range_max <= guess:
            print('Your guess %d is beyond the valid range.' % guess)
        elif guess == answer:
            print('Yes, answer is %d!' % answer)
            break
        else:
            if answer < guess:
                range_max = guess
            else:
                range_min = guess
            guess_count += 1
    
if __name__ == '__main__':
    main()

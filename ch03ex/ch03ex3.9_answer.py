

def check_ab(answer, guess):
    a_count = 0
    b_count = 0
    for i in range(len(guess)):
        if guess[i] == answer[i]:
            a_count += 1
        elif guess[i] in answer:
            b_count += 1
        
    return (a_count, b_count)
    
if __name__ == '__main__':
    # simple test
    if check_ab('5234', '5346') != (1, 2):
        print('Failed: answer 5234, guess 5346')
    if check_ab('5234', '5234') != (4, 0):
        print('Failed: answer 5234, guess 5234')
    if check_ab('1234', '4321') != (0, 4):
        print('Failed: answer 1234, guess 4321')
    if check_ab('1234', '2134') != (2, 2):
        print('Failed: answer 1234, guess 2134')
    if check_ab('1234', '3241') != (1, 3):
        print('Failed: answer 1234, guess 3241')

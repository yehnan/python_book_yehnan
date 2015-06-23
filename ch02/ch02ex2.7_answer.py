

def plateau(data):
    if len(data) == 0:
        return None
        
    result_i_max = 0
    result_x_max = data[0]
    count_max = 1
    
    result_i = 0
    result_x = data[0]
    count = 1
    
    for i in range(1, len(data)):
        if data[i] > result_x:
            if count > count_max:
                result_i_max = result_i
                result_x_max = result_x
                count_max = count
            result_i = i
            result_x = data[i]
            count = 1
        else: # data[i] == result_x:
            count += 1
            
    return result_x_max

if __name__ == '__main__':
    # simple tests
    data = [0, 1, 1, 2, 3, 4, 5, 5, 9, 9, 9, 23, 25, 25, 25]
    if plateau(data) != 9:
        print('Failed')
        
    data = [1, 1, 1, 2, 3, 4, 5, 5, 9, 9, 9, 23, 25, 25, 25]
    if plateau(data) != 1:
        print('Failed')

    data = [1, 1, 1, 2, 3, 5, 5, 5, 5, 9, 9, 23, 25, 25, 25]
    if plateau(data) != 5:
        print('Failed')
        
# Can you improve this function to use lesser objects?


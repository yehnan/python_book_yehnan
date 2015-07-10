
# -*- coding: utf-8 -*-
# 串列裡含有由小到大排列好的整數，數字可能重複，
# 例如 [0, 1, 1, 2, 3, 4, 5, 5, 9, 9, 9, 23, 25, 25, 25]，
# 請撰寫函式找出重複最多次的整數，若重複次數相等則回傳值較小的，
# 以此例而言，9 與 25 都重複 3 次，應回傳 9。

# 若把「重複的整數」稱為「平台」，
# 那麼此問題可稱為找出「最長平台」的問題，
# 以上例而言，整數0這個平台的長度是1，整數1這個平台的長度為2，
# 依此類推，最長平台是9與25，根據題意應回傳9。

def plateau(data):
    if len(data) == 0:
        return None
                              # 記錄到目前為止找到的最長平台
    result_i_max = 0          # 一開始先把索引值0的元素當做最長平台
    result_x_max = data[0]    # 記錄該平台的整數，最後會成為此函式的回傳
    count_max = 1             # 該平台的長度，目前是1
    
                              # 記錄目前正在處理中的平台
    result_i = 0              # 從索引值0開始處理
    result_x = data[0]        # 記錄該平台的整數
    count = 1                 # 該平台的長度，目前是1
    
    for i in range(1, len(data)):          # 從索引值1開始
                                            # 檢查該元素（整數）是否大於前一平台，
        if data[i] > result_x:             # 若大於代表進入新的平台
            if count > count_max:          # 檢查前一平台的長度是否較長
                result_i_max = result_i
                result_x_max = result_x
                count_max = count
            result_i = i                   # 進入新的平台了，
            result_x = data[i]             # 所以重新設定目前正在處理的平台
            count = 1
        else: # data[i] == result_x:       # 若元素（整數）等於前一平台，該平台的長度加一
            count += 1                     # 換句話說，該平台繼續延伸
            
    return result_x_max                    # 此題目要求回傳result_x_max，
                                           # 有時則會需要result_i_max

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


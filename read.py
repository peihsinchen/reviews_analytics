# 算出評價資料有幾筆
data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1 # count = count + 1
        if count % 1000 == 0: # 每1000筆讀一次資料
            print(len(data)) # len 為清單長度
print('檔案讀取完了，總共有', len(data), '筆資料')

# 計算留言平均字數
sum_len = 0
for d in data:
    sum_len += len(d) # sum_len = sum_len + len(d)
print('留言的平均長度是', sum_len/len(data))

# 篩選出小於100字的留言
new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0]) # 印出長度小於100的第一筆資料
print(new[1])
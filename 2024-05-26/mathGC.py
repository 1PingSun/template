from statistics import mean, median, pstdev, pvariance, linear_regression, correlation


dataA = [[10, 8.04], [8, 6.95], [13, 7.58], [9, 8.81], [11, 8.33], [14,9.96], [6,7.24], [4, 4.26], [12, 10.84], [7, 4.82], [5, 5.68]]

dataB = [[10, 9.14], [8, 8.14], [13, 8.74], [9, 8.77], [11, 9.26], [14, 8.1], [6, 6.13], [4, 3.1], [12, 9.13], [7, 7.26], [5, 4.74]]

dataC = [[10,7.46], [8, 6.77], [13, 12.74], [9, 7.11], [11, 7.81], [14, 8.84], [6, 6.08], [4, 5.39], [12, 8.15], [7, 6.42], [5, 5.73]]

dataD = [[8, 6.58], [8, 5.76], [8, 7.71], [8, 8.84], [8, 8.47], [8, 7.04], [8, 5.25], [19, 12.5], [8, 5.56], [8, 7.91], [8, 6.89]]

arrayName = ["數據 A", "數據 B", "數據 C", "數據 D"]

allDatas = []
allDatas.append(dataA)
allDatas.append(dataB)
allDatas.append(dataC)
allDatas.append(dataD)

# 算術平均數
def getMean(data):
    return mean(data)

# 中位數
def getMedian(data):
    return median(data)

# 標準差
def getPstdev(data):
    return pstdev(data)

# 變異數
def getPvariance(data):
    return pvariance(data)

# 皮爾森相關係數
def getCorrelation(x, y):
    return correlation(x, y)

# 斜率與截距
# y = ax + b
# 斜率: a
# 截距: b
def getLinear_regression(x, y):
    return linear_regression(x, y)

# ===============================

count = 0
for data in allDatas:
    dataXArray = []
    dataYArray = []
    for i in data:
        dataXArray.append(i[0])
        dataYArray.append(i[1])

    print(f"=== For {arrayName[count]} ===")
    print(f"x 項陣列的算術平均數是：{getMean(dataXArray)}")
    print(f"y 項陣列的算術平均數是：{getMean(dataYArray)}")
    
    print(f"x 項陣列的標準差是：{getPstdev(dataXArray)}")
    print(f"y 項陣列的標準差是：{getPstdev(dataYArray)}")
    
    print(f"x 項陣列的變異數是：{getPvariance(dataXArray)}")
    print(f"y 項陣列的變異數是：{getPvariance(dataXArray)}")
    
    print(f"相關係數是：{getCorrelation(dataXArray, dataYArray)}")
    
    tmp1, tmp2 = getLinear_regression(dataXArray, dataYArray)
    print(f"y 對 x 的回歸直線是：y = {tmp1}x + {tmp2}")

    print()

    count += 1

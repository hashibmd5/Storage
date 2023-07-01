from DB.dbhandle import saveData, checkUserData, saveData_goods, check_goods
import time
def rechargeInfor(money,visitor):
    userData = checkUserData(visitor)
    visitor = userData['userName']
    userData['balance'] += money
    global accountData
    accountData = f'{time.strftime("%Y-%m-%d %X")}' \
                  f'用户{visitor}存入{money}元，当前账户余额为{userData["balance"]}元'
    userData['account'].append(accountData)
    saveData(userData)
    return True,f'用户{visitor}存款成功，现账户余额为{userData["balance"]}'

def accountInfor(visitor):
    userData = checkUserData(visitor)
    userDataInfor = f"用户{visitor}注册时间为{userData['注册时间']},账户余额为{userData['balance']}元"
    return True,userDataInfor,userData['account']

def tradeInfor(goodsName,goodsPrice,tradeNum,banlance):
    accountData = f'{time.strftime("%Y-%m-%d %X")}' \
                  f'用户{visitor}购买{goodsName}消费{goodsPrice * tradeNum}元，当前账户余额为{banlance}元'
    userData['account'].append(accountData)
    saveData(userData)
    return f'用户{visitor}购买{goodsName}成功，现账户余额为{banlance}元'

def setGoodsData():
    goodsData = {
        'goodsName': input("请输入商品名称"),
        'goodsBrand': input("请输入商品的品牌"),
        'goodsNum': input("请输入商品的数量"),
        'goodsPrice': input('请输入商品单价')
    }
    saveData_goods(goodsData)
    return True,f'商品录入成功，请选择接下来的操作'

def checkGoodsData(goodsName):
    goodsData = check_goods(goodsName)
    if goodsData:
        print(f'商品名称:{goodsData["goodsName"]}')
        print(f'品牌:{goodsData["goodsBrand"]}')
        print(f'数量:{goodsData["goodsNum"]}')
        print(f'单价:{goodsData["goodsPrice"]}')
        return True
    else:
        print('该商品不存在')



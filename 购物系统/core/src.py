from lib.common import divide
import hashlib, time
from DB.dbhandle import thoughGoodsInfor,check_goods,checkUserData
from api.user_i import registerInfor, loginInfor
from api.back_i import rechargeInfor, accountInfor, setGoodsData,checkGoodsData,tradeInfor
visitor = '游客'
manageName = ''
def seeGoods():
    print("》》》》》》浏览商品《《《《《《".center(50))
    items = thoughGoodsInfor()
    for goodsData in items:
        print(f'商品名称:{goodsData["goodsName"]}')
        print(f'品牌:{goodsData["goodsBrand"]}')
        print(f'数量:{goodsData["goodsNum"]}')
        print(f'单价:{goodsData["goodsPrice"]}')
    time.sleep(3)
    run()


def register():
    print("》》》》》》注册《《《《《《".center(50))
    userName = input("请输入您的用户名")
    userPassword = input("请输入您的密码")
    rePassword = input("请确认您的密码")
    if userPassword == rePassword:
        passwordSHA = hashlib.sha1(userPassword.encode())
        userPassword = passwordSHA.hexdigest()
        judge,result = registerInfor(userName,userPassword,registerTime = f"{time.strftime('%Y-%m-%d %X')}")
        if judge:
            print(result)
            time.sleep(3)
            run()
        else:
            print(result)
            time.sleep(3)
            run()
    else:
        print("两次密码输入不一致，请重新输入")
        time.sleep(3)
        register()
def login():
    print("》》》》》》登录《《《《《《".center(50))
    userName = input("请输入您的用户名")
    userPassword = input("请输入您的密码")
    passwordSHA = hashlib.sha1(userPassword.encode())
    userPassword = passwordSHA.hexdigest()
    judge,result = loginInfor(userName,userPassword)
    if judge:
        print(result)
        global visitor
        visitor = userName
        time.sleep(3)
        run()
    else:
        print(result)
        time.sleep(3)
        run()

@divide
def recharge():
    print("》》》》》》充值《《《《《《".center(50))
    time.sleep(1.5)
    money = int(input("请输入充值金额"))
    judge,result = rechargeInfor(money,visitor)
    if judge:
        print(result)
        time.sleep(3)
        run()
    else:
        print(result)
        time.sleep(3)
        login()
@divide
def checkAccount():
    print("》》》》》》查询账号信息《《《《《《".center(50))
    judge,result,account = accountInfor(visitor)
    if judge:
        print(result,'\n',account)
        time.sleep(3)
        run()

@divide
def trade():
    print("》》》》》》交易《《《《《《".center(50))
    goodsName = input('请输入要购买的商品')
    judge = checkGoodsData(goodsName)
    if judge:
        balance = checkUserData(visitor)['balance']
        tradeNum = int(input('请输入购买数量'))
        goodsNum = check_goods(goodsName)['goodsNum']
        goodsPrice = check_goods(goodsName)['goodsPrice']
        if tradeNum <= goodsNum:
            goodsNum -= tradeNum
            if balance >= goodsPrice * tradeNum:
                balance -= goodsPrice *tradeNum
                print(tradeInfor(goodsName,goodsPrice,tradeNum,balance))

def setGoods():
    manageData = {
        'manageName' : '浪子',
        'managePassword' : '20040416'
    }
    print("该功能仅对管理员开放")
    time.sleep(1.5)
    manageName = input("请输入管理员用户名")
    managePassword = input("请输入管理员密码")
    if managePassword in manageData['managePassword'] and manageName in manageData['manageName']:
        def inputGoods():
            print('请录入商品信息')
            judge,result = setGoodsData()
            if judge:
                print(result)
                print('''
                *************************
                *  1.继续入库  2.返回服务  *
                *************************
                ''')
                serve = int(input('请选择'))
                if serve == 1:
                    inputGoods()
                elif serve == 2:
                    run()
                else:
                    run()
        inputGoods()
    else:
        print('管理员账户或密码错误')
        time.sleep(3)
        run()





def welcome1():
    print(''''
    **********************
    *   欢迎来到京D购物中心  *
    **********************
    ''')
def welcome2():
    print('''
    ************************
    *     请选择服务项目      *
    * 1.浏览商品    2.注册    *
    * 3.登录       4.充值    *
    * 5.查询账号信息 6.交易   *
    * 7.退出       8.入库    *
    ************************
    ''')

funcSelect = {
    1: ["浏览商品",seeGoods],
    2: ["注册",register],
    3: ["登录", login],
    4: ["充值", recharge],
    5: ["查询账号信息",checkAccount],
    6: ["交易",trade],
    7: ["退出",exit],
    8: ['入库',setGoods]
}

def run():
    welcome2()
    Serve = int(input("请选择服务项目"))
    if Serve in funcSelect.keys():
        funcSelect[Serve][1]()
    else:
        print("输入错误，请重新输入")
        run()





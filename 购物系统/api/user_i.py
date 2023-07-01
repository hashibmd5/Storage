import time
from DB.dbhandle import saveData,checkUserData
def registerInfor(userName,userPassword,registerTime):
    userData = {
        "userName" : userName,
        "userPassword" : userPassword,
        "注册时间" : registerTime,
        "balance" : 0,
        'account':[]
    }
    if checkUserData(userName) == None:
        saveData(userData)
        return True,f"用户{userName}注册成功"
    else:
        return False,f"用户已存在，请重新注册"

def loginInfor(visitor,userPassword):
    if checkUserData(visitor) == None:
        return False,f"用户{visitor}不存在，请注册或重新输入"
    else:
        userData = checkUserData(visitor)
        if userPassword == userData['userPassword']:
            return True,f"用户{visitor}登录成功"
        else:
            return False,f'密码错误，请核对密码后输入'







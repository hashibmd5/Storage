
import json,os
from config.setting import filePathUser,filePathGood
def saveData(userData):
    name = userData["userName"]
    fileName = f"{filePathUser}/{name}"
    with open(f"{fileName}.json",mode='w',encoding="utf-8") as f:
        json.dump(userData,f)
def checkUserData(visitor):
    fileName = f"{filePathUser}/{visitor}.json"
    if os.path.exists(fileName):
        with open(fileName,mode='r',encoding='utf-8') as f:
            userData = json.load(f)
            return userData

def saveData_goods(goodsData):
    goodsName = goodsData['goodsName']
    fileName = f'{filePathGood}/{goodsName}'
    with open(f'{fileName}.txt',mode='w',encoding='utf-8') as goodsfile:
        goodsfile.write(f'商品名称:{goodsData["goodsName"]}\n')
        goodsfile.write(f'品牌:{goodsData["goodsBrand"]}\n')
        goodsfile.write(f'数量:{goodsData["goodsNum"]}\n')
        goodsfile.write(f'单价:{goodsData["goodsPrice"]}\n')

def check_goods(goodsName):
    fileName = f'{filePathGood}/{goodsName}'
    try:
        with open(fileName,'r',encoding='utf-8') as goodsData:
            goodsInfor = {
                'goodsName' : goodsName,
                'goodsBrand' : '',
                'goodsNum' : 0,
                'goodsPrice' : 0
            }
            for start in goodsData:
                if start.startswith('品牌: '):
                    goodsData['goodsBrand'] = start.split(': ')[1]
                elif start.startswith('数量: '):
                    goodsData['goodsNum'] = start.split(': ')[1]
                elif start.startswith('单价: '):
                    goodsData['goodsPrice'] = start.split(': ')[1]
                return goodsInfor
    except FileExistsError:
        return None

def thoughGoodsInfor():
    with open(filePathGood,'r',encoding='utf-8') as fileGood:
        return fileGood.read()








from core import src
import time
def divide(func):
    def inner(*args,**kwargs):
        if src.visitor == '游客':
            print("请先登陆")
            time.sleep(1.5)
            src.run()
        else:
            func(*args,**kwargs)
    return inner





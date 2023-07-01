
api -> 运行程序的主要接口 -》主要负责业务逻辑处理的功能 ——》 取钱，存钱。controller控制层（往往这个层面是比较繁杂）
	user_i.py => 用户业务逻辑处理，专门处理用户传进来的用户数据
	bank_i.py => 银行业务逻辑处理，专门处理银行的数据
	

config -> 配置信息 （数据库账号，数据库链接地址，文件存放地址）
	setting.py => 所有的项目配置文件

DB -》 database（数据库）数据层，进行数据储存的或者文件保存的位置
	dbHandle.py => 操作数据（增删改查）
	userData(文件夹) =》是一个文件夹，用来存储json文件

lib -》功能模块，主要放置中间件（redis，kafka，zookeper）或者装饰器
	common.py  =》这里只有装饰器
	
	
core -》 视图层，主要是管理用户视图
	src.py 用户显示的界面 
	
run.py -> 就是启动程序入口

readme.md -> 说明文档
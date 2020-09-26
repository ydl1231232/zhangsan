"""
print("你好，hello world!") #字符串
print(2333) #整数
print(2.333) #小数
print(True) #布尔值(一般用来判断) True False
print(()) #元祖
print([]) #数组
print({}) #字典
print("嘻嘻",2333,2.333)
print("哈哈"+"嘻哈")
print(((1+2)*100-99)/2)
print(4>3)

   变量
   赋值

a = "张三"#把张三这个值赋值给了名字叫a的这个变量#
print(a)
"""
# a = float(input("请输入:"))
# b = float(input("请输入:"))
# print("input获取内容:",a+b)
#数据格式转换
# print(type("哈哈笑"))
# print(type(2333))
# print(type(2.333))
# print(type(True))
# print(type(()))
# print(type([]))
# print(type({}))
#整数转换成小数
# a = int(input("请输入整数:"))
# b =int(input("请输入整数："))
# print("输出结果：",float(a+b))

#小数转换成整数
# a = float(input("请输入小数："))
# b = float(input("请输入小数："))
# print("输出结果：",int(a+b))

# """
# 练习：通过代码获取两端内容，并且计算他们的长度和
# """
# a = input("请输入：")
# b = input("请输入：")
# print("输出结果:",len(a+b),"位")


# 元祖,下标(从0开始编号)
#a = (1,2,3,4,"哈哈","哈哈","哈哈","哈哈","哈哈","嘻嘻",True,False)#
#print (a[0])#--下标格式变量a[需要的那个数字排列第几位-1]
#print(a.index("哈哈"))#查找某一个值的下标
#print(a.count("哈哈"))#统计有值的数量
#切片
#print(a[:4])#左闭右开
#print(a[4:10])
#print(a[10:])
#二维元祖
# b = (a,"嘻嘻","哈哈","嘻嘻","嘻嘻")
# print(b[0][4])  #a里面的哈哈

#元祖一旦写好过后不能修改，数组是可以修改的

#数组[]
# a=[1,2,3,4,"哈哈","哈哈","哈哈","哈哈","哈哈","嘻嘻",True,False]
# #a.append("append1")
# #a.append("append2")
# #a.insert(1,"insert")#insert是往数组中指定的位置插入数据
# # b=a.pop (0)#剪切 拿走“嘻嘻”
# # c=a.pop (0)
# # print (a)
# # print (b+c)
# a.remove("嘻嘻")#remove删除数组中的某个值
# print(a)

"""
python的语法
所有的方法都是小括号结尾。比如：print(),input(),len()
元祖、数组、字典的取值，都是用中括号,比如：a[0]
元祖，数组，字典的定语，分别是(),[],{}
"""

"""
字典的特点
1.字典中的值没有顺序
2.字典的接口必须是 键值对的结构。 key:value
3.字典的取值是，是通过Key去取这个value

"""
a={
   "name":"张三",
   0:"哈哈",
   "age":"25"
}
#取值
# print(a["name"])
# #新增
# a["high"]="183cm"
# print(a)
# #修改
# a["name"]="李四"
# print(a)

# b=a.get("name")
# print(b)
# b=a.pop("name")
# print(b)
# a.update(name=1111)
# print(a)
# print("............................")
# print (a.get("name"))
# print (a["name"])

# #数组跟字典的删除
# del a["name"]
# print(a)

"""
练习：
获取用户输入的个人信息，并且存储到字典中
个人信息包括了,name,age,sex.
"""
name=input("请输入用户姓名：")
age=input("请输入用户年纪：")
sex=input("请输入用户性别：")
userinfo = {}
userinfo.update(name=name,age=age,sex=sex)
print(userinfo)



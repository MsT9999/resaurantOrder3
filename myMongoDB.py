#!/usr/bin/python
#-*- coding: utf-8 -*-
# 後端連接
import datetime
import pymongo


# 資料庫連線
def connectDB():
    try:
        client = pymongo.MongoClient(
            "mongodb+srv://dbUser1:test123@dbtest.ojwhb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        )
        db = client.restaurant
        print('restaurant db connect succeed')
        return db
    except Exception as e:
        print(e)


# 讀取db collection中全部資料，並集合成list回傳
def findAllOrder():
    db = connectDB()
    mycol = db.order
    data ={}
    print(mycol.count_documents({}))  # db['mycol']內有多少筆資料
    doc: object
    for num,doc in enumerate(mycol.find({})):
        print("doc {}: {}".format(num, doc))
        data[str(num)] = doc
    print(data)
    return data

# 測試功能example 修改
def example_update():
    db = connectDB()
    mycol = db.order
    myquery = {"_id": "20210425001"}
    newvalues = {"$set": {"telephone": "(11)11111111"}}
    mycol.update_one(myquery, newvalues)
    print("modified")


# 測試功能example 刪除
def example_del():
    db = connectDB()
    mycol = db.order
    myquery = {"_id": "20210425001"}
    mycol.delete_one(myquery)
    print("deleted")


# 測試功能example 新增
def example_insert():
    db = connectDB()
    posts = db.order
    today = datetime.datetime.now()  # 當日日期 2021-04-25 ...
    datestr = str(today).split(' ')[0].replace('-', '')  # 當日日期字串處理 20210425
    post = {
        "_id": "20210516001",
        " Customer_name": "王小明",
        "telephone": "0923547813",
        "VIP": False,
        "Meals": {
            "pre-meal": ["salad", "chowder"],
            "Main_meal": "pasta",
            "dessert": " cheese cake",
            "drink": "Americano"
        },
        "Table_number": "01"
    }
    post_id = posts.insert_one(post)
    print(post_id + " inserted")


# 主程式測試
if __name__ == '__main__':
    connectDB()
    findAllOrder()

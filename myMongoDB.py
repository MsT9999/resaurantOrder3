#!/usr/bin/python
# -*- coding: utf-8 -*-
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
        print('<db connect succeed>')
        return db
    except Exception as e:
        print(e)
        print('<db connect failed>')


# 讀取db collection中全部資料，並集合成list回傳
def findAllOrder():
    try:
        db = connectDB()
        mycol = db.order
        data = []
        print(mycol.count_documents({}))  # db['mycol']內有多少筆資料
        doc: object
        for num, doc in enumerate(mycol.find({})):
            # print("doc {}: {}".format(num, doc))  # 印出json內容確認
            data.append(doc)
        # print(data)
        return data
    except Exception as e:
        print(e)
        return "action:find all <error!>"


# insert_one
# input parameter為 dict,json...
def insert(jsonodj):
    db = connectDB()
    mycol = db.order
    today = datetime.datetime.now()  # 當日日期
    datestr = str(today).split(' ')[0].replace('-', '')  # 當日日期字串處理
    timestr = str(today).split(' ')[1].split('.')[0].replace('.', '')
    post = {
        "_id": str(today),
        "date": datestr,
        "time": timestr,
        "data": jsonodj
    }
    mycol.insert_one(post)
    print("successfully inserted %n post date=",post)


# delete_one
# 單筆刪除
def delByID(idKey):
    print("<to delete> id=", idKey)
    query = {"_id": idKey}
    try:
        db = connectDB()
        mycoll = db.order
        mycoll.delete_one(query)
        print("[" + idKey + "]deleted")
    except Exception as e:
        print(e)


# findMany
# db collection中符合query的doc，並集合成list回傳
def findMany(query=""):
    print("<find Many> 條件=", query)
    try:
        db = connectDB()
        mycol = db.order
        data = []
        doc: object
        for num, doc in enumerate(mycol.find(query)):
            print("doc {}: {}".format(num, doc))  # 印出json內容確認
            data.append(doc)
        print("data", data)
        return data
    except Exception as e:
        print(e)


# find_one()
# db collection中符合query的第一筆doc
# example: query = {"date": "20210520"}
def findOne(query=""):
    print("<find One> 條件=", query)
    try:
        db = connectDB()
        mycol = db.order
        data = mycol.find_one(query)
        return data
    except Exception as e:
        print(e)


# updateOne
# 搜尋條件例子 myquery = {"_id": "2021-05-20_16.03.30.647379"}
# values參數
# 單一欄位值變更 格式:{欄位名稱:變更的新值} values範例-> {"data.telephone": "(11)11111111"}
# 多個欄位值變更 values範例-> {"data.telephone": "(11)11111111", "data.Customer_name": "小野大輔"}
def updateOne(myquery, values):
    try:
        db = connectDB()
        mycol = db.order
        newvalues = {"$set": values}
        mycol.update_one(myquery, newvalues)
        print("already updated")
    except Exception as e:
        print(e)


# updateMany
# 搜尋條件例子 myquery = {"_id": "2021-05-20_16.03.30.647379"}
# values參數
# 單一欄位值變更 格式:{欄位名稱:變更的新值} values範例-> {"data.telephone": "(11)11111111"}
# 多個欄位值變更 values範例-> {"data.telephone": "(11)11111111", "data.Customer_name": "小野大輔"}
def updateMany(myquery, values):
    try:
        db = connectDB()
        mycoll = db.order
        Devalues = {"$set": values}
        mycoll.update(myquery, Devalues)
        print("successfully modified")
    except Exception as e:
        print(e)


# 測試example 修改
def example_update():
    db = connectDB()
    mycol = db.order
    myquery = {"_id": "2021-05-20_16.03.30.647379"}
    newvalues = {"$set": {"data.telephone": "(11)11111111", "data.Customer_name": "小野大輔"}}  # {$set: {欄位名稱:變更的新值}}
    mycol.update_one(myquery, newvalues)
    print("modified")


# 測試 example 新增
def example_insert():
    db = connectDB()
    posts = db.order
    today = datetime.datetime.now()  # 當日日期
    datestr = str(today).split(' ')[0].replace('-', '')  # 當日日期字串處理
    timestr = str(today).split(' ')[1].split('.')[0].replace('.', '')
    print(datestr, timestr)
    post = {
        "_id": str(today).replace(" ", "_").replace(":", "."),
        "date": datestr,
        "time": timestr,
        "data": {"Customer_name": "凹醬",
                 "telephone": "0912123123",
                 "VIP": False,
                 "Meals": {
                     "pre": ["salad", "chowder"],
                     "soup": "today special",
                     "main": ["pasta", "pizza"],
                     "dish": "主廚推薦",
                     "garnishes": "當季時蔬",
                     "dessert": ["cheese cake", "ice cream"],
                     "drink": "Americano"
                 },
                 "Table_number": "18"}
    }
    post_id = posts.insert_one(post)
    print(str(post_id) + " inserted")


# 主程式測試
if __name__ == '__main__':
    findAllOrder()
    example_insert()
    example_update()

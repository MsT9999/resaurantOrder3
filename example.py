import pymongo
import datetime


def connectDB():    # 建立資料庫連線
    try:
        print('connecting...')
        # 建立Mongo Client的連線
        client = pymongo.MongoClient(
            "mongodb+srv://dbUser1:test123@dbtest.ojwhb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        )   # 此處字串於雲端Atler的連接方式中複製
        db = client.restaurant  # 使用名稱為restaurant的database
        print('connected successfully!')
        return db   # 回傳database
    except Exception as e:  # 例外錯誤處理
        print(e)    # 印出錯誤訊息


def exampleFindAll():   # 查詢collection中全部文件，並印出
    try:
        db = connectDB()  # 建立資料庫連線
        myCollection = db.order  # 使用名稱為order的collection
        # 印出db['<myCollection>']內有多少筆document
        print(str(myCollection.count_documents({})) + " record(s)")
        data = []   # 宣告data為list
        for doc in myCollection.find({}):
            data.append(doc)    # 將資料放入data的[]中
        print(data)  # 印出collection中所有資料
    except Exception as e:  # 例外錯誤處理
        print(e)    # 印出錯誤訊息


def exampleUpdate():    # 測試example 修改
    today = datetime.datetime.now()  # 當日日期
    db = connectDB()
    mycol = db.order
    myquery = {"_id": "10001"}
    test = {
        "data": {
            "name": "Abby",
            "phoneNumber": "091234567859",
            "VIP": False,
            "Table_number": "1",
            "Meals": {
                "pre": "菲達起司鮮果沙拉",
                "soup": "大蒜馬鈴薯湯",
                "dish": "海鹽醬烤茭白筍",
                "main": "香烤豬大排",
                "garnishes": "義式烤時蔬",
                "dessert": "焦糖烤布雷",
                "drink": "黑森林莓果茶"
            }
        },
        "datetime": today
    }
    newvalues = {"$set": test}  # {$set: {欄位名稱:變更的新值}}
    mycol.update_one(myquery, newvalues)
    print("updated successfully!")


def testUpdate():   # 測試example 修改
    db = connectDB()    # 建立資料庫連線
    myCollection= db.order  # 使用名稱為order的collection
    query = {"_id": "10001"}    # 查詢條件
    newValue = {
        "data.phoneNumber": "0912123456"
    }   # 要修改的資料內容 {欄位名稱:變更的新值}
    setValues = {"$set": newValue}  # {$set: {欄位名稱:變更的新值}}
    myCollection.update_one(query, setValues)   # 執行update_one
    print("updated successfully!")


def exampleInsert():    # 測試 example 新增
    try:
        db = connectDB()    # 建立資料庫連線
        myCollection = db.order    # 使用名稱為order的collection
        today = datetime.datetime.now()  # 當日日期
        post = {
            "_id": "10001",
            "datetime": today,
            "data": {"name": "Ardbert",
                     "phoneNumber": "0912123123",
                     "VIP": False,
                     "Table_number": "18",
                     "Meals": {
                         "pre": "沙拉",
                         "soup": "馬鈴薯湯",
                         "main": "茭白筍",
                         "dish": "豬大排",
                         "garnishes": "當季時蔬",
                         "dessert": "烤布雷",
                         "drink": "果茶"
                     }
            }
        }
        post_id = myCollection.insert_one(post)
        print(str(post_id) + " inserted successfully!")
    except Exception as e:  # 例外錯誤處理
        print(e)    # 印出錯誤訊息

def deleteByID(delId="10001"):  # delID為輸入參數，作為指定查詢_id的變數
    try:
        print("<to delete> id=", delId)
        db = connectDB()  # 建立資料庫連線
        mycoll = db.order  # 使用order這個collection
        query = {"_id": delId}  # 此處使用 _id 作為查詢條件
        mycoll.delete_one(query)    # 從db中刪除 _id符合的該筆資料
        print("[_id=" + delId + "]deleted successfully!")
    except Exception as e:  # 例外錯誤處理
        print(e)  # 印出錯誤訊息


def testDelete():
    try:
        db = connectDB()  # 建立資料庫連線
        mycoll = db.order  # 使用order這個collection
        # 從db中刪除 _id符合的該筆資料
        mycoll.delete_one({"_id": "10001"})
        print("[_id=10001]deleted successfully!")
    except Exception as e:  # 例外錯誤處理
        print(e)  # 印出錯誤訊息


# 主程式測試
if __name__ == '__main__':
    testDelete()
    exampleFindAll()
    exampleInsert()
    exampleFindAll()
    testUpdate()
    exampleFindAll()

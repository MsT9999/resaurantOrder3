from flask import Flask, render_template, url_for, jsonify, request
import myMongoDB as myMgDB

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


# 網頁路徑
# modify.html
@app.route('/modify')
def modifyPage():
    return render_template('modify.html')


# delete.html
@app.route('/delete')
def deletePage():
    return render_template('delete.html')


# insert.html
@app.route('/insert')
def insertPage():
    return render_template('insert.html')


# insert.html
@app.route('/insertV2')
def insertV2Page():
    return render_template('insertV2.html')


# index.html
@app.route('/index')
def indePage():
    return render_template('index.html')


# 首頁 根目錄
@app.route('/')
def root():
    return render_template('index.html')


# -----資料庫功能------
# 全部資料 find All
@app.route('/allOrder/'
           )  # root之下有allOrder這個路徑 輸入http://127.0.0.1:5000/allOrder/ 就可以看到json資料格式
def allOrder():  # 設置連接資料庫參數
    # 使用myMongoDB.py中的findAll方法 find全部資料
    data = myMgDB.findAllOrder()
    return jsonify(data)  # 回傳JSON資料


# 資料findOne 尋找單筆資料
@app.route('/findThis', methods=["GET", "POST"])
def find_this():
    if request.method == "POST":
        data = request.form
    if request.method == "GET":
        data = request.arg
    print("request = ", data)
    try:
        r_date = myMgDB.findOne(data)
        return r_date
    except Exception as e:
        print(e)
        return {'message': "error!", "action": "findOne"}


# insert功能 新增單筆紀錄
@app.route('/insertAn', methods=['GET', 'POST'])
def insert_an_order():  # 新增doc到db collection
    # 由於POST、GET獲取資料的方式不同，需要使用if語句進行判斷
    name = ""
    if request.method == "POST":
        name = request.get_json()["name"]
        data = request.get_json()
    if request.method == "GET":
        name = request.get_json()["name"]
        data = request.get_json()
        # 如果獲取的資料為空
    if name is None:
        # 訊息回傳網頁/insertAn路徑  返回值均為json
        return {'message': "error!"}
    else:
        # 使用 myMongoDb.py中的insert方法 參數為結構json
        myMgDB.insert(data)
        # 回傳網頁/insertAn路徑 返回值均為json
        return {'message': "success!", "data": data}

#  delete功能 刪除單筆紀錄
# app的路由地址"/delele1"即為ajax中定義的url地址，採用POST、GET方法均可提交
@app.route('/delele1', methods=["GET", "POST"])
def delete_by_idKey():
    idToDel = ""
    # 由於POST、GET獲取資料的方式不同，需要使用if語句進行判斷
    if request.method == "POST":
        idToDel = request.form.get("idKey")
    if request.method == "GET":
        idToDel = request.args.get("idKey")
    print(idToDel)
    if idToDel is None:
        return {'message': "error!", "action": "delete"}
    try:
        myMgDB.delByID(idToDel)  # 刪除該資料
        return {'message': "success!", "action": "delete"}
    except Exception as e:
        print(e)

# 資料修改
# UpdateOne
@app.route('/Update1', methods=["GET", "POST"])
def UpdateOne():  # 更新doc到db collection
    # query為搜尋條件 newValue為修改後的資料內容
    # 為json格式
    if request.method == "POST":
        myQuery = request.get_json()["query"]
        updateData = request.get_json()["newValue"]
    if request.method == "GET":
        myQuery = request.get_json()["query"]
        updateData = request.get_json()["newValue"]
    try:
        # print("you got a success")
        myMgDB.updateOne(myQuery,updateData)
        return {'message': "success!", "action": "UpdateOne"}
    except Exception as e:
        # print("you got an error")
        print(e)
        return {'message': "error!", "action": "UpdateOne"}


if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True  # 當template有修改會自動更新
    app.debug = True
    app.run()

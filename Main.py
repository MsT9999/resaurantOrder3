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
# 資料find
@app.route('/allOrder/'
           )  # root之下有allOrder這個路徑 輸入http://127.0.0.1:5000/allOrder/ 就可以看到json資料格式
def allOrder():  # 設置連接資料庫參數
    data = myMgDB.findAllOrder()
    return jsonify(data)  # 回傳JSON資料


# 資料findOne
@app.route('/findThis', methods=["GET", "POST"])
def find_this():  # 更新doc到db collection
    if request.method == "POST":
        data = request.form
    if request.method == "GET":
        data = request.arg
        # 如果獲取的資料為空
    print("request = ", data)
    try:
        rDate = myMgDB.findOne(data)
        return rDate
    except Exception as e:
        print(e)
        return {'message': "error!", "action": "UpdateOne"}


# 資料insert
@app.route('/insertAn', methods=["GET", "POST"])
def insert_an_order():  # 新增doc到db collection
    # 由於POST、GET獲取資料的方式不同，需要使用if語句進行判斷
    name = ""
    if request.method == "POST":
        name = request.form.get("name")
        data = request.form
    if request.method == "GET":
        name = request.args.get("name")
        data = request.args
        # 如果獲取的資料為空
    print(request)
    if name is None:
        return {'message': "error!"}
    else:
        print("request = ", data)
        myMgDB.insert(data)
        return {'message': "success!", "data": data}


#   delete
# 刪除單筆紀錄
@app.route('/delele1', methods=["GET", "POST"])
def delete_by_idKey():
    idToDel = ""
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

#
# 資料UpdateOne
@app.route('/Update1', methods=["GET", "POST"])
def UpdateOne():  # 更新doc到db collection
    print(request.form)
    print(request.args)
    try:
        # 這邊要調用myMongoDB.py的相關方法
        # myMgDB.updateOne() #需要參數 request的json之類的
        return {'message': "success!", "action": "UpdateOne"}
    except Exception as e:
        print(e)
        return {'message': "error!", "action": "UpdateOne"}


# (以下參考用)
# 前端網頁回傳測試
@app.route('/test')
def testP():
    return render_template('test.html')


# app的路由地址"/submit"即為ajax中定義的url地址，採用POST、GET方法均可提交
@app.route("/submit", methods=["GET", "POST"])
# 從這裡定義具體的函數 返回值均為json格式
def submit():
    # 由於POST、GET獲取資料的方式不同，需要使用if語句進行判斷
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
    if request.method == "GET":
        name = request.args.get("name")
        age = request.args.get("age")
    # 如果獲取的資料為空
    if len(name) == 0 or len(age) == 0:
        return {'message': "error!"}
    else:
        myMgDB.insert({'name': name, 'age': age})
        return {'message': "success!", 'name': name, 'age': age}
    # (以上為參考測試用)


if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True  # 當template有修改會自動更新
    app.run()

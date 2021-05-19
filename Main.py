from flask import Flask, render_template, url_for, jsonify, request
import myMongoDB as myMgDB

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/allOrder/'
           )  # root之下有allOrder這個路徑 輸入http://127.0.0.1:5000/allOrder/ 就可以看到json資料格式
def allOrder():  # 設置連接資料庫參數
    data = myMgDB.findAllOrder()
    return jsonify(data)  # 回傳JSON資料


@app.route('/PostOne/<VAL>')
def PostOne(VAL):  # 新增doc到db collection
    print(VAL)

    return ""


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
def insertPage():
    return render_template('insertV2.html')


# index.html
@app.route('/index')
def indexPage():
    return render_template('index.html')


# 首頁 根目錄
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run()

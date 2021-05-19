// window.setInterval(view, 10000);    //視窗每10秒執行view() function
function view() {       //view() function
    var jsonobj = null  //空資料
    $.getJSON("/allOrder/", {}, function (r) {   //接受Main.py的資料庫回傳值
        jsonobj = r;        //將資料庫回傳值放到jsonobj
        //json 網頁資料呈現

//        以下需要幫幫 用JS寫 把 json的資料塞到到index.html
//         http://127.0.0.1:5000/allOrder/ <-這邊有整個find all的json資料
        console.log(jsonobj);//確認json

    });
}

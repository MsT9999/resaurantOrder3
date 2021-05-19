window.setInterval(view, 5000);    //視窗每5秒執行view() function
function view() {       //view() function
    var jsonobj = null  //空資料
    $.getJSON("/allOrder/", {}, function (r) {   //接受Main.py的資料庫回傳值
        jsonobj = r;        //將資料庫回傳值放到jsonobj
        //json 網頁資料呈現

        //以下需要幫幫 用JS寫 把 json的資料塞到到index.html
        console.log(jsonobj);//確認json

    });
}

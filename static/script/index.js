// window.setInterval(view, 10000);    //視窗每10秒執行view() function
function view() {       //view() function
    var jsonobj = null  //空資料
    $.getJSON("/allOrder/", {}, function (r) {   //接受Main.py的資料庫回傳值
        jsonobj = r;        //將資料庫回傳值放到jsonobj
        //json 網頁資料呈現
            console.log("find");
            alert("find")
//          把json的資料塞到到index.html
//         http://127.0.0.1:5000/allOrder/ <-這邊有整個find all的json資料
//        console.log("json:",jsonobj);//確認json
//        console.log("find");
//        var data = jsonobj;
//        for (var item in data) {
//                console.log(item);
//                let content =
//                    "<div class='guest'>" +
//                    "<div class='list_head'>訂單編號:"+data[item]._id+"</div>"+
//                    "<ul>"+
//                    "<li>" + data[item].Customer_name +
//                    "<li>" + data[item].telephone +
//                    "</ul></div>";
//                    console.log("內容:",content);//確認
//
//                $("#history").append(content);
//            }
    });
}

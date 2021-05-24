const jsonUrl = "/allOrder/";
function view() {       //view() function
    document.getElementById("history").innerHTML='';
    var jsonobj = null  //空資料
    $.getJSON(jsonUrl,function (r) {   //接受Main.py的資料庫回傳值
        jsonobj = r;
        console.log("json:",jsonobj);//確認json
        var data = jsonobj;
        for (var item in data) {
            console.log("id:",data[item]._id);
            console.log("name:",data[item].data.Customer_name);
            let content =
                "<div class='row'>"+
                "<div class='guest col-md-6 offset-md-3 border-warning border-4'>" +
                "<div class='list_head border border-info'>訂單編號: " + data[item]._id+
                " <button class='btn btn-outline-danger btn-sm' onclick=\"control('" + data[item]._id + "');\">刪除此訂單</button>"+
                "</div>"+ "<ul>"+
                "<li>時間:" + data[item].date +" "+ data[item].time +
                "<li>客人姓名: " + data[item].data.name +
                "<li>客人電話: " + data[item].data.phoneNumber +
                    "<li>是否為VIP: " + data[item].data.VIP +
                "<li>餐點內容 "+
                    "<ul>"+
                        "<li> 前餐: "+ JSON.stringify(data[item].data.Meals.pre)+
                        "<li> 湯品: "+ JSON.stringify(data[item].data.Meals.soup)+
                        "<li> 副菜: "+ JSON.stringify(data[item].data.Meals.dish)+
                        "<li> 主菜: "+ JSON.stringify(data[item].data.Meals.main)+
                        "<li> 蔬菜: "+ JSON.stringify(data[item].data.Meals.garnishes)+
                        "<li> 甜點: "+ JSON.stringify(data[item].data.Meals.dessert)+
                        "<li> 飲品: "+ JSON.stringify(data[item].data.Meals.drink)+
                    "</ul>"+
                    "<li>桌號: "+ data[item].data.Table_number+
                "</ul></div></div>";
            $("#history").append(content);
        }
    });
}
function control(val) {
    console.log("準備刪除",val);
    $.ajax({
        url: "/delele1", /*資料(idKey)提交到delele1處*/
        type: "POST", /*採用POST方法提交*/
        data: { "idKey": val,"action":"going to Delete"
        }, /*提交的資料（json格式）*/
    /*result為後端函數返回的json*/
        success: function (result) {
            if (result.message == "success!") {
                alert(result.message,result.data)
            }
            else {
                alert(result.message)
            }
        }
    });
    view();
}
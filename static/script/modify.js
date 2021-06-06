
var name;

window.onload = showThis();

function showThis() {       //view() function
    var jsonobj = null  //空資料
    const jsonUrl = "/allOrder/";
    $.getJSON(jsonUrl,function (r) {   //接受Main.py的資料庫回傳值
        jsonobj = r;
        console.log("json:",jsonobj);//確認json
        var original = sessionStorage.getItem('_id');
        var data = jsonobj;
        for (var item in data) {
            if(data[item]._id==original){     
                document.getElementById("name").placeholder = data[item].data.name;
                document.getElementById("phoneNumber").placeholder = data[item].data.phoneNumber;
                document.getElementById("VIP").placeholder = data[item].data.VIP;
                document.getElementById("Table_number").placeholder = data[item].data.Table_number;
                
                if(JSON.stringify(data[item].data.Meals.pre) != undefined)
                    document.getElementById("pre").placeholder = JSON.stringify(data[item].data.Meals.pre);
                if(JSON.stringify(data[item].data.Meals.soup) != undefined)
                    document.getElementById("soup").placeholder = JSON.stringify(data[item].data.Meals.soup);
                if(JSON.stringify(data[item].data.Meals.dish) != undefined)
                    document.getElementById("dish").placeholder = JSON.stringify(data[item].data.Meals.dish);
                if(JSON.stringify(data[item].data.Meals.main) != undefined)
                    document.getElementById("main").placeholder = JSON.stringify(data[item].data.Meals.main);
                if(JSON.stringify(data[item].data.Meals.garnishes) != undefined)
                    document.getElementById("garnishes").placeholder = JSON.stringify(data[item].data.Meals.garnishes);
                if(JSON.stringify(data[item].data.Meals.dessert) != undefined)
                    document.getElementById("dessert").placeholder = JSON.stringify(data[item].data.Meals.dessert);
                if(JSON.stringify(data[item].data.Meals.drink) != undefined)
                    document.getElementById("drink").placeholder = JSON.stringify(data[item].data.Meals.drink);
            }
        }
        sessionStorage.removeItem('_id');
    });
}

function addData(){
    const var_name = ['phoneNumber', 'VIP', 'Table_number', 'pre', 'soup', 'dish', 'main', 'garnishes', 'dessert', 'drink']
    var length = var_name.length
    var obj = {};
    var tmp;
    for(var i = 0; i<3; i++){
        tmp = document.querySelector("#"+var_name[i])
        if((tmp != null) && (tmp.value != "")){
            if(var_name[i]==="VIP"){
                if((tmp.value.toString()==="yes")){
                    tmp.value = true;
                }
                else if((tmp.value.toString()==="no")){
                    tmp.value = false;
                }
                else{
                    alert("請更換VIP欄位敘述，如果該位為VIP顧客請輸入yes，如不是請輸入no");
                    return
                }
            }
            tmp = tmp.value;
            console.log(tmp)
            obj[var_name[i]] = tmp
        }
    }

    var Meals={};
    for(var i = 3; i<length; i++){
        tmp = document.querySelector("#"+var_name[i])
        if((tmp != null) && (tmp.value != "")){
            var str = tmp.value
            Meals[var_name[i]] = str.slice(0, str.length-1);
        }
    }

    if((Meals!=null) && (Meals.value!="")){
        obj['Meals'] = Meals
    } 

    $.ajax({
        url: '/insertAn', /*資料提交到insertAnOrder處*/
        type: 'POST', /*採用POST方法提交*/
        data: JSON.stringify(obj),
        contentType: 'application/json; charset=UTF-8',
        /*提交的資料（json格式），從輸入框中獲取
        result為後端函數返回的json*/
        success: function (_data, result) {
        },
        error: function(XMLHttpRequest, textStatus, errorThrown){
        }
    });

 }

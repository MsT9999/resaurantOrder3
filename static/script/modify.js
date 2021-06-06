

window.onload = showThis();

function showThis() {       //view() function
    var jsonobj = null  //空資料
    const jsonUrl = "/allOrder/";
    $.getJSON(jsonUrl,function (r) {   //接受Main.py的資料庫回傳值
        jsonobj = r;
        console.log("json:",jsonobj);//確認json
        var original = sessionStorage.getItem('_id');
        var data = jsonobj;
        var str;
        for (var item in data) {
            if(data[item]._id==original){    
                if(data[item].data.name != undefined){
                    str = data[item].data.name;
                    str = str.replace(/\"/g, "");
                    document.getElementById("name").value = str 
                }   
                if(data[item].data.phoneNumber != undefined){
                    str = data[item].data.phoneNumber;
                    str = str.replace(/\"/g, "");
                    document.getElementById("phoneNumber").value = str 
                }   
                if(data[item].data.VIP != undefined){
                    str = data[item].data.VIP;
                    str = str.replace(/\"/g, "");
                    document.getElementById("VIP").value = str 
                }   
                if(data[item].data.Table_number != undefined){
                    str = data[item].data.Table_number;
                    str = str.replace(/\"/g, "");
                    document.getElementById("Table_number").value = str 
                }   
                
                if(JSON.stringify(data[item].data.Meals.pre) != undefined){
                    str = JSON.stringify(data[item].data.Meals.pre);
                    str = str.replace(/\"/g, "");
                    document.getElementById("pre").value = str 
                }              
                if(JSON.stringify(data[item].data.Meals.soup) != undefined){
                    str = JSON.stringify(data[item].data.Meals.soup);
                    str = str.replace(/\"/g, "");
                    document.getElementById("soup").value = str 
                }
                if(JSON.stringify(data[item].data.Meals.dish) != undefined){
                    str = JSON.stringify(data[item].data.Meals.dish);
                    str = str.replace(/\"/g, "");
                    document.getElementById("dish").value = str 
                }
                if(JSON.stringify(data[item].data.Meals.main) != undefined){
                    str = JSON.stringify(data[item].data.Meals.pre);
                    str = str.replace(/\"/g, "");
                    document.getElementById("pre").value = str 
                }
                if(JSON.stringify(data[item].data.Meals.garnishes) != undefined){
                    str = JSON.stringify(data[item].data.Meals.garnishes);
                    str = str.replace(/\"/g, "");
                    document.getElementById("garnishes").value = str 
                }
                if(JSON.stringify(data[item].data.Meals.dessert) != undefined){
                    str = JSON.stringify(data[item].data.Meals.dessert);
                    str = str.replace(/\"/g, "");
                    document.getElementById("dessert").value = str 
                }
                if(JSON.stringify(data[item].data.Meals.drink) != undefined){
                    str = JSON.stringify(data[item].data.Meals.drink);
                    str = str.replace(/\"/g, "");
                    document.getElementById("drink").value = str 
                }
            }
        }
    });
}

function modifyData(){
    var original = sessionStorage.getItem('_id');
    const var_name = ['phoneNumber', 'VIP', 'Table_number', 'pre', 'soup', 'dish', 'main', 'garnishes', 'dessert', 'drink']
    var length = var_name.length
    var obj = {};
    var tmp;
    for(var i = 0; i<3; i++){
        tmp = document.querySelector("#"+var_name[i])
        if((tmp != null) && (tmp.value != "")){
            if(var_name[i]==="VIP"){
                if((tmp.value.toString()==="yes")){
                    tmp.value = "yes";
                }
                else if((tmp.value.toString()==="no")){
                    tmp.value = "no";
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
            var str = tmp.value;
            str = str.replace(/\"/g, "");
            Meals[var_name[i]] = str.slice(0, str.length-1);
        }
    }

    if((Meals!=null) && (Meals.value!="")){
        obj['Meals'] = Meals
    } 

    var modifyObj = {};
    var queryObj = {};
    var newObj = {};
    
    queryObj['_id'] = original;
    newObj['data'] = obj
    modifyObj['query'] = queryObj;
    modifyObj['newValue'] = newObj;

    console.log(modifyObj);
    
    $.ajax({
        url: '/Update1', /*資料提交到insertAnOrder處*/
        type: 'POST', /*採用POST方法提交*/
        data: JSON.stringify(modifyObj),
        contentType: 'application/json; charset=UTF-8',
        /*提交的資料（json格式），從輸入框中獲取
        result為後端函數返回的json*/
        success: function (_data, result) {
        },
        error: function(XMLHttpRequest, textStatus, errorThrown){
        }
    });
    
    sessionStorage.removeItem('_id');

 }

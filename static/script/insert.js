
 function addData(){
    const var_name = ['phoneNumber', 'VIP', 'Table_number', 'pre', 'soup', 'dish', 'main', 'garnishes', 'dessert', 'drink']
    var length = var_name.length
    var obj = {
        name: document.querySelector("#name").value
    };
    var formname = document.querySelector("#name").value;
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

    console.log(obj);

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

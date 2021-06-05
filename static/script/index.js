// 先放在index.html中，確認完全能使用在分檔
const jsonUrl = "/allOrder/";
var datas ;
var counts;counts=0;
function test(){
        document.getElementById("order").innerHTML='';
        var jsonobj = null  //空資料
        $.getJSON(jsonUrl,function (r) {   //接受Main.py的資料庫回傳值
        jsonobj = r;
        console.log("json:",jsonobj);//確認json
        data = jsonobj;
         for (var item in data) {
         console.log("id:",data[item]._id);
           datas =  data[item].data._id;
        }
       });
        counts=datas.length;
         var i;
         for (i=0;i < counts; i++) {
         document.order.options[i] = new Option(datas[i],i); }
        }
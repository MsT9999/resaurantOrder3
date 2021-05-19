
function addData() {
    var Cname = document.querySelector("#name").val;
    var Tnum = document.querySelector("#phoneNumber").val;
    console.log(Cname,Tnum);
    $.ajax({
        url: "insertAnOrder", /*資料提交到insertAnOrder處*/
        type: "POST", /*採用POST方法提交*/
        data: { "name": $("#name").val(),"phoneNumber":$("#phoneNumber").val()
        }, /*提交的資料（json格式），從輸入框中獲取*/
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
 }
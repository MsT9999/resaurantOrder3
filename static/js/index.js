window.setInterval(view, 20000);    //視窗每2秒執行view() function
        function view() {       //view() function

        }
        function control(val) { $.getJSON("/relay/" + val, {}, function (r) { }); }
        function controlLED(val) { $.getJSON("/led/" + val, {}, function (r) { }); }
var myVar = setInterval(myTimer, 1000);
            var id = document.getElementById("proslo");
            var id = document.getElementById("int");
            var int = 0;
            var myVar = setInterval(myTimerr, 1000);
            function myTimer() {
                var d = new Date();
                document.getElementById("demo").innerHTML = d.toLocaleTimeString();
            }

            function myTimerr() {
                document.getElementById("int").innerHTML = int;
                int++;
                id.value = int;
            }
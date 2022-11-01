 open-popup = document.querySelector("#open-popup").addEventlistener("click",function() {
                document.querySelector(".open-popup").classList.add("active");
        });
 close-btn = document.querySelector(".popup .close-btn").addEventlistener("click",function() {
            document.querySelector(".popup").classList.remove("active");
        });
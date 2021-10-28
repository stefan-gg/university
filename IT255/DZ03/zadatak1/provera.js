function provera() {
    var ime = document.getElementById("ime").value;
    var godine = parseInt(document.getElementById("godine").value);
    var email = document.getElementById("email").value;

    for (var i = 0; i < ime.length; i++) {
        if (!isNaN(ime.charAt(i))) {
            alert('Imate broj u imenu, ili ste uneli više od jedne reči, ispravite to.');
        }
    }

    if(godine < 0 || godine > 150){
        document.getElementById("greska").innerHTML =  "Uneli ste negativan ili preveliki broj u polju za godne !! (maksimum je 150)";
    }

    if(email.length == 0){
        alert("Polje za email ste ostavili prazno !!");
    }
}
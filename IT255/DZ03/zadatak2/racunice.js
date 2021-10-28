function sabiranje() {
    var prviBroj = parseInt(document.getElementById("broj1").value);
    var drugiBroj = parseInt(document.getElementById("broj2").value);
    var rez = prviBroj + drugiBroj
    document.getElementById("rez").innerHTML = "Rezultat je : " + rez;
}

function oduzimanje() {
    var prviBroj = parseInt(document.getElementById("broj1").value);
    var drugiBroj = parseInt(document.getElementById("broj2").value);
    var rez = prviBroj - drugiBroj
    document.getElementById("rez").innerHTML = "Rezultat je : " + rez;
}

function mnozenje() {
    var prviBroj = parseInt(document.getElementById("broj1").value);
    var drugiBroj = parseInt(document.getElementById("broj2").value);
    var rez = prviBroj * drugiBroj
    document.getElementById("rez").innerHTML = "Rezultat je : " + rez;
}

function deljenje() {
    var prviBroj = parseInt(document.getElementById("broj1").value);
    var drugiBroj = parseInt(document.getElementById("broj2").value);
    var rez = prviBroj / drugiBroj
    document.getElementById("rez").innerHTML = "Rezultat je : " + rez;
}

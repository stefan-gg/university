function proveriPodatke() {

    let validnaDuzina = new Promise(

        function (resolve, reject) {

            let password = document.getElementById("password").value;
            
            if (password.length > 6 && password.length < 10) {
                resolve();
            } else {
                reject();
            }
        }
    );

    validnaDuzina.then(
        function () { window.location.replace("uspeh.html"); },

        function () { document.getElementById("greska").innerHTML = "Šifra mora imati između 6 i 10 karaktera"; }
    );
}
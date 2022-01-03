from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return """
        <!DOCTYPE html>
            <head>
                <title>Flask - prva stranica</title>
            </head>
            <body>
                <a>Prva stranica statičkog HTML-a</a>
                <p>Najobičniji HTML sadržaj</p>
                <p>Za više sadržaja posetite /nova_ruta</p>
            </body>
        </html>
    """


@app.route('/nova_ruta')
def page01():
    content = """
   <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IT255 - DZ02</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
        integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
        crossorigin="anonymous"></script>
    <style>
        .levo{
            margin-left: 7%;
            display: flex;
            flex-direction: column;
        }

        .razmak{
            letter-spacing: 2px;
            margin-top: 20px;
            margin-bottom: unset;
            font-size: 22px;
        }

        .link{
            margin-left: 15%;
        }

        .dugme{
            border: 1px solid black;
            padding: 15px;
        }

        .desno{
            display: flex;
            flex-direction: column;
            margin-left: 30%;
            align-items: center;
            justify-content: center;
        }

        .sredina{
            display: flex;
            flex-direction: row;
            justify-content: center;
            align-items: center;
            margin-left: 30%;
        }

        .wrapper{
            display: flex;
        }

        img{
            height: 1700px;
            width: 100%;
        }

        .slika{
            height: 700px;
            background-image: url(https://github.com/stefan-gg/university/blob/third-year/IT255/DZ02/zadatak1/slika.png?raw=true);
        }

        .tekst{
            align-items: center;
            text-align: center;
            justify-content: center;
            display: flex;
            flex-direction: column;
            height: 700px;
            color: white;
        }

        h1{
            letter-spacing: 15px;
        }

        button{
            margin-top: 5%;
            color: black;
            padding: 10px;
        }    
    </style>
</head>

<body>
    <nav>
        <div class="wrapper">
            <div class="levo">
                <p class="razmak"><a href="#">ARARAT</a></p>
                <p>Architectyre</p>
            </div>
            <div class="sredina">
                <a class="link" href="#">About</a>
                <a class="link" href="#">Home</a>
                <a class="link" href="#">Products</a>
                <a class="link" href="#">Services</a>
            </div>
            <div class="desno">
                <a href="#" class="dugme">
                    Get in touch
                </a>
            </div>
        </div>
    </nav>
    <div class="slika">
        <div class="tekst">
            <h1>WE DESIGN YOUR SPACE</h1>
            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Illo, necessitatibus!</p>
            <button type="button" class="btn btn-outline-light">Light</button>
        </div>
    </div>
</body>

</html>
    """
    return content

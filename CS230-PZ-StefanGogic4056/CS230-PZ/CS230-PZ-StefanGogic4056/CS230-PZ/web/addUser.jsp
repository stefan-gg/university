<%@page import="entities.Korisnik"%>
<%@page import="crud.CrudUser"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Create new account</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"  crossorigin="anonymous" />
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"  crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" crossorigin="anonymous"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"/> 
        <link rel="stylesheet" href="css/style.css" />
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <%
                if (session.getAttribute("admin") != null) {
            %>
            <form method="POST" action="Admin">
                <input type="submit" class="btn btn-secondary" value="Admin page" />
            </form>
            <%
                }
            %>
            <a class="navbar-brand" href="index.html">Home page</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

        </nav>
        <%
            if (request.getParameter("username") != null) {
                out.println(request.getParameter("username"));
                String username = request.getParameter("username").toString();
                String password = request.getParameter("password").toString();
                String confPassword = request.getParameter("confPassword").toString();

                Korisnik user = CrudUser.checkUsername(username);
                if (user == null) {
                    if (password.equals(confPassword)) {
                        user = new Korisnik();
                        user.setUsername(username);
                        user.setPassword(password);
                        user.setIdRola(CrudUser.readUserRole("User"));
                        user.setPreostaloVreme(0);
                        user.setUkupanBrojMinuta(0);
                        user.setImeSlike(null);
                        user.setIdRacunara(CrudUser.readComputerId(0));
                        CrudUser.insert(user);
                        session.setAttribute("newUsername", username);
                        out.println("<p class=\"text-light\">Account is created, if you want to add picture press button under this text!</p>");
        %>
        <form method="POST" enctype="multipart/form-data" action="upload.jsp" > 
            <input type="file" class="btn btn-secondary" accept="image/*" name="file" size="50" /> <br/> 
            <input class="btn btn-primary" type="submit" value="Submit my picture" /> 
        </form> 
        <%
        } else {
        %>
        <div class="alert alert-danger" role="alert">
            Password and confirm password do not match !
        </div>
        <%
            }
        } else {
        %>
        <div class="alert alert-danger" role="alert">
            That username is already taken !
        </div>
        <%
                }
            }
        %>
        <h1 class="text-light">Fill all the fields please !</h1>
        <div class="add">
            <form method="POST" action="addUser.jsp">
                <div class="form-group">
                    <label class="font-weight-bold" for="username">Username</label>
                    <input type="text" placeholder="Username" class="form-control" name="username" id="username" required="" minlength="5" /><br/>
                </div>
                <div class="form-group">
                    <label class="font-weight-bold" for="password">Password</label>
                    <input type="password" placeholder="Password" class="form-control" name="password" id="password" required="" minlength="6" /><br/>
                </div>
                <div class="form-group">
                    <label class="font-weight-bold" for="confPassword">Confirm password</label>
                    <input type="password" placeholder="Confirm Password" class="form-control" name="confPassword" id="confPassword" required="" minlength="6" />
                </div>
                <h6 class="font-weight-bold">*By creating account you accept our <span class="badge badge-secondary">COOKIES !</span></h6>
                <input type="submit" class="btn btn-info" value="Create account" />
            </form>
        </div>
    </body>
</html>

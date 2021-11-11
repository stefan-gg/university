<%@page import="crud.CrudUser"%>
<%@page import="entities.Korisnik"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>CRUD page</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"  crossorigin="anonymous" />
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"  crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" crossorigin="anonymous"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"/> 
        <link rel="stylesheet" href="css/crud.css" />
    </head>
    <body>

        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="logout font-weight-bold navbar-brand" href="logout.jsp"><i class="fa fa-sign-out" aria-hidden="true"></i>Log out</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
        </nav>
        <form method="POST" action="Admin">
            <input class="btn btn-primary" type="submit" value="Take me back to the admin page"/>
        </form>
        <%
            if (request.getParameter("delete") != null) {
                int i = Integer.parseInt(request.getParameter("delete"));
                Korisnik user = CrudUser.read(i);
                CrudUser.delete(user);
                out.println("User is deleted !");
            } else if (request.getParameter("idd") != null) {
                int i = Integer.parseInt(request.getParameter("idd"));
                Korisnik user = CrudUser.read(i);

                user.setUsername(request.getParameter("username"));
                user.setIdRacunara(CrudUser.readComputerId(Integer.parseInt(request.getParameter("idComp"))));
                user.setPreostaloVreme(Integer.parseInt(request.getParameter("time")));
                user.setPassword(request.getParameter("pass"));

                CrudUser.update(user);
                out.println("User is updated !");
            } else if (request.getParameter("id") != null) {

                int i = Integer.parseInt(request.getParameter("id"));

                Korisnik user = CrudUser.read(i);

                int crud = Integer.parseInt(request.getParameter("crud"));

                if (crud == 0) {
                    out.println("<form method=\"POST\" action=\"crud.jsp\">\n"
                            + "            <p>ID </p><input type=\"text\" readonly name=\"idd\" value=\"" + user.getId() + "\"  />\n"
                            + "            <p>Usename </p><input type=\"text\"  name=\"username\" value=\"" + user.getUsername() + "\"  />\n"
                            + "            <p>Role </p><input type=\"text\" disabled=\"true\"  name=\"role\" value=\"" + user.getIdRola().getNazivRole() + "\"  />\n"
                            + "            <p>Password </p><input type=\"text\" name=\"pass\" value=\"" + user.getPassword() + "\"  />\n"
                            + "            <p>Time left </p><input type=\"text\"  name=\"time\" value=\"" + user.getPreostaloVreme() + "\"  />\n"
                            + "            <p>Total time </p><input type=\"text\" disabled=\"true\" name=\"timee\" value=\"" + user.getUkupanBrojMinuta() + "\"  />\n"
                            + "            <p>Computer ID </p><input type=\"number\" maxlength=\"1\"  min=\"0\" max=\"9\"  name=\"idComp\" value=\"" + user.getIdRacunara() + "\"  /><br/>\n"
                            + "            <input type=\"submit\" class=\"btn btn-success\" value=\"Update\"/>\n"
                            + "        </form>");
                } else {
        %>
        <p>Are you sure you want to delete this user ?</p>
        <%
                    out.println("<form method=\"POST\" action=\"crud.jsp\">\n"
                            + "            <p>ID </p><input type=\"text\" readonly name=\"delete\" value=\"" + user.getId() + "\"  /><br/>\n"
                            + "            <p>Usename </p><input type=\"text\" disabled=\"true\"  name=\"username\" value=\"" + user.getUsername() + "\"  /><br/>\n"
                            + "            <p>Password </p><input type=\"text\" disabled=\"true\" name=\"pass\" value=\"" + user.getPassword() + "\"  /><br/>\n"
                            + "            <p>Remaining time </p><input type=\"text\" disabled=\"true\"  name=\"time\" value=\"" + user.getPreostaloVreme() + "\"  /><br/>\n"
                            + "            <p>Total time </p><input type=\"text\" disabled=\"true\" name=\"timee\" value=\"" + user.getUkupanBrojMinuta() + "\"  /><br/>\n"
                            + "            <p>Computer ID </p><input type=\"number\" disabled=\"true\"  name=\"idComp\" value=\"" + user.getIdRacunara() + "\"  /><br/>\n"
                            + "            <input type=\"submit\" class=\"btn btn-danger\" value=\"Delete\"/>\n"
                            + "        </form>");
                }
            } else {
                response.sendRedirect("http://localhost:8080/CS230-PZ/index.html");
            }
        %>
    </body>
</html>

<%@page import="util.PreostaloVreme"%>
<%@page import="java.util.ArrayList"%>
<%@page import="crud.CrudUser"%>
<%@page import="crud.CrudUser"%>
<%@page import="entities.Korisnik"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Choose your computer</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"  crossorigin="anonymous" />
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"  crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" crossorigin="anonymous"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"/> 
        <link rel="stylesheet" href="css/guest.css" />
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="logout font-weight-bold navbar-brand" href="logout.jsp"><i class="fa fa-sign-out" aria-hidden="true"></i>Log out</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
        </nav>
        <%
            if (request.getParameter("computer") != null) {
                int comput = Integer.parseInt(request.getParameter("computer"));

                String username = (String) session.getAttribute("username");
        %>
        <p class="font-weight-bold">Current time </p><p class="timer" id="demo"></p>

        <h3>Welcome, <%= username + " !"%></h3>
        <%
            Korisnik k = CrudUser.checkUsername(username);
            PreostaloVreme pr = new PreostaloVreme();

            k.setIdRacunara(CrudUser.readComputerId(comput));
            CrudUser.update(k);

            session.setAttribute("id", k.getId());
            int tim = k.getUkupanBrojMinuta() + 2;

            response.setHeader("Refresh", "" + tim + ";url=http://localhost:8080/CS230-PZ/logout.jsp");
            pr.setUserId(k.getId());
            pr.setVreme(0);
            pr.start();

            out.println("<p> Total time : " + k.getPreostaloVreme() + "</p>");
        %>
        <p font-weight-bold>Time passed : <input class="font-weight-bold" type="text" disabled="true" value="" id="int" /></p>
        <div class="games">
            <p>All available games are shown below</p>
            <a href="#"><img class="game"  src="games/csgo.jpg" alt="CS:GO"/></a>
            <a href="#"><img class="mc"  src="games/minecraft.jpg" alt="Minecraft"/></a>
            <a href="#"><img class="game"  src="games/fifa21.jpg" alt="FIFA 21"/></a>
            <a href="#"><img class="game"  src="games/pes21.jpg" alt="PES 21"/></a>
        </div>
        <script src="javascript/timer.js">
        </script>
        <%} else {
                response.sendRedirect("http://localhost:8080/CS230-PZ/index.html");
            }
        %>
    </body>
</html>
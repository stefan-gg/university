<%@page import="util.PreostaloVreme"%>
<%@page import="crud.CrudUser"%>
<%@page import="entities.Korisnik"%>
<%@page import="entities.Korisnik"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>User Page</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"  crossorigin="anonymous" />
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"  crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" crossorigin="anonymous"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"/> 
        <link rel="stylesheet" href="css/user.css" />
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <div class="logout dropdown show">
                <a class="btn btn-secondary dropdown-toggle" href="#" role="button" id="dropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    <i class="profile fa fa-user" aria-hidden="true"></i>Profile
                </a>

                <div class="dropdown-menu" aria-labelledby="dropdownMenuLink">
                    <a class="dropdown-item" href="logout.jsp"><i class="fa fa-sign-out" aria-hidden="true"></i>Log out</a>
                </div>
            </div>

        </nav>
        <%
            if (request.getParameter("computer") != null && request.getParameter("addTime") != null) {

                int comput = Integer.parseInt(request.getParameter("computer"));
                int time = Integer.parseInt(request.getParameter("addTime"));

                String username = (String) session.getAttribute("username");
                Korisnik k = CrudUser.checkUsername(username);
                
                String picture = k.getImeSlike();
                
                if(picture == null){
                    picture = "default.png";
                }
                out.println("<img class=\"rounded float-right\" src=\"pictures/" + picture + "\" alt=\"Profile picture\" />");
        %>
        <p class="align font-weight-bold">Current time </p><p class="align timer" id="demo"></p>

        <h3 class="align">Welcome, <%= username + " !"%></h3>
        <%

            k.setUkupanBrojMinuta(k.getUkupanBrojMinuta() + time);
            k.setPreostaloVreme(k.getPreostaloVreme() + time);
            k.setIdRacunara(CrudUser.readComputerId(comput));
            CrudUser.update(k);

            session.setAttribute("id", k.getId());
            int tim = k.getUkupanBrojMinuta() + 2;

            response.setHeader("Refresh", "" + tim + ";url=http://localhost:8080/CS230-PZ/logout.jsp");
            PreostaloVreme pr = new PreostaloVreme();
            pr.setUserId(k.getId());
            pr.setVreme(0);
            pr.start();
            if (k.getPreostaloVreme() == 1) {
                session.invalidate();
            }

            out.println("<p class=\"align\"> Total time : " + k.getPreostaloVreme() + "</p>");
        %>
        <p  class="font-weight-bold">Time passed : <input class="font-weight-bold" type="text" disabled="true" value="" id="int" /></p>

        <button type="button"><a href="logout.jsp">Log out earlier</a></button>

        <div class="games">
            <p>All available games are shown below</p>

            <a href="#"><img class="game" src="games/csgo.jpg" alt="CS:GO"/></a>
            <a href="#"><img class="game" src="games/minecraft.jpg" alt="Minecraft"/></a>
            <a href="#"><img class="game" src="games/fifa21.jpg" alt="FIFA 21"/></a>
            <a href="#"><img class="game" src="games/pes21.jpg" alt="PES 21"/></a>
        </div>
        <script src="javascript/timer.js">
        </script>
        <%            } else {
                response.sendRedirect("http://localhost:8080/CS230-PZ/index.html");
            }
        %>

    </body>
</html>

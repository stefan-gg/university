<%@page import="entities.Korisnik"%>
<%@page import="crud.CrudUser"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Checking your information...</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"  crossorigin="anonymous" />
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"  crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" crossorigin="anonymous"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"/> 
        <link rel="stylesheet" href="css/style.css" />
    </head>
    <body>
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="navbar-brand" href="index.html">Home page</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
        </nav>
        <%
            if (request.getParameter("username") == null || request.getParameter("password") == null) {
                out.println("<h3>Your must fill all fields</h3>");
                out.println("<p>Redirecting back to home page in 5 seconds...</p>");
                response.setHeader("Refresh", "5;url=http://localhost:8080/CS230-PZ/index.html");
            } else if (request.getParameter("username") != null && request.getParameter("password") != null) {
                String username = (String) request.getParameter("username");
                String password = (String) request.getParameter("password");
                Korisnik k = CrudUser.checkData(username, password);

                if (k == null) {
                    out.println("<h3>Your username or password are not correct</h3>");
                    out.println("<p>Redirecting back to home page in 5 seconds...</p>");
                    response.setHeader("Refresh", "5;url=http://localhost:8080/CS230-PZ/index.html");
                } else {
                    if (k.getIdRola().getNazivRole().equals("Admin")) {
                        session.setAttribute("id", k.getId());
                        session.setAttribute("admin", "1");
        %>
        <form method="POST" action="Admin">
            <input class="check btn btn-primary" type="submit" value="Take me to the admin page"/>
        </form>
        <%
        } else if (k.getIdRola().getNazivRole().equals("User")) {

            Cookie[] cookies = request.getCookies();
            for (int i = 0; i < cookies.length; i++) {
                if (cookies[i].getName().toString().contains("userr")) {
                    String idd = cookies[i].getName().toString().replace("userr", "");
                    int id = Integer.parseInt(idd);
                    int time = Integer.parseInt(cookies[i].getValue());

                    if (id == k.getId()) {
                        k.setPreostaloVreme(time);
                        CrudUser.update(k);
                    }

                    /*cookies[i].setMaxAge(0);
                    response.addCookie(cookies[i]);*/
                }
            }

            session.setAttribute("idU", k.getId());
        %>
        <form method="POST" action="Guest">
            <input class="check btn btn-primary" type="submit" value="Choose computer"/>
        </form>
        <%
                    }
                }
            } else {
                response.sendRedirect("http://localhost:8080/CS230-PZ/index.html");
            }
        %>
    </body>
</html>

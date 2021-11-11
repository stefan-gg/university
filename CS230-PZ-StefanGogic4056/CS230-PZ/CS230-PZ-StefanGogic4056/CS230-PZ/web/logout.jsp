<%@page import="entities.Korisnik"%>
<%@page import="crud.CrudUser"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Log out</title>
    </head>
    <body>
        <%  Korisnik user = null;
            if (session.getAttribute("id") != null) {
                int id = Integer.parseInt(session.getAttribute("id").toString());
                user = CrudUser.read(id);
                if (user.getIdRola().getNazivRole().equals("Guest")) {
                    CrudUser.delete(user);
                    session.invalidate();
                    response.setHeader("Refresh", "3;url=http://localhost:8080/CS230-PZ/index.html");
                } else if (user.getIdRola().getNazivRole().equals("User")) {
                    // dodaj da se nadoknadi vreme tj. da se sacuva trenutno vreme u sesiju a da se setuje preostalo vreme na 0 kako bi stao tajmer
                    int idUsera = Integer.parseInt(session.getAttribute("id").toString());
                    user = CrudUser.read(idUsera);

                    int time = user.getPreostaloVreme();

                    user.setPreostaloVreme(0);
                    user.setIdRacunara(CrudUser.readComputerId(0));
                    CrudUser.update(user);

                    Cookie cookie = new Cookie("userr" + idUsera, "" + time);
                    cookie.setMaxAge(60 * 60 * 24 * 365);
                    response.addCookie(cookie);

                    /*user.setPreostaloVreme(time);
                    
                    CrudUser.update(user);*/
                    session.setAttribute("userId", user.getId());
                    session.setAttribute("timeLeft", time);

                    session.setAttribute("idU", null);
                    session.invalidate();
                    response.setHeader("Refresh", "4;url=http://localhost:8080/CS230-PZ/index.html");
                } else {
                    session.invalidate();
                    response.setHeader("Refresh", "4;url=http://localhost:8080/CS230-PZ/index.html");
                }

        %>
        <h3>Logging out...</h3>
        <%} else {
                response.sendRedirect("http://localhost:8080/CS230-PZ/index.html");
            }
        %>
    </body>
</html>

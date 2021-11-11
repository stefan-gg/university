package rs.ac.metropolitan.cs230.servleti;

import crud.CrudUser;
import entities.Korisnik;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

@WebServlet(name = "Guest", urlPatterns = {"/Guest"})
public class Guest extends HttpServlet {

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        PrintWriter out = response.getWriter();

        out.println("<!DOCTYPE html>");
        out.println("<html>");
        out.println("<head>");
        out.println("<link rel=\"stylesheet\" href=\"https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css\"  crossorigin=\"anonymous\" />\n"
                + "        <script src=\"https://code.jquery.com/jquery-3.3.1.slim.min.js\"  crossorigin=\"anonymous\"></script>\n"
                + "        <script src=\"https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js\" crossorigin=\"anonymous\"></script>\n"
                + "        <script src=\"https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js\" crossorigin=\"anonymous\"></script>\n"
                + "        <link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css\"/> ");
        out.println("<style>\n"
                + "body{text-align: center;}\n"
                + ".div { margin-left: auto; margin-right: auto; width: 500px;}\n"
             
                + "</style>");
        out.println("<title>Choose your computer</title>");
        out.println("</head>");
        out.println("<body>");
        HttpSession session = request.getSession();

        Korisnik userr = null;

        if (session.getAttribute("idU") == null && request.getParameter("time") != null) {
            String guest = "guest";
            int time = Integer.parseInt(request.getParameter("time"));
            session.setAttribute("time", time);
            while (true) {
                if (CrudUser.checkUsername(guest) != null) {
                    guest += 1;
                } else {
                    break;
                }
            }

            session.setAttribute("username", guest);
            session.setAttribute("time", time);

            userr = new Korisnik();
            userr.setIdRacunara(CrudUser.readComputerId(0));
            userr.setIdRola(CrudUser.readUserRole("Guest"));
            userr.setUsername(guest);
            userr.setPassword("1111");
            userr.setImeSlike(null);
            userr.setUkupanBrojMinuta(time);
            userr.setPreostaloVreme(time);

            CrudUser.insert(userr);

            out.print("<h2> Hello " + guest + ", your time is : " + userr.getPreostaloVreme() + "</h2>");

        } else {
            userr = CrudUser.read(Integer.parseInt(session.getAttribute("idU").toString()));
            out.print("<h2> Hello " + userr.getUsername() + ", your remaning time is : " + userr.getPreostaloVreme() + "</h2>");
        }

        out.println("<h4>Choose the computer where you want to sit : </h4>");
        if (session.getAttribute("idU") == null) {
            out.println("<form method=\"POST\" action=\"guest.jsp\">");
        } else {
            out.println("<form method=\"POST\" action=\"user.jsp\">");
        }
        ArrayList<Korisnik> users = (ArrayList<Korisnik>) CrudUser.readAll();
        ArrayList<Integer> slobodnaMesta = new ArrayList<>();
        for (Korisnik k : users) {
            if (!slobodnaMesta.contains(k.getIdRacunara().getIdRacunara())) {
                slobodnaMesta.add(k.getIdRacunara().getIdRacunara());
            }
        }
        for (int i = 1; i < 9; i++) {
            if (!slobodnaMesta.contains(i)) {
                out.println("<input type=\"radio\" id=\"comp\" name=\"computer\" value=\"" + i + "\">\n"
                        + "  <label for=\"comp\">" + i + "</label><br>");
            }
        }

        if (session.getAttribute("idU") != null) {
            session.setAttribute("username", userr.getUsername());
            out.println("<p>If you want to add some time to your account choose one of the values :  </p>");
            out.println(""
                    + "<div class=\"div input-group mb-3\">\n"
                    + " <label for=\"addTime\"></label>\n"
                    + "  <div class=\"input-group-append\">\n"
                    + "    <label class=\"input-group-text\" for=\"inputGroupSelect02\">Choose how much time you want to add</label>\n"
                    + "  </div>\n"
                    + "  <select class=\"custom-select\" name=\"addTime\" id=\"addTime\">\n"
                    + "    <option value=\"0\">dont add time</option>\n"
                    + "    <option value=\"60\">add 1h</option>\n"
                    + "    <option value=\"180\">add 3h</option>\n"
                    + "    <option value=\"300\">add 5h</option>\n"
                    + "  </select>\n"
                    + "</div>"
            );
        }
        out.println("<input type=\"submit\" class=\"btn btn-primary\" value=\"Save my computer\"/>");
        out.println("</form>");
        out.println("</body>");
        out.println("</html>");
    }

}

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

@WebServlet(name = "Admin", urlPatterns = {"/Admin"})
public class Admin extends HttpServlet {

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        PrintWriter out = response.getWriter();

        ArrayList<Korisnik> users = (ArrayList<Korisnik>) CrudUser.readAll();

        out.println("<!DOCTYPE html>");
        out.println("<html>");
        out.println("<head>");
        out.println("<title>Admin page</title>");
        out.println("<link rel=\"stylesheet\" href=\"https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css\"  crossorigin=\"anonymous\" />\n"
                + "        <script src=\"https://code.jquery.com/jquery-3.3.1.slim.min.js\"  crossorigin=\"anonymous\"></script>\n"
                + "        <script src=\"https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js\" crossorigin=\"anonymous\"></script>\n"
                + "        <script src=\"https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js\" crossorigin=\"anonymous\"></script>\n"
                + "        <link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css\"/> ");
        out.println("<style>\n"
                + "body{text-align: center;}\n"
                + ".div { margin-left: auto; margin-right: auto; width: 500px;}\n"
                + "table{ margin: auto; }\n"
                + "td, th {\n"
                + "    padding: 10px 20px;\n"
                + "    border: 1px solid black;\n"
                + "}"
                + ".logout { margin-left: 90%; }"
                + "</style>");
        out.println("</head>");
        out.println("<body>");
        out.println("<nav class=\"navbar navbar-expand-lg navbar-light bg-light\">\n" +
"            <a class=\"logout font-weight-bold navbar-brand\" href=\"logout.jsp\"><i class=\"fa fa-sign-out\" aria-hidden=\"true\"></i>Log out</a>\n" +
"            <button class=\"navbar-toggler\" type=\"button\" data-toggle=\"collapse\" data-target=\"#navbarNavDropdown\" aria-controls=\"navbarNavDropdown\" aria-expanded=\"false\" aria-label=\"Toggle navigation\">\n" +
"                <span class=\"navbar-toggler-icon\"></span>\n" +
"            </button>\n" +
"        </nav>");
        out.println("<button class=\"btn btn-outline-info\" type=\"button\"><a href=\"addUser.jsp\">Create account</a></button>");
        out.println("<p>List of all users :</p>");
        out.println("<table>");
        out.println("<tr>");
        out.println("<th>ID</th>");
        out.println("<th>Role ID</th>");
        out.println("<th>Username</th>");
        out.println("<th>Password</th>");
        out.println("<th>Number of total minutes</th>");
        out.println("<th>Number of minutes left</th>");
        out.println("<th>Computer ID</th>");
        out.println("<th>Update</th>");
        out.println("<th>Delete</th>");
        out.println("</tr>");
        for (Korisnik u : users) {
            out.println("<tr><td>" + u.getId() + "</td><td>" + u.getIdRola().getNazivRole() + "</td><td>"
                    + u.getUsername() + "</td><td>"
                    + u.getPassword() + "</td><td>"
                    + u.getUkupanBrojMinuta() + "</td><td>"
                    + u.getPreostaloVreme() + "</td><td>"
                    + u.getIdRacunara() + "</td><td>"
                    + "<form method=\"POST\" action=\"crud.jsp\">\n"
                    + "            <input type=\"hidden\" name=\"id\" value=\"" + u.getId() + "\"  />\n"
                    + "            <input type=\"hidden\" name=\"crud\" value=\"0\"  />\n"
                    + "            <input type=\"submit\" class=\"btn btn-success\" value=\"Update\"/>\n"
                    + "        </form>" + "</td><td>"
                    + "<form method=\"POST\" action=\"crud.jsp\">\n"
                    + "            <input type=\"hidden\" name=\"id\" value=\"" + u.getId() + "\"  />\n"
                    + "            <input type=\"hidden\" name=\"crud\" value=\"1\"  />\n"
                    + "            <input type=\"submit\" class=\"btn btn-danger\" value=\"Delete\"/>\n"
                    + "        </form>"
                    + "</td></tr>");
        }
        out.println("</table>");
        out.println("</body>");
        out.println("</html>");
    }

}

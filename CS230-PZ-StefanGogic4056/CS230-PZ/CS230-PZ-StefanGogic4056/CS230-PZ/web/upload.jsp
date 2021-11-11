<%@page import="entities.Korisnik"%>
<%@page import="crud.CrudUser"%>
<%@ page import="java.io.*,java.util.*, javax.servlet.*" %> 
<%@ page import="javax.servlet.http.*" %> 
<%@ page import="org.apache.commons.fileupload.*" %> 
<%@ page import="org.apache.commons.fileupload.disk.*" %> 
<%@ page import="org.apache.commons.fileupload.servlet.*" %> 
<%@ page import="org.apache.commons.io.output.*" %> 
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
    <head>
        <title>Picture upload page</title>
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
            if (session.getAttribute("newUsername") != null) {
                File file;

                int maxFileSize = 6000 * 1024;
                int maxMemSize = 6000 * 1024;
                String filePath = getServletContext().getRealPath("/");;
                filePath = filePath.replace("web\\", "web\\pictures\\");
                
                String contentType = request.getContentType();

                if ((contentType.indexOf("multipart/form-data") >= 0)) {

                    DiskFileItemFactory factory = new DiskFileItemFactory();
                    factory.setSizeThreshold(maxMemSize);
                    factory.setRepository(new File("C:\\Users\\User\\Desktop\\CS230-PZ\\CS230-PZ-StefanGogic4056\\CS230-PZ\\web\\pictures\\"));
                    ServletFileUpload upload = new ServletFileUpload(factory);
                    upload.setSizeMax(maxFileSize);
                    try {

                        List fileItems = upload.parseRequest(request);
                        Iterator i = fileItems.iterator();
                        while (i.hasNext()) {
                            FileItem fi = (FileItem) i.next();

                            if (!fi.isFormField()) {

                                String fileName = fi.getName();

                                Korisnik u = CrudUser.checkUsername(session.getAttribute("newUsername").toString());
                                while (true) {
                                    Korisnik user = CrudUser.readPictureName(fileName);
                                    if (user == null) {
                                        u.setImeSlike(fileName);
                                        CrudUser.update(u);
                                        break;
                                    } else {
                                        fileName = "1" + fileName;
                                    }
                                }

                                if (fileName.lastIndexOf("\\") >= 0) {
                                    file = new File(filePath + fileName.substring(fileName.lastIndexOf("\\")));
                                } else {
                                    file = new File(filePath + fileName.substring(fileName.lastIndexOf("\\") + 1));
                                }
                                fi.write(file);
                                out.println("<p class=\"p\">Your picture with name : " + fileName + " is successfully uploaded !</p><br/>");
                                session.removeAttribute("newUsername");
                            }
                        }
                    } catch (Exception ex) {
                        System.out.println(ex);
                    }
                } else {
        %>
        <p>Your picture was not deployed and saved.</p>
        <%
            }
        %>
    </body>
</html>
<%
    } else {
        response.sendRedirect("http://localhost:8080/CS230-PZ/index.html");
    }
%>
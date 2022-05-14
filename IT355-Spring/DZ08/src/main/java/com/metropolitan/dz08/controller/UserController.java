package com.metropolitan.dz08.controller;

import com.metropolitan.dz08.model.User;
import com.metropolitan.dz08.service.UserDao;
import com.metropolitan.dz08.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * This class is a controller class that handles all the requests from the user.
 */
@Controller
public class UserController {

    @Autowired
    private UserService userService;

    @GetMapping("/")
    public String viewAllUsers(Model model) {
        model.addAttribute("listUsers", userService.getAllUsers());
        return "index";
    }

    @GetMapping("/showNewUserForm")
    public String showNewUserForm(Model model){
        User user = new User();
        model.addAttribute("user", user);
        return "new_user";
    }

    @PostMapping(value = "/deleteUser/{id}")
    public String deleteUser(@PathVariable Integer id){
        List<User> usersList = userService.getAllUsers();
        for(User user : usersList){
            if(user.getId() == id){
                userService.delete(user);
            }
        }
        return "redirect:/";
    }

    @PostMapping("/saveUser")
    public String saveEmployee(@ModelAttribute("user") User user){
        userService.update(user);
        return "redirect:/";
    }

    @GetMapping("/showEditUserForm/{id}")
    public String showEditEmployeeForm(@PathVariable Integer id, Model model){
        List<User> usersList = userService.getAllUsers();

        for(User user : usersList){
            if(user.getId() == id){
                model.addAttribute("user", user);
            }
        }
        return "edit_user";
    }
}

package com.metropolitan.dz06.controller;

import com.metropolitan.dz06.model.Exam;
import com.metropolitan.dz06.model.User;
import com.metropolitan.dz06.service.ExamService;
import com.metropolitan.dz06.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;

@org.springframework.stereotype.Controller
public class Controller {

    @Autowired
    private ExamService examService;
    @Autowired
    private UserService userService;

    @GetMapping("/exams")
    public String viewHomePage(Model model) {
        model.addAttribute("listExams", examService.getAllExams());
        return "index";
    }

    @GetMapping("/saveChanges/{id}")
    public String saveChanges(@PathVariable Integer id, Model model) {
        Exam exam = examService.findById(id);
        model.addAttribute("exam", exam);
        return "edit";
    }

    @GetMapping("/saveUser")
    public String newUser(Model model){
        User user = new User();
        model.addAttribute("user", user);
        return "saveUser";
    }

    @PostMapping("/saveUser")
    public String saveUser(@ModelAttribute("user") User user){
        User test = userService.findByData(user);
        if(test == null){
            userService.saveUser(user);
            return "redirect:/exams";
        } else {
            return "redirect:/saveUser";
        }
    }

    @GetMapping("/")
    public String loginPage(Model model){
        User user = new User();
        model.addAttribute("user", user);
        return "login";
    }

    @PostMapping("/")
    public String login(@ModelAttribute("user") User user){
        User test = userService.findByData(user);
        if(test != null){
            if(user.getPassword().equals(test.getPassword())){
                return "redirect:/exams";
            } else {
                return "redirect:/";
            }
        } else {
            return "redirect:/saveUser";
        }
    }

    @PostMapping("/saveEdited")
    public String saveEdited(@ModelAttribute("exam") Exam exam){
        examService.addOrRemoveExamFromSchedule(exam);
        return "redirect:/exams";
    }
}

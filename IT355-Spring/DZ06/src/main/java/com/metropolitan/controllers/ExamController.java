package com.metropolitan.controllers;

import com.metropolitan.models.Exam;
import com.metropolitan.services.ExamService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

@Controller
public class ExamController {

    @Autowired
    private ExamService examService;

    @GetMapping("/")
    public String viewHomePage(Model model){
        model.addAttribute("listExams", examService.getAllExams());
        return "index";
    }

    @PostMapping("/saveChanges")
    public String saveChanges(@ModelAttribute("exam") Exam exam){
        examService.addOrRemoveExamFromSchedule(exam);
        return "redirect:/";
    }
}

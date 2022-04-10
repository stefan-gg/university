package com.metropolitan.services;

import com.metropolitan.models.Exam;
import com.metropolitan.repositories.ExamRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ExamServiceImpl implements ExamService{

    @Autowired
    private ExamRepository examRepository;

    @Override
    public List<Exam> getAllExams() {
        return examRepository.findAll();
    }

    @Override
    public void addOrRemoveExamFromSchedule(Exam exam) {
        this.examRepository.save(exam);
    }
}

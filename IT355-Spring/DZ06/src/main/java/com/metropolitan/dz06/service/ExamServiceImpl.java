package com.metropolitan.dz06.service;

import com.metropolitan.dz06.model.Exam;
import com.metropolitan.dz06.repository.ExamRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.NoSuchElementException;

@Service
public class ExamServiceImpl implements ExamService{

    @Autowired
    private ExamRepository examRepository;

    @Override
    public List<Exam> getAllExams() {
        return examRepository.findAll();
    }

    @Override
    public Exam findById(Integer id) {
        return this.examRepository.findById(id).orElseThrow(NoSuchElementException ::new);
    }

    @Override
    public void addOrRemoveExamFromSchedule(Exam exam) {
        this.examRepository.save(exam);
    }
}
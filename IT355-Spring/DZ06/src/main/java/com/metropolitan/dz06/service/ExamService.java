package com.metropolitan.dz06.service;

import com.metropolitan.dz06.model.Exam;

import java.util.List;

public interface ExamService {
    List<Exam> getAllExams();

    Exam findById(Integer id);

    void addOrRemoveExamFromSchedule(Exam exam);
}

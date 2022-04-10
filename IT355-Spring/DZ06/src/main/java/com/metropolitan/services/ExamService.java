package com.metropolitan.services;

import com.metropolitan.models.Exam;

import java.util.List;

public interface ExamService {
    List<Exam> getAllExams();

    void addOrRemoveExamFromSchedule(Exam exam);
}

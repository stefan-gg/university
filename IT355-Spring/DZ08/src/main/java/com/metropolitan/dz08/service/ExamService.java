package com.metropolitan.dz08.service;

import com.metropolitan.dz08.model.Exam;

import java.util.List;

// A service interface.
public interface ExamService {
    List<Exam> findAll();

    Exam save(Exam exam);

    Exam update(Exam exam);

    void delete(Exam exam);
}

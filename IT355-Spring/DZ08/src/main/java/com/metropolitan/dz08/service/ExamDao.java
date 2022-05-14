package com.metropolitan.dz08.service;

import com.metropolitan.dz08.model.Exam;

import java.util.List;

// A DAO interface.
public interface ExamDao {
    List<Exam> findAll();

    Exam save(Exam exam);

    Exam update(Exam exam);

    void delete(Exam exam);
}

package com.metropolitan.dz08.service.impl;

import com.metropolitan.dz08.model.Exam;
import com.metropolitan.dz08.service.ExamDao;
import org.hibernate.SessionFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import javax.persistence.TypedQuery;
import java.util.List;

@Repository
public class ExamDaoImpl implements ExamDao {

    @Autowired
    private SessionFactory sessionFactory;

    @Override
    public List<Exam> findAll() {
        @SuppressWarnings("unchecked")
        TypedQuery<Exam> query = sessionFactory.getCurrentSession().createQuery("from Exam");
        return query.getResultList();
    }

    @Override
    public Exam save(Exam exam) {
        sessionFactory.getCurrentSession().saveOrUpdate(exam);
        return exam;
    }

    @Override
    public Exam update(Exam exam) {
        sessionFactory.getCurrentSession().saveOrUpdate(exam);
        return exam;
    }

    @Override
    public void delete(Exam exam) {
        sessionFactory.getCurrentSession().delete(exam);
    }
}

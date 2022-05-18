package com.metropolitan.dz08.service.impl;

import com.metropolitan.dz08.model.User;
import com.metropolitan.dz08.service.UserDao;
import org.hibernate.SessionFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import javax.persistence.TypedQuery;
import java.util.List;

@Repository
public class UserDaoImpl implements UserDao {

    @Autowired
    private SessionFactory sessionFactory;

    @Override
    public User add(User user) {
        sessionFactory.getCurrentSession().saveOrUpdate(user);
        return user;
    }

    @Override
    public List<User> getAllUsers() {
       @SuppressWarnings("unchecked")
       TypedQuery<User> query = sessionFactory.getCurrentSession().createQuery("from User");
       return query.getResultList();
    }

    @Override
    public User getUserByUsername(String username) {
        @SuppressWarnings("unchecked")
        TypedQuery<User> query = sessionFactory.getCurrentSession().createQuery("from User u where u.username=:username")
                .setParameter("username", username);
        return query.getSingleResult();
    }

    @Override
    public void update(User user) {
        sessionFactory.getCurrentSession().saveOrUpdate(user);
    }

    @Override
    public void delete(User user) {
        sessionFactory.getCurrentSession().delete(user);
    }
}

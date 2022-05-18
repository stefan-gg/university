package com.metropolitan.dz08.service;

import com.metropolitan.dz08.model.User;

import java.util.List;

// A Java interface.
public interface UserDao {

    User add(User user);
    List<User> getAllUsers();
    User getUserByUsername(String username);
    void update(User user);
    void delete(User user);
}

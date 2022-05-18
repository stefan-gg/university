package com.metropolitan.dz08.service;

import com.metropolitan.dz08.model.User;

import java.util.List;

// A service interface.
public interface UserService {
    User add(User user);
    List<User> getAllUsers();
    User getUserByUsername(String username);
    void update(User user);
    void delete(User user);
}

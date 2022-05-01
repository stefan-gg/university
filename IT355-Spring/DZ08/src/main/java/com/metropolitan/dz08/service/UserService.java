package com.metropolitan.dz08.service;

import com.metropolitan.dz08.model.User;

import java.util.List;

public interface UserService {
    void add(User user);
    List<User> getAllUsers();
    void update(User user);
    void delete(User user);
}

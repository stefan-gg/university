package com.metropolitan.dz06.service;

import com.metropolitan.dz06.model.User;

import java.util.List;

public interface UserService {
    List<User> getAllUsers();

    User findByData(User user);

    void saveUser(User user);
}

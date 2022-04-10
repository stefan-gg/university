package com.metropolitan.dz06.service;

import com.metropolitan.dz06.model.User;
import com.metropolitan.dz06.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class UserServiceImpl implements UserService{

    @Autowired
    private UserRepository userRepository;

    @Override
    public List<User> getAllUsers() {
        return userRepository.findAll();
    }

    @Override
    public User findByData(User user) {
        return this.userRepository.findByUsername(user.getUsername()).orElse(null);
    }

    @Override
    public void saveUser(User user) {
        this.userRepository.save(user);
    }
}

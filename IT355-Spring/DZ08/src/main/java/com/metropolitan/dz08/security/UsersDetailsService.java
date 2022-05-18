package com.metropolitan.dz08.security;

import com.metropolitan.dz08.model.User;
import com.metropolitan.dz08.service.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class UsersDetailsService implements org.springframework.security.core.userdetails.UserDetailsService{
    private final UserService userService;

    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        User user = userService.getUserByUsername(username);

        return new com.metropolitan.dz08.security.UserDetails(user);
    }
}

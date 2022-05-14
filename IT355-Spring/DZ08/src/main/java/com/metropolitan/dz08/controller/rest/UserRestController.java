package com.metropolitan.dz08.controller.rest;

import com.metropolitan.dz08.model.User;
import com.metropolitan.dz08.service.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/users")
@RequiredArgsConstructor
public class UserRestController {
    private final UserService userService;

    @GetMapping
    public ResponseEntity<List<User>> getAllUsers(){
        return new ResponseEntity<List<User>>(userService.getAllUsers(), HttpStatus.OK);
    }

    @PostMapping
    public ResponseEntity<User> save(@RequestBody User user){
        return ResponseEntity.ok(userService.add(user));
    }

    @PutMapping
    public ResponseEntity<User> update(@RequestBody User user){
        return ResponseEntity.ok(userService.add(user));
    }

    @DeleteMapping("/{userId}")
    public void deleteById(@PathVariable Integer userId){
        List<User> usersList = userService.getAllUsers();
        for(User user : usersList){
            if(user.getId() == userId){
                userService.delete(user);
            }
        }
    }
}

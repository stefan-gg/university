package com.metropolitan.dz08;

import com.metropolitan.dz08.controller.UserController;
import com.metropolitan.dz08.model.User;
import com.metropolitan.dz08.service.UserService;
import org.aspectj.lang.annotation.Before;
import org.junit.jupiter.api.Test;
import org.mockito.Mockito;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.ui.Model;
import org.springframework.ui.ModelMap;

import static org.junit.jupiter.api.Assertions.assertEquals;


@SpringBootTest
class Dz08ApplicationTests {
    private UserService userService;
    private UserController userController;

    @Before("")
    public void init() {
        userService = Mockito.mock(UserService.class);
        userController = new UserController();
    }

    @Test
    public void showEditEmployeeForm() {
        User user = new User();
        user.setUsername("Stefan");
        user.setPassword("$2a$04$W1DIGFBNXv85146useZtQ.X0e7.yHyJpN3iVhyVbEDNc7x9teBmq2");
        user.setRole("ROLE_USER");

        Mockito.when(userService.getUserByUsername("Stefan")).thenReturn(user);
        ModelMap model = new ModelMap();

        String viewName = userController.showEditEmployeeForm(1, (Model) model);
        assertEquals(viewName, "edit_user");
        assertEquals(model.get("user"), user);
    }
}

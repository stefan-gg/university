package com.metropolitan.dz08;

import com.metropolitan.dz08.appConfig.AppConfig;
import com.metropolitan.dz08.service.UserService;
import com.metropolitan.dz08.service.impl.UserServiceImpl;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.orm.jpa.HibernateJpaAutoConfiguration;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

import java.sql.SQLException;

@SpringBootApplication(exclude = HibernateJpaAutoConfiguration.class)
public class Dz08Application {

    public static void main(String[] args) throws SQLException {

        SpringApplication.run(Dz08Application.class, args);

    }
}

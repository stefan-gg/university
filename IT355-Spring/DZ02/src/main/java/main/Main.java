package main;

import configurations.AppConfiguration;
import interfaces.Animal;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class Main {
    public static void main(String[] args) {
        // Java konfiguracija
        ApplicationContext context = new AnnotationConfigApplicationContext(AppConfiguration.class);

        // XML konfiguracija
        //ApplicationContext context = new ClassPathXmlApplicationContext("classpath:/conf.xml");

        Animal dog = (Animal) context.getBean("dog");
        System.out.println("DOG->" + dog.feedTheAnimal() + " " + dog.response());

        Animal chicken = (Animal) context.getBean("chicken");
        System.out.println("CHICKEN->" + chicken.feedTheAnimal() + " " + chicken.response());

        Animal sheep = (Animal) context.getBean("sheep");
        System.out.println("SHEEP->" + sheep.feedTheAnimal() + " " + sheep.response());
    }
}

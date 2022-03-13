package main;

import aspects.InterceptorLog;
import configurations.AppConfiguration;
import interfaces.Animal;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class Main {

    public static void main(String[] args) {


        // Java konfiguracija
        ApplicationContext context = new AnnotationConfigApplicationContext(AppConfiguration.class);

        // XML konfiguracija
        //ApplicationContext context = new ClassPathXmlApplicationContext("classpath:/conf.xml");

        Animal dog = (Animal) context.getBean("dog", Animal.class);
        try {
            System.out.println("DOG->" + dog.feedTheAnimal() + " ");
            dog.response();
        } catch (Throwable e) {
            e.printStackTrace();
        }

        Animal chicken = (Animal) context.getBean("chicken", Animal.class);
        try {
            System.out.println("CHICKEN->" + chicken.feedTheAnimal() + " ");
            chicken.response();
        } catch (Throwable e) {
            e.printStackTrace();
        }

        Animal sheep = (Animal) context.getBean("sheep", Animal.class);
        try {
            System.out.println("SHEEP->" + sheep.feedTheAnimal() + " ");
            sheep.response();
        } catch (Throwable e) {
            e.printStackTrace();
        }

        InterceptorLog log = context.getBean("log", InterceptorLog.class);
    }
}

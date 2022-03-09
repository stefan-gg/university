package configurations;

import animals.Chicken;
import animals.Dog;
import animals.Sheep;
import interfaces.Animal;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class AppConfiguration {

    @Bean(name="dog")
    public Animal getDog(){
        return new Dog();
    }

    @Bean(name="sheep")
    public Animal getSheep(){
        return new Sheep();
    }

    @Bean(name="chicken")
    public Animal getChicken(){
        return new Chicken();
    }
}

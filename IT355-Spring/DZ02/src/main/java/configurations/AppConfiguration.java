package configurations;

import animals.Chicken;
import animals.Dog;
import animals.Sheep;
import aspects.InterceptorLog;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.EnableAspectJAutoProxy;

@Configuration
@ComponentScan
@EnableAspectJAutoProxy
public class AppConfiguration {

    @Bean(name="dog")
    public Dog getDog(){
        return new Dog();
    }

    @Bean(name="sheep")
    public Sheep getSheep(){
        return new Sheep();
    }

    @Bean(name="chicken")
    public Chicken getChicken(){
        return new Chicken();
    }

    @Bean(name="log")
    public InterceptorLog getAspect(){
        return new InterceptorLog();
    }
}

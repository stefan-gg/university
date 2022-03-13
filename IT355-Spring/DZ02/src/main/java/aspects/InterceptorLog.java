package aspects;

import org.aspectj.lang.JoinPoint;
import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.*;

import java.util.Arrays;

@Aspect
public class InterceptorLog {

    @Before("execution(* animals.Chicken.feedTheAnimal(..))")
    public void logBefore(JoinPoint joinPoint){
        System.out.println("*****************************************************");
        System.out.println("Before");
        System.out.println("Chicked -> feedTheAnimal() method is being called!");
        System.out.println(joinPoint.getSignature().getName());
        System.out.println("*****************************************************");
    }

    @After("execution(* animals.Dog.feedTheAnimal(..))")
    public void logAfter(JoinPoint joinPoint){
        System.out.println("*****************************************************");
        System.out.println("After");
        System.out.println("Dog -> feedTheAnimal() method is being called!");
        System.out.println(joinPoint.getSignature().getName());
        System.out.println("*****************************************************");
    }

    @AfterReturning("execution(* animals.Sheep.feedTheAnimal())")
    public void throwAfter(JoinPoint joinPoint){
        System.out.println("*****************************************************");
        System.out.println("AfterRerurning");
        System.out.println("Dog -> feedTheAnimal() method is being called!");
        System.out.println(joinPoint.getSignature().getName());
        System.out.println("*****************************************************");
    }

    @AfterThrowing(pointcut = "execution(* animals.Dog.response())", throwing = "exception")
    public void throwAfter(JoinPoint joinPoint, Throwable exception){
        System.out.println("*****************************************************");
        System.out.println("AfterThrowing");
        System.out.println("Dog -> feedTheAnimal() method is being called!");
        System.out.println(joinPoint.getSignature().getName());
        System.out.println("Exception: " + exception);
        System.out.println("*****************************************************");
    }

    @Around("execution(* animals.Sheep.response(..))")
    public void logAround(ProceedingJoinPoint joinPoint) throws Throwable{
        System.out.println("*****************************************************");
        System.out.println("Around");
        System.out.println("Sheep -> response() method is being called!");
        System.out.println(joinPoint.getSignature().getName());
        System.out.println("Args: " + Arrays.toString(joinPoint.getArgs()));
        System.out.println("*****************************************************");
    }
}

package animals;

import interfaces.Animal;

public class Dog implements Animal {
    @Override
    public String feedTheAnimal() {
        return "Dog is fed";
    }

    @Override
    public void response() throws Throwable {
        System.out.println("*Dog sounds*");
        throw new Exception("Dog exception");
    }
}

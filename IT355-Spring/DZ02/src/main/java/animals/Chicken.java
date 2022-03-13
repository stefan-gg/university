package animals;

import interfaces.Animal;

public class Chicken implements Animal {

    @Override
    public String feedTheAnimal() {
        return "Chicken is fed";
    }

    @Override
    public void response() throws Throwable {
        System.out.println("*Chicken sounds*");
        throw new Exception("Chicken exception");
    }
}

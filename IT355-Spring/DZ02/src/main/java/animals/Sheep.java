package animals;

import interfaces.Animal;

public class Sheep implements Animal {

    @Override
    public String feedTheAnimal() {
        return "Sheep is fed";
    }

    @Override
    public void response() throws Throwable {
        System.out.println("*Sheep sounds*");
        throw new Exception("Sheep exception");
    }
}

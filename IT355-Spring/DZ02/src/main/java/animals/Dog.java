package animals;

import interfaces.Animal;

public class Dog implements Animal {
    @Override
    public String feedTheAnimal() {
        return "Dog is fed";
    }

    @Override
    public String response() {
        return "*Dog sounds*";
    }
}

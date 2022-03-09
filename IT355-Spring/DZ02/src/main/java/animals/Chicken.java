package animals;

import interfaces.Animal;

public class Chicken implements Animal {
    @Override
    public String feedTheAnimal() {
        return "Chicken is fed";
    }

    @Override
    public String response() {
        return "*Chicken sounds*";
    }
}

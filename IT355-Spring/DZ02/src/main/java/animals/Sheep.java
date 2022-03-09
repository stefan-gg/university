package animals;

import interfaces.Animal;

public class Sheep implements Animal {
    @Override
    public String feedTheAnimal() {
        return "Sheep is fed";
    }

    @Override
    public String response() {
        return "*Sheep sounds*";
    }
}

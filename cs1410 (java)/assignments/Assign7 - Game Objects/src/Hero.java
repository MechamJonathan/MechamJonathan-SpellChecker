import java.util.ArrayList;
import java.util.List;

class Hero extends Entity {
    private ArrayList<Treasure> treasures;
    private String name;

    Hero(String name, int x, int y) {
        this.position = new Position(x, y);
        this.name = name;
        this.treasures = new ArrayList<>();
    }


    String getName() {
        return this.name;
    }


    void attack(Entity entity){
        if (entity instanceof Crate) {
            treasures.add(((Crate)entity).getTreasure());
        }
        if (entity instanceof Dragon && ((Dragon)entity).getColor() == "Golden") {
            treasures.add(Treasure.Coins);
        }
    }

    ArrayList<Treasure> getTreasures() {
        return treasures;
    }

    @Override
    public String toString() {
        return  ("'" + this.name + " standing at " + getPosition() + "'");
    }

}

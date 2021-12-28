import java.util.ArrayList;

public class Arena {
    int sizeX; // columns
    int sizeY; //rows
    Hero hero;


    ArrayList<Entity[]> grid;

    public Arena(int sizeX, int sizeY) {
        this.sizeX = sizeX;
        this.sizeY = sizeY;
        grid = new ArrayList<>();
        for (int i = 0; i < sizeX; i++) {
            grid.add(new Entity[sizeY]);
        }
    }

    boolean add(Entity ent) {
        int x = ent.getPosition().x;
        int y = ent.getPosition().y;

        if (grid.get(x)[y] != null) {
            return false;
        }
        if (ent instanceof Hero) {
            if (hero != null) {
                System.out.println("Could not add " + ent + " to the game arena because there is already a hero in the arena.");
                return false;
            }
            hero = (Hero)ent;
        }
        grid.get(x)[y] = ent;
        System.out.println("Successfully added " + ent + " to game arena.");
        return true;
    }

    public void moveHero(int x, int y) {
        if (hero == null){
            return;
        }
        if (grid.get(x)[y] != null) {
            hero.attack(grid.get(x)[y]);
            if (grid.get(x)[y] instanceof Dragon) {
                System.out.print(hero.getName() + " bravely defeated the " + ((Dragon)grid.get(x)[y]).getColor() + " Dragon");
                if (((Dragon)grid.get(x)[y]).getColor() == "Golden") {
                    System.out.print(" and came away with gold coins as a prize.");
                }
                System.out.println("");
            }
            if (grid.get(x)[y] instanceof Crate) {
                System.out.println(hero.getName() + " crushed the crate into bits and found " + ((Crate)grid.get(x)[y]).getTreasure());
            }
        }

        grid.get(hero.position.x)[hero.position.y] = null;

        hero.setPosition(x, y);
        System.out.println(hero.getName() + " moved to " + hero.position);

        grid.get(x)[y] = hero;

    }

    public Hero getHero() {
        return hero;
    }


    public ArrayList<Entity[]> getGrid() {
        return grid;
    }

    public int getEntityCount() {
        int entCount = 0;
        for (int i = 0; i < sizeX; i++) {
            for (int k = 0; k < sizeY; k++) {
                if (grid.get(i)[k] != null)
                entCount++;
            }
        }
        return entCount;
    }

    public int getDragonCount() {
        int entCount = 0;
        for (int i = 0; i < sizeX; i++) {
            for (int k = 0; k < sizeY; k++) {
                if (grid.get(i)[k] != null && grid.get(i)[k] instanceof Dragon)
                    entCount++;
            }
        }
        return entCount;
    }


    public int getTreasureCount(Treasure treasure) {
        int entCount = 0;
        for (int i = 0; i < sizeX; i++) {
            for (int k = 0; k < sizeY; k++) {
                if (grid.get(i)[k] != null && (grid.get(i)[k] instanceof Crate) && ((Crate)grid.get(i)[k]).getTreasure() == treasure)
                    entCount++;
            }
        }
        return entCount;
    }



    public void reportHero() {
        System.out.println("--- Hero report for " + hero.getName() + " ---");
        System.out.println("Position: (" + hero.position.x + ", " + hero.position.y + ")");
        System.out.println("Treasures:");
        for (int i = 0; i < hero.getTreasures().size(); i++) {
            System.out.println(hero.getTreasures().get(i));
        }
        System.out.println("");
    }



}

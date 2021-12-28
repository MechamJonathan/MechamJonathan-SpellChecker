class Crate extends Entity {
    private Treasure item;

    Crate(Treasure item, int posX, int posY) {
        this.position = new Position(posX, posY);
        this.item = item;

    }

    Treasure getTreasure() {
        return item;
    }


    Position getPosition() {
        return this.position;
    }


    @Override
    public String toString() {
        return  ("'Crate with " + this.item + " at " + getPosition() + "'");
    }


}

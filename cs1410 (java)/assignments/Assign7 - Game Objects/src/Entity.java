
public class Entity {
    Position position;

    public Entity() {
        int x = 0;
        int y = 0;
        position = new Position (x , y);
    }

    Entity(int posX, int posY) {
        position = new Position(posX, posY);
    }

    Position getPosition() {
        return this.position;
    }

    void setPosition(int x, int y) {
        this.position = new Position(x, y);
    }




}

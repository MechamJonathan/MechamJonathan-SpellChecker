class Dragon extends Entity{
    public String color;

    Dragon(String color, int x, int y) {
        this.position = new Position( x, y);
        this.color = color;

    }

    public String getColor() {
        return this.color;
    }



    @Override
    public String toString() {
        return  ("'The " + this.color + "Dragon breathing fire at " + getPosition() + "'");
    }


}

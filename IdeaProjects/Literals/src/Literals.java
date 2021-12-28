public class Literals {
    public static void main(String [] args) {
        int value1 = 11;
        int value2 = 0b11;
        int value3 = 011;
        int value4 = 0x11;


        System.out.println(value1);
        System.out.println(value2);
        System.out.println(value3);
        System.out.println(value4);

        int r = 5 / 3;
        double r2 = 5 / 3;
        int r3 = (int)(5 / 3.1);


        System.out.println(r);
        System.out.println(r2);
        System.out.println(r3);

        int i = 0;

        i += 1;
        i++;
        i--;

        ++i;
        --i;

    }
}

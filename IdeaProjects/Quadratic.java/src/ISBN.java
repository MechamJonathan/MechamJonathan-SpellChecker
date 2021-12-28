import java.util.*;

public class ISBN {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.print("Enter the first 9 digits of an ISBN: ");

        int number = input.nextInt();

        int d1 = number / 100000000;
        number -= d1 * 100000000;

        int d2 = number / 10000000;
        number -= d2 * 10000000;

        int d3 = number / 1000000;
        number -= d3* 1000000;

        int d4 = number / 100000;
        number -= d4 * 100000;

        int d5 = number / 10000;
        number -= d5 * 10000;

        int d6 = number / 1000;
        number -= d6 * 1000;

        int d7 = number / 100;
        number -= d7 * 100;

        int d8 = number / 10;
        number -= d8 * 10;

        int d9 = number;
        number -= d9;

        int checksum = (d1 + d2 * 2 + d3 * 3 + d4 * 4 + d5 * 5 + d6 * 6 + d7 * 7 + d8 * 8 + d9 * 9) % 11;





        System.out.print("The ISBN-10 number is ");
        System.out.print(d1);
        System.out.print(d2);
        System.out.print(d3);
        System.out.print(d4);
        System.out.print(d5);
        System.out.print(d6);
        System.out.print(d7);
        System.out.print(d8);
        System.out.print(d9);

        if (checksum != 10) {
            System.out.print(checksum);}
        else {System.out.print("X"); }




        int[] first = { 1, 2, 3, 4, 5 };
        int[] second = { 1, 2, 3, 4, 5 };

        first = second;



        int[] myInts = new int[5];
        myInts[5] = 42;
    }
}

import java.util.*;

public class Pyramid1 {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.print("Enter number of lines:");

        int pyrSize = input.nextInt();
        String str = "" + pyrSize;
        int pyrSizeLen = str.length();
        pyrSizeLen += 1;

        // loop for each line
        for (int i = 1; i <= pyrSize; i++) {
            int spaces = pyrSize - i;

            for (int j = 0; j < spaces; j++) {
                for (int k = 0; k < pyrSizeLen; k ++) {
                    System.out.print(" ");
                }
            }

            String formatting = "%" + pyrSizeLen + "d";

            for (int l = i; l > 0; l--) {
                System.out.printf(formatting, l);
            }

            for (int l = 2; l <= i; l++) {
                System.out.printf(formatting, l);
            }
            System.out.println(" ");



        }


    }
}
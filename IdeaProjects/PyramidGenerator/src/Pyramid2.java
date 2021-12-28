




import java.util.*;

public class Pyramid2 {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.print("Enter number of lines:");

        int pyrSize = input.nextInt();
        String str = "" + Math.pow(2, pyrSize);
        int pyrSizeLen = str.length() - 1;

        // loop for each line
        for (int i = 0; i <= pyrSize; i++) {
            int spaces = pyrSize - i;

            for (int j = 0; j < spaces; j++) {
                for (int k = 0; k < pyrSizeLen; k++) {
                    System.out.print(" ");
                }
            }

            String formatting = "%" + pyrSizeLen + "d";

            for (int l = 0; l <= i; l++) {
                int poweredNum = (int)Math.pow(2,l);
                System.out.printf(formatting, poweredNum);
            }

            for (int l = i; l > 0; l--) {
                System.out.printf(formatting, l);
            }

            System.out.println(" ");
        }

    }
}

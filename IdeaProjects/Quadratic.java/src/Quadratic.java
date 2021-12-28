import java.util.*;

public class Quadratic {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

// take input from user
        System.out.print("Enter a b c:");
        double a = input.nextDouble();
        double b = input.nextDouble();
        double c = input.nextDouble();

// compute roots
        double root1 = ((-b + Math.sqrt(b*b - 4 * a * c)) / (2 * a));
        double root2 = ((-b - Math.sqrt(b*b - 4 * a * c)) / (2 * a));

// no roots
    if ((b*b - 4 * a * c) < 0 ){
        System.out.println("There are no roots for the quadratic equation with these coefficients.");
    }
// two roots
    else if (root1 != root2) {
        System.out.println("r1 = " + root1);
        System.out.println("r2 = " + root2); }

// one root
    else  {
        System.out.println("There is one root for a quadratic equation with these coefficients" +
                " r1 = " + root1); }


    }
}

public class Conditionals {
    public static void main(String[] args) {

        int finalGrade = 94;

        if (finalGrade >= 93) {
            System.out.println("A");
        }
        else if (finalGrade >= 90) {
            System.out.println("A-");
        }
        else if (finalGrade >= 87) {
            System.out.println("B+");
        }
        else {
            System.out.println("F");
        }

        String day = "Monday";
        switch (day) {
            case "Monday":
                System.out.println("first day of the week");
                break;
            case "Tuesday":
                System.out.println("seccond day of the week");
                break;
            case "Wednesday":
                System.out.println("third day of the week");
                break;
            case "Thursday":
                System.out.println("fourth day of the week");
                break;
            case "Friday":
                System.out.println("fifth day of the week");
                break;
            case "Saturday":
                System.out.println("sixth day of the week");
                break;

        }
    }
}

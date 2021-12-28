public class Calender {
    public static void main(String[] args) {

        printMonth();

    }

    public static void month (int year, int month){

    }
    public static boolean isLeapYear(int year) {
        return (year % 400 == 0) || (year % 4 == 0 && year % 100 != 0);
    }

    public static int getDaysInMonth(int year, int month) {
        switch (month) {
            case 1:
            case 3:
            case 5:
            case 7:
            case 8:
            case 10:
            case 12:
                return 31;
            case 4:
            case 6:
            case 9:
            case 11:
                return 30;
            case 2:
                if (isLeapYear(year)) {
                    return 29;
                }
                    else {
                        return 28;
                }
            default:
                return 0;
        }
    }
    public static int getTotalNumberOfDays(int year, int month) {
        int totalDays = 0;

        for (int countYear = 1800; countYear < year; countYear++) {
            if (isLeapYear(countYear)) {
                totalDays += 366;
            } else
                totalDays += 365;
        }

    }


    public static int getStartDay(int year, int month){
        return 1;
    }

    public static void printMonthBody(int year, int month) {

    }

    public static String getMonthName(int month){
        switch (month) {
            case 1: return "jan";
            case 2: return "feb";
            case 3: return "mar";
            case 4: return "apr";
            case 5: return "may";
            case 6: return "jun";
            case 7: return "jul";
            case 8: return "aug";
            case 9: return "sep";
            case 10: return "oct";
            case 11: return "nov";
            case 12: return "dec";
        }
    }

    public static void printMonth(){

    }
}

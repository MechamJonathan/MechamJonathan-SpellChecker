
public class JulianDate {
    private int year;
    private int month;
    private int day;


    public JulianDate() {
        this.year = 1;
        this.month = 1;
        this.day = 1;

        //adds days to jan 1, 1970 (gregorian date)
        addDays(719164);
        //sets date to today's date
        long currentTime = System.currentTimeMillis() + java.util.TimeZone.getDefault().getRawOffset();
        int days = (int) (currentTime / (1000*60*60*24));
        addDays(days);
    }

    public JulianDate(int year, int month, int day) {
        this.year = year;
        this.month = month;
        this.day = day;

    }

    void printShortDate() {
        System.out.print(this.month + "/" + this.day + "/" + this.year);

    }


    void printLongDate() {
        System.out.print(getMonthName(this.month) + " " + this.day + ", " + this.year);
    }

    // getters
    String getCurrentMonthName() {
        return getMonthName(this.month);
    }

    int getCurrentMonth() {
        return this.month;
    }

    int getCurrentYear() {
        return this.year;
    }

    int getCurrentDayOfMonth() {
        return this.day;
    }






    // methods
    // subtract days
    public void subtractDays(int days) {
        for (int day = 0; day < days; day++) {
            this.day--;
            if (this.day < 1) {
                this.month--;
                this.day = getNumberOfDaysInMonth();
                if (this.month < 1) {
                    this.month = 12;
                    this.year --;
                }
            }
        }
    }

    // adds days
    public void addDays(int days) {
        for (int day = 0; day < days; day++) {
            this.day++;
            if (this.day > getNumberOfDaysInMonth()){
                this.day = 1;
                this.month++;
                if (this.month > 12) {
                    this.month = 1;
                    this.year++;
                }
            }
        }
    }

    // Checks if leap year
    public boolean isLeapYear() {
        return (year % 4 == 0);
    }

    // gets days in month
    private int getNumberOfDaysInMonth() {
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
                if (isLeapYear()) {
                    return 29;
                } else {
                    return 28;
                }
            default:
                return 31;
        }
    }

    // gets days in year
    private int getNumberOfDaysInYear(int year) {
        int daysInYear = 0;

        if (isLeapYear()) {
            daysInYear += 366;
        }
        else {
            daysInYear += 365;
        }
        return  daysInYear;
    }

    // gets month name
    private String getMonthName(int month) {
        switch (month) {
            case 1:
                return "January";
            case 2:
                return "February";
            case 3:
                return "March";
            case 4:
                return "April";
            case 5:
                return "May";
            case 6:
                return "June";
            case 7:
                return "July";
            case 8:
                return "August";
            case 9:
                return "September";
            case 10:
                return "October";
            case 11:
                return "November";
            case 12:
                return "December";
            default:
                return "whoops";
        }
    }
}


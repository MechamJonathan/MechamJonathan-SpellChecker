class JulianDate extends Date {

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

    @Override
    public boolean isLeapYear() {
        return (year % 4 == 0);
    }


}
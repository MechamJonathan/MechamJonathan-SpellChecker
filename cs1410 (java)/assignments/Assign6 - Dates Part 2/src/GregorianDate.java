class GregorianDate extends Date {

    public GregorianDate() {
        this.year = 1970;
        this.month = 1;
        this.day = 1;

        long currentTime = System.currentTimeMillis() + java.util.TimeZone.getDefault().getRawOffset();
        int days = (int) (currentTime / (1000*60*60*24));
        addDays(days);
    }

    public GregorianDate(int year, int month, int day) {
        this.year = year;
        this.month = month;
        this.day = day;
    }



    @Override
    public boolean isLeapYear() {
        return (year % 400 == 0) || (year % 4 == 0 && year % 100 != 0);

    }

}
import java.util.*;

/**
 * Assignment 4 for CS 1410
 * This program evaluates the linear and binary searching, along
 * with comparing performance difference between the selection sort
 * and the built-in java.util.Arrays.sort.
 *
 * @author James Dean Mathias
 */
public class EvaluationDriver {
    static final int MAX_VALUE = 1_000_000;
    static final int MAX_ARRAY_SIZE = 100_000;
    static final int ARRAY_INCREMENT = 20_000;
    static final int NUMBER_SEARCHES = 50_000;

    public static void main(String[] args) {

        demoLinearSearchUnsorted();
        demoLinearSearchSorted();
        demoBinarySearchSelectionSort();
        demoBinarySearchFastSort();


    }

    // Write a method that creates and returns an array of integers
    // Generates number list
    // Checks if howmany is valid integer
    public static int[] generateNumbers(int howMany, int maxValue) {
        if (howMany == (int)howMany && howMany > 0){
            int[] numList = new int[howMany];
            for (int i = 0; i < howMany; i++) {
                numList[i] = (int) (Math.random() * maxValue);
            }
            return numList;
        }
        else {
            return null;
        }
    }

    //Linear search
    //look for specific value return true or false
    public static boolean linearSearch(int[] data, int search) {
        boolean check = false;
        for (int i = 0; i < data.length; i++) {
            if (search == data[i])
                 check = true;
        }
        return check;
    }

    //binary search
    public static boolean binarySearch(int[] data, int search) {
        Arrays.sort(data);

        int low = 0;
        int high = data.length - 1;

        while (high >= low) {
            int mid = (low + high) / 2;
            if (search < data[mid])
                high = mid - 1;
            else if (search == data[mid])
                return true;

            else
                low = mid + 1;
        }
        return false;
    }

    // selection sort
    public static void selectionSort(int[] data) {
        for (int i = 0; i < data.length - 1; i++) {
            double currentMin = data[i];
            int currentMinIndex = i;

            //select
            for (int j = i + 1; j < data.length; j++) {
                if (currentMin > data[j]) {
                        currentMin = data[j];
                        currentMinIndex = j;
                }
            }

            //swap
            if (currentMinIndex != i) {
                data[currentMinIndex] = data[i];
                data[i] = (int) currentMin;
            }
        }
    }

    public static void printData(int items, int found, int time) {

        System.out.printf("Number of items %7s %d%n", ":",  items);
        System.out.println("Times value was found : " +  found);
        System.out.printf("Total search time %5s %d ms%n ", ":", time);
        System.out.println("");
    }






    /**
     * Demonstrates linear searching over an unsorted array
     *
     * @author
     */
    public static void demoLinearSearchUnsorted() {
        System.out.println("--- Linear Search Timing (unsorted) ---");
       int inc = ARRAY_INCREMENT;
       // increments it
       while (inc < MAX_ARRAY_SIZE) {
           int[] list = generateNumbers(inc, MAX_VALUE);

           //takes starting time
           double start = System.currentTimeMillis();
           //performs the search
           int trueCount = 0;
           for (int i = 0; i < NUMBER_SEARCHES; i++){
               double searchValue = (double) Math.random() * MAX_VALUE;
               if (linearSearch(list, (int) searchValue)) {
                   trueCount += 1;
               }
           }
           //end time/ calculates total time
           double end = System.currentTimeMillis();
           double totalTime = end - start;

           //prints output
           printData(inc,trueCount, (int) totalTime);

           inc += ARRAY_INCREMENT;
       }
    }

    /**
     * Demonstrates linear searching over a sorted array
     *
     * @author
     */
    public static void demoLinearSearchSorted() {
        System.out.println("--- Linear Search Timing (Selection Sort) ---");
        int inc = ARRAY_INCREMENT;
        while (inc < MAX_ARRAY_SIZE) {
            int[] numList = generateNumbers(inc, MAX_VALUE);

            double start = System.currentTimeMillis();
            selectionSort(numList);
            // linear search
            int trueCount = 0;
            for (int i = 0; i < NUMBER_SEARCHES; i++){
                double searchValue = (double) Math.random() * MAX_VALUE;
                if (linearSearch(numList, (int) searchValue)) {
                    trueCount += 1;
                }
            }
            double end = System.currentTimeMillis();
            double runTime = end - start;
        printData(inc, trueCount, (int) runTime);
        inc += ARRAY_INCREMENT;
    }
    }

    /**
     * Demonstrates binary searching when using a Selection Sort
     *
     * @author
     */
    public static void demoBinarySearchSelectionSort() {
        System.out.println("--- Binary Search Timing (Selection Sort) ---");
        int inc = ARRAY_INCREMENT;
        while (inc < MAX_ARRAY_SIZE) {
            int[] numList = generateNumbers(inc, MAX_VALUE);

            double start = System.currentTimeMillis();
            selectionSort(numList);

            // binary search
            int trueCount = 0;
            for (int i = 0; i < NUMBER_SEARCHES; i++) {
                double searchValue = (double) Math.random() * MAX_VALUE;
                if (binarySearch(numList, (int) searchValue)) {
                    trueCount += 1;
                }
            }
            double end = System.currentTimeMillis();
            double runTime = end - start;
            printData(inc, trueCount, (int) runTime);
            inc += ARRAY_INCREMENT;

        }
    }

    /**
     * Demonstrates binary searching when using the build in Arrays.sort
     *
     * @author
     */
    public static void demoBinarySearchFastSort() {
        System.out.println("--- Binary Search Timing (Arrays.sort) ---");
        int inc = ARRAY_INCREMENT;
        while (inc < MAX_ARRAY_SIZE) {
            int[] numList = generateNumbers(inc, MAX_VALUE);

            double start = System.currentTimeMillis();
            Arrays.sort(numList);

            // binary search
            int trueCount = 0;
            for (int i = 0; i < NUMBER_SEARCHES; i++) {
                double searchValue = (double) Math.random() * MAX_VALUE;
                if (binarySearch(numList, (int) searchValue)) {
                    trueCount += 1;
                }
            }
            double end = System.currentTimeMillis();
            double runTime = end - start;
            printData(inc, trueCount, (int) runTime);
            inc += ARRAY_INCREMENT;

        }
    }
}

/**
 * Assignment 3 for CS 1410
 * This program determines if points are contained within circles or rectangles.
 *
 * @author James Dean Mathias
 */

import java.util.*;

public class Inside {
    /**
     * This is the primary driver code to test the "inside" capabilities of the
     * various functions.
     *
     * @author James Dean mathias
     */
    public static void main(String[] args) {
        double[] ptX = {1, 2, 3, 4};
        double[] ptY = {1, 2, 3, 4};
        double[] circleX = {0, 5};
        double[] circleY = {0, 5};
        double[] circleRadius = {3, 3};
        double[] rectLeft = {-2.5, -2.5};
        double[] rectTop = {2.5, 5.0};
        double[] rectWidth = {6.0, 5.0};
        double[] rectHeight = {5.0, 2.5};


        //output
        System.out.println("--- Report of Points and Circles ---\n");
        for (int j = 0; j < circleX.length; j++){

            for (int i = 0; i < ptX.length; i++) {
                ptX[i] = ptX[i];
                ptY[i] = ptY[i];

                if (isPointInsideCircle(ptX[i], ptY[i], circleX[j], circleY[j], circleRadius[j])) {
                    reportPoint(ptX[i], ptY[i]);
                    System.out.print(" is inside ");
                    reportCircle(circleX[j], circleY[j], circleRadius[j]);
                    System.out.print("\n");
                }
                else {
                    reportPoint(ptX[i], ptY[i]);
                    System.out.print(" is outside ");
                    reportCircle(circleX[j], circleY[j], circleRadius[j]);
                    System.out.println("");
                }
            }
        }

        System.out.println("");
        System.out.println("--- Report of Points and Rectangles ---\n");
        for (int j = 0; j < rectTop.length; j++) {

            for (int i = 0; i < ptX.length; i++) {
                ptX[i] = ptX[i];
                ptY[i] = ptY[i];

                if (isPointInsideRectangle(ptX[i], ptY[i], rectLeft[j], rectTop[j], rectWidth[j], rectHeight[j])){
                    reportPoint(ptX[i], ptY[i]);
                    System.out.print(" is inside ");
                    reportRectangle(rectLeft[j], rectTop[j], rectWidth[j], rectHeight[j]);
                    System.out.print("\n");
                }
                else {
                    reportPoint(ptX[i], ptY[i]);
                    System.out.print(" is outside ");
                    reportRectangle(rectLeft[j], rectTop[j], rectWidth[j], rectHeight[j]);
                    System.out.println("");
                }
            }
        }





    }

    static void reportPoint(double x, double y) {
        System.out.print("Point(" + x + " , " + y + ") " );

    }

    static void reportCircle(double x, double y, double r) {
        System.out.print("Circle(" + x + " , " + y + ") Radius;" + r + " ");
    }

    static void reportRectangle(double left, double top, double width, double height) {
        System.out.print("Rectangle(" + left + ", " + top + ", " + (left + width) + ", " + (top - height) + ")");

    }

    static boolean isPointInsideCircle(double ptX, double ptY, double circleX, double circleY, double circleRadius){

        double pointDistance = java.lang.Math.sqrt(java.lang.Math.pow((ptX - circleX),2) + java.lang.Math.pow((ptY - circleY), 2));

        if (pointDistance <= circleRadius) {
            return true;
        } else {
            return false;
        }

    }

    static boolean isPointInsideRectangle(double ptX, double ptY, double rLeft, double rTop, double rWidth, double rHeight) {

        // LOGIC: Calculate area of rectangle and split int into 4 seperate triangles. If the area of all four triangles
        // is equal to rectangles total area, then the point lies within the rectangle
        //
        //help understanding algorythm from: https://www.geeksforgeeks.org/check-whether-given-point-lies-inside-rectangle-not/

        // A (x1,y1) top left corner  = rleft, rTop
        // B (x2,y2) top right corner = rleft + width, rtop
        // C (x3, y3) bottom right corner = rleft + width, rTop - height
        // D (x4, y4) bottom left corner = rleft, rTop - height
        // P point  = ptX, ptY

        double x = ptX;
        double y = ptY;
        double x1 = rLeft;
        double y1 = rTop;
        double x2 = rLeft + rWidth;
        double y2 = rTop;
        double x3 = rLeft + rWidth;
        double y3 = rTop - rHeight;
        double x4 = rLeft;
        double y4 = rTop - rHeight;

        //area of rectangle ABCD
        float A = area(x1, y1 ,x2 ,y2, x3, y3) + area(x1, y1, x4, y4, x3, y3);
        //area of triangle PAB
        float A1 = area(x, y, x1, y1, x2, y2);
        //area of triangle PBC
        float A2 = area(x, y, x2, y2, x3, y3);
        //area of triangle PCD
        float A3 = area(x, y, x3, y3, x4, y4);
        //area of triangle PAD
        float A4 = area(x, y, x1, y1, x4 ,y4);

        //Check sum of the 4 triangles
        if ((A1 + A2 + A3 + A4) == A) {
            return true;
        } else {
            return false;
        }
    }


    static float area(double x1, double y1, double x2, double y2, double x3, double y3){
        //double triangleArea = Math.abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2);
        return (float) Math.abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2);

    }



}

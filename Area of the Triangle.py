import java.util.Scanner;

public class Area {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        float a = sc.nextInt();
        float b = sc.nextInt();
        float c = sc.nextInt();
        float s = (a+b+c)/2;
        float x = s*(s-a)*(s-b)*(s-c);
        double res = Math.sqrt(x);
        System.out.printf("%.2f",res);
    }
}
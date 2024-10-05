import java.util.Scanner;
public class CM {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        double n = sc.nextDouble();
        double k = n*2.54;
        System.out.printf("%.2f",k);
    }
}
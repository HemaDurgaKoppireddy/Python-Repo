import java.util.Scanner;
public class Profit {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int X = sc.nextInt();
        int Y = sc.nextInt();
        float profit = Y - X ;
        float per = (profit/X)*100;
        System.out.printf("%.2f",per);
    }
}
import java.util.Scanner;
public class Loss{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        float cp = sc.nextInt();
        float sp = sc.nextInt();
        float los = cp-sp;
        float per = (los/cp)*100;
        System.out.printf("%.2f",per);
    }
}
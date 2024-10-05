import java.util.Scanner;
public class Year {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int d = n%100;
        int t=d;
        int c =0;
        while(t!=0){
            c+=1;
            t/=10;
        }
        if(c<2) System.out.println("0"+d);
        else System.out.println(d);
    }
}
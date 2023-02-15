import java.util.Scanner;

public class s1CCC2022{
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        int ans = 0;
        for(int i = 0;i<=N/4;i++){
            int temp = N-(i*4);
            if(temp%5==0){
                ans++;
            }
        }
        //4*x + 5*y = N
        //N-(4*i)=R
        //if R is divisble by 5, that means we can represent the rest of the sum with fives
        System.out.println(ans);
    }
}
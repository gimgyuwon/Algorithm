import java.util.Scanner;

public class Main{
    public static void main (String [] args){
        Scanner sc = new Scanner(System.in);
        int stair_num = sc.nextInt();
        int [] stair_score = new int[stair_num];
        for ( int i = 0; i < stair_num; i++ ){
            stair_score[i] = sc.nextInt();
        }

        int [] dp = new int[stair_num+1];

        dp[0] = stair_score[0];
        if (stair_num > 1)
            dp[1] = Math.max(stair_score[0]+stair_score[1] ,stair_score[1]);
        if (stair_num > 2)
            dp[2] = Math.max(stair_score[0]+stair_score[2], stair_score[1]+stair_score[2]);

        if (stair_num < 4){
            System.out.println(dp[stair_num-1]);
        } else{
            for ( int i = 3; i < stair_num; i++ ){
                dp[i] = Math.max(dp[i-2]+stair_score[i], dp[i-3]+stair_score[i-1]+stair_score[i]);
            }
            System.out.println(dp[stair_num-1]);
        }
    }
}
import java.util.Scanner;

public class Main {
    static Integer[] dp;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        System.out.println(recur(N,0));
    }
    static int recur(int N, int count) {
        if (N < 2){
            return count;
        }
        return Math.min(recur(N/2, count + 1 + (N%2)), recur(N/3, count + 1 + (N%3)));
    }
}

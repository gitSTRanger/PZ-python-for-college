import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int sum = (n / 100) + (n / 10 % 10) + (n % 10);
        System.out.println(sum);
	}
}
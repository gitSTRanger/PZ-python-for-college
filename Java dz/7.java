import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();
        int lastDigit = Math.abs(n % 10);
        System.out.println(lastDigit);
	}
}
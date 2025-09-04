import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		int number = scanner.nextInt();
		System.out.println(String.format("The next number for the number %d is %d.", number, number + 1));
		System.out.println(String.format("The previous number for the number %d is %d.", number, number - 1));
	}
}
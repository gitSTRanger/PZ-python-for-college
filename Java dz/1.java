import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		
		System.out.print("a = ");
		int inputA = scanner.nextInt();
		
		System.out.print("b = ");
		int inputB = scanner.nextInt();
		
		System.out.print("c = ");
		int inputC = scanner.nextInt();
		
		System.out.println(String.format("a * b * c = %d", inputA * inputB * inputC));
	}
}
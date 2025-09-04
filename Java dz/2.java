import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.print("Введите время движения: ");
		float time = scanner.nextFloat();
		System.out.print("Введите скорость: ");
		float speed = scanner.nextFloat();
		System.out.println(String.format("Пройденный путь - %f", speed * time));
	}
}
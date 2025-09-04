import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Введите длину: ");
        float length = scanner.nextFloat();
        System.out.print("Введите ширину: ");
        float width = scanner.nextFloat();
        float area = length * width;
        float perimeter = 2 *(length + width);
        System.out.println(String.format("Площадь: %f", area));
        System.out.println(String.format("Периметр: %f", perimeter));
	}
}
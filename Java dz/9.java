import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int v = scanner.nextInt(); // скорость
        int t = scanner.nextInt(); // время
        
        int position = ((v * t) % 109 + 109) % 109; 
        System.out.println(position);
	}
}
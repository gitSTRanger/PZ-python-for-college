import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        float inputR = scanner.nextFloat(); // рубли
        float inputK = scanner.nextFloat(); // копейки
        float inputQuantity = scanner.nextFloat();

        float rubToKopecks = ((inputR * 100) + inputK) * inputQuantity;

        float rub = rubToKopecks / 100;
        float kopecks = rubToKopecks % 100;

        System.out.println(rub + " " + kopecks);
	}
}
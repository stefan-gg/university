import java.util.UUID;

public class App {
    public static void main(String[] args) {
        App app = new App();
        System.out.println(app.compareTwoNumbers(12, 2223));
    }

    public int compareTwoNumbers(int prviBroj, int drugiBroj) {
        return prviBroj > drugiBroj ? prviBroj : drugiBroj;
    }
}

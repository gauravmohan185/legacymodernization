import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class AddNumbersFunction {

    private static final Logger logger = LoggerFactory.getLogger(AddNumbersFunction.class);

    private int num1 = 12345;
    private int num2 = 54321;
    private int result = 0;

    public static void main(String[] args) {
        AddNumbersFunction addNumbersFunction = new AddNumbersFunction();
        addNumbersFunction.execute();
    }

    public void execute() {
        try {
            addFunction(num1, num2);
            logger.info("The result of addition is: {}", result);
        } catch (Exception e) {
            logger.error("An error occurred during addition: {}", e.getMessage());
        }
    }

    private void addFunction(int param1, int param2) {
        result = param1 + param2;
    }
}
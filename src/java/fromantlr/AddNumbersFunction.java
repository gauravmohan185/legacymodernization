import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class AddNumbersFunction {

    private static final Logger logger = LoggerFactory.getLogger(AddNumbersFunction.class);

    private int num1;
    private int num2;
    private int result;

    public AddNumbersFunction() {
        this.num1 = 12345;
        this.num2 = 54321;
        this.result = 0;
    }

    public void addNumbers(int param1, int param2) {
        try {
            logger.info("Starting addition of {} and {}", param1, param2);
            this.result = param1 + param2;
            logger.info("Addition result: {}", this.result);
        } catch (Exception e) {
            logger.error("Error occurred during addition: {}", e.getMessage());
        }
    }

    public int getResult() {
        return result;
    }

    public static void main(String[] args) {
        AddNumbersFunction addNumbersFunction = new AddNumbersFunction();
        addNumbersFunction.addNumbers(addNumbersFunction.num1, addNumbersFunction.num2);
        System.out.println("The result of addition is: " + addNumbersFunction.getResult());
    }
}
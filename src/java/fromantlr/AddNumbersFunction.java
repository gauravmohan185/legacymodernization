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

    public void add(int param1, int param2) {
        try {
            this.num1 = param1;
            this.num2 = param2;
            this.result = this.num1 + this.num2;
            logger.info("Addition performed: {} + {} = {}", this.num1, this.num2, this.result);
        } catch (Exception e) {
            logger.error("Error occurred while adding numbers: {}", e.getMessage());
        }
    }

    public int getResult() {
        return result;
    }

    public static void main(String[] args) {
        AddNumbersFunction addNumbersFunction = new AddNumbersFunction();
        addNumbersFunction.add(12345, 54321);
        System.out.println("Result of addition: " + addNumbersFunction.getResult());
    }
}
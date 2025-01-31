public class AddNumbersFunctionTest  {
     public static void main(String[] args)  {
     int testNum1 = 12345, testNum2 = 54321;
    int expectedResult = 66666;
    int actualResult = AddNumbersFunction.addFunction(testNum1, testNum2);
    System.out.println("Test " + (actualResult == expectedResult ? "passed" : "failed") + ": expected " + expectedResult + ", got " + actualResult);
    
} 
}

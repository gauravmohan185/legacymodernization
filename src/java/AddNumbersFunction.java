public class AddNumbersFunction  {
     public static void main(String[] args)  {
     int num1 = 12345, num2 = 54321;
    int[] result = new int[1];
    addFunction(num1, num2, result);
    System.out.println(result[0]);
    
} static void addFunction(int param1, int param2, int[] functionResult)  {
     functionResult[0] = param1 + param2;
    
} 
}

package simpleCalculator;
import java.util.Scanner;
//created by Nathan.
//Simple calculator from programwiz.com
public class CalculatorSimple 
{
public static void main(String[] args)
{
		char operator;
		Double number1, number2, results;
		
		//creates an object scanner class
		Scanner input = new Scanner(System.in);
		
		//asks user to enter operator
		System.out.println("Choose an operator: +, -, *, or /");
		operator = input.next().charAt(0); 
		
		//asks user to enter numbers
		System.out.println("Enter first number");
		number1 = input.nextDouble();
		
		System.out.println("Enter second number");
		number2 = input.nextDouble();
		
		switch (operator) 
		{
		//performs addition
		case '+':
			results = number1 + number2;
			System.out.println(number1 + " + " + number2 + " = " + results);
			break;
			
		//perform subtraction
		case '-':
			results = number1 - number2;
			System.out.println(number1 + " - " + number2 + " = " + results);
			break;
		
		//performs multiplication 
		case '*':
			results = number1 * number2;
			System.out.println(number1 + " * " + number2 + " = " + results);
			
		//performs division
		case '/':
			results = number1 / number2;
			System.out.println(number1 + " / " + number2 + " = " + results);
			break;
		
			default:
				System.out.println("Invalid operator!");
				break;
		}
		input.close();
			
	}
}

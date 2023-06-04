package calculateAverageValue;

public class ArrayAverage {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//Java Array Exercise. 
//By Nathan
		
		int[] numbers = new int[] {20, 30, 40, 35, -15, 60, 50, -100}; //array elements
		//calculate sum of all array elements.
		int sum = 0;
		for(int i=0; i < numbers.length ; i++)
			sum = sum + numbers[i];
		//calculate the average value.
		double average = sum / numbers.length;
		System.out.println("Average value of the array elements is : " + average);
		
		
		
		
		
		
		//the following are method calls needed to be in the main program.
		String printInfo = "NoOutputWithInput";//this has to be ran in the main portion of the main code
		NoOutputNoInput(); //this is called a method-call	//this has to be ran in the main portion of the main code
		NoOutputWithInput("NoOutputWithInput");//this has to be ran in the main portion of the main code
		MultiParameter(1, 5, 7, " pear ");
		
		for(int i = 0; i < 10; i++)//prints out the following method call 100 times with as little code as possible
		{
			NoOutputNoInput();
		}
		
	}
//the following are different types of method call.	
public static void NoOutputNoInput()
{
	System.out.println("NoOutputNoInput");//this code wouldn't run with out the method-call in the above main program.
}
//the following are different types of method call.
public static void NoOutputWithInput(String printThis)
{
	System.out.println(printThis);
}

//the following are different types of method call.
public static String OutputNoInput()
{
String printInfo = "OutputNoInput";	
return printInfo;	
}
//the following are different types of method call.
public static String OutputInput(String printThis)
{
	printThis = printThis + "Input";
	
	return printThis;
}
//the following are different types of method call.		
public static void MultiParameter(int one, int two, double three, String four)
{
	System.out.println(one + two + three + four);//know as a widening, from an integer to a float 
												 //from a float to a double
}

}

package expectedValue;

import java.io.*;


//Java code to calculate expected
//value of an array
public class Main 
{

	public static void main(String[] args) 
	{
		float expect, n = 8f;
		float a[] = { 1f, 2f, 3f,
					   4f, 5f, 6f, 7f, 8f };
		
		//function for calculating expectation
		expect = calc_Expectation(a, n);
		
		//Display expectation of given array
		System.out.println("Expectation of array E(X) is: "
										+ expect);
		}

	private static float calc_Expectation(float[] a, float n) 
	{
		//variable prb is probability of each
		//element which is same for each element
		float prb = (1 /n);
		
		//calculate expectation overall
		float sum = 0;
		for (int i = 0; i < n ; i++)
			sum += a[i] * prb;
		
		//return expectation as sum
		return sum;
	}
}



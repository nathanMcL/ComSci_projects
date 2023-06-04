package hailstone;

import java.util.*;
public class Main 
{


	public static void main(String[] args) 
	{
	int N = 7;
	int x;
	
	//function to generate hailstone numbers
	x = HailstoneNumbers(N);
	//Output: number of steps
	System.out.println();
	System.out.println("Number of Steps: " + x);
	
	}
	
		
		static int c;
		static int HailstoneNumbers(int N)
		{
			System.out.print(N + " ");
			if (N == 1 && c == 0)
			{
				// N is initially 1.
				return c;
			}
			else if (N == 1 && c != 0)
			{
				// N is reduced to 1.
				c++;
				return c;
				}
			else if (N % 2 == 0)
			{
				// if N is Even.
				c++;
				HailstoneNumbers(N / 2);
			}
			else if (N % 2 != 0)
			{
				// N is Odd.
				c++;
				HailstoneNumbers(3 * N + 1);
				}
			return c;
	
		}
}

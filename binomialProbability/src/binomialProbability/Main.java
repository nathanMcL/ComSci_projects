package binomialProbability;

import java.util.*;

public class Main 
{

	public static void main(String[] args) 
	{
	int n = 8;
	int k = 4;
	float p = (float) 1.0/3;
	
	float probability = binomialProbability(n, k, p);
	
	System.out.print("probability of " +k);
	System.out.println(" heads when a coin is tossed " +n);
	System.out.println("times where probability of each head is " +p);
	System.out.println(" is = " + probability );
	
	}
	// function to calculate nCr i.e., number of 
    // ways to choose r out of n objects
	static int nCr(int n, int r)
	{
		 // Since nCr is same as nC(n-r)
        // To decrease number of iterations
		if (r > n / 2)
			r = n - r;
		int answer = 1;
		for(int i = 1; i <= r; i++)
		{
			answer *= (n - r +i);
			answer /= i;
		}
		return answer;
	}
	 // function to calculate binomial r.v. probability
	static float binomialProbability(int n, int k, float p)
	{
		return nCr(n, k) * (float)Math.pow(p, k) * (float)Math.pow(1 - p, n - k);
		
	}
}

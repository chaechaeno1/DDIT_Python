package day03;

public class MyMethod01 {

	static int add(int a, int b) {
		return a+b;
	}
	static int minus(int a, int b) {
		return a-b;
	}
	static int multply(int a, int b) {
		return a*b;
	}

	
	
	public static void main(String[] args) {
		int sum = add(4,2);
		System.out.println("sum : "+sum);
		int min = minus(4,2);
		System.out.println("min : "+min);
		int mul = multply(4,2);
		System.out.println("mul : "+mul);
		int div = divice(4,2);
		System.out.println("div : "+div);		

	}
	
	static int divice(int a, int b) {
		return a/b;
	}

}

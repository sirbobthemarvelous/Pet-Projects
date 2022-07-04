import java.util.Scanner;

class Madlibs {
    public static void main(String[] args) {
    Scanner myObj = new Scanner(System.in);

    System.out.println("Enter a noun:");

    // String input
    String noun = myObj.nextLine();
    System.out.println("Enter a proper noun:");
    String p_noun = myObj.nextLine();
    System.out.println("Enter a place:");
    String place = myObj.nextLine();
    System.out.println("Enter another noun:");
    String noun2 = myObj.nextLine();
    System.out.println("Enter an adjective:");
    String adjective = myObj.nextLine();
    System.out.println("Enter a third noun:");
    String noun3 = myObj.nextLine();

    /* Numerical input
    int age = myObj.nextInt();
    double salary = myObj.nextDouble(); */

    print ("------------------------------------------")
    print ("Be kind to your",noun,"- footed", p_noun)
    print ("For a duck may be somebody's", noun2,",")
    print ("Be kind to your",p_noun,"in",place)
    print ("Where the weather is always",adjective,".")
    print ()
    print ("You may think that is this the",noun3,",")
    print ("Well it is.")
    print ("------------------------------------------")
    }
}
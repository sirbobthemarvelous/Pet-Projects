import java.util.Scanner;
import java.util.Random;

class Madlibs {
    public static void main(String[] args) {
    Scanner myObj = new Scanner(System.in);
    Random randomized = new Random();
    int answer = randomized.nextInt(10)+1;

    int guesses = 0
    boolean guessing = true
    while(guessing){
        System.out.println("Enter a number between 1 and 10:");
        int guess = myObj.nextInt();
        
        if(guess<1 || guess >10){
            System.out.println("Out of bounds")
        }
        else if(guess == answer){
            System.out.println("Congrats you got it!")
            guessing = false;
        }
        else if(guess > answer){
            System.out.println("guess is too high")
            guesses++;
        }
        else if(guess < answer){
            System.out.println("guess is too low")
            guesses++
        }
    }

    }
}
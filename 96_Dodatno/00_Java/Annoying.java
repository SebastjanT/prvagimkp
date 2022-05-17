import java.util.*;

public class Annoying {
  public static void main(String[] args){
    // Infinate loop that repeats the users input back to them, if there is any
    Scanner sc = new Scanner(System.in);

    String userInput = "";
    while(true){
      userInput = sc.nextLine();

      if (userInput.isEmpty()){
        break;
      }

      System.out.println(userInput);
    }

    sc.close();
  }  
}

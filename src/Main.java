import java.io.*;

public class Main {

    public static void main(String[] args) {
        try {
//            Реализовать приложение вызывающее питон скрипт выводящий принятую в параметры информацию в консоль

//            System.out.println("Input str");
//            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
//            String str = reader.readLine();
//            Runtime.getRuntime().exec("cmd.exe /c start python Main.py " + str);

            Runtime.getRuntime().exec("cmd.exe /c start python Main.py " +
                    "arg_one --arg_2=arg_tho -+arg_3=arg_three");
            
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
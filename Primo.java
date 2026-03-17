import java.util.Scanner;



public class Primo{
    public static void main(String[]args){

        Scanner sc=new Scanner(System.in);

        System.out.println("Introduzca un numero para verificar si es primo: ");

        int primo=sc.nextInt();

        boolean esPrimo=true;

        if (primo==1 ){
            esPrimo=false;
        }else{
            for(int i=2; i <= primo / 2;i++){

                if (primo % i == 0){

                    esPrimo=false;

                    break;
                }

            }
        }

        if (esPrimo ){
            System.out.println("Numero primo");//mensaje cambiado 
        }else{
            System.out.println("El numero no es primo");
        }
        
    }
    
}


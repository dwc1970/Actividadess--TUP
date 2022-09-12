/*
erjercicio2 : leer un numero e identificar si es positico o negativo.
el Proceso se repetira hasta que se indroduzca 0 
hacer este ejercicio con la clase scaneer, luego hacerlo
con la clase JOptionPane
*/
package CiclosEjercicio02;

import java.util.Scanner;


public class EjercicioCiclos02 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un mumero");
        var numero = Integer.parseInt(entrada.nextLine());
        while(numero != 0){
            if(numero >= 0){
                System.out.println("si numero"+numero+"es positivo");
            }
                else {
                        System.out.println("El numero"+numero+"es negativo");
                       
                    }
                System.out.println("Digite otro numero: ");
                numero = Integer.parseInt(entrada.nextLine());                
            }
        System.out.println("El numero"+numero+"finaliza el programa");
        }
    }
 


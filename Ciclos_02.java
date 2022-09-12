/*
erjercicio2 : leer un numero e identificar si es positico o negativo.
el Proceso se repetira hasta que se indroduzca 0 
hacer este ejercicio con la clase scaneer, luego hacerlo
con la clase JOptionPane
*/

package CiclosEjercicio02;

import javax.swing.JOptionPane;


public class Ciclos_02 {
    public static void main(String[] args) {
       
        var numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while(numero != 0){
            if(numero >= 0){
                JOptionPane.showMessageDialog(null, "El numero es positivo");
            }
                else {
                        JOptionPane.showMessageDialog(null, "El numero es negativo");
                     
            }
              
                numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));                
            }
        JOptionPane.showMessageDialog(null, "El numero"+numero+"finaliza el programa");
        }
    }
 

    


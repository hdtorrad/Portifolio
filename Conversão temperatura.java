package Desafio;

import javax.swing.JOptionPane;

public class Desafio02Aula021VariaveiConstante 
{
	public static void main(String[] args) 
	{
		//Constantes:
		final float FATORFTOC = 5f/9f;
		final float FATORCTOF = 1.8f;
		final int AJUSTE = 32;
		
		//Variaveis:
		float celsius;
		float fahrenheit;
		boolean opcao = false;
		
		opcao = (Integer.parseInt(JOptionPane.showInputDialog("Insira a opção deseja: \n[0-Cº to Fº || 1-Fº to Cº]")) == 0) ? false : true;
		System.out.println(opcao);
		
		if(opcao)
		{
			fahrenheit = Float.parseFloat(JOptionPane.showInputDialog("Insira a temperatura em Fahrenheit"));
			JOptionPane.showMessageDialog(null, fahrenheit + "Fº em Celsius é igual a " + ((fahrenheit - AJUSTE) * FATORFTOC) + "Cº");
		}
		
		else
		{
			celsius = Float.parseFloat(JOptionPane.showInputDialog("Insira a temperatura em Celsius"));
			JOptionPane.showMessageDialog(null, celsius + "Cº em Fahrenheit é igual a " + ((celsius * FATORCTOF) + AJUSTE) + "Fº");
		}
	}
}

package src;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class GameManager {
    public static void main(String[] args) throws InterruptedException, IOException {
        Scanner sc = new Scanner(System.in);
        Random random = new Random();

        LimpaTela();
        System.out.println(" == Clue Card Game ==");
        pressEnter(sc);

        Deck evidencia = new Deck();
        evidencia.marcarCrime(random.nextInt(4));
        evidencia.marcarCrime(4 + random.nextInt(5));
        evidencia.marcarCrime(9 + random.nextInt(6));

        ArrayList<Player> players = new ArrayList<>();
        for(int i = 0; i < 4; i++){
            ArrayList<Carta> pistas = new ArrayList<>();
            int n = 0;
            do {
                int j = random.nextInt(15);
                Carta pista = evidencia.getCarta(j);
                if(!pista.isMarcada() && !pista.isCrime()){
                    pistas.add(pista);
                    evidencia.cartas.get(j).marcarCarta();
                    n++;
                }
            } while (n < 3);
            players.add(new Player(pistas));
        }

        boolean sair = false;
        int cont = 1, jogador = 0;

        System.out.println("\nCrime");
        for (int i = 0; i < evidencia.cartas.size(); i++){
            if(evidencia.cartas.get(i).isCrime()){
                System.out.println(evidencia.cartas.get(i));
            }
        }

        System.out.println("\nPistas por jogador");
        for (int i = 0; i < players.size(); i++){
            System.out.println("\nPlayer "+ i);
            for(int j = 0; j < players.get(i).getPistas().size(); j++){
                System.out.println(players.get(i).getPista(j).exibirCarta());
            }
        }

        sc.close();
    }

    public static void pressEnter(Scanner sc) {
        System.out.print("\n Pressione enter para continuar! ");
        sc.nextLine();
    }

    public static void LimpaTela() throws InterruptedException, IOException {
        // Isso aqui funciona pra identificar qual SO está sendo usado
        String osName = System.getProperty("os.name").toLowerCase();
        if (osName.contains("windows")) {
            new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
        } else {
            new ProcessBuilder("sh", "-c", "clear").inheritIO().start().waitFor();
        }
    }
}

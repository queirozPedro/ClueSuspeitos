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
        for (int i = 0; i < 4; i++) {
            ArrayList<Carta> pistas = new ArrayList<>();
            int n = 0;
            do {
                int j = random.nextInt(15);
                Carta pista = evidencia.getCarta(j);
                if (!pista.isMarcada() && !pista.isCrime()) {
                    pistas.add(pista);
                    evidencia.cartas.get(j).setCrime(true);
                    ;
                    n++;
                }
            } while (n < 3);
            players.add(new Player(pistas));
        }

        boolean sair = false;
        int cont = 0;
        Deck deckAux = new Deck();

        // Iniciando Jogo
        do {
            try {
                LimpaTela();
                System.out.println(" << Player " + (cont + 1) + " >>");
                System.out.println(players.get(cont).exibirMao());
                System.out.println("\n 1 -> Realizar Pergunta");
                System.out.println(" 2 -> Realizar Acusação");
                System.out.println(" 3 -> Marcar Cartas");
                System.out.println(" 4 -> Desmarcar Cartas");
                System.out.print(" > ");

                switch (Integer.valueOf(sc.nextLine())) {
                    case 1:
                        System.out.println("\n Quais Cartas deseja perguntar ao jogador " + (cont == 3? 1: cont + 2) + " ?");
                        System.out.print(" 1ª -> ");
                        Carta auxA = deckAux.getCarta(Integer.valueOf(sc.nextLine()) - 1);
                        System.out.print(" 2ª -> ");
                        Carta auxB = deckAux.getCarta(Integer.valueOf(sc.nextLine()) - 1);
                        if(auxA.getClasse() == auxB.getClasse()){
                            LimpaTela();
                            System.out.println(" Pergunta inválida, as cartas devem ser de tipos diferentes");
                            pressEnter(sc);
                            break;
                        }
                        LimpaTela();
                        System.out.println(" << Player " + (cont == 3? 1: cont + 2) + " >>");
                        System.out.println("\n Cartas Questionadas pelo Player "+ ((cont == 3? 1: cont + 2) - 1));
                        System.out.println(auxA.exibirCarta());
                        System.out.println(auxB.exibirCarta());
                        System.out.println(players.get(cont == 3? 0: cont + 1).exibirPistas());
                        pressEnter(sc);
                        LimpaTela();
                        System.out.println(" << Player " + (cont + 1) + " >>");
                        System.out.println(players.get(cont).exibirMao());
                        System.out.println("\n 1 -> Marcar Cartas");
                        System.out.println(" 2 -> Desmarcar Cartas");
                        System.out.println(" 3 -> Continuar");
                        System.out.print(" > ");
                        do {
                            switch (Integer.valueOf(sc.nextLine())) {
                                case 1:
                                    System.out.println("\n Qual Carta Deseja Marcar? ");
                                    System.out.print(" > ");
                                    players.get(cont).getDeckArquivo().marcarCarta(Integer.valueOf(sc.nextLine()) - 1);
                                    break;
                                case 2:
                                    System.out.println("\n Qual Carta Deseja Desmarcar? ");
                                    System.out.print(" > ");
                                    players.get(cont).getDeckArquivo().desmarcarCarta(Integer.valueOf(sc.nextLine()) - 1);
                                    break;
                                case 3:
                                    pressEnter(sc);
                                    sair = true;
                                    cont = cont == 3? 0: cont + 1;
                                    break;
                                default:
                                    System.out.println(" Operação Inválida!");
                                    pressEnter(sc);
                                    break;
                            }
                        } while (!sair);
                        sair = false;
                        break;
                    case 2:
                        LimpaTela();
                        System.out.println(" Indiquem seu palpite ");
                        System.out.println(" Jogado 1: ");
                        System.out.println(" Precisa ser feito");
                        pressEnter(sc);
                    case 3:
                        System.out.println(" Qual Carta Deseja Marcar? ");
                        System.out.print(" > ");
                        players.get(cont).getDeckArquivo().marcarCarta(Integer.valueOf(sc.nextLine()) - 1);
                        break;
                    case 4:
                        System.out.println(" Qual Carta Deseja Desmarcar? ");
                        System.out.print(" > ");
                        players.get(cont).getDeckArquivo().desmarcarCarta(Integer.valueOf(sc.nextLine()) - 1);
                        break;
                    default:
                        System.out.println(" Operação Inválida!");
                        pressEnter(sc);
                        break;
                }
            } catch (NumberFormatException e) {}
        } while (!sair);

        /* Passa os jogadores exibindo as cartas de cada um */

        // do {
        // LimpaTela();
        // System.out.println(" << Player "+ (cont+1) +" >>");
        // System.out.println(players.get(cont).exibirMao());
        // cont = cont == 3? 0: cont + 1;
        // pressEnter(sc);
        // } while (!sair);

        /* Mostra o Crime e as pistas de Cada Jogador */

        // System.out.println("\nCrime");
        // for (int i = 0; i < evidencia.cartas.size(); i++){
        // if(evidencia.cartas.get(i).isCrime()){
        // System.out.println(evidencia.cartas.get(i));
        // }
        // }

        // System.out.println("\nPistas por jogador");
        // for (int i = 0; i < players.size(); i++){
        // System.out.println("\nPlayer "+ i);
        // for(int j = 0; j < players.get(i).getPistas().size(); j++){
        // System.out.println(players.get(i).getPista(j).exibirCarta());
        // }
        // }

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

    public static final String resetCor = "\u001B[0m";
    public static final String corVermelho = "\u001B[31m";
    public static final String corVerde = "\u001B[32m";
    public static final String corAmarelo = "\u001B[33m";
    public static final String corLaranja = "\u001B[33m\u001B[31m";

    /**
     * Método que recebe o código de uma cor e uma string e altera a cor dela
     * 
     * @param texto
     * @param cor
     * @return String - Texto colorido
     */
    public static String colorirTexto(String texto, String cor) {
        return cor + texto + resetCor;
    }
}

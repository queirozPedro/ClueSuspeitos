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

        /* Mostra o Crime e as pistas de Cada Jogador */

        System.out.println("\n Crime");
        for (int i = 0; i < evidencia.cartas.size(); i++) {
            if (evidencia.cartas.get(i).isCrime()) {
                System.out.println(evidencia.getCarta(i).exibirCarta());
            }
        }

        System.out.println("\n Pistas por jogador");
        for (int i = 0; i < players.size(); i++) {
            System.out.println(" Player " + i);
            for (int j = 0; j < players.get(i).getPistas().size(); j++) {
                System.out.println(players.get(i).getPista(j).exibirCarta());
            }
        }

        System.out.println("\n Todas as Evidencias ");
        System.out.println(evidencia.exibirDeck());

        pressEnter(sc);

        boolean sair = false;
        int cont = 0;
        Deck deckAux = new Deck();

        // Iniciando Jogo
        do {
            try {
                LimpaTela();
                // cont é o jogador atual, cont + 1 é apenas para não mostrar 0
                System.out.println(" << Player " + (cont + 1) + " >>");
                System.out.println(players.get(cont).exibirMao());
                System.out.println("\n 1 -> Realizar Pergunta");
                System.out.println(" 2 -> Realizar Acusação");
                System.out.println(" 3 -> Marcar Cartas");
                System.out.println(" 4 -> Desmarcar Cartas");
                System.out.print(" > ");

                switch (Integer.valueOf(sc.nextLine())) {
                    case 1:
                        ArrayList<Carta> perguntas = new ArrayList<>();
                        System.out.println(
                                "\n Quais Cartas deseja perguntar ao player " + (cont == 3 ? 1 : cont + 2) + "?");
                        // cont + 1 é o próximo jogador, cont + 2 é uma maneira de imprimir ele
                        System.out.print(" 1ª -> ");
                        perguntas.add(deckAux.getCarta(Integer.valueOf(sc.nextLine()) - 1));
                        System.out.print(" 2ª -> ");
                        perguntas.add(deckAux.getCarta(Integer.valueOf(sc.nextLine()) - 1));
                        if (perguntas.get(0).getClasse() == perguntas.get(1).getClasse()) {
                            LimpaTela();
                            System.out.println(" Pergunta inválida, as cartas devem ser de tipos diferentes");
                            pressEnter(sc);
                            break;
                        }
                        LimpaTela();
                        System.out.println(" << Player " + (cont == 3 ? 1 : cont + 2) + " >>");
                        System.out.println("\n Cartas Questionadas pelo Player " + (cont == 3 ? 4 : cont + 1));
                        System.out.println(perguntas.get(0).exibirCarta());
                        System.out.println(perguntas.get(1).exibirCarta());
                        ArrayList<Carta> respostas = players.get((cont == 3 ? 0 : cont + 1))
                                .verificarResposta(perguntas);
                        pressEnter(sc);
                        switch (respostas.size()) {
                            case 1:
                                LimpaTela();
                                System.out.println(" << Player " + (cont + 1) + " >>");
                                System.out.println(" Resposta: ");
                                System.out.println(respostas.get(0).exibirCarta());
                                break;
                            case 2:
                                do {
                                    LimpaTela();
                                    System.out.println(" << Player " + (cont == 3 ? 1 : cont + 2) + " >>");
                                    System.out.println(" Escolha sua resposta");
                                    for (int i = 0; i < respostas.size(); i++) {
                                        System.out.println(respostas.get(i).exibirCarta());
                                    }
                                    System.out.println(" 1 -> Primera, 2 -> Segunda");
                                    System.out.print(" > ");
                                    switch (Integer.valueOf(sc.nextLine())) {
                                        case 1:
                                            LimpaTela();
                                            System.out.println(" << Player " + (cont + 1) + " >>");
                                            System.out.println(
                                                    " Resposta Obtida do Player " + (cont == 3 ? 1 : cont + 2));
                                            System.out.println(respostas.get(0).exibirCarta());
                                            sair = true;
                                            break;
                                        case 2:
                                            LimpaTela();
                                            System.out.println(" << Player " + (cont + 1) + " >>");
                                            System.out.println(
                                                    " Resposta Obtida do Player " + (cont == 3 ? 1 : cont + 2));
                                            System.out.println(respostas.get(1).exibirCarta());
                                            sair = true;
                                            break;
                                        default:
                                            System.out.println(" Opção inválida");
                                            pressEnter(sc);
                                            break;
                                    }
                                } while (!sair);
                                pressEnter(sc);
                                sair = false;
                                break;
                            case 0:
                                LimpaTela();
                                System.out.println(" << Player " + (cont + 1) + " >>");
                                System.out.println(
                                        " Resposta Obtida do Player " + (cont == 3 ? 1 : cont + 2));
                                System.out.println(" Não posso te ajudar!");
                                break;

                            default:
                                break;
                        }
                        pressEnter(sc);
                        do {
                            LimpaTela();
                            System.out.println(" << Player " + (cont + 1) + " >>");
                            System.out.println(players.get(cont).exibirMao());
                            System.out.println("\n 1 -> Marcar Cartas");
                            System.out.println(" 2 -> Desmarcar Cartas");
                            System.out.println(" 3 -> Continuar");
                            System.out.print(" > ");
                            switch (Integer.valueOf(sc.nextLine())) {
                                case 1:
                                    System.out.println("\n Qual Carta Deseja Marcar? ");
                                    System.out.print(" > ");
                                    players.get(cont).getDeckArquivo().marcarCarta(Integer.valueOf(sc.nextLine()) - 1);
                                    break;
                                case 2:
                                    System.out.println("\n Qual Carta Deseja Desmarcar? ");
                                    System.out.print(" > ");
                                    players.get(cont).getDeckArquivo()
                                            .desmarcarCarta(Integer.valueOf(sc.nextLine()) - 1);
                                    break;
                                case 3:
                                    sair = true;
                                    break;
                                default:
                                    System.out.println(" Operação Inválida!");
                                    pressEnter(sc);
                                    break;
                            }
                        } while (!sair);
                        cont = cont == 3 ? 0 : cont + 1;
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
            } catch (NumberFormatException e) {
            }
        } while (!sair);

        /* Passa os jogadores exibindo as cartas de cada um */

        // do {
        // LimpaTela();
        // System.out.println(" << Player "+ (cont+1) +" >>");
        // System.out.println(players.get(cont).exibirMao());
        // cont = cont == 3? 0: cont + 1;
        // pressEnter(sc);
        // } while (!sair);

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

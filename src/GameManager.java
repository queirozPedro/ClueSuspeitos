package src;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class GameManager {

    public static void main(String[] args) throws InterruptedException, IOException {
        Scanner sc = new Scanner(System.in);
        inicarJogo(sc);
        sc.close();
    }

    /**
     * É aqui que o jogo começa
     */
    public static void inicarJogo(Scanner sc) throws InterruptedException, IOException {

        LimpaTela();
        System.out.println(" == Clue Card Game ==");
        System.out.println(" Iniciar Jogo");
        pressEnter(sc);
        
        /*
        * Primeiro vamos gerar o deck das evidencia e criar o crime.
        * Em seguida vamos criar os jogadores e distribuir entre eles as 
        * cartas de evidências.
        */
        Deck evidencia = gerarCrime();
        ArrayList<Player> players = criarPlayers(evidencia);
        
        // Teste
        infoPartida(evidencia, players);
        pressEnter(sc);
        // Fim Teste

        /*
         * Iniciando o Jogo
         */

        boolean sair = false;
        int cont = 0;
        Deck deckAux = new Deck();

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
                        perguntas.get(0).marcarCarta();
                        System.out.println(perguntas.get(1).exibirCarta());
                        perguntas.get(1).marcarCarta();
                        ArrayList<Carta> respostas = players.get((cont == 3 ? 0 : cont + 1)).verificarResposta(perguntas);
                        pressEnter(sc);
                        switch (respostas.size()) {
                            case 1:
                                LimpaTela();
                                System.out.println(" << Player " + (cont + 1) + " >>");
                                System.out.println("\n Resposta: ");
                                System.out.println(respostas.get(0).exibirCarta());
                                break;
                            case 2:
                                do {
                                    LimpaTela();
                                    System.out.println(" << Player " + (cont == 3 ? 1 : cont + 2) + " >>");
                                    System.out.println("\n Escolha sua resposta");
                                    for (int i = 0; i < respostas.size(); i++) {
                                        System.out.println(" "+ (i+1) +" ->"+ respostas.get(i).exibirCarta());
                                    }
                                    System.out.print(" > ");
                                    switch (Integer.valueOf(sc.nextLine())) {
                                        case 1:
                                            LimpaTela();
                                            System.out.println(" << Player " + (cont + 1) + " >>");
                                            System.out.println("\n Resposta Obtida do Player " + (cont == 3 ? 1 : cont + 2));
                                            System.out.println(respostas.get(0).exibirCarta());
                                            sair = true;
                                            break;
                                        case 2:
                                            LimpaTela();
                                            System.out.println(" << Player " + (cont + 1) + " >>");
                                            System.out.println("\n Resposta Obtida do Player " + (cont == 3 ? 1 : cont + 2));
                                            System.out.println(respostas.get(1).exibirCarta());
                                            sair = true;
                                            break;
                                        default:
                                            System.out.println(" Opção inválida");
                                            break;
                                    }
                                } while (!sair);
                                sair = false;
                                break;
                            case 0:
                                LimpaTela();
                                System.out.println(" << Player " + (cont + 1) + " >>");
                                System.out.println(" Resposta Obtida do Player " + (cont == 3 ? 1 : cont + 2));
                                System.out.println(colorirTexto(" Não posso te ajudar!", corVermelho));
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
                        boolean endGame = false;
                        System.out.println("Indiquem seus palpites");
                        System.out.println(deckAux.exibirDeck());
                        for (int i = 0; i < players.size(); i++){
                            int[] acusacao = new int[3];
                            System.out.println("\n Player "+ (cont == 3? 4: cont + 1) + "");
                            System.out.print(" > ");
                            acusacao[0] = Integer.valueOf(sc.nextLine());    
                            System.out.print(" > ");
                            acusacao[1] = Integer.valueOf(sc.nextLine());    
                            System.out.print(" > ");
                            acusacao[2] = Integer.valueOf(sc.nextLine());
                            players.get(cont).setAcusacao(acusacao);   
                            cont = cont == 3? 0: cont + 1;
                        }
                        LimpaTela();
                        System.out.println(" O Crime era: ");
                        for (int i = 0; i < evidencia.getDeck().size(); i++){
                            if(evidencia.getCarta(i).isCrime()){
                                System.out.println(evidencia.getCarta(i).exibirCarta());
                            }
                        }
                        System.out.println();
                        for (int i = 0 ; i < players.size(); i++){
                            if (evidencia.getCarta(players.get(cont).getAcusacao(0) - 1).isCrime() && evidencia.getCarta(players.get(cont).getAcusacao(1) - 1).isCrime() && evidencia.getCarta(players.get(cont).getAcusacao(2) - 1).isCrime()){
                                if(endGame){
                                    System.out.println(" O Player "+ (cont + 1) +" Acertou!");
                                    
                                }
                                else{
                                    System.out.println(colorirTexto(" O Player "+ (cont + 1) +" Venceu!", corVerde));
                                    endGame = true;
                                }
                            }
                            else {
                                System.out.println(" O Player "+ (cont + 1)+ " Perdeu!");
                            }
                            cont = cont == 3? 0: cont + 1;
                        }
                        pressEnter(sc);
                        sair = true;
                        break;
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
        System.out.println(" <> Fim de Jogo <>");
    }

    /**
     * Método que gera o crime e cria o Deck de evidencias da partida
     * @return Deck
     */
    public static Deck gerarCrime() {
        Random random = new Random();
        
        /*
         * Aqui funciona assim, um deck será criado e dentro dele uma arma, um lugar e
         * um suspeito
         * serão marcadas como crime.
         */
        Deck evidencia = new Deck();
        // O indice das armas varia entre 0 e 3
        evidencia.marcarCrime(random.nextInt(4));
        // O indice do lugar varia entre 4 e 8
        evidencia.marcarCrime(4 + random.nextInt(5));
        // O indice do suspeito varia entre 9 e 14
        evidencia.marcarCrime(9 + random.nextInt(6));

        return evidencia;
    }
    
    /**
     * Metodo que recebe as evidencias e distribui as pistas entre os jogadores
     * @param evidencia
     * @return ArrayList<Player>
     */
    private static ArrayList<Player> criarPlayers(Deck evidencia) {
        Random random = new Random();
        
        /*
         * Aqui eu crio os jogadores e divido entre eles o restante das cartas de
         * maneira aleatória.
         * Cada Player tem um Deck e um Arraylist de Cartas que reprensenta as pistas.
         * Cada Deck tem 15 cartas (do 0 ao 14) que representam os 3 tipos de carta,
         * sendo eles
         * arma, lugar e suspeito, com 4, 5 e 6 cartas cada, respectivamente.
         */
        ArrayList<Player> players = new ArrayList<>();

        // São 4 jogadores
        for (int i = 0; i < 4; i++) {
            // Para cada jogador eu crio um Arraylist de Cartas que vai ficar com as pistas
            ArrayList<Carta> pistas = new ArrayList<>();
            int n = 0;
            do {
                // Ele vai pegar um valor aleatório entre 0 e 14 (variação de 15)
                int j = random.nextInt(15);
                // Uma carta aleatória vai ser retirada do restante das evidencias
                Carta pista = evidencia.getCarta(j);
                // Se ela for marcada, já foi removida, se for crime, também não pode ser
                // retirada
                if (!pista.isMarcada() && !pista.isCrime()) {
                    // Se não foi usada, será
                    pistas.add(pista);
                    // É marcada para garantir que não seja tirada mais de uma vez
                    evidencia.cartas.get(j).marcarCarta();
                    n++;
                }
            } while (n < 3);
            // Conseguidas as três cartas, elas serão entregues aos jogadores
            players.add(new Player(pistas));
        }
        return players;
    }
    

    /**
     * Imprime dados relevantes sobre a partida
     * 
     * @param evidencia
     * @param players
     */
    public static void infoPartida(Deck evidencia, ArrayList<Player> players) {
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
    }

    /**
     * Método que exibe informações sobre os Decks dos jogadores
     * 
     * @param sc
     * @throws IOException
     * @throws InterruptedException
     */
    public static void infoDecks(Scanner sc, ArrayList<Player> players) throws InterruptedException, IOException {
        int aux = 0;
        boolean sair = false;
        do {
            LimpaTela();
            System.out.println(" << Player " + (aux + 1) + " >>");
            System.out.println(players.get(aux).exibirMao());
            aux = aux == 3 ? 0 : aux + 1;
            pressEnter(sc);
        } while (!sair);
    }

    /*
     * Alguns métodos que servem para estilizar o terminal
     */

    public static void pressEnter(Scanner sc) {
        System.out.print("\n Pressione enter para continuar! ");
        sc.nextLine();
    }

    /**
     * Método que limpa o terminal
     * 
     * @throws InterruptedException
     * @throws IOException
     */
    public static void LimpaTela() throws InterruptedException, IOException {
        // Isso aqui funciona pra identificar qual SO está sendo usado
        String osName = System.getProperty("os.name").toLowerCase();
        if (osName.contains("windows")) {
            new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
        } else {
            new ProcessBuilder("sh", "-c", "clear").inheritIO().start().waitFor();
        }
    }

    // Algumas cores que vou usar para deixar bonito 
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
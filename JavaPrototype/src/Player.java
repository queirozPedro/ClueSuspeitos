package src;
import java.util.ArrayList;

public class Player {
    private Deck deckArquivo;
    private ArrayList<Carta> pistas;
    private int[] acusacao;

    public Player(ArrayList<Carta> pistas) {
        this.deckArquivo = new Deck();
        this.pistas = pistas;
    }

    public Deck getDeckArquivo() {
        return deckArquivo;
    }
    public void setDeckArquivo(Deck deckArquivo) {
        this.deckArquivo = deckArquivo;
    }
    
    public ArrayList<Carta> getPistas() {
        return pistas;
    }
    public void setPistas(ArrayList<Carta> pistas) {
        this.pistas = pistas;
    }
    
    public Carta getPista(int i){
        return pistas.get(i);
    }


    public String exibirMao(){
        String string = deckArquivo.exibirDeck() + "\n\n = Pistas do Jogador =";
        for(int i = 0; i < pistas.size(); i++){ 
            string += "\n" + pistas.get(i).exibirCarta();
        }
        return string;
    }

    public String exibirPistas(){
        String string ="\n = Pistas do Jogador =";
        for(int i = 0; i < pistas.size(); i++){
            string += "\n" + pistas.get(i).exibirCarta();
        }
        return string;
    }

    public ArrayList<Carta> verificarResposta(ArrayList<Carta> perguntas){
        ArrayList<Carta> respostas = new ArrayList<>();
        for (int i = 0; i < pistas.size(); i++){
            for (int j = 0; j < perguntas.size(); j++){
                if(pistas.get(i).getNome().equals(perguntas.get(j).getNome()))
                    respostas.add(perguntas.get(j));
            }
        }
        return respostas;
    }

    public void marcarNoDeck(){
        for (int i = 0; i < deckArquivo.getDeck().size(); i++){
            for (int j = 0; j < pistas.size(); j++){
                if(pistas.get(j) == deckArquivo.getCarta(i)){
                    deckArquivo.getCarta(i).marcarCarta();
                }
            }
        }
    }

    public int getAcusacao(int i) {
        return acusacao[i];
    }

    public void setAcusacao(int[] acusacao) {
        this.acusacao = acusacao;
    }

}

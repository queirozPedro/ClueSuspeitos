package src;
import java.util.ArrayList;

public class Player {
    private Deck deckArquivo;
    private ArrayList<Carta> pistas;

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
        for(int i = 0; i < getPistas().size(); i++){
            for (int j = 0; j < respostas.size(); j++){
                if (perguntas.get(j) == getPista(i)){
                    respostas.add(getPista(i));
                }
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

}

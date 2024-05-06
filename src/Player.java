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

}

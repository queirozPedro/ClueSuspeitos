package src;
import java.util.ArrayList;

public class Deck {
    ArrayList<Carta> cartas = new ArrayList<>();

    public Deck() {
        // 4 Armas (do 0 ao 3)
        cartas.add(new Carta("Arma", "Faca"));
        cartas.add(new Carta("Arma", "Revolver"));
        cartas.add(new Carta("Arma", "Corda"));
        cartas.add(new Carta("Arma", "Castiçal"));

        // 5 Lugares (do 4 ao 8)
        cartas.add(new Carta("Lugar", "Sala de Estar"));
        cartas.add(new Carta("Lugar", "Sala de Jantar"));
        cartas.add(new Carta("Lugar", "Spa"));
        cartas.add(new Carta("Lugar", "Hall"));
        cartas.add(new Carta("Lugar", "Cozinha"));

        // 6 Suspeitos (do 9 ao 14)
        cartas.add(new Carta("Suspeito", "White"));
        cartas.add(new Carta("Suspeito", "Scarlet"));
        cartas.add(new Carta("Suspeito", "Green"));
        cartas.add(new Carta("Suspeito", "Plum"));
        cartas.add(new Carta("Suspeito", "Peacock"));
        cartas.add(new Carta("Suspeito", "Mustard"));
    }

    public ArrayList<Carta> getDeck() {
        return cartas;
    }
    public void setDeck(ArrayList<Carta> cartas) {
        this.cartas = cartas;
    }
    
    
    public Carta getCarta(int i){
        return cartas.get(i);
    } 

    public void marcarCarta(int i){
        cartas.get(i).marcarCarta();
    }
    public void desmarcarCarta(int i){
        cartas.get(i).desmarcarCarta();
    }

    public boolean cartaIsMarcada(int i){
        return cartas.get(i).isMarcada();
    }

    public void marcarCrime(int i){
        cartas.get(i).setCrime(true);
    }
    public boolean ehCrime(int i){
        return cartas.get(i).isCrime();
    }

    public String exibirDeck(){
        String string = "\n = Deck =";
        for(int i = 0; i < getDeck().size(); i++){
            string += (i == 4 || i % 9 == 0)? "\n\n " + (i+1) + " -" + getCarta(i).exibirCarta(): "\n " + (i+1) + " -" + getCarta(i).exibirCarta();
        }
        return string;
    }


}

package src;
public class Carta {
    
    private String classe;
    private String nome;
    private boolean crime;
    private boolean marcada;
    
    public Carta(String classe, String nome) {
        this.classe = classe;
        this.nome = nome;
        this.crime = false;
        this.marcada = false;
    }

    public boolean isMarcada() {
        return marcada;
    }
    public void marcarCarta() {
        this.marcada = true;
    }

    public boolean isCrime() {
        return crime;
    }
    public void setCrime(boolean crime) {
        this.crime = crime;
    }

    public String exibirCarta() {
        return "Carta [classe=" + classe + ", nome=" + nome + ", marcada=" + marcada + "]";
    }

    @Override
    public String toString() {
        return "Carta [classe=" + classe + ", nome=" + nome + ", crime=" + crime + ", marcada=" + marcada + "]";
    }
    
}

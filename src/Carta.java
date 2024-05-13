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
    public void desmarcarCarta() {
        this.marcada = false;
    }

    public boolean isCrime() {
        return crime;
    }
    public void setCrime(boolean crime) {
        this.crime = crime;
    }

    public String exibirCarta() {
        if (isCrime()){
            return GameManager.colorirTexto(" Classe: " + classe + ", Nome: " + nome, GameManager.corLaranja);
        }
        else if (isMarcada()){
            return GameManager.colorirTexto(" Classe: " + classe + ", Nome: " + nome, GameManager.corAmarelo);
        }
        else{
            return " Classe: " + classe + ", Nome: " + nome;
        }
    }

    public String getClasse() {
        return classe;
    }

    public void setClasse(String classe) {
        this.classe = classe;
    }
    
    public String getNome() {
        return nome;
    }

    public String exibirCartaDetalhada() {
        return " Carta [classe=" + classe + ", nome=" + nome + ", crime=" + crime + ", marcada=" + marcada + "]";
    }
}

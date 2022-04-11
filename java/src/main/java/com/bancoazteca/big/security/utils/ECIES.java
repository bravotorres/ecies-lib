package com.bancoazteca.big.security.utils;

public class ECIES {
    private String saludo;

    public String getSaludo() {
        return saludo;
    }

    public void setSaludo(String saludo) {
        this.saludo = saludo;
    }

    public ECIES(String saludo) {
        this.saludo = saludo;
    }

    @Override
    public String toString() {
        return "ECIES{" + "saludo=" + saludo + '}';
    }
}

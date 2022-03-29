package com.bancoazteca.big.security;

import com.bancoazteca.big.security.utils.ECIES;


public class TestECIES {

    public static void main(String[] args) {
        ECIES ecies = new ECIES("Alex");
        
        System.out.printf("Hello World! %s\n", ecies);
    }
}

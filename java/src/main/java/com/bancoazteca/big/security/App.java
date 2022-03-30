package com.bancoazteca.big.security;

import com.bancoazteca.big.security.utils.Ecies;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;


public class App {
    private static final Logger logger = LoggerFactory.getLogger(App.class);
    public static void main(String[] args) {
        Ecies ecies = new Ecies();
        
        System.out.println("Hello World!");
        logger.info("Objeto: {}", ecies);
    }
}

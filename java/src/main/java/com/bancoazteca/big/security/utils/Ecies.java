package com.bancoazteca.big.security.utils;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class Ecies {
    private static final Logger logger = LoggerFactory.getLogger(Ecies.class);
    private String privateKey;
    private String publicKey;
    
    public Ecies() {
        logger.info("Objeto ECIES creado con éxito.");
    }
}

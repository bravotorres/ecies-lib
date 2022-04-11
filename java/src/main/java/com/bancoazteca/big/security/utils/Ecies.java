package com.bancoazteca.big.security.utils;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * Implementation of ECIES to encrypt and decrypt data for BIG APIs & uServices.
 * @author Alejandro Bravo <alejandro.bravo@bancoazteca.com.mx>
 */
public class ECIES {
    private static final Logger logger = LoggerFactory.getLogger(ECIES.class);
    private String privateKey;
    private String publicKey;

    public ECIES() {
        this.privateKey = "";
        this.publicKey = "";
    }
    
    /**
     * 
     * @param privateKey ECIES Private Key in Base64 format.
     * @param publicKey ECIES Public Key in Base64 format.
     */
    public ECIES(String privateKey, String publicKey) {
        this.privateKey = privateKey;
        this.publicKey = publicKey;
    }

    public String getPrivateKey() {
        return privateKey;
    }

    public void setPrivateKey(String privateKey) {
        this.privateKey = privateKey;
    }

    public String getPublicKey() {
        return publicKey;
    }

    public void setPublicKey(String publicKey) {
        this.publicKey = publicKey;
    }
    
    /**
     * 
     * @param message
     * @return
     * @throws Exception 
     */
    public String encrypt(String message) throws Exception {
        try {
            String encrypted;
            
            if(this.publicKey.equals("")) {
                throw new Exception("Can't encrypt your data, 'publicKey' is not defined.");
            }
            encrypted = "";
            return encrypted;
        } catch(Exception e) {
            logger.error(e.getMessage());
            throw e;
        }
    }
    
    /**
     * 
     * @param data
     * @return
     * @throws Exception 
     */
    public String decrypt(String data) throws Exception {
        try {
            if(this.publicKey.equals("")) {
                throw new Exception("Can't encrypt your data, 'publicKey' is not defined.");
            }
            String message;
            message  = "";
            return message;
        } catch(Exception e) {
            logger.error(e.getMessage());
            throw e;
        }
    }

    @Override
    public String toString() {
        return "ECIES{saludo='')";
    }
}

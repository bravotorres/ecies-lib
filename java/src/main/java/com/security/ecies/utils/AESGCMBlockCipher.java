package com.security.ecies.utils;


import org.bouncycastle.crypto.BufferedBlockCipher;
import org.bouncycastle.crypto.CipherParameters;
import org.bouncycastle.crypto.InvalidCipherTextException;
import org.bouncycastle.crypto.engines.AESEngine;
import org.bouncycastle.crypto.modes.GCMBlockCipher;

import javax.crypto.NoSuchPaddingException;
import java.security.NoSuchAlgorithmException;
import java.security.NoSuchProviderException;

/**
 * Auxiliary class to AES GCM Block Tools
 */
public class AESGCMBlockCipher extends BufferedBlockCipher {

    private final GCMBlockCipher internalCipher;

    public AESGCMBlockCipher() throws NoSuchAlgorithmException, NoSuchPaddingException, NoSuchProviderException {
        this.internalCipher = new GCMBlockCipher(new AESEngine());
    }

    @Override
    public void init(boolean forEncryption, CipherParameters params) {
        internalCipher.init(forEncryption, params);
    }

    @Override
    public int getOutputSize(int len) {
        return internalCipher.getOutputSize(len);
    }

    @Override
    public int doFinal(byte[] out, int outOff) throws InvalidCipherTextException {
        return internalCipher.doFinal(out, outOff);
    }

    @Override
    public int processBytes(byte[] in, int inOff, int len, byte[] out, int outOff) {
        return internalCipher.processBytes(in, inOff, len, out, outOff);
    }
}

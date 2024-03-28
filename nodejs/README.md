# ECIES integration module for JavaScript
Adecuation to include a ECIES system for encrypt y decrypt the transission of sensible data with 
finality of increment security, and performance, in uServices and APIs.

## Formats
The Keys, public & private, are generated as a array of bytes in the backend and exposed to the 
clients as a one of two crossed pairs in Hex representation and Base64 string format. 
Similarly, encrypted strings are transmitted in the request body as binary Base64 strings.

## Project
The projecs is initially conceived as a independent node module to describe and test the function, 
but the principal component to encrypt/decrypt with the provided keys is a class `ECIES` in 
`/node/ecies.js` file.


### Dependencies
- `npm`
- `"eciesjs": "^0.3.14"`


### Test
Now, as a simple test you can run this commands:

```shell
$ npm install
$ node index.js
```

Tested in
- OpenSUSE Leap 15.5 x64, with `node v20.10.0`
- Fedora 35 x64, with `node v14.19.1`
- Windows 10 x64, with `node v16.13.0`
- Windows 11 x64, with `node v15.13.0`

##### ToD's: 
- Formal Unit Tests.
- Formalize into TypeScript.
- Package as a _static_ template.
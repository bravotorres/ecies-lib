# ECIES integration module for JavaScript
Adecuation to include a ECIES system for encrypt y decrypt the transission of sensible data with 
finality of increment security, and performance, in uServices and APIs in BancoAzteca.

## Formats
The Keys, public & private, are generated as a array of bytes in the backend and exposed to the 
clients as a one of two crossed pairs in Base64 string format. Similarly, encrypted strings are 
transmitted in the request body as Base64 strings.

## Project
The projecs is initially conceived as a independent node module to describe and test the function, 
but the principal component to encrypt/decrypt with the provided keys is a class `ECIES` in 
`/node/ecies.js` file.


### Dependencies
- `npm` (tested in `node >= 14.x.x`)
- `"eciesjs": "^0.3.14"`


### Test (ToDo) 
The Big ToDo: Unit test.
Now, as a simple test you can run this command in CLI.
- `node index.js`

Tested in
- `Fedora 35 x64` with `node 14.19.1`
- `Windows 10 x64` with `node 16.13.0`
- `Windows 11 x64` with `node 15.13.0`

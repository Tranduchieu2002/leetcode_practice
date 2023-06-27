//
// Created by michael on 23/06/2023.
//

#include "substitution_cipher.h"

int main() {
    substitution_cipher sc = *new substitution_cipher();
    string encodedMessage = sc.encode();
    string decodedMessage = sc.decode(encodedMessage);
    cout << "Encoded Message: " << encodedMessage << endl;
    cout << "Decoded Message: " << decodedMessage << endl;
}
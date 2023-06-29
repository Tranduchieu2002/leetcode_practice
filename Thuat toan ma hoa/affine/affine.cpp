//
// Created by michael on 23/06/2023.
//

#include "affine.h"

int main() {
    affine sc = *new affine();
    string encodedMessage = sc.encode();
    string decodedMessage = sc.decode(encodedMessage);
    cout << "DecodeMessage: " << encodedMessage<< '\n';
    cout << "Encoded Message: " << decodedMessage << endl;
}
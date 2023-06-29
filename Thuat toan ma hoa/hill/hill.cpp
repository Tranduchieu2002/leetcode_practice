//
// Created by michael on 29/06/2023.
//

#include "hill.h"

int main() {
    string encodeString = Hill().encode("HELP");
    string decodeString = Hill().decode(encodeString);

    cout << "encodeString:  " << encodeString << '\n';
    cout << "decodeString:  " << decodeString << '\n';
}
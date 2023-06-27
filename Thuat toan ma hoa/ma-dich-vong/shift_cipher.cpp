//
// Created by michael on 23/06/2023.
//

#include "shift_cipher.h"

int main() {
    string sc_encode = shift_cipher().encode();
    string sc_decode = shift_cipher().decode(sc_encode);
    cout << "sc_encode : " << sc_encode << "   sc_decode:  " << sc_decode;
    return 0;
}
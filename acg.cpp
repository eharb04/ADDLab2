#include <iostream>

using namespace std;
const int T_EDGE = 100; 
const int L_EDGE = 100;
const int HEIGHT = 1000;
const int WIDTH = 1000;

int main() {

    for (int i = 0; i < 50; i++) {
        cout << "if pixelH == " << i * WIDTH / 50 << " and pixelV > " << T_EDGE + HEIGHT/2 -1 << " and pixelV < " << T_EDGE + HEIGHT/2 +1 << ") then " << endl;
        cout << "hatch <= 1;" << endl;
    }
    for (int i = 0; i < 50; i++) {
        cout << "if pixelH > " << L_EDGE + WIDTH/2 + 1 << " and if pixelH < " << L_EDGE + WIDTH/2 - 1 << " and pixelV == " << i * HEIGHT / 50 << ") then " << endl;
        cout << "hatch <= 1;" << endl;
    } 

    return 0;
}
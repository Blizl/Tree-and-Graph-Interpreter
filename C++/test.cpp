#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

int main() {
    unordered_map<char, string> some_map = {{"s","Sunday"}, {"m","monday"}};
    cout << some_map['s'] << endl;
    return 0;
}

#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

enum class Suit { HEARTS, DIAMONDS, CLUBS, SPADES };

struct Card {
    Suit suit;
    int value;

    bool operator<(const Card& oth) const {
        return value < oth.value;
    }

    bool operator==(const Card& oth) const {
        return value == oth.value;
    }
};

istream& operator>>(istream& is,Card& card) {
    string stuff;
    is >> stuff;

    switch(stuff[0]) {
        case '1':
        case '2':
        case '3':
        case '4':
        case '5':
        case '6':
        case '7':
        case '8':
        case '9': {
            card.value = stuff[0] - '0';
        } break;
        case 'T': {
            card.value = 10;
        } break;
        case 'J': {
            card.value = 11;
        } break;
        case 'Q': {
            card.value = 12;
        } break;
        case 'K': {
            card.value = 13;
        } break;
        case 'A': {
            card.value = 14;
        } break;
    }

    switch(stuff[1]) {
        case 'C': {
            card.suit = Suit::CLUBS;
        } break;
        case 'S': {
            card.suit = Suit::SPADES;
        } break;
        case 'D': {
            card.suit = Suit::DIAMONDS;
        } break;
        case 'H': {
            card.suit = Suit::HEARTS;
        } break;
    }

    return is;
}

ostream& operator<<(ostream& os, const Card& card) {
    string repr;
    if(card.value < 10) {
        repr += '0' + card.value;
    }
    else {
        switch(card.value) {
            case 10: {
                repr += "10";
            } break;
            case 11: {
                repr += "Jack";
            } break;
            case 12: {
                repr += "Queen";
            } break;
            case 13: {
                repr += "King";
            } break;
            case 14: {
                repr += "Ace";
            } break;
        }
    }
    repr += " of ";
    switch(card.suit) {
        case Suit::HEARTS:
            repr += "Hearts";
            break;
        case Suit::CLUBS:
            repr += "Clubs";
            break;
        case Suit::DIAMONDS:
            repr += "Diamonds";
            break;
        case Suit::SPADES:
            repr += "Spades";
            break;
    }
    os << repr;
    return os;
}

struct Hand
{
    Card cards[5];
};

istream& operator>>(istream& is, Hand &hand) {
    for(int i = 0; i < 5; ++i) {
        is >> hand.cards[i];
    }
    sort(begin(hand.cards),end(hand.cards));
    return is;
}

ostream& operator<<(ostream& os, const Hand& hand) {
    os << hand.cards[0] << "; ";
    os << hand.cards[1] << "; ";
    os << hand.cards[2] << "; ";
    os << hand.cards[3] << "; ";
    os << hand.cards[4];
    return os;
}

int main() {

    ifstream in("poker.txt");

    for(int i = 0; i < 2; ++i) {
        Hand player1,player2;
        in >> player1 >> player2;
        cout << player1 << '\n' << player2;
        cout << "\n\n";
    }
    
    return 0;
}
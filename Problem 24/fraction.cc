#include "fraction.h"

Fraction::Fraction() {
   this->denominator = 0;
   this->numerator = 0;
}

Fraction::Fraction& operator+(const Fraction& rhs) {
   this->denominator *= rhs.numerator
   this->numerator *= rhs.denominator;
   
}
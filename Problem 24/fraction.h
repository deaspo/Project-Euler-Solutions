class Fraction {
public:
   Fraction();
   Fraction& operator+(const Fraction& rhs);
private:
   void reduce();
   int denominator;
   int numerator;
};
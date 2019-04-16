#ifndef DATE_ARITH_CALC
#define DATE_ARITH_CALC
// Relays to the program how many days are in the given month.               
struct date{ // Struct that will be used to hold in the date 'object'          
  short int month;
  short int day;
  short int year;
};

int daysInMonth(int monthInQuestion, int yearInQuestion);
bool isLeapYear(const int &inputYear);
void runDateArith(void);
int getDaysLeftInYear(const date &start, const date &end);
int daysSpanInYear(const date &startDate, const date &endDate);




#endif // DATE_ARITH_CALC

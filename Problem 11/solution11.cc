#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;
void loadFile(unsigned int grid[20][20]);

int main() {
   int r, k;
   unsigned int grid[20][20], prod, best[3];
   best[0] = best[1] = best[2] = 0;
   loadFile(grid);

   /* Try all rows */
   for (r = 0; r < 20; r++) {
      for (k = 0; k < 17; k++) {
         prod = grid[r][k]*grid[r][k + 1]*grid[r][k + 2]*grid[r][k + 3];
         best[0] = (prod > best[0]) ? prod : best[0];
      }
   }

   /* Try all columns */
   for (k = 0; k < 20; k++) {
      for (r = 0; r < 17; r++) {
         prod = grid[r][k]*grid[r + 1][k]*grid[r + 2][k]*grid[r + 3][k];
         best[1] = (prod > best[1]) ? prod : best[1];
      }
   }

   /* Try all diagonals from bottom left to top right */
   for (r = 0; r < 17; r++) {
      for (k = 0; k < 17 ; k++) {
         prod = grid[r][k]*grid[r + 1][k + 1]*grid[r + 2][k + 2]*grid[r + 3][k + 3];
         best[2] = (prod > best[2]) ? prod : best[2];
      }
   }
   for (r = 3; r < 17; r++) {
      for (k = 0; k < 17 ; k++) {
         prod = grid[r][k]*grid[r - 1][k + 1]*grid[r - 2][k + 2]*grid[r - 3][k + 3];
         best[2] = (prod > best[2]) ? prod : best[2];
      }
   }


   cout << "Highest product, row wise is " << best[0] << endl;
   cout << "Highest product, column wise is " << best[1] << endl;
   cout << "Highest product, diagonally is " << best[2] << endl;
   cout << "Hence the highest is " << max(max(best[0],best[1]),best[2]) << endl;
   
   return EXIT_SUCCESS;
}

void loadFile(unsigned int grid[20][20]) {
   int i, r, k;
   char *end, c, val[2];

   ifstream inFile;
   inFile.open("grid.txt");
   if (!inFile.is_open()) {
      cout << "Error! File cannot be opened!" << endl;
      exit(EXIT_FAILURE);
   }
   else {
      i = r = k = 0;
      while (inFile.get(c)) {
         if (c != ' ' and c != '\n') {
            val[i] = c;
            i++;
         }
         else {
            grid[r][k] = atoi(val);
            k = (c == ' ') ? k + 1 : 0;
            r = (c == '\n') ? r + 1 : r;
            i = 0;
         }
      }
      inFile.close();
   }

}

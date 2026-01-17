#include <iostream>  
using namespace std;  

int total_moves = 0;  // Global counter to track the total number of moves

// Function to perform a move and print it, also increments the move counter
void pm(int start, int end) {
    total_moves++;  // Increment the total moves counter
    cout << start << " -> " << end << endl;  // Print the move from start peg to end peg
}

// Recursive function to solve Tower of Hanoi problem
// Moves n disks from start peg to end peg using a third auxiliary peg
void hanoi(int n, int start, int end) {
    if (n == 1) {
        // Base case: If only one disk, move it directly
        pm(start, end);
    } else {
        // Recursive case: Calculate the auxiliary peg (1+2+3=6, so other = 6 - start - end)
        int other = 6 - (start + end);
        // Step 1: Move n-1 disks from start to auxiliary peg
        hanoi(n - 1, start, other);
        // Step 2: Move the nth disk from start to end peg
        pm(start, end);
        // Step 3: Move n-1 disks from auxiliary peg to end peg
        hanoi(n - 1, other, end);
    }
}

int main() {
    // Solve Tower of Hanoi for 3 disks, moving from peg 1 to peg 3
    hanoi(3, 1, 3);
    // Print the total number of moves made
    cout << "Total moves: " << total_moves << endl;
    return 0;
}

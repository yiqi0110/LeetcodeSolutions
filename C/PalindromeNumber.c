// Given an integer x, return true if x is a , and false otherwise.

bool isPalindrome(int x){
    if (x < 0) {
        return false;
    }

    // Find the number of digits in the number
    int length = 0;
    int xCopy = x;
    while (xCopy > 0) {
        ++length;
        xCopy /= 10;
    }    

    // Now that we have the length of the number
    // We reverse it
    xCopy = x;
    int new = 0;
    while (length > 0) {
        new += (pow((float) 10, length-1) * (xCopy%10));
        xCopy /= 10;
        --length;
    }

    return (x == new);
}

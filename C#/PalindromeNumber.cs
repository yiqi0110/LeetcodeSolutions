// Given an integer x, return true if x is a , and false otherwise.

public class Solution {
    public bool IsPalindrome(int x) {
        if (x < 0) {
            return false;
        }

        int tmp = x;
        int place = 0;
        while (tmp > 0) {
            ++place;
            tmp /= 10;
        }
        place = (int) Math.Pow(10, place-1);

        int copyX = x;
        int pal = 0;
        while (x > 0) {
            pal += (x%10)*place;
            place /= 10;
            x /= 10;
        }

        return pal==copyX;
    }
}

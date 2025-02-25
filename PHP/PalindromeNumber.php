<!-- Given an integer x, return true if x is a , and false otherwise. -->

class Solution {
    /**
     * @param Integer $x
     * @return Boolean
     */
    function isPalindrome($x) {
        if ($x < 0) {
            return false;
        }

        if ($x < 10) {
            return true;
        }

        $cp = $x;
        $arr = [];
        $backwards = 0;
        $place = 1;

        while ($cp > 0) {
            $arr[] = ($cp % 10);
            $cp = floor($cp / 10);
            if ($cp == 0) {
                break;
            }
        }

        for ($i = count($arr)-1; $i > -1; $i--) {
            $backwards += ($place * $arr[$i]);
            $place *= 10;
        }

        return $x == $backwards;
    }
}
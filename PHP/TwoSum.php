class Solution {

    /**
    * @param Integer[] $nums
    * @param Integer $target
    * @return Integer[]
    */
    function twoSum($nums, $target) {
        #Brute force methodology
        for ($i = 0; $i < count($nums); $i++) {
            for ($j = 0; $j < count($nums); $j++) {
                if ($i != $j) {
                    if ($nums[$i] + $nums[$j] == $target) {
                        return [$i, $j];
                    }
                }
            }
        }
    }
}
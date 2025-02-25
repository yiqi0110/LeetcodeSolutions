/*
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
*/

public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> map = new Dictionary<int, int>();
        int[] result = new int[2];
        for (int i = 0; i < nums.Length; i++) {
            int complement = target - nums[i];
            if (map.ContainsKey(complement)) {
                result[0] = map[complement];
                result[1] = i;
                return result;
            }
            map[nums[i]] = i;
        }
        return result;
    }
}


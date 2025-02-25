/*
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
*/

func twoSum(nums []int, target int) []int {
    bank := make(map[int]int)
    for i, num := range nums {
        compliment := target - num
        complimentIndex, found := bank[compliment]
        if found {
            return []int{i, complimentIndex}
        } else {
            bank[num] = i
        }
    }

    return make([]int,0)
}

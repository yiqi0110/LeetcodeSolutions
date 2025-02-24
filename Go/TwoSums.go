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

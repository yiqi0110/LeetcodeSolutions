/**
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 */
 import "fmt"

 func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	 tmpNode := &ListNode{}
	 tmpList := tmpNode
	 remainder := 0
 
	 for l1 != nil || l2 != nil {
		 tmpNode.Next = &ListNode{}
		 tmpNode = tmpNode.Next
		 sum := remainder
		 fmt.Println("remainder: ", remainder)
 
		 if l1 != nil {
			 fmt.Println("l1 value: ", l1.Val)
			 sum += l1.Val
			 l1 = l1.Next
		 }
		 if l2 != nil {
			 fmt.Println("l2 value: ", l2.Val)
			 sum += l2.Val
			 l2 = l2.Next
		 }
 
		 remainder = sum / 10
		 tmpNode.Val = sum % 10
		 
	 }
 
	 if remainder == 1 {
		 tmpNode.Next = &ListNode{1, nil}
	 }
 
	 return tmpList.Next
 }
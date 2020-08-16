// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
//
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn insertion_sort_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut head = head;
        let mut new_head = ListNode::new(0);
        while let Some(mut boxed) = head.take() {
            head = boxed.next.take();
            let mut ptr = &mut new_head;
            while ptr.next.as_ref().is_some() && ptr.next.as_ref().unwrap().val < boxed.val {
                ptr = ptr.next.as_mut().unwrap();
            }
            boxed.next = ptr.next.take();
            ptr.next = Some(boxed);
        }
        new_head.next
    }
}

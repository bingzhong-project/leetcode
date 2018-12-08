/**
 * Definition for singly-linked list.
 */
 class ListNode {
     int val;
     ListNode next;
     ListNode(int x) {
         val = x;
         next = null;
     }
 }

 public class Solution {

    public ListNode detectCycle(ListNode head) {
        ListNode slowPoint = head;
        ListNode fastPoint = head;
        ListNode meetNode = null;
        while(fastPoint != null && fastPoint.next != null) {
            slowPoint = slowPoint.next;
            fastPoint = fastPoint.next.next;
            if(slowPoint == fastPoint) {
                meetNode = slowPoint;
                break;
            }
        }
    
        ListNode entrance = head;
        while(meetNode != null) {
            if(meetNode == entrance) {
                return entrance;
            }
            meetNode = meetNode.next;
            entrance = entrance.next;
        }

        return null;
    }
}
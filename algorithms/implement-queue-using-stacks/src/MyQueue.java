import java.util.Stack;

class MyQueue {

    private Stack<Integer> stack1;

    private Stack<Integer> stack2;

    /** Initialize your data structure here. */
    public MyQueue() {
        stack1 = new Stack<>();
        stack2 = new Stack<>();
    }

    /** Push element x to the back of queue. */
    public void push(int x) {
        if (stack2.isEmpty()) {
            stack2.push(x);
        } else {
            stack1.push(x);
        }
    }

    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
        int res = stack2.pop();
        while(!stack1.isEmpty()) {
            int val = stack1.pop();
            if(stack1.isEmpty()) {
                stack1.push(val);
                break;
            } else {
                stack2.push(val);
            }
        }

        Stack<Integer> temp = stack1;
        stack1 = stack2;
        stack2 = temp;

        return res;
    }

    /** Get the front element. */
    public int peek() {
        return stack2.peek();
    }

    /** Returns whether the queue is empty. */
    public boolean empty() {
        return stack2.isEmpty();
    }
}
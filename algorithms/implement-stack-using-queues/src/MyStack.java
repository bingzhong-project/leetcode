import java.util.ArrayDeque;
import java.util.Queue;

class MyStack {

    private Queue<Integer> queue1;

    private Queue<Integer> queue2;

    /** Initialize your data structure here. */
    public MyStack() {
        queue1 = new ArrayDeque<>();
        queue2 = new ArrayDeque<>();
    }

    /** Push element x onto stack. */
    public void push(int x) {
        if (queue2.isEmpty()) {
            queue2.offer(x);
        } else {
            queue1.offer(queue2.poll());
            queue2.offer(x);
        }
    }

    /** Removes the element on top of the stack and returns that element. */
    public int pop() {
        int res = queue2.poll();
        while (!queue1.isEmpty()) {
            int val = queue1.poll();
            if (queue1.isEmpty()) {
                queue1.offer(val);
                break;
            } else {
                queue2.offer(val);
            }
        }
        Queue<Integer> temp = queue1;
        queue1 = queue2;
        queue2 = temp;

        return res;
    }

    /** Get the top element. */
    public int top() {
        return queue2.peek();
    }

    /** Returns whether the stack is empty. */
    public boolean empty() {
        return queue2.isEmpty();
    }
}
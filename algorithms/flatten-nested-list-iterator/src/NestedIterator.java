import java.util.List;
import java.util.Stack;

/**
 * // This is the interface that allows for creating nested lists. // You should
 * not implement it, or speculate about its implementation
 */
public interface NestedInteger {

    // @return true if this NestedInteger holds a single integer, rather than a
    // nested list.
    public boolean isInteger();

    // @return the single integer that this NestedInteger holds, if it holds a
    // single integer
    // Return null if this NestedInteger holds a nested list
    public Integer getInteger();

    // @return the nested list that this NestedInteger holds, if it holds a nested
    // list
    // Return null if this NestedInteger holds a single integer
    public List<NestedInteger> getList();
}

public class NestedIterator implements Iterator<Integer> {

    private Stack<NestedInteger> stack;

    public NestedIterator(List<NestedInteger> nestedList) {
        stack = new Stack<>();
        for (int i = nestedList.size() - 1; i >= 0; i--) {
            stack.add(nestedList.get(i));
        }
    }

    @Override
    public Integer next() {
        return stack.pop().getInteger();
    }

    @Override
    public boolean hasNext() {
        flatten();
        return !stack.isEmpty();
    }

    private void flatten() {
        if (stack.isEmpty() || stack.peek().isInteger()) {
            return;
        }
        List<NestedInteger> nestedList = stack.pop().getList();
        for (int i = nestedList.size() - 1; i >= 0; i--) {
            if (!nestedList.get(i).isInteger() && nestedList.get(i).getList().size() == 0) {
                continue;
            }
            stack.add(nestedList.get(i));
        }
        flatten();
    }
}

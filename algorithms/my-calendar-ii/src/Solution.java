import java.util.TreeMap;

class MyCalendarTwo {

    private TreeMap<Integer, Integer> treeMap = new TreeMap<>();

    public boolean book(int start, int end) {
        treeMap.put(start, treeMap.getOrDefault(start, 0) + 1);
        treeMap.put(end, treeMap.getOrDefault(end, 0) - 1);

        int cnt = 0;
        for (int value : treeMap.values()) {
            cnt += value;
            if (cnt >= 3) {
                treeMap.put(start, treeMap.get(start) - 1);
                treeMap.put(end, treeMap.get(end) + 1);
                return false;
            }
        }

        return true;
    }
}

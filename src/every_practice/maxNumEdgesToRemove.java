import java.util.Arrays;
import java.util.Comparator;

class UnionFound {
    private int[] parent;
    private int[] size;
    private int setCount;

    public UnionFound(int n) {
        parent = new int[n];
        size = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
        setCount = n;
    }

    public boolean unite(int x, int y) {
        int swap;
        x = find(x);
        y = find(y);
        if (x == y) {
            return false;
        }
        if (size[x] < size[y]) {
            swap = x;
            x = y;
            y = swap;
        }
        parent[y] = x;
        size[x] += size[y];
        setCount--;
        return true;

    }

    public int find(int x) {
        if (x == parent[x]) {
            return x;
        }
        parent[x] = find(parent[x]);
        return parent[x];
    }

    public boolean connected(int x, int y) {
        return find(x) == find(y);
    }

    public int getSetCount() {
        return setCount;
    }
}

class Solution {
    public int maxNumEdgesToRemove(int n, int[][] edges) {
//        Arrays.sort(edges, (o1, o2) -> Integer.compare(o2[0], o1[0]));
        UnionFound u1 = new UnionFound(n);
        UnionFound u2 = new UnionFound(n);
        int ans = 0;
        for (int[] x : edges) {
            if (x[0] == 3) {
                if (!u1.unite(x[1] - 1, x[2] - 1)) {
                    ++ans;
                } else {
                    u2.unite(x[1] - 1, x[2] - 1);
                }
            }
        }
        for (int x[] : edges) {
            if (x[0] == 2) {
                if (!u1.unite(x[1] - 1, x[2] - 1)) {
                    ++ans;
                }
            } else  {
                if (!u2.unite(x[1] - 1, x[2] - 1)) {
                    ++ans;
                }
            }
        }
        if (u1.getSetCount() != 1 || u2.getSetCount() != 1) {
            return -1;
        }
        return ans;
    }
}

class maxNumEdgesToRemove {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.maxNumEdgesToRemove(4, new int[][]{{3, 1, 2}, {3, 2, 3}, {1, 1, 3}, {1, 2, 4}, {1, 1, 2}, {2, 3, 4}}));
        System.out.println(s.maxNumEdgesToRemove(4, new int[][]{{3, 1, 2}, {3, 2, 3}, {1, 1, 4}, {2, 1, 4}}));
        System.out.println(s.maxNumEdgesToRemove(4, new int[][]{{3, 2, 3}, {1, 1, 2}, {2, 3, 4}}));
    }
}
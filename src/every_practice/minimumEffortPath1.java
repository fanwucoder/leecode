import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class minimumEffortPath1 {

    class Solution {
        private List<Map<Integer,Integer>> ret_cache = null;

        public int minimumEffortPath(int[][] heights) {
            int[][] path = new int[heights.length][];
            ret_cache = new ArrayList<>(heights.length);
            for (int i = 0; i < heights.length; i++) {
                path[i] = new int[heights[i].length];
                ret_cache.add( new HashMap<Integer,Integer>());
            }
            return minimumEffortPath(0, 0, heights, path, 0,-2);
        }

        int minimumEffortPath(int i, int j, int[][] heights, int[][] path, int last,int from) {
            // System.out.println("----");
            // System.out.println(heights.length);
            // System.out.println(heights[i].length);
            // System.out.println("----");
            int min = Integer.MAX_VALUE;
            int k=(from+1)*(j+1);
            if (i == heights.length - 1 && j == heights[heights.length - 1].length - 1) {
                return last;
            }
            if (ret_cache.get(i).getOrDefault(k,null) != null) {
                return ret_cache.get(i).get(k);
            }
            if (i - 1 >= 0 && path[i - 1][j] == 0) {

                min = Math.min(min, get_direct(i, j, heights, path, last, 0));
            }
            if (j + 1 < heights[i].length && path[i][j + 1] == 0) {

                min = Math.min(min, get_direct(i, j, heights, path, last, 1));
            }

            if (i + 1 < heights.length && path[i + 1][j] == 0) {

                min = Math.min(min, get_direct(i, j, heights, path, last, 2));
            }
            if (j - 1 > 0 && path[i][j - 1] == 0) {

                min = Math.min(min, get_direct(i, j, heights, path, last, 3));
            }

            ret_cache.get(i).put(k, Math.max(min, last));
            return ret_cache.get(i).get(k);

        }

        int get_direct(int i, int j, int[][] heights, int[][] path, int last, int direct) {
            int i1 = i, j1 = j;
            if (direct == 0) {
                i1 = i - 1;
            } else if (direct == 1) {
                j1 = j + 1;
            } else if (direct == 2) {
                i1 = i + 1;
            } else {
                j1 = j - 1;
            }
            int a = Math.abs(heights[i][j] - heights[i1][j1]);
            int h1 = Math.max(a, last);
            System.out.println(String.format("%d,%d,%d,%d:%d",i,j,i1,j1,h1));
            path[i1][j1] = 1;
            int ret = minimumEffortPath(i1, j1, heights, path, h1,direct);
            path[i1][j1] = 0;
            return ret;
        }
    }

    public static void main(String[] args) {
        minimumEffortPath1 s1 = new minimumEffortPath1();

        Solution s = s1.new Solution();
        // System.out.println(s.minimumEffortPath(new int[][] { { 1, 2, 2 }, { 3, 8, 2 }, { 5, 3, 5 } }));
        // System.out.println(s.minimumEffortPath(new int[][] { { 1, 2, 3 }, { 3, 8, 4 }, { 5, 3, 5 } }));
        System.out.println(s.minimumEffortPath(new int[][] { { 1, 2, 1, 1, 1 }, { 1, 2, 1, 2, 1 }, { 1, 2, 1, 2, 1 },
                { 1, 2, 1, 2, 1 }, { 1, 1, 1, 2, 1 } }));

    }
}
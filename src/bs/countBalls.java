import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class countBalls {
    class Solution {
        public int countBalls(int lowLimit, int highLimit) {
            Map<Integer,int[]> ret = new HashMap<>();
            int key = 0;
            for (int i = lowLimit; i <= highLimit; i++) {
                key = getNum(i);
                int [] last=ret.getOrDefault(key, new int[] { key, 0});
                last[1] = last[1] + 1;
                
                ret.put(key, last);
            }
            List<int[]> ret1=new ArrayList<>(ret.values());
            ret1.sort((o1, o2) -> Integer.compare(o2 == null ? 0 : o2[1], o1 == null ? 0 : o1[1]));
            
            return ret1.get(0)[1];
        }

        int getNum(int x) {
            int sum = 0;
            while (x != 0) {
                sum += x % 10;
                x = x / 10;
            }
            return sum;
        }
    }

    public static void main(String[] args) {
        countBalls c = new countBalls();
        Solution s = c.new Solution();
        System.out.println(s.countBalls(1, 10));
        System.out.println(s.countBalls(5, 15));
        System.out.println(s.countBalls(19, 28));
    }
}

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;

import java.util.Map;
import java.util.Set;



public class restoreArray {
    class Solution {
        public int[] restoreArray(int[][] adjacentPairs) {
            Map<Integer, Set<Integer>> range = new HashMap<>();
            for (int[] temp : adjacentPairs) {
                Set<Integer> a = range.getOrDefault(temp[0], new HashSet<Integer>());
                if (!a.contains(temp[1])) {
                    a.add(temp[1]);
                }

                range.put(temp[0], a);
                a = range.getOrDefault(temp[1], new HashSet<Integer>());
                if (!a.contains(temp[0]))
                    a.add(temp[0]);
                range.put(temp[1], a);
            }
            int[] ret = new int[adjacentPairs.length + 1];
            int i = 1;
            ret[0] = adjacentPairs[0][0];
            ret[1]=adjacentPairs[0][1];
            for(int x:ret)
            System.out.println(x);
            System.out.println("xxx");
            while (true) {
                Set<Integer> p=range.get(ret[i]);
                if(p==null)
                    break;
                range.remove(ret[i]);
                for (Integer m : p) {
                    if(m!=ret[i]){
                        i=i+1;
                        ret[i]=m;
                    }   
                }
                for(int x:ret)
                System.out.println(x);
                System.out.println("xxx");
                
            }
            return null;
           
        }
      
    }

    public static void main(String[] args) {
        restoreArray a=new restoreArray();
        Solution s=a.new Solution();
        System.out.println(s.restoreArray(new int[][]{{4,-2},{1,4},{-3,1}}));
    }
}

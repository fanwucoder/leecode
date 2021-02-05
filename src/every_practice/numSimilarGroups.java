import java.util.Arrays;

/*839. 相似字符串组
*/
public class numSimilarGroups {
    class UnionFind {
        int[] parent;
        int[] size;
        int n;
        // 当前连通分量数目
        int setCount;

        public UnionFind(int n) {
            this.n = n;
            this.setCount = n;
            this.parent = new int[n];
            this.size = new int[n];
            Arrays.fill(size, 1);
            for (int i = 0; i < n; ++i) {
                parent[i] = i;
            }
        }

        public int findset(int x) {
            return parent[x] == x ? x : (parent[x] = findset(parent[x]));
        }

        public boolean unite(int x, int y) {
            x = findset(x);
            y = findset(y);
            if (x == y) {
                return false;
            }
            if (size[x] < size[y]) {
                int temp = x;
                x = y;
                y = temp;
            }
            parent[y] = x;
            size[x] += size[y];
            --setCount;
            return true;
        }

        public boolean connected(int x, int y) {
            x = findset(x);
            y = findset(y);
            return x == y;
        }
    }
    
    class Solution {
        public int numSimilarGroups(String[] strs) {
            UnionFind uf=new UnionFind(strs.length);
            for (int i = 0; i < strs.length; i++) {
                for (int j = i + 1; j < strs.length; j++) {
                    boolean ret=isSimilar(strs[i], strs[j]);
                        if(ret){
                            uf.unite(i, j);
                        }
                        System.out.println(String.format("%s,%s,%s", strs[i],strs[j],ret));
                }
            }
            return uf.setCount;
        }

        private boolean isSimilar(String s1,String s2){
     
            int diff=0;
            for(int i=0;i<s1.length();i++){
                    if(s1.charAt(i)!=s2.charAt(i)){
              
                        diff++;
                    }

                    if(diff>2)
                    return false;
                    
            }
           
            return true;
        }
    }
    public static void main(String[] args) {
        numSimilarGroups n=new numSimilarGroups();
        Solution s1=n.new Solution();
        // System.out.println(s1.numSimilarGroups(new String[] {"tars","rats","arts","star"}));
        // System.out.println(s1.numSimilarGroups(new String[] {"omv","ovm"}));
        System.out.println(s1.numSimilarGroups(new String[] {"jvhpg","jhvpg","hpvgj","hvpgj","vhgjp"}));
        
    }

}

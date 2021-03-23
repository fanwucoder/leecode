package leetcode.editor.cn;

//给你一个嵌套的整型列表。请你设计一个迭代器，使其能够遍历这个整型列表中的所有整数。 
//
// 列表中的每一项或者为一个整数，或者是另一个列表。其中列表的元素也可能是整数或是其他列表。 
//
// 
//
// 示例 1: 
//
// 输入: [[1,1],2,[1,1]]
//输出: [1,1,2,1,1]
//解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,1,2,1,1]。 
//
// 示例 2: 
//
// 输入: [1,[4,[6]]]
//输出: [1,4,6]
//解释: 通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,4,6]。
// 
// Related Topics 栈 设计 
// 👍 265 👎 0

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class FlattenNestedListIterator1 {
     public static void main(String[] args) {
//          Solution solution = new FlattenNestedListIterator().new Solution();
     
     }

//leetcode submit region begin(Prohibit modification and deletion)

  // This is the interface that allows for creating nested lists.
  // You should not implement it, or speculate about its implementation
  public interface NestedInteger {

      // @return true if this NestedInteger holds a single integer, rather than a nested list.
      public boolean isInteger();

      // @return the single integer that this NestedInteger holds, if it holds a single integer
      // Return null if this NestedInteger holds a nested list
      public Integer getInteger();

      // @return the nested list that this NestedInteger holds, if it holds a nested list
      // Return null if this NestedInteger holds a single integer
      public List<NestedInteger> getList();
  }
public class NestedIterator implements Iterator<Integer> {
    List<NestedInteger> nestedList;
    List<Integer> pos= new ArrayList<>();
    List<List<NestedInteger>> popList;
    public NestedIterator(List<NestedInteger> nestedList) {
        this.nestedList=nestedList;
        if(nestedList.size()>0){
            pos.add(0);
            popList=new ArrayList<>();
            popList.add(nestedList);
            popList();

        }
    }

    @Override
    public Integer next() {
        Integer ret=getLast().getInteger();
        addIdx();
        popList();
        return ret;
    }

    private void popList() {
        while (pos.size()>0){
            Integer lastIdx=pos.size()-1;
            Integer lastPos=pos.get(lastIdx);
            if(lastPos>=popList.get(lastIdx).size()){
                popList.remove(lastIdx.intValue());
                pos.remove(lastIdx.intValue());
            }else{
                break;
            }
        }
    }

    public void addIdx(){
        int curIdx=pos.size()-1;
        pos.set(curIdx,pos.get(curIdx)+1);
    }
    public NestedInteger getLast(){
        int cur=pos.get(pos.size()-1);
        NestedInteger integer=popList.get(popList.size()-1).get(cur);
        return integer;
    }
    private void pushList(NestedInteger nestedInteger){
        addIdx();
        pos.add(0);
        popList.add(nestedInteger.getList());

    }
    @Override
    public boolean hasNext() {
        while (pos.size()>0){
            NestedInteger integer=getLast();
            if(integer.isInteger()){
                return true;
            }
            if(integer.getList().size()>0){
                pushList(integer);
            }else {
                addIdx();
            }
            popList();
        }
        return false;
    }
}

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i = new NestedIterator(nestedList);
 * while (i.hasNext()) v[f()] = i.next();
 */
//leetcode submit region end(Prohibit modification and deletion)

}
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
// 👍 267 👎 0

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class FlattenNestedListIterator{
     public static void main(String[] args) {
//          Solution solution = new FlattenNestedListIterator().new Solution();
     
     }

//leetcode submit region begin(Prohibit modification and deletion)
public interface NestedInteger {

    // @return true if this NestedInteger holds a single integer, rather than a nested list.
    public boolean isInteger();

    // @return the single integer that this NestedInteger holds, if it holds a single integer
    // Return null if this NestedInteger holds a nested list
    public Integer getInteger();

    // @return the nested list that this NestedInteger holds, if it holds a nested list
    // Return null if this NestedInteger holds a single integer
    public List<FlattenNestedListIterator.NestedInteger> getList();
}
public class NestedIterator implements Iterator<Integer> {
    private List<Integer> integers=new ArrayList<>();
    private Iterator<Integer> integerIterator;
    public NestedIterator(List<NestedInteger> nestedList) {
        for (NestedInteger x :                nestedList) {
            flatten(integers,x);
        }
        integerIterator=integers.iterator();
    }

    @Override
    public Integer next() {
        return integerIterator.next();
    }
    private void flatten(List<Integer> integers, NestedInteger x) {
        if(x.isInteger()){
            integers.add(x.getInteger());
        }else {
            for (NestedInteger y:x.getList()) {
                flatten(integers,y);
            }
        }
    }
    @Override
    public boolean hasNext() {
        return integerIterator.hasNext();
    }
}



/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i = new NestedIterator(nestedList);
 * while (i.hasNext()) v[f()] = i.next();
 */
//leetcode submit region end(Prohibit modification and deletion)

}
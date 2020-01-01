//
// Created by fanwu on 2020/1/1.
//

#ifndef LEECODE_COMMON_H
#define LEECODE_COMMON_H

#include <stack>
#include <iostream>

using namespace std;

template<typename T>
void preOrder(T *root) {
    stack<T *> s;
    T *p = root;
    while (!s.empty() || p != NULL) {
        if (p != NULL) {
            cout << p->val;
            s.push(p);
            p = p->left;
        } else {
            p = s.top();
            s.pop();
            p = p->right;
        }
    }
}


template<typename T>
T *ArrToTree(int *arr, int len, T *a) {
    T *pRoot = NULL;
    int i;


    //创建结构体数组
    pRoot = new T[len];
    if (NULL == pRoot) {
        printf("pRoot空间分配失败！\n");
        exit(-1);
    }

    //结构体数组赋初值
    for (i = 0; i < len; ++i) {
        pRoot[i].val = arr[i];
        pRoot[i].left = NULL;
        pRoot[i].right = NULL;
    }

    //父亲节点与左右孩子关联
    for (i = 0; i <= len / 2 - 1; ++i) {
        //有左孩子
        if (2 * i + 1 < len) {
            pRoot[i].left = &pRoot[2 * i + 1];
        }

        //有右孩子
        if (2 * i + 2 < len) {
            pRoot[i].right = &pRoot[2 * i + 2];
        }
    }

    return pRoot;
}

template<typename T>
T *
creatBTree(int **data, int index, T *a) {
    T *pNode = NULL;
    int len = sizeof(data) - 1;
    if (index < len) {
        if (data[index] == NULL)
            return NULL;
        pNode = new T(*data[index]);
        pNode->left = creatBTree(data, 2 * index + 1, a);
        pNode->right = creatBTree(data, 2 * index + 2, a);

    }
    return pNode;

}

template<typename T>
void PrevOrderTraversal(T *pRoot) {
    if (NULL == pRoot) {
        return;
    }

    printf("%d ", pRoot->val);
    PrevOrderTraversal(pRoot->left);
    PrevOrderTraversal(pRoot->right);
}
//
//int main(void)
//{
//    BiTree * pRoot = NULL;
//
//    int arr[] = {1, 2, 3, 4, 5, 6, 7};
//    int len = sizeof(arr)/sizeof(arr[0]);
//    pRoot = ArrToBiTree(arr, len);
//    PrevOrderTraversal(pRoot);
//
//    return 0;
//}
#endif //LEECODE_COMMON_H

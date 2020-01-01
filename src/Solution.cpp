//
// Created by admin on 2019/12/26.
//

#include "Solution.h"
#include <iostream>


using namespace std;
int myAtoi::Solution::myAtoi(string str) {
    unsigned long long int size=str.size();
    int flag=1;
    long long ret=0;
    int i=0;
    for (; i < size&&str[i]==' '; ++i);
    if(i<size){
        if(str[i]=='+'){flag=1;i++;}
        else if(str[i]=='-'){flag=-1;i++;}
    }


    for (; i < size; ++i) {

        if (str[i]<'0' || str[i]>'9'){
            break;
        }

        ret=ret*10+(str[i]-'0')*flag;
//        cout<<ret<<endl;
        if(ret>=INT_MAX){
            return INT_MAX;
        }
        if(ret<=INT_MIN )
            return INT_MIN;
    }
    return static_cast<int>(ret);
}

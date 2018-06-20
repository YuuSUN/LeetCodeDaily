# LeetCodeDaily
## Menu 目录
- [Problem Set](https://github.com/vivi3nli/LeetCodeDaily#problem-set-%E6%AF%8F%E6%97%A5%E4%B8%80%E9%A2%98)

Week| Mon | Tue | Wed | Thu | Fri | Sat | Sun  
:-: | :-: | :-: | :-: | :-: | :-: | :-: | :-:
24  | | [394](https://github.com/vivi3nli/LeetCodeDaily#20180612%E9%A2%98%E7%9B%AE) | [43](https://github.com/vivi3nli/LeetCodeDaily#20180613%E9%A2%98%E7%9B%AE)|[15](https://github.com/vivi3nli/LeetCodeDaily#2018614%E9%A2%98%E7%9B%AE)|[51](https://github.com/vivi3nli/LeetCodeDaily#20180615%E9%A2%98%E7%9B%AE51-n-queens)|[1](https://github.com/vivi3nli/LeetCodeDaily#201806161-two-sum)||
25|[46](https://github.com/vivi3nli/LeetCodeDaily#2018061846-permutations)

- [My Solutions](https://github.com/vivi3nli/LeetCodeDaily#my-leetcoding-solutions-%E6%88%91%E7%9A%84%E8%A7%A3%E7%AD%94)
- [Group Members](https://github.com/vivi3nli/LeetCodeDaily#group-members-%E5%AD%A6%E4%B9%A0%E5%B0%8F%E7%BB%84%E6%88%90%E5%91%98)
- [References](https://github.com/vivi3nli/LeetCodeDaily#references-%E5%8F%82%E8%80%83%E8%B5%84%E6%96%99)
- [Rules](https://github.com/vivi3nli/LeetCodeDaily#%E6%AF%8F%E6%97%A5leetcode%E6%B4%BB%E5%8A%A8%E8%A7%84%E5%88%99)

## Problem Set 每日一题
### 【2018/06/12题目】[394. Decode String](https://leetcode.com/problems/decode-string/description/)

- 题目类型 #simulation
- 第一天我们来一道摸底题吧，不是太难，也不是two sum那么简单

### 【2018/06/13题目】[43. Multiply Strings](https://leetcode.com/problems/multiply-strings/description/)

- 题目类型 #高精度计算
- 不可以使用Java内置的BigInt。
- 建议大家用C或者C++写，这题比较合适给大家做C cpp练手
- 【可以先做这道练练手】[66. Plus One](https://leetcode.com/problems/plus-one/description/)
- 思路参考 [浙江大学SCL 高精度计算章-大数](https://wenku.baidu.com/view/a3a9373b31126edb6f1a10af.html?rec_flag=default&sxts=1528822472490) leetcode大部分的题都能在这个小手册里找到思路
- 附 [楼教主十几年前出的男人八题](https://wenku.baidu.com/view/1de9e435ee06eff9aef80734.html?sxts=1528823190178)

### 【2018/6/14题目】[15. 3Sum](https://leetcode.com/problems/3sum/description/)

- 我们来一道经典面试题threesome吧
- python中list对象的存储结构采用的是线性表，因此其查询复杂度为O(n),而dict对象的存储结构采用的是散列表(hash表)，其在最优情况下查询复杂度为O(1)。

### 【2018/06/15题目】[51. N-Queens](https://leetcode-cn.com/problems/n-queens/description/)

- 题目类型 #N皇后 
- 在建立棋盘的时候用乘法可能会导致棋牌某一列均相同，因为在python中复杂类型是浅拷贝、简单类型是深拷贝
- 在棋盘中确认是否重复时，从左上到右下的一斜行坐标差值相同，右上到左下的一斜行坐标和相同，所以可以用这一数值统一标记，无需单个确认。（在非常大的棋盘时可能会加快速度？）

### 【2018.06.16】[1. Two Sum](https://leetcode.com/problems/two-sum/description/)

- 附加要求：虽然比3sum简单，但请大家实现尽可能快的版本，最快的人将会获得一笔bonus奖金（数额保密）

### 【20180618】[46. Permutations](https://leetcode.com/problems/permutations/description/)

- 全排列
- 全排列那个可以就用回溯做，递归n层，每层在前面诸层中未选择的数字集合中选择candidate，选好了就进入下一层。各层share一个全局的长度为n的布尔数组，来标记每个数字是否被使用

### 【2018/06/19】[]https://leetcode-cn.com/problems/merge-two-sorted-lists/description/

- 类型：#合并链表
- 大二作业题，不能更水了

【2018/06/20】https://leetcode.com/problems/factorial-trailing-zeroes/description/

- 阶乘最末0


## My LeetCoding Solutions 我的解答
- 2018/6/12 [394. Decode String Solution](https://github.com/vivi3nli/LeetCodeDaily/blob/master/394_Decode_String_20180612.py)
- 2018/6/13 [66. Plus One Solution](https://github.com/vivi3nli/LeetCodeDaily/blob/master/66_Plus_One_20180613.py) and [43. Multiply Strings Solutions](https://github.com/vivi3nli/LeetCodeDaily/blob/master/43_Multiply_Strings_20180613.py)
- 2018/6/14 [15. 3Sum Solution](https://github.com/vivi3nli/LeetCodeDaily/blob/master/15_3Sum_20180614.py)
- 2018/6/15 [51. N-Queens Solution](https://github.com/vivi3nli/LeetCodeDaily/blob/master/51_N-Queens_20180615.py)
- 2018/6/16 [1. Two Sum Solution](https://github.com/vivi3nli/LeetCodeDaily/blob/master/1_Two_Sum_20180616.py)
- 2018/6/18 [46. Permutations Solution](https://github.com/vivi3nli/LeetCodeDaily/blob/master/46_Permutations_20180618.py)

## Group Members 学习小组成员

[Gao Haoxiang](https://github.com/pluto-the-lost/LeetCode)

[Chen Wenchang](https://github.com/chenwenchang/Leetcode)

[Li Jiaqi](https://github.com/LiJiaqi96/Play-with-Leetcode)

[Li Fanhong](https://github.com/vivi3nli/LeetCodeDaily)

## References 参考资料

- [短码之美](https://book.douban.com/subject/5416095/)
- [浙江大学SCL](https://wenku.baidu.com/view/a3a9373b31126edb6f1a10af.html?rec_flag=default&sxts=1528822472490)


## 每日Leetcode活动规则

最重要的群规：真诚！真诚！真诚！

- 一、 每人每天上交【10块钱】至会长处，作为刷题鼓励金，会长选择建议的题目。

- 二、刷题奖励金的发放方式：
  - 若所有人都刷题了，第二天会长会把鼓励金返回给大家；刷题完成标准以AC为主，讲不讲得明白作为辅助的主观参考。如果讲不明白，给予major revision或者minor revision的重讲机会。完全讲不出来的，给予rejection处理。
  - 若部分人未刷题，则鼓励金均发给其他运动的会员；
  - 若所有人都未刷题，则鼓励金累积后延，直至出现条件2的情况。
- 三、每晚12：00之前，所有会员把刷题记录截屏发群里，第二天会长根据截屏记录分发红包。希望大家对自己诚实，不要直接粘解题方法，所有刷过的题要能说出解题思路，可以互相考察。
- 四、讲题会活动：每周一下午7pm
- 五、病假制度：每月有3天假期（请假者不收取会费也不参与红包分发），超过3天则每天上交10块会费。
- 六、押金规则：每天中午12点之前，会长会返还昨日押金，会员在领取后顺便上交今日押金，最晚不超过中午12点。已经上交押金后，不能再申请请假。
- 七、退费会用：100块（均分给其他未退群的人）

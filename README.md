# LeetCodeDaily
## Menu 目录
- [Problem Set](https://github.com/vivi3nli/LeetCodeDaily#problem-set-%E6%AF%8F%E6%97%A5%E4%B8%80%E9%A2%98)

Week| Mon | Tue | Wed | Thu | Fri | Sat | Sun  
:-: | :-: | :-: | :-: | :-: | :-: | :-: | :-:
24  | | [394](https://github.com/vivi3nli/LeetCodeDaily#20180612%E9%A2%98%E7%9B%AE) | [43](https://github.com/vivi3nli/LeetCodeDaily#20180613%E9%A2%98%E7%9B%AE)|[15](https://github.com/vivi3nli/LeetCodeDaily#2018614%E9%A2%98%E7%9B%AE)|[51](https://github.com/vivi3nli/LeetCodeDaily#20180615%E9%A2%98%E7%9B%AE51-n-queens)|[1](https://github.com/vivi3nli/LeetCodeDaily#201806161-two-sum)||
25|[46](https://github.com/vivi3nli/LeetCodeDaily#2018061846-permutations)|[21](https://github.com/vivi3nli/LeetCodeDaily#2018061921-merge-two-sorted-lists)|[172](https://github.com/vivi3nli/LeetCodeDaily#20180620172-factorial-trailing-zeroes)|[223](https://github.com/vivi3nli/LeetCodeDaily#20180621223-rectangle-area)|[136](https://github.com/vivi3nli/LeetCodeDaily#2018-06-22136-single-number)|[300](https://github.com/vivi3nli/LeetCodeDaily#2018-06-23300-longest-increasing-subsequence)||
26|[19](https://github.com/vivi3nli/LeetCodeDaily#2018-06-2519-remove-nth-node-from-end-of-list)|[78](https://github.com/vivi3nli/LeetCodeDaily#2018-06-2678-subsets)|[335](https://github.com/vivi3nli/LeetCodeDaily#2018-06-27335-self-crossing)


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

### 【2018/06/15题目】[51. N-Queens](https://leetcode.com/problems/n-queens/description/)

- 题目类型 #N皇后 
- 在建立棋盘的时候用乘法可能会导致棋牌某一列均相同，因为在python中复杂类型是浅拷贝、简单类型是深拷贝
- 在棋盘中确认是否重复时，从左上到右下的一斜行坐标差值相同，右上到左下的一斜行坐标和相同，所以可以用这一数值统一标记，无需单个确认。（在非常大的棋盘时可能会加快速度？）

### 【2018.06.16】[1. Two Sum](https://leetcode.com/problems/two-sum/description/)

- 附加要求：虽然比3sum简单，但请大家实现尽可能快的版本，最快的人将会获得一笔bonus奖金（数额保密）

### 【20180618】[46. Permutations](https://leetcode.com/problems/permutations/description/)

- 全排列
- 全排列那个可以就用回溯做，递归n层，每层在前面诸层中未选择的数字集合中选择candidate，选好了就进入下一层。各层share一个全局的长度为n的布尔数组，来标记每个数字是否被使用

### 【2018/06/19】[21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/description/)

- 类型：#合并链表
- 大二作业题，不能更水了

### 【2018/06/20】[172. Factorial Trailing Zeroes](https://leetcode.com/problems/factorial-trailing-zeroes/description/)

- 阶乘最末0

### 【2018/06/21】[223. Rectangle Area](https://leetcode.com/problems/rectangle-area/description/)

- 类型#简单计算几何 
- 分解[836. Rectangle Overlap](https://leetcode.com/problems/rectangle-overlap/description/)

### 【2018-06-22】[136. Single Number](https://leetcode.com/problems/single-number/description/)
- 类型： #不要看答案不要看discuss不要搜，自己想  

### 【2018-06-23】[300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/description/) 
- type #LIS

### 【2018-06-25】[19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/)

- type #LinkedList
- 希望大家能实现一趟扫描就完成任务的版本，不要扫完了再倒着找
- 俩指针，一个指针比另一个指针提前跑n位，每一步俩指针各动一步，前面的指针碰到尾巴的时候回，落在后面的指针就自动落在倒数第n个上
- 你用单指针把它一个个读下来，存到一个大小为n的队列里，不就行了，但是耗空间多
- 双指针是O(1)空间，单指针存队列是O(n)空间
- 双指针的另一个典型应用是找链表中点
- 链式存储不允许随机访问，如果n特别大，又是在单片机上，哪来的那么大内存放数据呢
- 我强调下一下，这题是不能不用双指针的，如果面试中没写出双指针的代码，面试官会问你有没有优化方法要求你想想再写的。
- 如果你在一台单片机上编程，内存往往非常小，不用双指针，一个数组只能存几千个数字，就保存不下这个问题了。这种问题的考点就在这里，面试官就是想问这个。你们要触碰他们的点。
- 这题一定一定一定！要用！双！指！针！[睡]
- 程序员，尤其是出面试题的程序员，就是一群这么喜欢抠小聪明的人，这种细节答出来了，他们就会感觉是对的人，要是答不出来，他们就会有连这都不知道的一种感觉
- 北京很多公司的面试题，其实是外包给一些acm选手出的，出一套几千块
- 刷LeetCode其实跟刷五三是一回事，都是过拟合

### 【2018-06-26】[78. Subsets](https://leetcode.com/problems/subsets/description/) 

- type#backtrack 
- 明天做这道吧，用不用递归都行

### 【2018-06-27】[335. Self Crossing](https://leetcode.com/problems/self-crossing/description/)

- type#计算几何 
- 这题的关键在于判断是否相交，可能有些难度
- 这是我们出的第一道标记为Hard题

### 【20160628】[587. Erect the Fence](https://leetcode.com/problems/erect-the-fence/description)

- type # computational geometry  
https://leetcode.com/problems/erect-the-fence/description
- 希望大家做出来，不要diserect

### 【2018-06=29】[72. Edit Distance](https://leetcode.com/problems/edit-distance/description/)

- type  #dynammic programming  #edit distance 
- 不管今天写不写得完，请务必学会这道题，这不仅是生物信息学的基础题，而且是大家的第一道动态规划题，现在面试还是挺流行考动态规划的。动态规划题目中，这道可以算是最简单了

### 【20180630】[18. 4Sum](https://leetcode.com/problems/4sum/description/)

### 【20180702】[53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/description/)

- type #动态规划  
- 最大子序列问题也毫无疑问是个动规问题，网上的解析非常多。我就不多说了，建议大家做动规题时候自己多想想，不要直接看答案，这样比较锻炼大脑。
- vote: 11-20这10天用来马拉松，出15道题，10天内刷完即可，题目偏水，个别题难点，在7号公布。你们同不同意？如果觉得时间不好或者数目不好，投不同意。否决后另案解决

### [2018-07-03] [120. Triangle](https://leetcode.com/problems/triangle/description/)

- type #DP 今天我们再来一道入门动规。
- 关于动态规划，给大家推荐一篇[入门文章](https://www.cnblogs.com/SDJL/archive/2008/08/22/1274312.html)很久很久以前的一篇科普老文了，初中生都能看懂，讲得比较有趣
- 以前在cpp我们都是用88888888或者0x3f3f3f3f来初始化,因为大概是int最大值的一半，这样两个这样的“无穷大“加在一起仍然不会溢出

### 【20180704】[100. Same Tree](https://leetcode.com/problems/same-tree/description/) 

### 【20180705】[70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/description/)

- type#数学题 动规
- 这一类求解F(n)=aF(n-1)+bF(n-2)+c的问题，叫做
二阶线性非齐次递推关系，闭式解法可以再《具体数学》这本小神书里面找到
- 提示，可以手算几个，然后上oeis上面查:[oeis](https://oeis.org/)是数列的数据库，支持数列的搜索，专业的。有acm选手作弊的的，就在上厕所的时候偷偷用oeis查手算的数据。当然平时打在线比赛的时候，oeis还是可以光明正大地用的
- 这个数据库就是内部存了海量的各种各样的数列，它把它的各种匹配的都给你，而且是局部比对
- 你随便输一些数字，都会发现是一个意想不到的数列

### 【20180706】[93. Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/description/)  

- type #可能比较麻烦


## My LeetCoding Solutions 我的解答
- 2018/6/12 [394. Decode String Solution](https://github.com/vivi3nli/LeetCodeDaily/blob/master/394_Decode_String_20180612.py)
- 2018/6/13 [66. Plus One Solution](https://github.com/vivi3nli/LeetCodeDaily/blob/master/66_Plus_One_20180613.py) and [43. Multiply Strings Solutions](https://github.com/vivi3nli/LeetCodeDaily/blob/master/43_Multiply_Strings_20180613.py)
- 2018/6/14 [15. 3Sum Solution](https://github.com/vivi3nli/LeetCodeDaily/blob/master/15_3Sum_20180614.py)
- 2018/6/15 [51. N-Queens Solution](https://github.com/vivi3nli/LeetCodeDaily/blob/master/51_N-Queens_20180615.py)
- 2018/6/16 [1. Two Sum Solution](https://github.com/vivi3nli/LeetCodeDaily/blob/master/1_Two_Sum_20180616.py)
- 2018/6/18 [46. Permutations Solution](https://github.com/vivi3nli/LeetCodeDaily/blob/master/46_Permutations_20180618.py)
- 2018/6/19 [21. Merge Two Sorted Lists Solution](https://github.com/vivi3nli/LeetCodeDaily/blob/master/21_Merge_Two_Sorted_List_20180620.py)
- 2018/6/20 [172. Factorial Trailing Zeroes Solution](https://github.com/vivi3nli/LeetCodeDaily/blob/master/172_Factorial_Trailing_Zeroes_20180620.py)
- 2018/6/21 [223. Rectangle Area Solution](https://github.com/vivi3nli/LeetCodeDaily/blob/master/223_Rectangle_Area_20180621.py) and [836. Rectangle Overlap Solution](https://github.com/vivi3nli/LeetCodeDaily/blob/master/836_Rectangle_Overlap.py) and reviewed [51. N-Queens Solution](https://github.com/vivi3nli/LeetCodeDaily/blob/master/51_N-Queens_20180621.py) [52. N-Queens II Solution](https://github.com/vivi3nli/LeetCodeDaily/blob/master/52_N-Queens_II_20180621.py)
- 2018/6/22 [136. Single Number Solution](https://github.com/vivi3nli/LeetCodeDaily/blob/master/136_Single_Number_20180622.py)
- 2018-6-26 [78. Subsets Solution](https://github.com/vivi3nli/LeetCodeDaily/blob/master/78_Subsets_20180626.py)
- 2018-6-27 [335. Self Crossing Solution](https://github.com/vivi3nli/LeetCodeDaily/blob/master/335_Self_Crossing_20180627.py)

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

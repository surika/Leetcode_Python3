# 暴力两次遍历：python会超时
# 该写法思路正确，具体运行未验证
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        l = len(prices)
        for i in range(l):
            for j in range(i, l):
                tmp = prices[j] - prices[i]
                if tmp > ans:
                    ans = tmp
        return ans
'''
# 动态规划1 
1. 记录【今天之前买入的最小值】
2. 计算【今天之前最小值买入，今天卖出的获利】，也即【今天卖出的最大获利】
3. 比较【每天的最大获利】，取最大值即可
'''
# 自己写的版本，maxsize在此题中直接写99999也能过
import sys
MAX_INT = sys.maxsize
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = MAX_INT
        ans = 0
        for i in prices:
            tmp = i - m
            if tmp > ans:
                ans = tmp
            # 更新今天之前的最小价格
            if i < m:
                m = i
        return ans

'''
动态规划2
前i天的最大收益 = max{前i-1天的最大收益，第i天的价格-前i-1天中的最小价格}
1. 找到状态转移方程：res = max(res, prices[i] - min_val);，res为前i天的最大收益，min_val为前i天的最小值。
2. 初始化状态量：res = 0;, min_val = INT_MAX;
'''

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int res = 0;
        int min_val = INT_MAX;
        for (int i = 0; i < prices.size(); i++) {
            min_val = min(min_val, prices[i]);
            res = max(res, prices[i] - min_val);
        }
        return res;
    }
};

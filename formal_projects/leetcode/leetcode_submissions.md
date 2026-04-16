# LeetCode 提交汇总

- 生成时间：2026/04/13 14:58:07 CST
- AC 题目数：442
- 总提交数：2304

## 1. 两数之和 (`two-sum`)

- 题目链接：https://leetcode.cn/problems/two-sum/
- 难度：Easy
- 标签：Array, Hash Table
- 总提交次数：2
- 最近提交时间：2025/11/30 15:07:18 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 681664260 | 2025/11/30 15:07:18 CST | python | Accepted | 0 ms | 18.6 MB |
| 681222981 | 2025/11/28 08:44:34 CST | python | Accepted | 0 ms | 18.7 MB |

### 最近一次 AC 代码

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            if target - num in hash_map:
                return [hash_map[target-num], i]
            hash_map[num] = i
        return []
```

## 2. 两数相加 (`add-two-numbers`)

- 题目链接：https://leetcode.cn/problems/add-two-numbers/
- 难度：Medium
- 标签：Recursion, Linked List, Math
- 总提交次数：5
- 最近提交时间：2026/03/31 14:02:52 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 713815500 | 2026/03/31 14:02:52 CST | python | Accepted | 11 ms | 19.2 MB |
| 713815372 | 2026/03/31 14:02:27 CST | python | Runtime Error | N/A | N/A |
| 683841236 | 2025/12/10 11:11:38 CST | python | Accepted | 3 ms | 17.8 MB |
| 682395013 | 2025/12/03 15:23:20 CST | python | Accepted | 0 ms | 17.6 MB |
| 648207438 | 2025/07/30 07:47:14 CST | python | Accepted | 3 ms | 17.7 MB |

### 最近一次 AC 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            total = l1_val + l2_val + carry
            new_val = total % 10
            carry = total // 10
            curr.next = ListNode(new_val)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
```

## 3. 无重复字符的最长子串 (`longest-substring-without-repeating-characters`)

- 题目链接：https://leetcode.cn/problems/longest-substring-without-repeating-characters/
- 难度：Medium
- 标签：Hash Table, String, Sliding Window
- 总提交次数：25
- 最近提交时间：2026/03/23 14:16:56 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 710876032 | 2026/03/23 14:16:56 CST | python | Accepted | 15 ms | 19.2 MB |
| 710875796 | 2026/03/23 14:16:26 CST | python | Runtime Error | N/A | N/A |
| 708647186 | 2026/03/18 10:16:17 CST | python | Accepted | 11 ms | 19 MB |
| 708646727 | 2026/03/18 10:15:20 CST | python | Wrong Answer | N/A | N/A |
| 700616866 | 2026/02/26 11:12:12 CST | python | Accepted | 11 ms | 18.9 MB |
| 685794311 | 2025/12/19 13:42:40 CST | python | Accepted | 19 ms | 17.1 MB |
| 685569619 | 2025/12/18 12:40:34 CST | python | Accepted | 19 ms | 17.1 MB |
| 685569547 | 2025/12/18 12:39:55 CST | python | Wrong Answer | N/A | N/A |
| 681901441 | 2025/12/01 15:59:21 CST | python | Accepted | 15 ms | 17.5 MB |
| 681901261 | 2025/12/01 15:58:43 CST | python | Wrong Answer | N/A | N/A |
| 681666736 | 2025/11/30 15:15:59 CST | python | Accepted | 19 ms | 17.8 MB |
| 681666460 | 2025/11/30 15:14:47 CST | python | Wrong Answer | N/A | N/A |
| 681222580 | 2025/11/28 08:38:33 CST | python | Accepted | 12 ms | 17.5 MB |
| 681222457 | 2025/11/28 08:36:43 CST | python | Wrong Answer | N/A | N/A |
| 681222404 | 2025/11/28 08:35:48 CST | python | Runtime Error | N/A | N/A |
| 681222374 | 2025/11/28 08:35:12 CST | python | Runtime Error | N/A | N/A |
| 681222359 | 2025/11/28 08:34:52 CST | python | Runtime Error | N/A | N/A |
| 675932140 | 2025/11/05 08:22:33 CST | python | Accepted | 12 ms | 17.8 MB |
| 675932020 | 2025/11/05 08:20:44 CST | python | Wrong Answer | N/A | N/A |
| 660929659 | 2025/09/09 11:25:13 CST | python | Accepted | 15 ms | 17.8 MB |
| 660909504 | 2025/09/09 10:46:06 CST | python | Accepted | 27 ms | 17.8 MB |
| 660909405 | 2025/09/09 10:45:54 CST | python | Runtime Error | N/A | N/A |
| 659084003 | 2025/09/03 14:14:43 CST | python | Accepted | 19 ms | 17.8 MB |
| 659083058 | 2025/09/03 14:11:42 CST | python | Accepted | 15 ms | 17.8 MB |
| 659079906 | 2025/09/03 14:01:09 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        max_len = 0
        left = 0
        for right, r_char in enumerate(s):
            if r_char in window and window[r_char] >= left:
                left = window[r_char] + 1
            window[r_char] = right
            max_len = max(max_len, right - left + 1)
        return max_len
```

## 4. 寻找两个正序数组的中位数 (`median-of-two-sorted-arrays`)

- 题目链接：https://leetcode.cn/problems/median-of-two-sorted-arrays/
- 难度：Hard
- 标签：Array, Binary Search, Divide and Conquer
- 总提交次数：7
- 最近提交时间：2026/03/06 16:14:18 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 703472186 | 2026/03/06 16:14:18 CST | python | Accepted | 4 ms | 19.8 MB |
| 703471577 | 2026/03/06 16:13:27 CST | python | Runtime Error | N/A | N/A |
| 703470856 | 2026/03/06 16:12:22 CST | python | Runtime Error | N/A | N/A |
| 682429149 | 2025/12/03 17:01:44 CST | python | Accepted | 1 ms | 18.1 MB |
| 681810675 | 2025/12/01 10:02:46 CST | python | Accepted | 11 ms | 17.9 MB |
| 681810527 | 2025/12/01 10:02:05 CST | python | Runtime Error | N/A | N/A |
| 681810301 | 2025/12/01 10:01:00 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def find_kth(k, array_1, array_2):
            m, n = len(array_1), len(array_2)
            if m > n:
                return find_kth(k, array_2, array_1)
            if m == 0:
                return array_2[k - 1]
            if k == 1:
                return min(array_1[0], array_2[0])
            i = min(k // 2, m)
            j = min(k // 2, n)
            if array_1[i - 1] < array_2[j - 1]:
                return find_kth(k - i, array_1[i:], array_2)
            else:
                return find_kth(k - j, array_1, array_2[j:])

        total = len(nums1) + len(nums2)
        if total % 2 == 1:
            return find_kth((total + 1) // 2, nums1, nums2)
        else:
            left = find_kth(total // 2, nums1, nums2)
            right = find_kth(total // 2 + 1, nums1, nums2)
            return (left + right) / 2
```

## 5. 最长回文子串 (`longest-palindromic-substring`)

- 题目链接：https://leetcode.cn/problems/longest-palindromic-substring/
- 难度：Medium
- 标签：Two Pointers, String, Dynamic Programming
- 总提交次数：18
- 最近提交时间：2026/03/23 10:23:55 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 710788546 | 2026/03/23 10:23:55 CST | python | Accepted | 215 ms | 19 MB |
| 710787841 | 2026/03/23 10:22:18 CST | python | Wrong Answer | N/A | N/A |
| 708289080 | 2026/03/17 15:07:41 CST | python | Accepted | 211 ms | 19.3 MB |
| 708288609 | 2026/03/17 15:06:59 CST | python | Runtime Error | N/A | N/A |
| 692366839 | 2026/01/19 10:50:34 CST | python | Accepted | 210 ms | 19.2 MB |
| 690756534 | 2026/01/12 14:01:17 CST | python | Accepted | 207 ms | 19.3 MB |
| 690756338 | 2026/01/12 14:00:31 CST | python | Runtime Error | N/A | N/A |
| 685795165 | 2025/12/19 13:48:08 CST | python | Accepted | 207 ms | 17.2 MB |
| 685795126 | 2025/12/19 13:47:49 CST | python | Runtime Error | N/A | N/A |
| 685795105 | 2025/12/19 13:47:41 CST | python | Runtime Error | N/A | N/A |
| 685559037 | 2025/12/18 11:37:04 CST | python | Accepted | 211 ms | 17 MB |
| 681907036 | 2025/12/01 16:16:22 CST | python | Accepted | 291 ms | 17.7 MB |
| 681906993 | 2025/12/01 16:16:16 CST | python | Runtime Error | N/A | N/A |
| 681671141 | 2025/11/30 15:32:41 CST | python | Accepted | 291 ms | 17.4 MB |
| 681286360 | 2025/11/28 14:07:26 CST | python | Accepted | 263 ms | 17.5 MB |
| 681285628 | 2025/11/28 14:03:53 CST | python | Wrong Answer | N/A | N/A |
| 681284772 | 2025/11/28 13:59:20 CST | python | Accepted | 267 ms | 17.4 MB |
| 681284721 | 2025/11/28 13:59:07 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def palindrome(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1 : right]
        res = ''
        for i in range(n):
            s1 = palindrome(i, i)
            s2 = palindrome(i, i + 1)
            res = s1 if len(s1) > len(res) else res
            res = s2 if len(s2) > len(res) else res
        return res
```

## 10. 正则表达式匹配 (`regular-expression-matching`)

- 题目链接：https://leetcode.cn/problems/regular-expression-matching/
- 难度：Hard
- 标签：Recursion, String, Dynamic Programming
- 总提交次数：5
- 最近提交时间：2026/02/14 09:29:42 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 698530120 | 2026/02/14 09:29:42 CST | python | Accepted | 3 ms | 19.1 MB |
| 698529946 | 2026/02/14 09:27:53 CST | python | Wrong Answer | N/A | N/A |
| 698529808 | 2026/02/14 09:26:19 CST | python | Wrong Answer | N/A | N/A |
| 698346918 | 2026/02/13 10:43:39 CST | python | Accepted | 11 ms | 19.1 MB |
| 698346293 | 2026/02/13 10:41:03 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(2, n + 1, 2):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # 匹配0次
                    match_zero = dp[i][j - 2]
                    # 匹配 1 次或多次
                    match_more = False
                    if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                        match_more = dp[i - 1][j]
                    dp[i][j] = match_zero or match_more
                else:
                    if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                        dp[i][j] = dp[i - 1][j - 1]
        return dp[m][n]
```

## 11. 盛最多水的容器 (`container-with-most-water`)

- 题目链接：https://leetcode.cn/problems/container-with-most-water/
- 难度：Medium
- 标签：Greedy, Array, Two Pointers
- 总提交次数：7
- 最近提交时间：2026/03/17 18:24:43 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 708415401 | 2026/03/17 18:24:43 CST | python | Accepted | 42 ms | 29.2 MB |
| 696574109 | 2026/02/05 11:32:57 CST | python | Accepted | 51 ms | 29.2 MB |
| 685556301 | 2025/12/18 11:26:41 CST | python | Accepted | 79 ms | 27.2 MB |
| 681945580 | 2025/12/01 18:31:37 CST | python | Accepted | 73 ms | 28 MB |
| 679950115 | 2025/11/22 21:31:46 CST | python | Accepted | 119 ms | 28.1 MB |
| 679615674 | 2025/11/21 08:24:48 CST | python | Accepted | 115 ms | 28 MB |
| 679615644 | 2025/11/21 08:24:16 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1
        while left < right:
            if height[left] < height[right]:
                max_area = max(max_area, (right - left) * height[left])
                left += 1
            else:
                max_area = max(max_area, (right - left) * height[right])
                right -= 1
        return max_area
```

## 14. 最长公共前缀 (`longest-common-prefix`)

- 题目链接：https://leetcode.cn/problems/longest-common-prefix/
- 难度：Easy
- 标签：Trie, Array, String
- 总提交次数：2
- 最近提交时间：2026/03/23 13:58:37 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 710868478 | 2026/03/23 13:58:37 CST | python | Accepted | 0 ms | 19.1 MB |
| 708366956 | 2026/03/17 16:56:23 CST | python | Accepted | 3 ms | 19.2 MB |

### 最近一次 AC 代码

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        first_str = strs[0]
        for i, char in enumerate(first_str):
            for string in strs[1:]:
                if i >= len(string) or string[i] != char:
                    return first_str[:i]
        return first_str
```

## 15. 三数之和 (`3sum`)

- 题目链接：https://leetcode.cn/problems/3sum/
- 难度：Medium
- 标签：Array, Two Pointers, Sorting
- 总提交次数：11
- 最近提交时间：2026/03/23 10:47:34 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 710799524 | 2026/03/23 10:47:34 CST | python | Accepted | 667 ms | 21.9 MB |
| 710798568 | 2026/03/23 10:45:46 CST | python | Wrong Answer | N/A | N/A |
| 708253933 | 2026/03/17 14:06:14 CST | python | Accepted | 647 ms | 22.2 MB |
| 708253804 | 2026/03/17 14:05:56 CST | python | Runtime Error | N/A | N/A |
| 708253622 | 2026/03/17 14:05:34 CST | python | Runtime Error | N/A | N/A |
| 708251953 | 2026/03/17 14:01:54 CST | python | Time Limit Exceeded | N/A | N/A |
| 681924972 | 2025/12/01 17:10:45 CST | python | Accepted | 923 ms | 20.4 MB |
| 681924849 | 2025/12/01 17:10:23 CST | python | Accepted | 830 ms | 20.4 MB |
| 681924467 | 2025/12/01 17:09:11 CST | python | Time Limit Exceeded | N/A | N/A |
| 681711311 | 2025/11/30 18:02:13 CST | python | Accepted | 451 ms | 20.3 MB |
| 681710969 | 2025/11/30 18:00:30 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        if n < 3:
            return []
        res = []
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif curr_sum > 0:
                    right -= 1
                else:
                    left += 1
        return res
```

## 17. 电话号码的字母组合 (`letter-combinations-of-a-phone-number`)

- 题目链接：https://leetcode.cn/problems/letter-combinations-of-a-phone-number/
- 难度：Medium
- 标签：Hash Table, String, Backtracking
- 总提交次数：5
- 最近提交时间：2026/04/09 11:24:29 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 716503877 | 2026/04/09 11:24:29 CST | python | Accepted | 0 ms | 19 MB |
| 699800695 | 2026/02/22 16:26:13 CST | python | Accepted | 0 ms | 19.1 MB |
| 699800544 | 2026/02/22 16:25:31 CST | python | Runtime Error | N/A | N/A |
| 687864341 | 2025/12/29 15:04:05 CST | python | Accepted | 0 ms | 17.1 MB |
| 687864284 | 2025/12/29 15:03:51 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        path = []
        res = []
        n = len(digits)
        def backtrack(idx):
            if idx == n:
                res.append(''.join(path))
                return
            cur_digit = digits[idx]
            for ch in mapping[cur_digit]:
                path.append(ch)
                backtrack(idx + 1)
                path.pop()
        backtrack(0)
        return res
```

## 18. 四数之和 (`4sum`)

- 题目链接：https://leetcode.cn/problems/4sum/
- 难度：Medium
- 标签：Array, Two Pointers, Sorting
- 总提交次数：4
- 最近提交时间：2026/03/23 11:01:02 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 710806819 | 2026/03/23 11:01:02 CST | python | Accepted | 15 ms | 19.2 MB |
| 708277795 | 2026/03/17 14:49:23 CST | python | Accepted | 19 ms | 19.1 MB |
| 708275985 | 2026/03/17 14:46:27 CST | python | Wrong Answer | N/A | N/A |
| 708275748 | 2026/03/17 14:46:14 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        if n < 4:
            return []
        res = []
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            min_sum = nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3]
            if min_sum > target:
                break
            max_sum = nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1]
            if max_sum < target:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                min_sum = nums[i] + nums[j] + nums[j + 1] + nums[j + 2]
                if min_sum > target:
                    break
                max_sum = nums[i] + nums[j] + nums[n - 2] + nums[n - 1]
                if max_sum < target:
                    continue
                left, right = j + 1, n - 1
                while left < right:
                    curr_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if curr_sum == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif curr_sum > target:
                        right -= 1
                    else:
                        left += 1
        return res
```

## 19. 删除链表的倒数第 N 个结点 (`remove-nth-node-from-end-of-list`)

- 题目链接：https://leetcode.cn/problems/remove-nth-node-from-end-of-list/
- 难度：Medium
- 标签：Linked List, Two Pointers
- 总提交次数：5
- 最近提交时间：2026/03/31 10:43:09 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 713754229 | 2026/03/31 10:43:09 CST | python | Accepted | 0 ms | 19 MB |
| 683645403 | 2025/12/09 14:49:55 CST | python | Accepted | 0 ms | 17.7 MB |
| 683645232 | 2025/12/09 14:49:24 CST | python | Runtime Error | N/A | N/A |
| 679636678 | 2025/11/21 10:38:39 CST | python | Accepted | 0 ms | 17.6 MB |
| 645609950 | 2025/07/21 07:57:52 CST | python | Accepted | 0 ms | 17.5 MB |

### 最近一次 AC 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = fast = dummy
        for _ in range(n + 1):
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next
```

## 20. 有效的括号 (`valid-parentheses`)

- 题目链接：https://leetcode.cn/problems/valid-parentheses/
- 难度：Easy
- 标签：Stack, String
- 总提交次数：3
- 最近提交时间：2026/03/26 10:05:54 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 712081509 | 2026/03/26 10:05:54 CST | python | Accepted | 4 ms | 19.1 MB |
| 712081307 | 2026/03/26 10:05:16 CST | python | Runtime Error | N/A | N/A |
| 712081230 | 2026/03/26 10:05:01 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for ch in s:
            if ch in '([{':
                stack.append(ch)
            else:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
        return not stack
```

## 21. 合并两个有序链表 (`merge-two-sorted-lists`)

- 题目链接：https://leetcode.cn/problems/merge-two-sorted-lists/
- 难度：Easy
- 标签：Recursion, Linked List
- 总提交次数：2
- 最近提交时间：2025/12/09 09:01:23 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 683569637 | 2025/12/09 09:01:23 CST | python | Accepted | 3 ms | 17.5 MB |
| 644610117 | 2025/07/17 08:07:37 CST | python | Accepted | 3 ms | 17.4 MB |

### 最近一次 AC 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        p_tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                p_tail.next = list1
                list1 = list1.next
            else:
                p_tail.next = list2
                list2 = list2.next
            p_tail = p_tail.next
        p_tail.next = list1 if list1 else list2
        return dummy.next
```

## 22. 括号生成 (`generate-parentheses`)

- 题目链接：https://leetcode.cn/problems/generate-parentheses/
- 难度：Medium
- 标签：String, Dynamic Programming, Backtracking
- 总提交次数：8
- 最近提交时间：2026/04/09 08:30:32 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 716458458 | 2026/04/09 08:30:32 CST | python | Accepted | 0 ms | 19.2 MB |
| 716458449 | 2026/04/09 08:30:25 CST | python | Runtime Error | N/A | N/A |
| 699801959 | 2026/02/22 16:31:51 CST | python | Accepted | 3 ms | 19.4 MB |
| 683401461 | 2025/12/08 14:22:38 CST | python | Accepted | 0 ms | 17.6 MB |
| 683210359 | 2025/12/07 14:57:31 CST | python | Accepted | 3 ms | 17.9 MB |
| 681812361 | 2025/12/01 10:11:06 CST | python | Accepted | 3 ms | 17.8 MB |
| 681604545 | 2025/11/30 10:26:14 CST | python | Accepted | 0 ms | 17.6 MB |
| 681555422 | 2025/11/29 21:38:06 CST | python | Accepted | 3 ms | 17.6 MB |

### 最近一次 AC 代码

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = []
        res = []
        def backtrack(left_count, right_count):
            if len(path) == 2 * n:
                res.append(''.join(path))
                return
            if left_count < n:
                path.append('(')
                backtrack(left_count + 1, right_count)
                path.pop()
            if right_count < left_count:
                path.append(')')
                backtrack(left_count, right_count + 1)
                path.pop()
        backtrack(0, 0)
        return res
```

## 23. 合并 K 个升序链表 (`merge-k-sorted-lists`)

- 题目链接：https://leetcode.cn/problems/merge-k-sorted-lists/
- 难度：Hard
- 标签：Linked List, Divide and Conquer, Heap (Priority Queue), Merge Sort
- 总提交次数：14
- 最近提交时间：2026/04/10 19:06:10 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 716972786 | 2026/04/10 19:06:10 CST | python | Accepted | 12 ms | 22.7 MB |
| 715037759 | 2026/04/04 11:56:49 CST | python | Accepted | 7 ms | 22.8 MB |
| 713746601 | 2026/03/31 10:25:11 CST | python | Accepted | 11 ms | 22.5 MB |
| 713746124 | 2026/03/31 10:24:02 CST | python | Runtime Error | N/A | N/A |
| 713745471 | 2026/03/31 10:22:20 CST | python | Runtime Error | N/A | N/A |
| 713745363 | 2026/03/31 10:22:03 CST | python | Runtime Error | N/A | N/A |
| 685795941 | 2025/12/19 13:52:52 CST | python | Accepted | 8 ms | 19.6 MB |
| 685555257 | 2025/12/18 11:22:48 CST | python | Accepted | 11 ms | 19.3 MB |
| 685555175 | 2025/12/18 11:22:32 CST | python | Runtime Error | N/A | N/A |
| 683581845 | 2025/12/09 10:07:32 CST | python | Accepted | 15 ms | 20 MB |
| 683581696 | 2025/12/09 10:06:55 CST | python | Runtime Error | N/A | N/A |
| 682078111 | 2025/12/02 10:46:59 CST | python | Accepted | 12 ms | 20 MB |
| 682077990 | 2025/12/02 10:46:37 CST | python | Runtime Error | N/A | N/A |
| 645378519 | 2025/07/20 09:40:10 CST | python | Accepted | 11 ms | 20 MB |

### 最近一次 AC 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for idx, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, idx, node))
        dummy = ListNode()
        tail = dummy
        while min_heap:
            _, idx, node = heapq.heappop(min_heap)
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(min_heap, (node.next.val, idx, node.next))
        return dummy.next
```

## 24. 两两交换链表中的节点 (`swap-nodes-in-pairs`)

- 题目链接：https://leetcode.cn/problems/swap-nodes-in-pairs/
- 难度：Medium
- 标签：Recursion, Linked List
- 总提交次数：7
- 最近提交时间：2026/04/02 10:53:12 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 714466731 | 2026/04/02 10:53:12 CST | python | Accepted | 0 ms | 19.2 MB |
| 714430800 | 2026/04/02 08:36:35 CST | python | Accepted | 0 ms | 19.1 MB |
| 714107278 | 2026/04/01 10:17:40 CST | python | Accepted | 0 ms | 19.1 MB |
| 684349875 | 2025/12/12 15:24:27 CST | python | Accepted | 0 ms | 17.4 MB |
| 684347999 | 2025/12/12 15:17:49 CST | python | Accepted | 0 ms | 17.6 MB |
| 684347685 | 2025/12/12 15:16:44 CST | python | Wrong Answer | N/A | N/A |
| 684347578 | 2025/12/12 15:16:21 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        pre = dummy
        while pre.next and pre.next.next:
            first = pre.next
            second = pre.next.next

            first.next = second.next
            second.next = first

            pre.next = second
            pre = first
        return dummy.next
```

## 25. K 个一组翻转链表 (`reverse-nodes-in-k-group`)

- 题目链接：https://leetcode.cn/problems/reverse-nodes-in-k-group/
- 难度：Hard
- 标签：Recursion, Linked List
- 总提交次数：4
- 最近提交时间：2026/04/02 10:46:55 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 714464022 | 2026/04/02 10:46:55 CST | python | Accepted | 0 ms | 20.2 MB |
| 714113350 | 2026/04/01 10:34:30 CST | python | Accepted | 0 ms | 20.3 MB |
| 687029431 | 2025/12/25 11:21:48 CST | python | Accepted | 0 ms | 17.6 MB |
| 684343497 | 2025/12/12 15:01:59 CST | python | Accepted | 0 ms | 18.4 MB |

### 最近一次 AC 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k <= 1:
            return head
        p = head
        for _ in range(k):
            if not p:
                return head
            p = p.next
        
        pre, cur = None, head
        for _ in range(k):
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        head.next = self.reverseKGroup(cur, k)

        return pre
```

## 26. 删除有序数组中的重复项 (`remove-duplicates-from-sorted-array`)

- 题目链接：https://leetcode.cn/problems/remove-duplicates-from-sorted-array/
- 难度：Easy
- 标签：Array, Two Pointers
- 总提交次数：9
- 最近提交时间：2026/03/17 15:24:16 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 708299869 | 2026/03/17 15:24:16 CST | python | Accepted | 0 ms | 20.3 MB |
| 708299479 | 2026/03/17 15:23:38 CST | python | Wrong Answer | N/A | N/A |
| 708297904 | 2026/03/17 15:21:20 CST | python | Accepted | 0 ms | 20.3 MB |
| 708201378 | 2026/03/17 11:35:53 CST | python | Accepted | 3 ms | 20.5 MB |
| 708200162 | 2026/03/17 11:33:38 CST | python | Wrong Answer | N/A | N/A |
| 679647143 | 2025/11/21 11:15:50 CST | python | Accepted | 0 ms | 18.8 MB |
| 679647021 | 2025/11/21 11:15:20 CST | python | Wrong Answer | N/A | N/A |
| 679639481 | 2025/11/21 10:49:12 CST | python | Accepted | 6 ms | 18.5 MB |
| 649584282 | 2025/08/04 07:41:54 CST | python | Accepted | 0 ms | 18.8 MB |

### 最近一次 AC 代码

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        slow = 1
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow - 1]:
                nums[slow] = nums[fast]
                slow += 1
        return slow
```

## 27. 移除元素 (`remove-element`)

- 题目链接：https://leetcode.cn/problems/remove-element/
- 难度：Easy
- 标签：Array, Two Pointers
- 总提交次数：5
- 最近提交时间：2026/03/23 10:08:20 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 710782120 | 2026/03/23 10:08:20 CST | python | Accepted | 0 ms | 19.1 MB |
| 708219197 | 2026/03/17 12:21:10 CST | python | Accepted | 0 ms | 19 MB |
| 708218988 | 2026/03/17 12:20:22 CST | python | Wrong Answer | N/A | N/A |
| 708218830 | 2026/03/17 12:19:45 CST | python | Runtime Error | N/A | N/A |
| 649591060 | 2025/08/04 09:12:04 CST | python | Accepted | 0 ms | 17.5 MB |

### 最近一次 AC 代码

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow
```

## 33. 搜索旋转排序数组 (`search-in-rotated-sorted-array`)

- 题目链接：https://leetcode.cn/problems/search-in-rotated-sorted-array/
- 难度：Medium
- 标签：Array, Binary Search
- 总提交次数：3
- 最近提交时间：2026/03/20 18:16:50 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 709817995 | 2026/03/20 18:16:50 CST | python | Accepted | 0 ms | 19.1 MB |
| 702152229 | 2026/03/03 14:22:02 CST | python | Accepted | 0 ms | 19.2 MB |
| 666660752 | 2025/09/28 13:40:00 CST | python | Accepted | 0 ms | 17.8 MB |

### 最近一次 AC 代码

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
```

## 34. 在排序数组中查找元素的第一个和最后一个位置 (`find-first-and-last-position-of-element-in-sorted-array`)

- 题目链接：https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/
- 难度：Medium
- 标签：Array, Binary Search
- 总提交次数：5
- 最近提交时间：2026/03/18 15:49:01 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 708804885 | 2026/03/18 15:49:01 CST | python | Accepted | 0 ms | 20.2 MB |
| 702138197 | 2026/03/03 13:43:42 CST | python | Accepted | 0 ms | 20.3 MB |
| 666237042 | 2025/09/26 16:46:11 CST | python | Accepted | 0 ms | 18.8 MB |
| 666236832 | 2025/09/26 16:45:38 CST | python | Runtime Error | N/A | N/A |
| 666234568 | 2025/09/26 16:39:51 CST | python | Accepted | 0 ms | 18.7 MB |

### 最近一次 AC 代码

```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_bound = bisect.bisect_left(nums, target)
        if left_bound == len(nums) or nums[left_bound] != target:
            return [-1, -1]
        right_bound = bisect.bisect_right(nums, target) - 1
        return [left_bound, right_bound]
```

## 35. 搜索插入位置 (`search-insert-position`)

- 题目链接：https://leetcode.cn/problems/search-insert-position/
- 难度：Easy
- 标签：Array, Binary Search
- 总提交次数：4
- 最近提交时间：2026/03/24 10:28:26 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 711248131 | 2026/03/24 10:28:26 CST | python | Accepted | 0 ms | 19.8 MB |
| 709740407 | 2026/03/20 15:53:48 CST | python | Accepted | 0 ms | 19.5 MB |
| 709739382 | 2026/03/20 15:52:13 CST | python | Time Limit Exceeded | N/A | N/A |
| 666622245 | 2025/09/28 11:11:33 CST | python | Accepted | 0 ms | 18 MB |

### 最近一次 AC 代码

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)
```

## 37. 解数独 (`sudoku-solver`)

- 题目链接：https://leetcode.cn/problems/sudoku-solver/
- 难度：Hard
- 标签：Array, Hash Table, Backtracking, Matrix
- 总提交次数：15
- 最近提交时间：2026/04/09 13:11:34 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 716527703 | 2026/04/09 13:11:34 CST | python | Accepted | 1835 ms | 19.5 MB |
| 716152538 | 2026/04/08 10:18:10 CST | python | Accepted | 1879 ms | 19.4 MB |
| 716152481 | 2026/04/08 10:18:02 CST | python | Runtime Error | N/A | N/A |
| 716152416 | 2026/04/08 10:17:50 CST | python | Runtime Error | N/A | N/A |
| 699788555 | 2026/02/22 15:32:10 CST | python | Accepted | 1055 ms | 19.5 MB |
| 699788299 | 2026/02/22 15:30:52 CST | python | Wrong Answer | N/A | N/A |
| 699788246 | 2026/02/22 15:30:36 CST | python | Runtime Error | N/A | N/A |
| 699787963 | 2026/02/22 15:29:15 CST | python | Runtime Error | N/A | N/A |
| 687296096 | 2025/12/26 15:27:15 CST | python | Accepted | 1435 ms | 17.2 MB |
| 687295843 | 2025/12/26 15:26:24 CST | python | Wrong Answer | N/A | N/A |
| 687295288 | 2025/12/26 15:24:32 CST | python | Runtime Error | N/A | N/A |
| 687294853 | 2025/12/26 15:23:01 CST | python | Runtime Error | N/A | N/A |
| 687294760 | 2025/12/26 15:22:41 CST | python | Runtime Error | N/A | N/A |
| 687294696 | 2025/12/26 15:22:26 CST | python | Runtime Error | N/A | N/A |
| 687283900 | 2025/12/26 14:45:37 CST | python | Time Limit Exceeded | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_used = [set() for _ in range(9)]
        col_used = [set() for _ in range(9)]
        box_used = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    row_used[i].add(num)
                    col_used[j].add(num)
                    box_used[i // 3][j // 3].add(num)
        def backtrack(pos):
            if pos == 81:
                return True
            r, c = pos // 9, pos % 9
            if board[r][c] != '.':
                return backtrack(pos + 1)
            br, bc = r // 3, c // 3
            for num in range(1, 10):
                if num in row_used[r] or num in col_used[c] or num in box_used[br][bc]:
                    continue
                board[r][c] = str(num)
                row_used[r].add(num)
                col_used[c].add(num)
                box_used[br][bc].add(num)
                if backtrack(pos + 1):
                    return True
                board[r][c] = '.'
                box_used[br][bc].discard(num)
                col_used[c].discard(num)
                row_used[r].discard(num)
            return False
        backtrack(0)
```

## 39. 组合总和 (`combination-sum`)

- 题目链接：https://leetcode.cn/problems/combination-sum/
- 难度：Medium
- 标签：Array, Backtracking
- 总提交次数：3
- 最近提交时间：2026/04/08 21:36:58 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 716390610 | 2026/04/08 21:36:58 CST | python | Accepted | 12 ms | 19.4 MB |
| 699070162 | 2026/02/17 21:01:30 CST | python | Accepted | 11 ms | 19.6 MB |
| 687484075 | 2025/12/27 16:03:15 CST | python | Accepted | 11 ms | 17.4 MB |

### 最近一次 AC 代码

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        self.path_sum = 0
        n = len(candidates)
        def backtrack(start_idx):
            if self.path_sum == target:
                res.append(list(path))
                return
            if self.path_sum > target:
                return
            for i in range(start_idx, n):
                path.append(candidates[i])
                self.path_sum += candidates[i]
                backtrack(i)
                self.path_sum -= candidates[i]
                path.pop()
        backtrack(0)
        return res
```

## 40. 组合总和 II (`combination-sum-ii`)

- 题目链接：https://leetcode.cn/problems/combination-sum-ii/
- 难度：Medium
- 标签：Array, Backtracking
- 总提交次数：9
- 最近提交时间：2026/04/08 21:08:41 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 716379014 | 2026/04/08 21:08:41 CST | python | Accepted | 31 ms | 19.6 MB |
| 716378839 | 2026/04/08 21:08:17 CST | python | Runtime Error | N/A | N/A |
| 699204582 | 2026/02/18 21:06:01 CST | python | Accepted | 23 ms | 19.4 MB |
| 699204317 | 2026/02/18 21:04:33 CST | python | Wrong Answer | N/A | N/A |
| 699204269 | 2026/02/18 21:04:20 CST | python | Runtime Error | N/A | N/A |
| 687827765 | 2025/12/29 11:39:51 CST | python | Accepted | 23 ms | 17.1 MB |
| 687827326 | 2025/12/29 11:38:04 CST | python | Wrong Answer | N/A | N/A |
| 687380200 | 2025/12/26 21:44:59 CST | python | Accepted | 27 ms | 17 MB |
| 687380121 | 2025/12/26 21:44:29 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        path = []
        res = []
        self.path_sum = 0
        n = len(candidates)
        def backtrack(start_idx):
            if self.path_sum == target:
                res.append(list(path))
                return
            if self.path_sum > target:
                return
            for i in range(start_idx, n):
                if i > start_idx and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                self.path_sum += candidates[i]
                backtrack(i + 1)
                self.path_sum -= candidates[i]
                path.pop()
        backtrack(0)
        return res
```

## 41. 缺失的第一个正数 (`first-missing-positive`)

- 题目链接：https://leetcode.cn/problems/first-missing-positive/
- 难度：Hard
- 标签：Array, Hash Table
- 总提交次数：3
- 最近提交时间：2026/04/06 21:35:55 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715725091 | 2026/04/06 21:35:55 CST | python | Accepted | 47 ms | 30.2 MB |
| 682574160 | 2025/12/04 10:50:23 CST | python | Accepted | 47 ms | 28.3 MB |
| 682573839 | 2025/12/04 10:49:20 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                target_idx = nums[i] - 1
                nums[i], nums[target_idx] = nums[target_idx], nums[i]
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1
```

## 42. 接雨水 (`trapping-rain-water`)

- 题目链接：https://leetcode.cn/problems/trapping-rain-water/
- 难度：Hard
- 标签：Stack, Array, Two Pointers, Dynamic Programming, Monotonic Stack
- 总提交次数：3
- 最近提交时间：2026/03/17 18:12:47 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 708411105 | 2026/03/17 18:12:47 CST | python | Accepted | 3 ms | 20.6 MB |
| 681919444 | 2025/12/01 16:53:11 CST | python | Accepted | 3 ms | 18.9 MB |
| 681703839 | 2025/11/30 17:26:06 CST | python | Accepted | 4 ms | 19 MB |

### 最近一次 AC 代码

```python
class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] < left_max:
                    res += (left_max - height[left])
                else:
                    left_max = height[left]
                left += 1
            else:
                if height[right] < right_max:
                    res += (right_max - height[right])
                else:
                    right_max = height[right]
                right -= 1
        return res
```

## 44. 通配符匹配 (`wildcard-matching`)

- 题目链接：https://leetcode.cn/problems/wildcard-matching/
- 难度：Hard
- 标签：Greedy, Recursion, String, Dynamic Programming
- 总提交次数：5
- 最近提交时间：2026/02/14 10:16:16 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 698536272 | 2026/02/14 10:16:16 CST | python | Accepted | 567 ms | 49.8 MB |
| 698331018 | 2026/02/13 08:50:04 CST | python | Accepted | 607 ms | 49.6 MB |
| 698331007 | 2026/02/13 08:49:54 CST | python | Runtime Error | N/A | N/A |
| 698111465 | 2026/02/12 09:12:39 CST | python | Accepted | 615 ms | 49.7 MB |
| 698111235 | 2026/02/12 09:10:10 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = True
            else:
                break
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j]= dp[i][j - 1] or dp[i - 1][j]
                elif s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[m][n]
```

## 45. 跳跃游戏 II (`jump-game-ii`)

- 题目链接：https://leetcode.cn/problems/jump-game-ii/
- 难度：Medium
- 标签：Greedy, Array, Dynamic Programming
- 总提交次数：8
- 最近提交时间：2026/02/05 10:24:46 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 696553162 | 2026/02/05 10:24:46 CST | python | Accepted | 7 ms | 20.1 MB |
| 696311166 | 2026/02/04 10:24:55 CST | python | Accepted | 3 ms | 19.8 MB |
| 696311111 | 2026/02/04 10:24:42 CST | python | Runtime Error | N/A | N/A |
| 696306289 | 2026/02/04 10:05:23 CST | python | Accepted | 3 ms | 20 MB |
| 696305060 | 2026/02/04 10:00:08 CST | python | Accepted | 3 ms | 19.8 MB |
| 696303999 | 2026/02/04 09:54:52 CST | python | Wrong Answer | N/A | N/A |
| 696100109 | 2026/02/03 14:02:59 CST | python | Accepted | 12 ms | 19.7 MB |
| 696099909 | 2026/02/03 14:02:11 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        end = 0
        farthest = 0
        steps = 0
        i = 0
        while end < n - 1:
            while i <= end:
                farthest = max(farthest, i + nums[i])
                i += 1
            steps += 1
            end = farthest
        return steps
```

## 46. 全排列 (`permutations`)

- 题目链接：https://leetcode.cn/problems/permutations/
- 难度：Medium
- 标签：Array, Backtracking
- 总提交次数：15
- 最近提交时间：2026/04/08 09:31:05 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 716139079 | 2026/04/08 09:31:05 CST | python | Accepted | 0 ms | 19.5 MB |
| 699505858 | 2026/02/20 20:52:14 CST | python | Accepted | 0 ms | 19.2 MB |
| 687251533 | 2025/12/26 11:37:39 CST | python | Accepted | 4 ms | 17.2 MB |
| 682995113 | 2025/12/06 11:38:18 CST | python | Accepted | 3 ms | 17.7 MB |
| 682994957 | 2025/12/06 11:37:23 CST | python | Wrong Answer | N/A | N/A |
| 681813765 | 2025/12/01 10:16:51 CST | python | Accepted | 0 ms | 17.9 MB |
| 681813450 | 2025/12/01 10:15:34 CST | python | Wrong Answer | N/A | N/A |
| 681605399 | 2025/11/30 10:31:53 CST | python | Accepted | 3 ms | 17.7 MB |
| 681605280 | 2025/11/30 10:31:13 CST | python | Wrong Answer | N/A | N/A |
| 681559647 | 2025/11/29 21:59:50 CST | python | Accepted | 3 ms | 18 MB |
| 680476665 | 2025/11/25 09:47:38 CST | python | Accepted | 0 ms | 17.8 MB |
| 680476618 | 2025/11/25 09:47:27 CST | python | Wrong Answer | N/A | N/A |
| 680476444 | 2025/11/25 09:46:36 CST | python | Wrong Answer | N/A | N/A |
| 680476310 | 2025/11/25 09:45:59 CST | python | Runtime Error | N/A | N/A |
| 680476254 | 2025/11/25 09:45:48 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        n = len(nums)
        used = [False] * n
        def backtrack():
            if len(path) == n:
                res.append(list(path))
                return
            for i in range(n):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = True
                backtrack()
                used[i] = False
                path.pop()
        backtrack()
        return res
```

## 47. 全排列 II (`permutations-ii`)

- 题目链接：https://leetcode.cn/problems/permutations-ii/
- 难度：Medium
- 标签：Array, Backtracking, Sorting
- 总提交次数：14
- 最近提交时间：2026/04/08 21:25:54 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 716386060 | 2026/04/08 21:25:54 CST | python | Accepted | 3 ms | 19.6 MB |
| 699508196 | 2026/02/20 21:04:32 CST | python | Accepted | 3 ms | 19.6 MB |
| 699508053 | 2026/02/20 21:03:53 CST | python | Wrong Answer | N/A | N/A |
| 687451921 | 2025/12/27 13:34:22 CST | python | Accepted | 3 ms | 17.8 MB |
| 687450839 | 2025/12/27 13:25:47 CST | python | Accepted | 15 ms | 17.5 MB |
| 687450374 | 2025/12/27 13:22:02 CST | python | Accepted | 3 ms | 17.6 MB |
| 682997647 | 2025/12/06 11:55:04 CST | python | Accepted | 3 ms | 17.7 MB |
| 682997258 | 2025/12/06 11:52:19 CST | python | Wrong Answer | N/A | N/A |
| 682997152 | 2025/12/06 11:51:31 CST | python | Wrong Answer | N/A | N/A |
| 680523107 | 2025/11/25 12:57:08 CST | python | Accepted | 7 ms | 17.9 MB |
| 680483215 | 2025/11/25 10:14:08 CST | python | Accepted | 3 ms | 17.9 MB |
| 680482851 | 2025/11/25 10:12:44 CST | python | Wrong Answer | N/A | N/A |
| 680482598 | 2025/11/25 10:11:53 CST | python | Wrong Answer | N/A | N/A |
| 680482420 | 2025/11/25 10:11:14 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        path = []
        res = []
        nums.sort()
        used = [False] * n
        def backtrack():
            if len(path) == n:
                res.append(list(path))
                return
            for i in range(n):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                path.append(nums[i])
                used[i] = True
                backtrack()
                path.pop()
                used[i] = False
        backtrack()
        return res
```

## 48. 旋转图像 (`rotate-image`)

- 题目链接：https://leetcode.cn/problems/rotate-image/
- 难度：Medium
- 标签：Array, Math, Matrix
- 总提交次数：4
- 最近提交时间：2026/03/23 09:32:42 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 710770763 | 2026/03/23 09:32:42 CST | python | Accepted | 0 ms | 19.2 MB |
| 710770567 | 2026/03/23 09:31:51 CST | python | Runtime Error | N/A | N/A |
| 710770289 | 2026/03/23 09:30:44 CST | python | Wrong Answer | N/A | N/A |
| 707834474 | 2026/03/16 15:55:03 CST | python | Accepted | 0 ms | 19.2 MB |

### 最近一次 AC 代码

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            i, j = 0, n - 1
            while i < j:
                row[i], row[j] = row[j], row[i]
                i += 1
                j -= 1
```

## 49. 字母异位词分组 (`group-anagrams`)

- 题目链接：https://leetcode.cn/problems/group-anagrams/
- 难度：Medium
- 标签：Array, Hash Table, String, Sorting
- 总提交次数：3
- 最近提交时间：2026/03/29 17:59:01 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 713221418 | 2026/03/29 17:59:01 CST | python | Accepted | 17 ms | 23.6 MB |
| 681941805 | 2025/12/01 18:19:26 CST | python | Accepted | 19 ms | 22.2 MB |
| 679109295 | 2025/11/19 08:08:55 CST | python | Accepted | 19 ms | 22.2 MB |

### 最近一次 AC 代码

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)
        for chars in strs:
            char_list = [0] * 26
            for char in chars:
                char_list[ord(char) - ord('a')] += 1
            groups[tuple(char_list)].append(chars)
        return list(groups.values())
```

## 51. N 皇后 (`n-queens`)

- 题目链接：https://leetcode.cn/problems/n-queens/
- 难度：Hard
- 标签：Array, Backtracking
- 总提交次数：8
- 最近提交时间：2026/04/08 10:41:51 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 716161543 | 2026/04/08 10:41:51 CST | python | Accepted | 11 ms | 19.5 MB |
| 716161113 | 2026/04/08 10:40:47 CST | python | Runtime Error | N/A | N/A |
| 699777063 | 2026/02/22 14:30:18 CST | python | Accepted | 11 ms | 19.7 MB |
| 699776793 | 2026/02/22 14:28:42 CST | python | Wrong Answer | N/A | N/A |
| 699776505 | 2026/02/22 14:26:55 CST | python | Wrong Answer | N/A | N/A |
| 687313874 | 2025/12/26 16:21:28 CST | python | Accepted | 11 ms | 17.4 MB |
| 683205973 | 2025/12/07 14:43:07 CST | python | Accepted | 7 ms | 18 MB |
| 681661207 | 2025/11/30 14:53:50 CST | python | Accepted | 11 ms | 17.9 MB |

### 最近一次 AC 代码

```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        diag_1 = set()
        diag_2 = set()
        res = []
        queens = []
        def backtrack(row):
            if row == n:
                res.append(
                    ['.' * c + 'Q' + '.' * (n - 1 - c) for c in queens]
                )
                return
            for col in range(n):
                if col in cols or (row - col) in diag_1 or (row + col) in diag_2:
                    continue
                cols.add(col)
                diag_1.add(row - col)
                diag_2.add(row + col)
                queens.append(col)
                backtrack(row + 1)
                cols.discard(col)
                diag_1.discard(row - col)
                diag_2.discard(row + col)
                queens.pop()
        backtrack(0)
        return res
```

## 52. N 皇后 II (`n-queens-ii`)

- 题目链接：https://leetcode.cn/problems/n-queens-ii/
- 难度：Hard
- 标签：Backtracking
- 总提交次数：4
- 最近提交时间：2026/04/08 10:56:11 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 716167560 | 2026/04/08 10:56:11 CST | python | Accepted | 11 ms | 19.2 MB |
| 699779060 | 2026/02/22 14:42:18 CST | python | Accepted | 7 ms | 19.3 MB |
| 687316779 | 2025/12/26 16:29:16 CST | python | Accepted | 11 ms | 17.1 MB |
| 687316639 | 2025/12/26 16:28:47 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        diag_1 = set()
        diag_2 = set()
        self.res = 0
        def backtrack(row):
            if row == n:
                self.res += 1
                return
            for col in range(n):
                if col in cols or (row - col) in diag_1 or (row + col) in diag_2:
                    continue
                cols.add(col)
                diag_1.add(row - col)
                diag_2.add(row + col)
                backtrack(row + 1)
                cols.discard(col)
                diag_1.discard(row - col)
                diag_2.discard(row + col)
        backtrack(0)
        return self.res
```

## 53. 最大子数组和 (`maximum-subarray`)

- 题目链接：https://leetcode.cn/problems/maximum-subarray/
- 难度：Medium
- 标签：Array, Divide and Conquer, Dynamic Programming
- 总提交次数：10
- 最近提交时间：2026/04/13 12:19:04 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 717650359 | 2026/04/13 12:19:04 CST | python | Accepted | 35 ms | 31 MB |
| 697651199 | 2026/02/10 08:39:04 CST | python | Accepted | 27 ms | 31.1 MB |
| 697445968 | 2026/02/09 11:15:30 CST | python | Accepted | 31 ms | 30.9 MB |
| 690633402 | 2026/01/11 21:34:21 CST | python | Accepted | 32 ms | 31 MB |
| 690633288 | 2026/01/11 21:33:57 CST | python | Wrong Answer | N/A | N/A |
| 688513749 | 2026/01/02 08:16:38 CST | python | Accepted | 51 ms | 29.3 MB |
| 688513688 | 2026/01/02 08:13:58 CST | python | Accepted | 79 ms | 29.3 MB |
| 685091160 | 2025/12/16 12:20:07 CST | python | Accepted | 59 ms | 31.9 MB |
| 682359796 | 2025/12/03 12:50:52 CST | python | Accepted | 56 ms | 31.9 MB |
| 682359771 | 2025/12/03 12:50:35 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = curr_sum = nums[0]
        for num in nums[1:]:
            if curr_sum > 0:
                curr_sum += num
            else:
                curr_sum = num
            max_sum = max(max_sum, curr_sum)
        return max_sum
```

## 54. 螺旋矩阵 (`spiral-matrix`)

- 题目链接：https://leetcode.cn/problems/spiral-matrix/
- 难度：Medium
- 标签：Array, Matrix, Simulation
- 总提交次数：2
- 最近提交时间：2026/03/16 16:12:08 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 707846692 | 2026/03/16 16:12:08 CST | python | Accepted | 3 ms | 19 MB |
| 682585678 | 2025/12/04 11:27:53 CST | python | Accepted | 0 ms | 17.3 MB |

### 最近一次 AC 代码

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        res = []
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            if top > bottom or left > right:
                break
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res
```

## 55. 跳跃游戏 (`jump-game`)

- 题目链接：https://leetcode.cn/problems/jump-game/
- 难度：Medium
- 标签：Greedy, Array, Dynamic Programming
- 总提交次数：6
- 最近提交时间：2026/02/05 10:14:23 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 696550412 | 2026/02/05 10:14:23 CST | python | Accepted | 24 ms | 19.8 MB |
| 696550363 | 2026/02/05 10:14:11 CST | python | Wrong Answer | N/A | N/A |
| 696331336 | 2026/02/04 11:29:28 CST | python | Accepted | 7 ms | 20 MB |
| 696331190 | 2026/02/04 11:29:01 CST | python | Wrong Answer | N/A | N/A |
| 696071583 | 2026/02/03 11:35:08 CST | python | Accepted | 36 ms | 19.9 MB |
| 682369117 | 2025/12/03 13:48:03 CST | python | Accepted | 35 ms | 18.3 MB |

### 最近一次 AC 代码

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_reach = 0
        for i in range(n):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
            if max_reach > n - 1:
                return True
        return True
```

## 56. 合并区间 (`merge-intervals`)

- 题目链接：https://leetcode.cn/problems/merge-intervals/
- 难度：Medium
- 标签：Array, Sorting
- 总提交次数：5
- 最近提交时间：2026/02/26 10:27:11 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 700603378 | 2026/02/26 10:27:11 CST | python | Accepted | 7 ms | 23.1 MB |
| 696548642 | 2026/02/05 10:07:05 CST | python | Accepted | 11 ms | 22.8 MB |
| 677527497 | 2025/11/12 09:46:27 CST | python | Accepted | 8 ms | 21.3 MB |
| 677527309 | 2025/11/12 09:45:32 CST | python | Runtime Error | N/A | N/A |
| 677515737 | 2025/11/12 08:11:58 CST | python | Accepted | 11 ms | 21.4 MB |

### 最近一次 AC 代码

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        intervals.sort()
        for start, end in intervals:
            if not merged or start > merged[-1][1]:
                merged.append([start, end])
            else:
                merged[-1][1] = max(end, merged[-1][1])
        return merged
```

## 57. 插入区间 (`insert-interval`)

- 题目链接：https://leetcode.cn/problems/insert-interval/
- 难度：Medium
- 标签：Array
- 总提交次数：6
- 最近提交时间：2026/02/26 10:44:15 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 700608151 | 2026/02/26 10:44:15 CST | python | Accepted | 0 ms | 21.2 MB |
| 700607586 | 2026/02/26 10:42:22 CST | python | Wrong Answer | N/A | N/A |
| 700607501 | 2026/02/26 10:42:04 CST | python | Wrong Answer | N/A | N/A |
| 677764095 | 2025/11/13 08:05:58 CST | python | Accepted | 0 ms | 19.4 MB |
| 677764041 | 2025/11/13 08:04:25 CST | python | Wrong Answer | N/A | N/A |
| 677764025 | 2025/11/13 08:04:08 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        new_start, new_end = newInterval
        res = []
        i = 0
        while i < n and intervals[i][1] < new_start:
            res.append(intervals[i])
            i += 1
        while i < n and intervals[i][0] <= new_end:
            new_start = min(new_start, intervals[i][0])
            new_end = max(new_end, intervals[i][1])
            i += 1
        res.append([new_start, new_end])
        while i < n:
            res.append(intervals[i])
            i += 1
        return res
```

## 59. 螺旋矩阵 II (`spiral-matrix-ii`)

- 题目链接：https://leetcode.cn/problems/spiral-matrix-ii/
- 难度：Medium
- 标签：Array, Matrix, Simulation
- 总提交次数：2
- 最近提交时间：2026/03/23 09:51:19 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 710776218 | 2026/03/23 09:51:19 CST | python | Accepted | 4 ms | 19.1 MB |
| 707857730 | 2026/03/16 16:27:59 CST | python | Accepted | 0 ms | 19.2 MB |

### 最近一次 AC 代码

```python
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        num = 1
        while num <= n ** 2:
            if top <= bottom:
                for i in range(left, right + 1):
                    res[top][i] = num
                    num += 1
                top += 1
            if left <= right:
                for i in range(top, bottom + 1):
                    res[i][right] = num
                    num += 1
                right -= 1
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res[bottom][i] = num
                    num += 1
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res[i][left] = num
                    num += 1
                left += 1
        return res
```

## 61. 旋转链表 (`rotate-list`)

- 题目链接：https://leetcode.cn/problems/rotate-list/
- 难度：Medium
- 标签：Linked List, Two Pointers
- 总提交次数：2
- 最近提交时间：2025/09/24 08:03:11 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 665504822 | 2025/09/24 08:03:11 CST | python | Accepted | 3 ms | 17.5 MB |
| 665504805 | 2025/09/24 08:02:39 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 边界情况处理
        if not head or not head.next or k == 0:
            return head

        # 先遍历出链表的总长度
        cur = head
        n = 1
        while cur.next:
            cur = cur.next
            n += 1
        # 实际有效的旋转次数
        valid_rotate = k % n
        # 链表成环
        cur.next = head
        # 确定从原链表头结点到新链表尾节点需要走的步数
        steps_to_new_tail = n - valid_rotate - 1 
        # 找到新链表的尾节点
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next
        # 确定新链表的头结点
        new_head = new_tail.next
        # 断开环
        new_tail.next = None
        return new_head
```

## 63. 不同路径 II (`unique-paths-ii`)

- 题目链接：https://leetcode.cn/problems/unique-paths-ii/
- 难度：Medium
- 标签：Array, Dynamic Programming, Matrix
- 总提交次数：5
- 最近提交时间：2026/01/30 11:06:04 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 695145379 | 2026/01/30 11:06:04 CST | python | Accepted | 0 ms | 19.1 MB |
| 695143326 | 2026/01/30 10:59:14 CST | python | Wrong Answer | N/A | N/A |
| 695143292 | 2026/01/30 10:59:05 CST | python | Runtime Error | N/A | N/A |
| 694960879 | 2026/01/29 15:22:15 CST | python | Accepted | 0 ms | 19.2 MB |
| 694960537 | 2026/01/29 15:21:19 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            dp[0][0] = 1
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i - 1][0]
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                else:
                    dp[i][j] = 0
        return dp[m - 1][n - 1]
```

## 64. 最小路径和 (`minimum-path-sum`)

- 题目链接：https://leetcode.cn/problems/minimum-path-sum/
- 难度：Medium
- 标签：Array, Dynamic Programming, Matrix
- 总提交次数：3
- 最近提交时间：2025/12/31 10:15:37 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 688240807 | 2025/12/31 10:15:37 CST | python | Accepted | 11 ms | 19.1 MB |
| 685049112 | 2025/12/16 09:07:26 CST | python | Accepted | 15 ms | 19.7 MB |
| 685048867 | 2025/12/16 09:05:00 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[m - 1][n - 1]
```

## 70. 爬楼梯 (`climbing-stairs`)

- 题目链接：https://leetcode.cn/problems/climbing-stairs/
- 难度：Easy
- 标签：Memoization, Math, Dynamic Programming
- 总提交次数：2
- 最近提交时间：2026/04/12 11:21:51 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 717354069 | 2026/04/12 11:21:51 CST | python | Accepted | 0 ms | 19.1 MB |
| 685827884 | 2025/12/19 15:59:44 CST | python | Accepted | 0 ms | 17 MB |

### 最近一次 AC 代码

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        prev_2, prev_1 = 1, 2
        for _ in range(3, n + 1):
            prev_2, prev_1 = prev_1, prev_1 + prev_2
        return prev_1
```

## 71. 简化路径 (`simplify-path`)

- 题目链接：https://leetcode.cn/problems/simplify-path/
- 难度：Medium
- 标签：Stack, String
- 总提交次数：5
- 最近提交时间：2026/03/27 07:59:05 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 712432425 | 2026/03/27 07:59:05 CST | python | Accepted | 0 ms | 19.2 MB |
| 712432404 | 2026/03/27 07:58:30 CST | python | Wrong Answer | N/A | N/A |
| 712078745 | 2026/03/26 09:57:09 CST | python | Accepted | 3 ms | 19.3 MB |
| 712078694 | 2026/03/26 09:56:59 CST | python | Wrong Answer | N/A | N/A |
| 712078631 | 2026/03/26 09:56:47 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for part in path.split('/'):
            if part == '.' or part == '':
                continue
            elif part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return '/' + '/'.join(stack)
```

## 72. 编辑距离 (`edit-distance`)

- 题目链接：https://leetcode.cn/problems/edit-distance/
- 难度：Medium
- 标签：String, Dynamic Programming
- 总提交次数：10
- 最近提交时间：2026/04/13 12:12:53 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 717649320 | 2026/04/13 12:12:53 CST | python | Accepted | 63 ms | 22.4 MB |
| 697946434 | 2026/02/11 14:17:04 CST | python | Accepted | 43 ms | 22.3 MB |
| 692374783 | 2026/01/19 11:16:13 CST | python | Accepted | 47 ms | 22.3 MB |
| 692374747 | 2026/01/19 11:16:06 CST | python | Runtime Error | N/A | N/A |
| 690376130 | 2026/01/10 17:29:42 CST | python | Accepted | 47 ms | 22.3 MB |
| 688277717 | 2025/12/31 13:52:50 CST | python | Accepted | 75 ms | 20.3 MB |
| 682002098 | 2025/12/01 22:00:35 CST | python | Accepted | 72 ms | 20.9 MB |
| 682002018 | 2025/12/01 22:00:19 CST | python | Runtime Error | N/A | N/A |
| 679406918 | 2025/11/20 11:12:15 CST | python | Accepted | 71 ms | 20.9 MB |
| 679406845 | 2025/11/20 11:12:01 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if not m * n:
            return m + n
        dp = [[0] *(n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            dp[i][0] = i
        for j in range(1, n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
        return dp[m][n]
```

## 74. 搜索二维矩阵 (`search-a-2d-matrix`)

- 题目链接：https://leetcode.cn/problems/search-a-2d-matrix/
- 难度：Medium
- 标签：Array, Binary Search, Matrix
- 总提交次数：5
- 最近提交时间：2026/03/19 13:50:33 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 709219609 | 2026/03/19 13:50:33 CST | python | Accepted | 0 ms | 19.4 MB |
| 709217748 | 2026/03/19 13:45:29 CST | python | Wrong Answer | N/A | N/A |
| 703392101 | 2026/03/06 13:42:13 CST | python | Accepted | 0 ms | 19.3 MB |
| 703391640 | 2026/03/06 13:40:50 CST | python | Wrong Answer | N/A | N/A |
| 685293541 | 2025/12/17 09:04:09 CST | python | Accepted | 0 ms | 17.9 MB |

### 最近一次 AC 代码

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_val = matrix[mid // n][mid % n]
            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
```

## 75. 颜色分类 (`sort-colors`)

- 题目链接：https://leetcode.cn/problems/sort-colors/
- 难度：Medium
- 标签：Array, Two Pointers, Sorting
- 总提交次数：5
- 最近提交时间：2026/03/23 13:44:24 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 710863129 | 2026/03/23 13:44:24 CST | python | Accepted | 0 ms | 19.2 MB |
| 708323988 | 2026/03/17 15:56:46 CST | python | Accepted | 0 ms | 19.1 MB |
| 708323477 | 2026/03/17 15:56:03 CST | python | Wrong Answer | N/A | N/A |
| 708321801 | 2026/03/17 15:53:38 CST | python | Wrong Answer | N/A | N/A |
| 708321654 | 2026/03/17 15:53:26 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
        n = len(nums)
        i = 0
        left = 0
        right =  n - 1
        while i <= right:
            if nums[i] == 0:
                swap(i, left)
                left += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                swap(i, right)
                right -= 1
```

## 76. 最小覆盖子串 (`minimum-window-substring`)

- 题目链接：https://leetcode.cn/problems/minimum-window-substring/
- 难度：Hard
- 标签：Hash Table, String, Sliding Window
- 总提交次数：20
- 最近提交时间：2026/03/18 09:52:54 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 708637166 | 2026/03/18 09:52:54 CST | python | Accepted | 67 ms | 19.4 MB |
| 677589092 | 2025/11/12 14:16:39 CST | python | Accepted | 94 ms | 17.9 MB |
| 677588261 | 2025/11/12 14:13:26 CST | python | Wrong Answer | N/A | N/A |
| 677587958 | 2025/11/12 14:12:09 CST | python | Wrong Answer | N/A | N/A |
| 675679440 | 2025/11/04 09:26:49 CST | python | Accepted | 63 ms | 18.2 MB |
| 662841333 | 2025/09/15 12:36:24 CST | python | Accepted | 69 ms | 17.8 MB |
| 660613691 | 2025/09/08 14:34:27 CST | python | Accepted | 90 ms | 18.1 MB |
| 660611366 | 2025/09/08 14:28:30 CST | python | Wrong Answer | N/A | N/A |
| 660610029 | 2025/09/08 14:25:10 CST | python | Time Limit Exceeded | N/A | N/A |
| 660601783 | 2025/09/08 13:59:57 CST | python | Wrong Answer | N/A | N/A |
| 658740985 | 2025/09/02 14:35:06 CST | python | Accepted | 111 ms | 18.1 MB |
| 658735712 | 2025/09/02 14:21:28 CST | python | Wrong Answer | N/A | N/A |
| 658734227 | 2025/09/02 14:17:29 CST | python | Runtime Error | N/A | N/A |
| 658731149 | 2025/09/02 14:08:34 CST | python | Wrong Answer | N/A | N/A |
| 658730404 | 2025/09/02 14:06:17 CST | python | Wrong Answer | N/A | N/A |
| 658730208 | 2025/09/02 14:05:42 CST | python | Runtime Error | N/A | N/A |
| 658730052 | 2025/09/02 14:05:10 CST | python | Runtime Error | N/A | N/A |
| 650614334 | 2025/08/07 07:33:30 CST | python | Accepted | 71 ms | 18.1 MB |
| 650289033 | 2025/08/06 09:35:27 CST | python | Accepted | 63 ms | 17.9 MB |
| 650277735 | 2025/08/06 08:20:47 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        window = collections.defaultdict(int)
        start = 0
        min_len = float('inf')
        left = 0
        valid = 0
        for right, r_char in enumerate(s):
            if r_char in need:
                window[r_char] += 1
                if window[r_char] == need[r_char]:
                    valid += 1
            while valid == len(need):
                curr_len = right - left + 1
                if curr_len < min_len:
                    min_len = curr_len
                    start = left
                l_char = s[left]
                if l_char in need:
                    if window[l_char] == need[l_char]:
                        valid -= 1
                    window[l_char] -= 1
                left += 1
        return s[start : start + min_len] if min_len != float(inf) else ''
```

## 77. 组合 (`combinations`)

- 题目链接：https://leetcode.cn/problems/combinations/
- 难度：Medium
- 标签：Backtracking
- 总提交次数：6
- 最近提交时间：2026/04/08 18:50:01 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 716330286 | 2026/04/08 18:50:01 CST | python | Accepted | 139 ms | 60.1 MB |
| 716330216 | 2026/04/08 18:49:40 CST | python | Wrong Answer | N/A | N/A |
| 698963136 | 2026/02/16 21:27:59 CST | python | Accepted | 215 ms | 60.3 MB |
| 698836970 | 2026/02/15 21:18:08 CST | python | Accepted | 127 ms | 60.2 MB |
| 687343695 | 2025/12/26 18:03:10 CST | python | Accepted | 243 ms | 58.3 MB |
| 685312612 | 2025/12/17 10:36:45 CST | python | Accepted | 147 ms | 58.7 MB |

### 最近一次 AC 代码

```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        def backtrack(start):
            if len(path) == k:
                res.append(list(path))
                return 
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1)
                path.pop()
        backtrack(1)
        return res
```

## 78. 子集 (`subsets`)

- 题目链接：https://leetcode.cn/problems/subsets/
- 难度：Medium
- 标签：Bit Manipulation, Array, Backtracking
- 总提交次数：7
- 最近提交时间：2026/04/08 18:46:20 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 716329376 | 2026/04/08 18:46:20 CST | python | Accepted | 0 ms | 19.3 MB |
| 698965975 | 2026/02/16 22:02:33 CST | python | Accepted | 3 ms | 19.1 MB |
| 687332047 | 2025/12/26 17:12:37 CST | python | Accepted | 3 ms | 17.4 MB |
| 683405933 | 2025/12/08 14:40:16 CST | python | Accepted | 0 ms | 17.8 MB |
| 683016774 | 2025/12/06 14:26:36 CST | python | Accepted | 0 ms | 17.8 MB |
| 683016526 | 2025/12/06 14:25:08 CST | python | Wrong Answer | N/A | N/A |
| 682597940 | 2025/12/04 12:35:50 CST | python | Accepted | 0 ms | 17.8 MB |

### 最近一次 AC 代码

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        n = len(nums)
        def backtrack(start_idx):
            res.append(list(path))
            for i in range(start_idx, n):
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()
        backtrack(0)
        return res
```

## 79. 单词搜索 (`word-search`)

- 题目链接：https://leetcode.cn/problems/word-search/
- 难度：Medium
- 标签：Depth-First Search, Array, String, Backtracking, Matrix
- 总提交次数：3
- 最近提交时间：2026/04/09 12:30:35 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 716520603 | 2026/04/09 12:30:35 CST | python | Accepted | 3634 ms | 19.3 MB |
| 687872640 | 2025/12/29 15:31:02 CST | python | Accepted | 3220 ms | 17.1 MB |
| 687872018 | 2025/12/29 15:29:08 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        L = len(word)
        def backtrack(r, c, idx):
            if board[r][c] != word[idx]:
                return False
            if idx == L - 1:
                return True
            board[r][c] = '#'
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    if backtrack(nr, nc, idx + 1):
                        return True
            board[r][c] = word[idx]
            return False
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True
        return False
```

## 80. 删除有序数组中的重复项 II (`remove-duplicates-from-sorted-array-ii`)

- 题目链接：https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/
- 难度：Medium
- 标签：Array, Two Pointers
- 总提交次数：5
- 最近提交时间：2026/03/17 15:27:04 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 708301730 | 2026/03/17 15:27:04 CST | python | Accepted | 96 ms | 21.7 MB |
| 679648011 | 2025/11/21 11:18:54 CST | python | Accepted | 99 ms | 20.1 MB |
| 679647852 | 2025/11/21 11:18:23 CST | python | Runtime Error | N/A | N/A |
| 679647782 | 2025/11/21 11:18:07 CST | python | Runtime Error | N/A | N/A |
| 665553970 | 2025/09/24 11:15:34 CST | python | Accepted | 89 ms | 20.2 MB |

### 最近一次 AC 代码

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        slow = 2
        for fast in range(2, n):
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1
        return slow
```

## 81. 搜索旋转排序数组 II (`search-in-rotated-sorted-array-ii`)

- 题目链接：https://leetcode.cn/problems/search-in-rotated-sorted-array-ii/
- 难度：Medium
- 标签：Array, Binary Search
- 总提交次数：2
- 最近提交时间：2026/03/24 10:52:41 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 711260857 | 2026/03/24 10:52:41 CST | python | Accepted | 0 ms | 19.2 MB |
| 709822919 | 2026/03/20 18:33:21 CST | python | Accepted | 0 ms | 19.5 MB |

### 最近一次 AC 代码

```python
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
```

## 82. 删除排序链表中的重复元素 II (`remove-duplicates-from-sorted-list-ii`)

- 题目链接：https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/
- 难度：Medium
- 标签：Linked List, Two Pointers
- 总提交次数：4
- 最近提交时间：2026/04/01 08:26:24 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 714084989 | 2026/04/01 08:26:24 CST | python | Accepted | 0 ms | 19.3 MB |
| 713801472 | 2026/03/31 13:10:24 CST | python | Accepted | 0 ms | 19 MB |
| 683811198 | 2025/12/10 09:02:03 CST | python | Accepted | 4 ms | 17.4 MB |
| 646850181 | 2025/07/25 09:36:03 CST | python | Accepted | 0 ms | 17.5 MB |

### 最近一次 AC 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        while curr:
            if curr.next and curr.val == curr.next.val:
                dup_val = curr.val
                while curr and curr.val == dup_val:
                    curr = curr.next
                prev.next = curr
            else:
                prev = curr
                curr = curr.next
        return dummy.next
```

## 83. 删除排序链表中的重复元素 (`remove-duplicates-from-sorted-list`)

- 题目链接：https://leetcode.cn/problems/remove-duplicates-from-sorted-list/
- 难度：Easy
- 标签：Linked List
- 总提交次数：3
- 最近提交时间：2026/03/17 11:41:26 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 708204288 | 2026/03/17 11:41:26 CST | python | Accepted | 3 ms | 19 MB |
| 683807965 | 2025/12/10 08:21:42 CST | python | Accepted | 0 ms | 17.7 MB |
| 649584787 | 2025/08/04 07:57:00 CST | python | Accepted | 0 ms | 17.4 MB |

### 最近一次 AC 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
```

## 84. 柱状图中最大的矩形 (`largest-rectangle-in-histogram`)

- 题目链接：https://leetcode.cn/problems/largest-rectangle-in-histogram/
- 难度：Hard
- 标签：Stack, Array, Monotonic Stack
- 总提交次数：4
- 最近提交时间：2026/03/28 09:21:54 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 712756316 | 2026/03/28 09:21:54 CST | python | Accepted | 127 ms | 31.3 MB |
| 712756213 | 2026/03/28 09:21:00 CST | python | Runtime Error | N/A | N/A |
| 712494546 | 2026/03/27 11:46:00 CST | python | Accepted | 191 ms | 31.2 MB |
| 712494482 | 2026/03/27 11:45:49 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        new_heights = [0] + heights + [0]
        max_area = 0
        stack = []
        for i, num in enumerate(new_heights):
            while stack and new_heights[stack[-1]] > num:
                curr_idx = stack.pop()
                curr_height = new_heights[curr_idx]
                left_idx = stack[-1]
                width = i - left_idx - 1
                max_area = max(max_area, curr_height * width)
            stack.append(i)
        return max_area
```

## 86. 分隔链表 (`partition-list`)

- 题目链接：https://leetcode.cn/problems/partition-list/
- 难度：Medium
- 标签：Linked List, Two Pointers
- 总提交次数：4
- 最近提交时间：2026/03/31 10:11:37 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 713741608 | 2026/03/31 10:11:37 CST | python | Accepted | 0 ms | 19.1 MB |
| 683576757 | 2025/12/09 09:44:14 CST | python | Accepted | 0 ms | 17.4 MB |
| 683576330 | 2025/12/09 09:41:56 CST | python | Runtime Error | N/A | N/A |
| 645150718 | 2025/07/19 08:20:43 CST | python | Accepted | 0 ms | 17.7 MB |

### 最近一次 AC 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small_dummy = ListNode()
        large_dummy = ListNode()
        small_tail = small_dummy
        large_tail = large_dummy
        curr = head
        while curr:
            next_node = curr.next
            if curr.val < x:
                small_tail.next = curr
                small_tail = small_tail.next
            else:
                large_tail.next = curr
                large_tail = large_tail.next
            curr.next = None
            curr = next_node
        small_tail.next = large_dummy.next
        return small_dummy.next
```

## 88. 合并两个有序数组 (`merge-sorted-array`)

- 题目链接：https://leetcode.cn/problems/merge-sorted-array/
- 难度：Easy
- 标签：Array, Two Pointers, Sorting
- 总提交次数：3
- 最近提交时间：2026/03/17 16:05:29 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 708330085 | 2026/03/17 16:05:29 CST | python | Accepted | 0 ms | 19.2 MB |
| 682402229 | 2025/12/03 15:44:18 CST | python | Accepted | 0 ms | 17.6 MB |
| 665877273 | 2025/09/25 13:05:26 CST | python | Accepted | 0 ms | 17.8 MB |

### 最近一次 AC 代码

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        tail = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[tail] = nums1[p1]
                p1 -= 1
            else:
                nums1[tail] = nums2[p2]
                p2 -= 1
            tail -= 1
        
        if p2 >= 0:
            nums1[:p2+1] = nums2[:p2+1]
```

## 89. 格雷编码 (`gray-code`)

- 题目链接：https://leetcode.cn/problems/gray-code/
- 难度：Medium
- 标签：Bit Manipulation, Math, Backtracking
- 总提交次数：3
- 最近提交时间：2026/02/22 17:24:58 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 699813270 | 2026/02/22 17:24:58 CST | python | Accepted | 8 ms | 22.2 MB |
| 687857501 | 2025/12/29 14:39:33 CST | python | Accepted | 62 ms | 36 MB |
| 687855499 | 2025/12/29 14:32:05 CST | python | Accepted | 59 ms | 36 MB |

### 最近一次 AC 代码

```python
class Solution:
    def grayCode(self, n: int) -> List[int]:
        return [i ^ (i >> 1) for i in range(1 << n)]
```

## 90. 子集 II (`subsets-ii`)

- 题目链接：https://leetcode.cn/problems/subsets-ii/
- 难度：Medium
- 标签：Bit Manipulation, Array, Backtracking
- 总提交次数：8
- 最近提交时间：2026/04/08 21:01:49 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 716376173 | 2026/04/08 21:01:49 CST | python | Accepted | 0 ms | 19.2 MB |
| 699292265 | 2026/02/19 14:04:52 CST | python | Accepted | 0 ms | 19.3 MB |
| 687378511 | 2025/12/26 21:35:28 CST | python | Accepted | 0 ms | 17.2 MB |
| 687378373 | 2025/12/26 21:34:39 CST | python | Runtime Error | N/A | N/A |
| 683411461 | 2025/12/08 14:59:53 CST | python | Accepted | 0 ms | 17.9 MB |
| 683408046 | 2025/12/08 14:48:10 CST | python | Wrong Answer | N/A | N/A |
| 683019300 | 2025/12/06 14:39:58 CST | python | Accepted | 0 ms | 17.7 MB |
| 683018964 | 2025/12/06 14:38:17 CST | python | Memory Limit Exceeded | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        path = []
        res = []
        n = len(nums)
        def backtrack(start_idx):
            res.append(list(path))
            for i in range(start_idx, n):
                if i > start_idx and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()
        backtrack(0)
        return res
```

## 92. 反转链表 II (`reverse-linked-list-ii`)

- 题目链接：https://leetcode.cn/problems/reverse-linked-list-ii/
- 难度：Medium
- 标签：Linked List
- 总提交次数：7
- 最近提交时间：2026/04/02 10:34:34 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 714458847 | 2026/04/02 10:34:34 CST | python | Accepted | 0 ms | 19.2 MB |
| 714103672 | 2026/04/01 10:06:30 CST | python | Accepted | 0 ms | 19.1 MB |
| 685796587 | 2025/12/19 13:56:43 CST | python | Accepted | 0 ms | 17.2 MB |
| 685552831 | 2025/12/18 11:14:38 CST | python | Accepted | 0 ms | 17.1 MB |
| 684107820 | 2025/12/11 14:21:38 CST | python | Accepted | 0 ms | 17.8 MB |
| 684107730 | 2025/12/11 14:21:19 CST | python | Wrong Answer | N/A | N/A |
| 682052295 | 2025/12/02 08:53:18 CST | python | Accepted | 0 ms | 17.5 MB |

### 最近一次 AC 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        pre = dummy
        for _ in range(left - 1):
            pre = pre.next
        
        start = pre.next
        for _ in range(right - left):
            next_node = start.next
            start.next = next_node.next
            next_node.next = pre.next
            pre.next = next_node
        return dummy.next
```

## 93. 复原 IP 地址 (`restore-ip-addresses`)

- 题目链接：https://leetcode.cn/problems/restore-ip-addresses/
- 难度：Medium
- 标签：String, Backtracking
- 总提交次数：24
- 最近提交时间：2026/04/09 10:56:32 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 716492757 | 2026/04/09 10:56:32 CST | python | Accepted | 0 ms | 19.4 MB |
| 716492343 | 2026/04/09 10:55:31 CST | python | Wrong Answer | N/A | N/A |
| 716491864 | 2026/04/09 10:54:19 CST | python | Wrong Answer | N/A | N/A |
| 716491732 | 2026/04/09 10:53:56 CST | python | Wrong Answer | N/A | N/A |
| 716491675 | 2026/04/09 10:53:44 CST | python | Runtime Error | N/A | N/A |
| 699667818 | 2026/02/21 20:40:43 CST | python | Accepted | 0 ms | 19.4 MB |
| 699667344 | 2026/02/21 20:37:53 CST | python | Wrong Answer | N/A | N/A |
| 699666759 | 2026/02/21 20:34:44 CST | python | Wrong Answer | N/A | N/A |
| 699666704 | 2026/02/21 20:34:28 CST | python | Runtime Error | N/A | N/A |
| 687838456 | 2025/12/29 12:52:55 CST | python | Accepted | 0 ms | 17.1 MB |
| 687697906 | 2025/12/28 18:09:38 CST | python | Accepted | 3 ms | 16.9 MB |
| 687697581 | 2025/12/28 18:07:42 CST | python | Wrong Answer | N/A | N/A |
| 683414673 | 2025/12/08 15:10:00 CST | python | Accepted | 0 ms | 17.5 MB |
| 683414273 | 2025/12/08 15:08:37 CST | python | Wrong Answer | N/A | N/A |
| 683027883 | 2025/12/06 15:20:06 CST | python | Accepted | 0 ms | 17.5 MB |
| 683027439 | 2025/12/06 15:18:08 CST | python | Wrong Answer | N/A | N/A |
| 683027249 | 2025/12/06 15:17:20 CST | python | Wrong Answer | N/A | N/A |
| 681820899 | 2025/12/01 10:43:48 CST | python | Accepted | 0 ms | 17.7 MB |
| 681608604 | 2025/11/30 10:40:53 CST | python | Accepted | 3 ms | 17.5 MB |
| 681551995 | 2025/11/29 21:20:26 CST | python | Accepted | 0 ms | 17.8 MB |
| 681502389 | 2025/11/29 16:36:25 CST | python | Accepted | 0 ms | 17.8 MB |
| 681502367 | 2025/11/29 16:36:19 CST | python | Accepted | 3 ms | 17.7 MB |
| 681502289 | 2025/11/29 16:35:55 CST | python | Wrong Answer | N/A | N/A |
| 681502094 | 2025/11/29 16:34:55 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_valid(segment):
            if len(segment) > 1 and segment[0] == '0':
                return False
            if int(segment) > 255:
                return False
            return True
        path = []
        res = []
        n = len(s)
        def backtrack(start_idx):
            if len(path) == 4 and start_idx == n:
                res.append('.'.join(path))
                return
            remaining_chars = n - start_idx
            remaining_segments = 4 - len(path)
            if remaining_chars < remaining_segments or remaining_chars > 3 * remaining_segments:
                return
            for length in range(1, 4):
                end_idx = start_idx + length
                if end_idx > n:
                    break
                segment = s[start_idx : end_idx]
                if not is_valid(segment):
                    continue
                path.append(segment)
                backtrack(end_idx)
                path.pop()
        backtrack(0)
        return res
```

## 94. 二叉树的中序遍历 (`binary-tree-inorder-traversal`)

- 题目链接：https://leetcode.cn/problems/binary-tree-inorder-traversal/
- 难度：Easy
- 标签：Stack, Tree, Depth-First Search, Binary Tree
- 总提交次数：9
- 最近提交时间：2026/04/03 08:28:23 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 714752711 | 2026/04/03 08:28:23 CST | python | Accepted | 0 ms | 19.1 MB |
| 714752699 | 2026/04/03 08:28:16 CST | python | Runtime Error | N/A | N/A |
| 714485118 | 2026/04/02 11:37:41 CST | python | Accepted | 0 ms | 19.2 MB |
| 714480634 | 2026/04/02 11:26:23 CST | python | Accepted | 0 ms | 19 MB |
| 701725366 | 2026/03/02 12:25:57 CST | python | Accepted | 0 ms | 19.1 MB |
| 684599087 | 2025/12/13 22:05:22 CST | python | Accepted | 0 ms | 17.4 MB |
| 684596583 | 2025/12/13 21:51:39 CST | python | Accepted | 0 ms | 17.4 MB |
| 684563249 | 2025/12/13 18:30:14 CST | python | Accepted | 0 ms | 17.5 MB |
| 681993183 | 2025/12/01 21:30:53 CST | python | Accepted | 0 ms | 17.4 MB |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res
```

## 95. 不同的二叉搜索树 II (`unique-binary-search-trees-ii`)

- 题目链接：https://leetcode.cn/problems/unique-binary-search-trees-ii/
- 难度：Medium
- 标签：Tree, Binary Search Tree, Dynamic Programming, Backtracking, Binary Tree
- 总提交次数：3
- 最近提交时间：2026/04/04 11:19:03 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715029827 | 2026/04/04 11:19:03 CST | python | Accepted | 7 ms | 20.1 MB |
| 714885002 | 2026/04/03 16:36:40 CST | python | Accepted | 4 ms | 20.1 MB |
| 714884774 | 2026/04/03 16:36:09 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def _build(low, high):
            if low > high:
                return [None]
            all_trees = []
            for root_val in range(low, high + 1):
                left_trees = _build(low, root_val - 1)
                right_trees = _build(root_val + 1, high)
                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(root_val)
                        root.left = left
                        root.right = right
                        all_trees.append(root)
            return all_trees
        return _build(1, n)
```

## 96. 不同的二叉搜索树 (`unique-binary-search-trees`)

- 题目链接：https://leetcode.cn/problems/unique-binary-search-trees/
- 难度：Medium
- 标签：Tree, Binary Search Tree, Math, Dynamic Programming, Binary Tree
- 总提交次数：2
- 最近提交时间：2026/04/04 11:09:06 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715027724 | 2026/04/04 11:09:06 CST | python | Accepted | 0 ms | 19.2 MB |
| 714865891 | 2026/04/03 15:49:13 CST | python | Accepted | 0 ms | 19.3 MB |

### 最近一次 AC 代码

```python
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            total = 0
            for root in range(1, i + 1):
                left_count = root - 1
                right_count = i - root
                total += dp[left_count] * dp[right_count]
            dp[i] = total
        return dp[n]
```

## 97. 交错字符串 (`interleaving-string`)

- 题目链接：https://leetcode.cn/problems/interleaving-string/
- 难度：Medium
- 标签：String, Dynamic Programming
- 总提交次数：8
- 最近提交时间：2026/02/14 11:47:19 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 698554609 | 2026/02/14 11:47:19 CST | python | Accepted | 66 ms | 19.1 MB |
| 695796378 | 2026/02/02 10:56:51 CST | python | Accepted | 47 ms | 19.4 MB |
| 695661623 | 2026/02/01 17:10:09 CST | python | Accepted | 51 ms | 19.1 MB |
| 695661225 | 2026/02/01 17:08:37 CST | python | Wrong Answer | N/A | N/A |
| 692419116 | 2026/01/19 14:39:14 CST | python | Accepted | 70 ms | 19.2 MB |
| 692419047 | 2026/01/19 14:39:00 CST | python | Runtime Error | N/A | N/A |
| 690751806 | 2026/01/12 13:37:53 CST | python | Accepted | 53 ms | 19.4 MB |
| 690746726 | 2026/01/12 13:06:00 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                k = i + j - 1
                if dp[i - 1][j] and s1[i - 1] == s3[k]:
                    dp[i][j] = True
                    continue
                if dp[i][j - 1] and s2[j - 1] == s3[k]:
                    dp[i][j] = True
        return dp[m][n]
```

## 98. 验证二叉搜索树 (`validate-binary-search-tree`)

- 题目链接：https://leetcode.cn/problems/validate-binary-search-tree/
- 难度：Medium
- 标签：Tree, Depth-First Search, Binary Search Tree, Binary Tree
- 总提交次数：2
- 最近提交时间：2026/04/04 10:38:24 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715020964 | 2026/04/04 10:38:24 CST | python | Accepted | 0 ms | 20.8 MB |
| 714827010 | 2026/04/03 13:58:15 CST | python | Accepted | 4 ms | 20.6 MB |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lower, upper):
            if not node:
                return True
            if not (lower < node.val < upper):
                return False
            return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)
        return dfs(root, float('-inf'), float('inf'))
```

## 102. 二叉树的层序遍历 (`binary-tree-level-order-traversal`)

- 题目链接：https://leetcode.cn/problems/binary-tree-level-order-traversal/
- 难度：Medium
- 标签：Tree, Breadth-First Search, Binary Tree
- 总提交次数：5
- 最近提交时间：2026/04/02 12:53:57 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 714501926 | 2026/04/02 12:53:57 CST | python | Accepted | 0 ms | 19.6 MB |
| 700850689 | 2026/02/27 08:45:00 CST | python | Accepted | 0 ms | 19.8 MB |
| 684561088 | 2025/12/13 18:13:10 CST | python | Accepted | 3 ms | 18.1 MB |
| 680723563 | 2025/11/26 08:34:47 CST | python | Accepted | 0 ms | 18.2 MB |
| 680723262 | 2025/11/26 08:30:34 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        dq = collections.deque([root])
        while dq:
            sz = len(dq)
            level_vals = []
            for _ in range(sz):
                node = dq.popleft()
                level_vals.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            res.append(level_vals)
        return res
```

## 103. 二叉树的锯齿形层序遍历 (`binary-tree-zigzag-level-order-traversal`)

- 题目链接：https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal/
- 难度：Medium
- 标签：Tree, Breadth-First Search, Binary Tree
- 总提交次数：4
- 最近提交时间：2026/02/27 09:56:20 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 700859967 | 2026/02/27 09:56:20 CST | python | Accepted | 0 ms | 19.3 MB |
| 685959425 | 2025/12/20 12:26:42 CST | python | Accepted | 0 ms | 17.4 MB |
| 685831111 | 2025/12/19 16:11:04 CST | python | Accepted | 0 ms | 17.1 MB |
| 685830927 | 2025/12/19 16:10:26 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        dq = collections.deque([root])
        res = []
        left_to_right = True
        while dq:
            sz = len(dq)
            level_vals = []
            for _ in range(sz):
                node = dq.popleft()
                level_vals.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            if not left_to_right:
                level_vals.reverse()
            res.append(level_vals)
            left_to_right = not left_to_right
        return res
```

## 104. 二叉树的最大深度 (`maximum-depth-of-binary-tree`)

- 题目链接：https://leetcode.cn/problems/maximum-depth-of-binary-tree/
- 难度：Easy
- 标签：Tree, Depth-First Search, Breadth-First Search, Binary Tree
- 总提交次数：6
- 最近提交时间：2026/04/03 10:03:41 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 714766866 | 2026/04/03 10:03:41 CST | python | Accepted | 0 ms | 20.1 MB |
| 714542931 | 2026/04/02 15:10:12 CST | python | Accepted | 7 ms | 20.1 MB |
| 701451646 | 2026/03/01 15:04:50 CST | python | Accepted | 0 ms | 19.9 MB |
| 701111308 | 2026/02/28 08:41:07 CST | python | Accepted | 0 ms | 20.2 MB |
| 684857278 | 2025/12/15 12:40:39 CST | python | Accepted | 0 ms | 18.7 MB |
| 680118503 | 2025/11/23 17:56:35 CST | python | Accepted | 0 ms | 18.7 MB |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return max(left_height, right_height) + 1
```

## 105. 从前序与中序遍历序列构造二叉树 (`construct-binary-tree-from-preorder-and-inorder-traversal`)

- 题目链接：https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
- 难度：Medium
- 标签：Tree, Array, Hash Table, Divide and Conquer, Binary Tree
- 总提交次数：6
- 最近提交时间：2026/04/07 08:42:10 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715790532 | 2026/04/07 08:42:10 CST | python | Accepted | 0 ms | 20.9 MB |
| 715790501 | 2026/04/07 08:41:53 CST | python | Runtime Error | N/A | N/A |
| 701662482 | 2026/03/02 09:51:45 CST | python | Accepted | 3 ms | 20.9 MB |
| 701662233 | 2026/03/02 09:50:47 CST | python | Runtime Error | N/A | N/A |
| 701662166 | 2026/03/02 09:50:29 CST | python | Runtime Error | N/A | N/A |
| 687075251 | 2025/12/25 15:20:51 CST | python | Accepted | 3 ms | 18.5 MB |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val : idx for idx, val in enumerate(inorder)}
        n = len(preorder)
        def _build(pre_start, pre_end, in_start, in_end):
            if pre_start >= pre_end or in_start >= in_end:
                return None
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            root_idx = inorder_map.get(root_val)
            size = root_idx - in_start
            root.left = _build(pre_start + 1, pre_start + 1 + size, in_start, root_idx)
            root.right = _build(pre_start + 1 + size, pre_end, root_idx + 1, in_end)
            return root
        return _build(0, n, 0, n)
```

## 106. 从中序与后序遍历序列构造二叉树 (`construct-binary-tree-from-inorder-and-postorder-traversal`)

- 题目链接：https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
- 难度：Medium
- 标签：Tree, Array, Hash Table, Divide and Conquer, Binary Tree
- 总提交次数：8
- 最近提交时间：2026/04/07 09:19:04 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715795616 | 2026/04/07 09:19:04 CST | python | Accepted | 0 ms | 21 MB |
| 715795517 | 2026/04/07 09:18:33 CST | python | Time Limit Exceeded | N/A | N/A |
| 715795413 | 2026/04/07 09:18:00 CST | python | Runtime Error | N/A | N/A |
| 701665483 | 2026/03/02 10:02:38 CST | python | Accepted | 3 ms | 20.9 MB |
| 701665184 | 2026/03/02 10:01:40 CST | python | Time Limit Exceeded | N/A | N/A |
| 687087475 | 2025/12/25 15:59:53 CST | python | Accepted | 0 ms | 18.5 MB |
| 687087026 | 2025/12/25 15:58:28 CST | python | Runtime Error | N/A | N/A |
| 687086776 | 2025/12/25 15:57:38 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val : idx for idx, val in enumerate(inorder)}
        n = len(inorder)
        def _build(in_start, in_end, post_start, post_end):
            if in_start >= in_end or post_start >= post_end:
                return
            root_val = postorder[post_end - 1]
            root_idx = inorder_map.get(root_val)
            size = root_idx - in_start
            root = TreeNode(root_val)
            root.left = _build(in_start, root_idx, post_start, post_start + size)
            root.right = _build(root_idx + 1, in_end, post_start + size, post_end - 1)
            return root
        return _build(0, n, 0, n)
```

## 107. 二叉树的层序遍历 II (`binary-tree-level-order-traversal-ii`)

- 题目链接：https://leetcode.cn/problems/binary-tree-level-order-traversal-ii/
- 难度：Medium
- 标签：Tree, Breadth-First Search, Binary Tree
- 总提交次数：3
- 最近提交时间：2026/02/27 08:49:37 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 700850988 | 2026/02/27 08:49:37 CST | python | Accepted | 0 ms | 19.2 MB |
| 685956812 | 2025/12/20 12:04:41 CST | python | Accepted | 0 ms | 17.3 MB |
| 685956631 | 2025/12/20 12:03:08 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        dq = collections.deque([root])
        res = collections.deque()
        while dq:
            level_size = len(dq)
            level_vals = []
            for _ in range(level_size):
                node = dq.popleft()
                level_vals.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            res.appendleft(level_vals)
        return list(res)
```

## 108. 将有序数组转换为二叉搜索树 (`convert-sorted-array-to-binary-search-tree`)

- 题目链接：https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/
- 难度：Easy
- 标签：Tree, Binary Search Tree, Array, Divide and Conquer, Binary Tree
- 总提交次数：1
- 最近提交时间：2026/03/02 10:46:22 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 701681338 | 2026/03/02 10:46:22 CST | python | Accepted | 0 ms | 20.1 MB |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(left, right):
            if left >= right:
                return
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = build(left, mid)
            root.right = build(mid + 1, right)
            return root
        return build(0, len(nums))
```

## 110. 平衡二叉树 (`balanced-binary-tree`)

- 题目链接：https://leetcode.cn/problems/balanced-binary-tree/
- 难度：Easy
- 标签：Tree, Depth-First Search, Binary Tree
- 总提交次数：9
- 最近提交时间：2026/02/28 08:46:39 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 701111696 | 2026/02/28 08:46:39 CST | python | Accepted | 0 ms | 20 MB |
| 685797734 | 2025/12/19 14:03:10 CST | python | Accepted | 0 ms | 18.1 MB |
| 685548668 | 2025/12/18 11:00:04 CST | python | Accepted | 0 ms | 18 MB |
| 685548615 | 2025/12/18 10:59:55 CST | python | Runtime Error | N/A | N/A |
| 685079399 | 2025/12/16 11:20:30 CST | python | Accepted | 0 ms | 18.5 MB |
| 685079204 | 2025/12/16 11:19:51 CST | python | Wrong Answer | N/A | N/A |
| 685078656 | 2025/12/16 11:17:52 CST | python | Wrong Answer | N/A | N/A |
| 685078536 | 2025/12/16 11:17:27 CST | python | Runtime Error | N/A | N/A |
| 685078262 | 2025/12/16 11:16:33 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced, _ = self._check(root)
        return is_balanced
    
    def _check(self, node):
        if not node:
            return True, 0

        left_balanced, left_height = self._check(node.left)
        if not left_balanced:
            return False, 0
        
        right_balanced, right_height = self._check(node.right)
        if not right_balanced:
            return False, 0
        
        if abs(left_height - right_height) > 1:
            return False, 0
        
        return True, max(left_height, right_height) + 1
```

## 111. 二叉树的最小深度 (`minimum-depth-of-binary-tree`)

- 题目链接：https://leetcode.cn/problems/minimum-depth-of-binary-tree/
- 难度：Easy
- 标签：Tree, Depth-First Search, Breadth-First Search, Binary Tree
- 总提交次数：4
- 最近提交时间：2026/04/02 14:53:10 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 714535794 | 2026/04/02 14:53:10 CST | python | Accepted | 0 ms | 44.2 MB |
| 701121515 | 2026/02/28 10:02:35 CST | python | Accepted | 3 ms | 43.4 MB |
| 701121494 | 2026/02/28 10:02:28 CST | python | Runtime Error | N/A | N/A |
| 684866812 | 2025/12/15 13:48:04 CST | python | Accepted | 2 ms | 48.9 MB |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        dq = collections.deque([root])
        depth = 1
        while dq:
            sz = len(dq)
            for _ in range(sz):
                node = dq.popleft()
                if not node.left and not node.right:
                    return depth
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            depth += 1
```

## 114. 二叉树展开为链表 (`flatten-binary-tree-to-linked-list`)

- 题目链接：https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/
- 难度：Medium
- 标签：Stack, Tree, Depth-First Search, Linked List, Binary Tree
- 总提交次数：6
- 最近提交时间：2026/04/06 10:03:12 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715518020 | 2026/04/06 10:03:12 CST | python | Accepted | 0 ms | 19.4 MB |
| 702074589 | 2026/03/03 10:38:41 CST | python | Accepted | 0 ms | 19.3 MB |
| 687020486 | 2025/12/25 10:51:27 CST | python | Accepted | 0 ms | 17.1 MB |
| 687019976 | 2025/12/25 10:49:43 CST | python | Time Limit Exceeded | N/A | N/A |
| 687013093 | 2025/12/25 10:24:26 CST | python | Accepted | 0 ms | 17.2 MB |
| 687012993 | 2025/12/25 10:23:58 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        while curr:
            if curr.left:
                pre = curr.left
                while pre.right:
                    pre = pre.right
                pre.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right
```

## 115. 不同的子序列 (`distinct-subsequences`)

- 题目链接：https://leetcode.cn/problems/distinct-subsequences/
- 难度：Hard
- 标签：String, Dynamic Programming
- 总提交次数：9
- 最近提交时间：2026/02/14 13:52:14 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 698571208 | 2026/02/14 13:52:14 CST | python | Accepted | 422 ms | 74.4 MB |
| 694619323 | 2026/01/28 10:27:34 CST | python | Accepted | 419 ms | 74.3 MB |
| 694331578 | 2026/01/27 08:44:42 CST | python | Accepted | 419 ms | 74 MB |
| 694083367 | 2026/01/26 10:10:31 CST | python | Accepted | 427 ms | 73.9 MB |
| 694082957 | 2026/01/26 10:08:38 CST | python | Wrong Answer | N/A | N/A |
| 693994063 | 2026/01/25 19:57:29 CST | python | Accepted | 547 ms | 74.4 MB |
| 693994020 | 2026/01/25 19:57:15 CST | python | Runtime Error | N/A | N/A |
| 693791958 | 2026/01/24 20:57:18 CST | python | Accepted | 471 ms | 74.2 MB |
| 693581042 | 2026/01/23 19:45:39 CST | python | Accepted | 463 ms | 74.1 MB |

### 最近一次 AC 代码

```python
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[m][n]
```

## 116. 填充每个节点的下一个右侧节点指针 (`populating-next-right-pointers-in-each-node`)

- 题目链接：https://leetcode.cn/problems/populating-next-right-pointers-in-each-node/
- 难度：Medium
- 标签：Tree, Depth-First Search, Breadth-First Search, Linked List, Binary Tree
- 总提交次数：10
- 最近提交时间：2026/04/06 09:32:59 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715513780 | 2026/04/06 09:32:59 CST | python | Accepted | 56 ms | 20.3 MB |
| 700887820 | 2026/02/27 11:27:12 CST | python | Accepted | 67 ms | 20.6 MB |
| 700887553 | 2026/02/27 11:26:27 CST | python | Time Limit Exceeded | N/A | N/A |
| 687000364 | 2025/12/25 09:25:37 CST | python | Accepted | 56 ms | 18.4 MB |
| 686537660 | 2025/12/23 09:12:08 CST | python | Accepted | 56 ms | 18.6 MB |
| 686293054 | 2025/12/22 09:16:13 CST | python | Accepted | 50 ms | 18.3 MB |
| 686110091 | 2025/12/21 09:32:16 CST | python | Accepted | 51 ms | 18.7 MB |
| 685998660 | 2025/12/20 15:59:27 CST | python | Accepted | 53 ms | 18.4 MB |
| 685979434 | 2025/12/20 14:47:30 CST | python | Accepted | 45 ms | 18.5 MB |
| 685978989 | 2025/12/20 14:45:16 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        level_head = root
        while level_head:
            if not level_head.left:
                break
            curr = level_head
            while curr:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                curr = curr.next
            level_head = level_head.left
        return root
```

## 117. 填充每个节点的下一个右侧节点指针 II (`populating-next-right-pointers-in-each-node-ii`)

- 题目链接：https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/
- 难度：Medium
- 标签：Tree, Depth-First Search, Breadth-First Search, Linked List, Binary Tree
- 总提交次数：10
- 最近提交时间：2026/04/06 09:36:30 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715514225 | 2026/04/06 09:36:30 CST | python | Accepted | 62 ms | 20.2 MB |
| 715336762 | 2026/04/05 16:26:35 CST | python | Accepted | 58 ms | 20.1 MB |
| 700891119 | 2026/02/27 11:37:50 CST | python | Accepted | 63 ms | 20.3 MB |
| 700890725 | 2026/02/27 11:36:33 CST | python | Wrong Answer | N/A | N/A |
| 686538156 | 2025/12/23 09:16:22 CST | python | Accepted | 57 ms | 18 MB |
| 686292363 | 2025/12/22 09:09:56 CST | python | Accepted | 43 ms | 18.1 MB |
| 686109582 | 2025/12/21 09:24:44 CST | python | Accepted | 40 ms | 18 MB |
| 686109535 | 2025/12/21 09:23:43 CST | python | Time Limit Exceeded | N/A | N/A |
| 685961972 | 2025/12/20 12:48:37 CST | python | Accepted | 50 ms | 18.1 MB |
| 685960072 | 2025/12/20 12:32:02 CST | python | Accepted | 51 ms | 18.1 MB |

### 最近一次 AC 代码

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        level_head = root
        while level_head:
            next_level_dummy = Node()
            next_level_tail = next_level_dummy
            curr = level_head
            while curr:
                if curr.left:
                    next_level_tail.next = curr.left
                    next_level_tail = next_level_tail.next
                if curr.right:
                    next_level_tail.next = curr.right
                    next_level_tail = next_level_tail.next
                curr = curr.next
            level_head = next_level_dummy.next
        return root
```

## 118. 杨辉三角 (`pascals-triangle`)

- 题目链接：https://leetcode.cn/problems/pascals-triangle/
- 难度：Easy
- 标签：Array, Dynamic Programming
- 总提交次数：1
- 最近提交时间：2026/04/06 21:41:56 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715727354 | 2026/04/06 21:41:56 CST | python | Accepted | 0 ms | 19.2 MB |

### 最近一次 AC 代码

```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = res[i - 1][j - 1] + res[i - 1][j]
            res.append(row)
        return res
```

## 120. 三角形最小路径和 (`triangle`)

- 题目链接：https://leetcode.cn/problems/triangle/
- 难度：Medium
- 标签：Array, Dynamic Programming
- 总提交次数：7
- 最近提交时间：2026/02/13 13:52:41 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 698382006 | 2026/02/13 13:52:41 CST | python | Accepted | 0 ms | 19.6 MB |
| 697236020 | 2026/02/08 11:27:52 CST | python | Accepted | 0 ms | 19.8 MB |
| 696045138 | 2026/02/03 10:12:12 CST | python | Accepted | 3 ms | 19.8 MB |
| 695810343 | 2026/02/02 11:46:26 CST | python | Accepted | 0 ms | 19.7 MB |
| 695808636 | 2026/02/02 11:40:09 CST | python | Wrong Answer | N/A | N/A |
| 695808575 | 2026/02/02 11:39:54 CST | python | Runtime Error | N/A | N/A |
| 695376655 | 2026/01/31 11:40:25 CST | python | Accepted | 4 ms | 19.7 MB |

### 最近一次 AC 代码

```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = triangle[n - 1]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        return dp[0]
```

## 124. 二叉树中的最大路径和 (`binary-tree-maximum-path-sum`)

- 题目链接：https://leetcode.cn/problems/binary-tree-maximum-path-sum/
- 难度：Hard
- 标签：Tree, Depth-First Search, Dynamic Programming, Binary Tree
- 总提交次数：1
- 最近提交时间：2026/02/28 14:31:21 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 701181574 | 2026/02/28 14:31:21 CST | python | Accepted | 11 ms | 23.6 MB |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum = float('-inf')
        def max_gain(node):  # 以 node 为起点的最大单边路径和
            if not node:
                return 0
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            current_path_sum = left_gain + right_gain + node.val
            self.max_path_sum = max(self.max_path_sum, current_path_sum)
            return node.val + max(left_gain, right_gain)
        max_gain(root)
        return self.max_path_sum
```

## 125. 验证回文串 (`valid-palindrome`)

- 题目链接：https://leetcode.cn/problems/valid-palindrome/
- 难度：Easy
- 标签：Two Pointers, String
- 总提交次数：3
- 最近提交时间：2026/03/17 15:35:49 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 708307728 | 2026/03/17 15:35:49 CST | python | Accepted | 8 ms | 23.1 MB |
| 708307266 | 2026/03/17 15:35:08 CST | python | Wrong Answer | N/A | N/A |
| 708306938 | 2026/03/17 15:34:40 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []
        for c in s:
            if c.isalnum():
                chars.append(c.lower())
        s = ''.join(chars)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
```

## 127. 单词接龙 (`word-ladder`)

- 题目链接：https://leetcode.cn/problems/word-ladder/
- 难度：Hard
- 标签：Breadth-First Search, Hash Table, String
- 总提交次数：7
- 最近提交时间：2025/12/24 11:36:06 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 686806112 | 2025/12/24 11:36:06 CST | python | Accepted | 347 ms | 18.7 MB |
| 679183215 | 2025/11/19 13:49:18 CST | python | Accepted | 371 ms | 18.4 MB |
| 679182835 | 2025/11/19 13:47:26 CST | python | Wrong Answer | N/A | N/A |
| 679182725 | 2025/11/19 13:46:48 CST | python | Runtime Error | N/A | N/A |
| 678445117 | 2025/11/16 14:59:32 CST | python | Accepted | 355 ms | 18.5 MB |
| 678442968 | 2025/11/16 14:49:47 CST | python | Accepted | 351 ms | 18.5 MB |
| 678442754 | 2025/11/16 14:48:44 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        dq = collections.deque([(beginWord, 1)])
        visited = {beginWord}
        while dq:
            curr_word, length = dq.popleft()
            if curr_word == endWord:
                return length
            for i in range(len(curr_word)):
                for ch_code in range(ord('a'), ord('z') + 1):
                    ch = chr(ch_code)
                    next_word = curr_word[:i] + ch + curr_word[i+1:]
                    if next_word in word_set and next_word not in visited:
                        visited.add(next_word)
                        dq.append((next_word, length+1))
        return 0
```

## 128. 最长连续序列 (`longest-consecutive-sequence`)

- 题目链接：https://leetcode.cn/problems/longest-consecutive-sequence/
- 难度：Medium
- 标签：Union Find, Array, Hash Table
- 总提交次数：11
- 最近提交时间：2026/03/28 09:13:17 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 712755404 | 2026/03/28 09:13:17 CST | python | Accepted | 55 ms | 35.8 MB |
| 712683751 | 2026/03/27 21:12:29 CST | python | Accepted | 55 ms | 36.2 MB |
| 712683538 | 2026/03/27 21:11:49 CST | python | Time Limit Exceeded | N/A | N/A |
| 712683425 | 2026/03/27 21:11:29 CST | python | Time Limit Exceeded | N/A | N/A |
| 682405638 | 2025/12/03 15:54:21 CST | python | Accepted | 55 ms | 32.7 MB |
| 682404833 | 2025/12/03 15:52:03 CST | python | Time Limit Exceeded | N/A | N/A |
| 681975892 | 2025/12/01 20:33:23 CST | python | Accepted | 55 ms | 32.6 MB |
| 681974666 | 2025/12/01 20:30:51 CST | python | Wrong Answer | N/A | N/A |
| 681973882 | 2025/12/01 20:28:28 CST | python | Wrong Answer | N/A | N/A |
| 681973525 | 2025/12/01 20:27:09 CST | python | Wrong Answer | N/A | N/A |
| 681796819 | 2025/12/01 08:21:43 CST | python | Accepted | 43 ms | 33.5 MB |

### 最近一次 AC 代码

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        nums_set = set(nums)
        for num in nums_set:
            if num - 1 in nums_set:
                continue
            curr_num = num
            curr_len = 1
            while curr_num + 1 in nums_set:
                curr_num += 1
                curr_len += 1
            max_len = max(max_len, curr_len)
        return max_len
```

## 129. 求根节点到叶节点数字之和 (`sum-root-to-leaf-numbers`)

- 题目链接：https://leetcode.cn/problems/sum-root-to-leaf-numbers/
- 难度：Medium
- 标签：Tree, Depth-First Search, Binary Tree
- 总提交次数：4
- 最近提交时间：2026/04/07 12:30:02 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715854516 | 2026/04/07 12:30:02 CST | python | Accepted | 0 ms | 19.1 MB |
| 715854242 | 2026/04/07 12:28:35 CST | python | Runtime Error | N/A | N/A |
| 715854200 | 2026/04/07 12:28:25 CST | python | Runtime Error | N/A | N/A |
| 715854169 | 2026/04/07 12:28:17 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        total = 0
        def traverse(node, cur):
            nonlocal total
            cur = cur * 10 + node.val
            if not node.left and not node.right:
                total += cur
                return 
            if node.left:
                traverse(node.left, cur)
            if node.right:
                traverse(node.right, cur)
        traverse(root, 0)
        return total
```

## 131. 分割回文串 (`palindrome-partitioning`)

- 题目链接：https://leetcode.cn/problems/palindrome-partitioning/
- 难度：Medium
- 标签：String, Dynamic Programming, Backtracking
- 总提交次数：16
- 最近提交时间：2026/04/09 11:11:44 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 716498913 | 2026/04/09 11:11:44 CST | python | Accepted | 47 ms | 33.7 MB |
| 716494495 | 2026/04/09 11:00:47 CST | python | Accepted | 43 ms | 32.9 MB |
| 716494257 | 2026/04/09 11:00:14 CST | python | Wrong Answer | N/A | N/A |
| 716485534 | 2026/04/09 10:37:19 CST | python | Accepted | 51 ms | 33 MB |
| 699662956 | 2026/02/21 20:12:18 CST | python | Accepted | 52 ms | 33 MB |
| 699662859 | 2026/02/21 20:11:42 CST | python | Wrong Answer | N/A | N/A |
| 687828919 | 2025/12/29 11:45:09 CST | python | Accepted | 47 ms | 33.5 MB |
| 687693494 | 2025/12/28 17:44:56 CST | python | Accepted | 43 ms | 33.5 MB |
| 683426469 | 2025/12/08 15:46:59 CST | python | Accepted | 51 ms | 33.9 MB |
| 683425791 | 2025/12/08 15:44:59 CST | python | Wrong Answer | N/A | N/A |
| 683424854 | 2025/12/08 15:42:01 CST | python | Wrong Answer | N/A | N/A |
| 683022358 | 2025/12/06 14:54:38 CST | python | Accepted | 48 ms | 33.9 MB |
| 681817720 | 2025/12/01 10:32:01 CST | python | Accepted | 55 ms | 33.7 MB |
| 681817363 | 2025/12/01 10:30:45 CST | python | Wrong Answer | N/A | N/A |
| 681817191 | 2025/12/01 10:30:09 CST | python | Wrong Answer | N/A | N/A |
| 681617872 | 2025/11/30 11:05:16 CST | python | Accepted | 51 ms | 34 MB |

### 最近一次 AC 代码

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        n = len(s)
        def backtack(start_idx):
            if start_idx == n:
                res.append(list(path))
                return
            for end_idx in range(start_idx + 1, n + 1):
                sub_string = s[start_idx : end_idx]
                if sub_string != sub_string[::-1]:
                    continue
                path.append(sub_string)
                backtack(end_idx)
                path.pop()
        backtack(0)
        return res
```

## 133. 克隆图 (`clone-graph`)

- 题目链接：https://leetcode.cn/problems/clone-graph/
- 难度：Medium
- 标签：Depth-First Search, Breadth-First Search, Graph, Hash Table
- 总提交次数：1
- 最近提交时间：2026/04/05 16:01:01 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715327380 | 2026/04/05 16:01:01 CST | python | Accepted | 46 ms | 19.5 MB |

### 最近一次 AC 代码

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        old_to_new = {}
        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]
            clone = Node(node.val)
            old_to_new[node] = clone
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone
        return dfs(node)
```

## 134. 加油站 (`gas-station`)

- 题目链接：https://leetcode.cn/problems/gas-station/
- 难度：Medium
- 标签：Greedy, Array
- 总提交次数：7
- 最近提交时间：2026/02/05 10:51:37 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 696560999 | 2026/02/05 10:51:37 CST | python | Accepted | 24 ms | 25.8 MB |
| 696328060 | 2026/02/04 11:19:31 CST | python | Accepted | 16 ms | 25.7 MB |
| 696327991 | 2026/02/04 11:19:19 CST | python | Wrong Answer | N/A | N/A |
| 696327737 | 2026/02/04 11:18:38 CST | python | Wrong Answer | N/A | N/A |
| 696327680 | 2026/02/04 11:18:27 CST | python | Runtime Error | N/A | N/A |
| 696111611 | 2026/02/03 14:43:48 CST | python | Accepted | 27 ms | 25.7 MB |
| 696110916 | 2026/02/03 14:41:41 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        curr = 0
        n = len(gas)
        start = 0
        for i in range(n):
            curr += (gas[i] - cost[i])
            if curr < 0:
                start = i + 1
                curr = 0
        return start
```

## 136. 只出现一次的数字 (`single-number`)

- 题目链接：https://leetcode.cn/problems/single-number/
- 难度：Easy
- 标签：Bit Manipulation, Array
- 总提交次数：1
- 最近提交时间：2026/04/06 17:37:40 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715652513 | 2026/04/06 17:37:40 CST | python | Accepted | 3 ms | 21 MB |

### 最近一次 AC 代码

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        return res
```

## 138. 随机链表的复制 (`copy-list-with-random-pointer`)

- 题目链接：https://leetcode.cn/problems/copy-list-with-random-pointer/
- 难度：Medium
- 标签：Hash Table, Linked List
- 总提交次数：1
- 最近提交时间：2026/03/29 17:20:35 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 713207537 | 2026/03/29 17:20:35 CST | python | Accepted | 59 ms | 19.9 MB |

### 最近一次 AC 代码

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        old_to_new = {}

        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            old_to_new[curr].next = old_to_new.get(curr.next)
            old_to_new[curr].random = old_to_new.get(curr.random)
            curr = curr.next
        
        return old_to_new[head]
```

## 139. 单词拆分 (`word-break`)

- 题目链接：https://leetcode.cn/problems/word-break/
- 难度：Medium
- 标签：Trie, Memoization, Array, Hash Table, String, Dynamic Programming
- 总提交次数：12
- 最近提交时间：2026/02/14 16:00:26 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 698597489 | 2026/02/14 16:00:26 CST | python | Accepted | 8 ms | 19.2 MB |
| 698595918 | 2026/02/14 15:58:39 CST | python | Runtime Error | N/A | N/A |
| 693278625 | 2026/01/22 16:42:08 CST | python | Accepted | 3 ms | 19 MB |
| 690097706 | 2026/01/09 10:33:00 CST | python | Accepted | 4 ms | 19 MB |
| 689208694 | 2026/01/05 16:22:17 CST | python | Accepted | 0 ms | 19.2 MB |
| 689208654 | 2026/01/05 16:22:09 CST | python | Runtime Error | N/A | N/A |
| 677328149 | 2025/11/11 14:22:28 CST | python | Accepted | 3 ms | 17.4 MB |
| 677328098 | 2025/11/11 14:22:15 CST | python | Runtime Error | N/A | N/A |
| 676478040 | 2025/11/07 14:03:33 CST | python | Accepted | 3 ms | 17.7 MB |
| 676477579 | 2025/11/07 14:01:12 CST | python | Accepted | 8 ms | 17.4 MB |
| 676188629 | 2025/11/06 09:34:37 CST | python | Accepted | 3 ms | 17.5 MB |
| 676188492 | 2025/11/06 09:33:52 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        word_set = set(wordDict)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[n]
```

## 141. 环形链表 (`linked-list-cycle`)

- 题目链接：https://leetcode.cn/problems/linked-list-cycle/
- 难度：Easy
- 标签：Hash Table, Linked List, Two Pointers
- 总提交次数：3
- 最近提交时间：2026/03/31 11:15:59 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 713769746 | 2026/03/31 11:15:59 CST | python | Accepted | 67 ms | 22.1 MB |
| 683601885 | 2025/12/09 11:13:56 CST | python | Accepted | 52 ms | 19.6 MB |
| 645916468 | 2025/07/22 07:30:57 CST | python | Accepted | 46 ms | 19.6 MB |

### 最近一次 AC 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
```

## 142. 环形链表 II (`linked-list-cycle-ii`)

- 题目链接：https://leetcode.cn/problems/linked-list-cycle-ii/
- 难度：Medium
- 标签：Hash Table, Linked List, Two Pointers
- 总提交次数：3
- 最近提交时间：2026/03/31 12:27:39 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 713792782 | 2026/03/31 12:27:39 CST | python | Accepted | 53 ms | 22 MB |
| 683637008 | 2025/12/09 14:19:57 CST | python | Accepted | 58 ms | 19.3 MB |
| 646235503 | 2025/07/23 08:13:01 CST | python | Accepted | 87 ms | 19.1 MB |

### 最近一次 AC 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        else:
            return None
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
```

## 144. 二叉树的前序遍历 (`binary-tree-preorder-traversal`)

- 题目链接：https://leetcode.cn/problems/binary-tree-preorder-traversal/
- 难度：Easy
- 标签：Stack, Tree, Depth-First Search, Binary Tree
- 总提交次数：9
- 最近提交时间：2026/04/02 11:24:35 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 714479889 | 2026/04/02 11:24:35 CST | python | Accepted | 0 ms | 19.3 MB |
| 714479665 | 2026/04/02 11:24:05 CST | python | Runtime Error | N/A | N/A |
| 714475748 | 2026/04/02 11:14:51 CST | python | Accepted | 0 ms | 19.2 MB |
| 714475334 | 2026/04/02 11:13:50 CST | python | Wrong Answer | N/A | N/A |
| 701375151 | 2026/03/01 10:21:53 CST | python | Accepted | 0 ms | 19.1 MB |
| 701374432 | 2026/03/01 10:18:30 CST | python | Accepted | 0 ms | 19 MB |
| 684597816 | 2025/12/13 21:58:18 CST | python | Accepted | 0 ms | 17.4 MB |
| 684562509 | 2025/12/13 18:24:21 CST | python | Accepted | 0 ms | 17.4 MB |
| 684561918 | 2025/12/13 18:19:29 CST | python | Accepted | 0 ms | 17.5 MB |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
```

## 145. 二叉树的后序遍历 (`binary-tree-postorder-traversal`)

- 题目链接：https://leetcode.cn/problems/binary-tree-postorder-traversal/
- 难度：Easy
- 标签：Stack, Tree, Depth-First Search, Binary Tree
- 总提交次数：8
- 最近提交时间：2026/04/02 12:13:28 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 714494961 | 2026/04/02 12:13:28 CST | python | Accepted | 0 ms | 19.3 MB |
| 714494799 | 2026/04/02 12:12:37 CST | python | Runtime Error | N/A | N/A |
| 714493508 | 2026/04/02 12:05:54 CST | python | Accepted | 0 ms | 19 MB |
| 684599693 | 2025/12/13 22:08:40 CST | python | Accepted | 0 ms | 17.7 MB |
| 684599619 | 2025/12/13 22:08:16 CST | python | Runtime Error | N/A | N/A |
| 684599575 | 2025/12/13 22:08:03 CST | python | Runtime Error | N/A | N/A |
| 684563288 | 2025/12/13 18:30:33 CST | python | Accepted | 0 ms | 17.4 MB |
| 684563111 | 2025/12/13 18:29:18 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res[::-1]
```

## 146. LRU 缓存 (`lru-cache`)

- 题目链接：https://leetcode.cn/problems/lru-cache/
- 难度：Medium
- 标签：Design, Hash Table, Linked List, Doubly-Linked List
- 总提交次数：12
- 最近提交时间：2026/03/29 19:29:43 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 713245042 | 2026/03/29 19:29:43 CST | python | Accepted | 119 ms | 75.2 MB |
| 685546894 | 2025/12/18 10:54:15 CST | python | Accepted | 85 ms | 76 MB |
| 681914975 | 2025/12/01 16:39:54 CST | python | Accepted | 120 ms | 76.7 MB |
| 681678132 | 2025/11/30 15:53:46 CST | python | Accepted | 119 ms | 76.4 MB |
| 681677953 | 2025/11/30 15:53:13 CST | python | Runtime Error | N/A | N/A |
| 681677856 | 2025/11/30 15:52:57 CST | python | Runtime Error | N/A | N/A |
| 677525816 | 2025/11/12 09:38:25 CST | python | Accepted | 116 ms | 76.6 MB |
| 677525763 | 2025/11/12 09:38:09 CST | python | Runtime Error | N/A | N/A |
| 675682205 | 2025/11/04 09:41:29 CST | python | Accepted | 103 ms | 76.6 MB |
| 675682157 | 2025/11/04 09:41:16 CST | python | Runtime Error | N/A | N/A |
| 675297724 | 2025/11/02 16:03:41 CST | python | Accepted | 113 ms | 76.7 MB |
| 675297632 | 2025/11/02 16:03:22 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.od = collections.OrderedDict()
        

    def get(self, key: int) -> int:
        if key not in self.od:
            return -1
        self.od.move_to_end(key)
        return self.od[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.od:
            self.od[key] = value
            self.od.move_to_end(key)
        else:
            self.od[key] = value
            self.od.move_to_end(key)
            if len(self.od) > self.capacity:
                self.od.popitem(last=False)        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```

## 148. 排序链表 (`sort-list`)

- 题目链接：https://leetcode.cn/problems/sort-list/
- 难度：Medium
- 标签：Linked List, Two Pointers, Divide and Conquer, Sorting, Merge Sort
- 总提交次数：10
- 最近提交时间：2025/12/16 10:35:45 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 685066608 | 2025/12/16 10:35:45 CST | python | Accepted | 183 ms | 32 MB |
| 685065480 | 2025/12/16 10:31:55 CST | python | Wrong Answer | N/A | N/A |
| 685064003 | 2025/12/16 10:26:36 CST | python | Accepted | 179 ms | 32 MB |
| 685062793 | 2025/12/16 10:21:54 CST | python | Time Limit Exceeded | N/A | N/A |
| 685060454 | 2025/12/16 10:11:56 CST | python | Accepted | 179 ms | 32.3 MB |
| 685060102 | 2025/12/16 10:10:30 CST | python | Runtime Error | N/A | N/A |
| 685060029 | 2025/12/16 10:10:09 CST | python | Accepted | 179 ms | 32 MB |
| 685059875 | 2025/12/16 10:09:26 CST | python | Runtime Error | N/A | N/A |
| 685059411 | 2025/12/16 10:07:19 CST | python | Runtime Error | N/A | N/A |
| 685059090 | 2025/12/16 10:05:56 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        mid = self.find_mid_divide(head)
        left_head = self.sortList(head)
        right_head = self.sortList(mid)
        return self.merge_sort(left_head, right_head)

    def find_mid_divide(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return mid
    
    def merge_sort(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next
```

## 150. 逆波兰表达式求值 (`evaluate-reverse-polish-notation`)

- 题目链接：https://leetcode.cn/problems/evaluate-reverse-polish-notation/
- 难度：Medium
- 标签：Stack, Array, Math
- 总提交次数：2
- 最近提交时间：2026/03/26 10:16:39 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 712085126 | 2026/03/26 10:16:39 CST | python | Accepted | 3 ms | 20.4 MB |
| 712084996 | 2026/03/26 10:16:13 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in {'+', '-', '*', '/'}:
                stack.append(int(token))
                continue
            right = stack.pop()
            left = stack.pop()
            if token == '+':
                stack.append(left + right)
            elif token == '-':
                stack.append(left - right)
            elif token == '*':
                stack.append(left * right)
            else:
                stack.append(int(left / right))
        return stack[-1]
```

## 151. 反转字符串中的单词 (`reverse-words-in-a-string`)

- 题目链接：https://leetcode.cn/problems/reverse-words-in-a-string/
- 难度：Medium
- 标签：Two Pointers, String
- 总提交次数：17
- 最近提交时间：2026/03/14 20:47:49 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 707114073 | 2026/03/14 20:47:49 CST | python | Accepted | 0 ms | 19.1 MB |
| 707113985 | 2026/03/14 20:47:39 CST | python | Runtime Error | N/A | N/A |
| 681289036 | 2025/11/28 14:18:38 CST | python | Accepted | 0 ms | 17.5 MB |
| 665506455 | 2025/09/24 08:28:59 CST | python | Accepted | 7 ms | 17.8 MB |
| 665506007 | 2025/09/24 08:23:38 CST | python | Wrong Answer | N/A | N/A |
| 665505981 | 2025/09/24 08:23:19 CST | python | Runtime Error | N/A | N/A |
| 665505939 | 2025/09/24 08:22:39 CST | python | Runtime Error | N/A | N/A |
| 665188708 | 2025/09/23 07:38:22 CST | python | Accepted | 7 ms | 17.6 MB |
| 665188587 | 2025/09/23 07:33:52 CST | python | Accepted | 7 ms | 17.6 MB |
| 665187742 | 2025/09/23 07:25:38 CST | python | Wrong Answer | N/A | N/A |
| 665187736 | 2025/09/23 07:25:18 CST | python | Runtime Error | N/A | N/A |
| 665187686 | 2025/09/23 07:22:50 CST | python | Wrong Answer | N/A | N/A |
| 665187638 | 2025/09/23 07:21:27 CST | python | Runtime Error | N/A | N/A |
| 665187629 | 2025/09/23 07:21:03 CST | python | Runtime Error | N/A | N/A |
| 665123775 | 2025/09/22 21:37:43 CST | python | Accepted | 15 ms | 17.7 MB |
| 665123600 | 2025/09/22 21:37:17 CST | python | Wrong Answer | N/A | N/A |
| 665123102 | 2025/09/22 21:35:53 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        return ' '.join(words)
```

## 152. 乘积最大子数组 (`maximum-product-subarray`)

- 题目链接：https://leetcode.cn/problems/maximum-product-subarray/
- 难度：Medium
- 标签：Array, Dynamic Programming
- 总提交次数：8
- 最近提交时间：2026/02/10 08:43:23 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 697651411 | 2026/02/10 08:43:23 CST | python | Accepted | 7 ms | 19.6 MB |
| 697447667 | 2026/02/09 11:21:36 CST | python | Accepted | 8 ms | 19.8 MB |
| 697447543 | 2026/02/09 11:21:11 CST | python | Wrong Answer | N/A | N/A |
| 695665778 | 2026/02/01 17:25:40 CST | python | Accepted | 16 ms | 19.5 MB |
| 692472423 | 2026/01/19 17:02:46 CST | python | Accepted | 8 ms | 19.8 MB |
| 690987275 | 2026/01/13 12:23:53 CST | python | Accepted | 3 ms | 19.6 MB |
| 690765622 | 2026/01/12 14:37:22 CST | python | Accepted | 3 ms | 19.5 MB |
| 685090653 | 2025/12/16 12:16:06 CST | python | Accepted | 11 ms | 18.2 MB |

### 最近一次 AC 代码

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = max_so_far = min_so_far = nums[0]
        for num in nums[1:]:
            candidates = (num, num * max_so_far, num * min_so_far)
            max_so_far = max(candidates)
            min_so_far = min(candidates)
            max_prod = max(max_prod, max_so_far)
        return max_prod
```

## 153. 寻找旋转排序数组中的最小值 (`find-minimum-in-rotated-sorted-array`)

- 题目链接：https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/
- 难度：Medium
- 标签：Array, Binary Search
- 总提交次数：2
- 最近提交时间：2026/03/24 10:58:35 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 711264094 | 2026/03/24 10:58:35 CST | python | Accepted | 0 ms | 19.3 MB |
| 709824985 | 2026/03/20 18:40:12 CST | python | Accepted | 0 ms | 19.2 MB |

### 最近一次 AC 代码

```python
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
```

## 155. 最小栈 (`min-stack`)

- 题目链接：https://leetcode.cn/problems/min-stack/
- 难度：Medium
- 标签：Stack, Design
- 总提交次数：2
- 最近提交时间：2026/03/29 21:46:05 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 713293147 | 2026/03/29 21:46:05 CST | python | Accepted | 4 ms | 22 MB |
| 712099621 | 2026/03/26 10:50:49 CST | python | Accepted | 12 ms | 22 MB |

### 最近一次 AC 代码

```python
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))
        

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
```

## 159. 至多包含两个不同字符的最长子串 (`longest-substring-with-at-most-two-distinct-characters`)

- 题目链接：https://leetcode.cn/problems/longest-substring-with-at-most-two-distinct-characters/
- 难度：Medium
- 标签：Hash Table, String, Sliding Window
- 总提交次数：3
- 最近提交时间：2026/02/26 11:18:03 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 700618802 | 2026/02/26 11:18:03 CST | python | Accepted | 143 ms | 19.4 MB |
| 559820091 | 2024/08/30 11:52:23 CST | python | Accepted | 233 ms | 16.8 MB |
| 559810197 | 2024/08/30 11:22:48 CST | python | Accepted | 226 ms | 16.8 MB |

### 最近一次 AC 代码

```python
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        char_count = {}
        left = 0
        max_len = 0
        for right, r_char in enumerate(s):
            if r_char in char_count:
                char_count[r_char] += 1
            else:
                char_count[r_char] = 1
            if len(char_count) > 2:
                l_char = s[left]
                char_count[l_char] -= 1
                if char_count[l_char] == 0:
                    del char_count[l_char]
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len
```

## 160. 相交链表 (`intersection-of-two-linked-lists`)

- 题目链接：https://leetcode.cn/problems/intersection-of-two-linked-lists/
- 难度：Easy
- 标签：Hash Table, Linked List, Two Pointers
- 总提交次数：3
- 最近提交时间：2026/03/31 12:31:42 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 713793572 | 2026/03/31 12:31:42 CST | python | Accepted | 124 ms | 37.4 MB |
| 683649333 | 2025/12/09 15:02:13 CST | python | Accepted | 135 ms | 32.1 MB |
| 646539996 | 2025/07/24 08:06:07 CST | python | Accepted | 105 ms | 27.3 MB |

### 最近一次 AC 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1, p2 = headA, headB
        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1
```

## 161. 相隔为 1 的编辑距离 (`one-edit-distance`)

- 题目链接：https://leetcode.cn/problems/one-edit-distance/
- 难度：Medium
- 标签：Two Pointers, String
- 总提交次数：5
- 最近提交时间：2026/02/24 11:27:44 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 700123731 | 2026/02/24 11:27:44 CST | python | Accepted | 3 ms | 19.3 MB |
| 559584332 | 2024/08/29 15:38:30 CST | python | Wrong Answer | N/A | N/A |
| 558561682 | 2024/08/26 09:52:51 CST | python | Accepted | 38 ms | 16.4 MB |
| 558553515 | 2024/08/26 09:45:29 CST | python | Wrong Answer | N/A | N/A |
| 557612425 | 2024/08/22 14:24:54 CST | python | Accepted | 34 ms | 16.4 MB |

### 最近一次 AC 代码

```python
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if abs(m - n) > 1:
            return False
        if m > n:
            s, t = t, s
            m, n = n, m
        i, j = 0, 0
        edit_once = False
        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
                j += 1
                continue
            if edit_once:
                return False
            edit_once = True
            if m == n:
                i += 1
                j += 1
            else:
                j += 1
        return edit_once or (n == m + 1)
```

## 162. 寻找峰值 (`find-peak-element`)

- 题目链接：https://leetcode.cn/problems/find-peak-element/
- 难度：Medium
- 标签：Array, Binary Search
- 总提交次数：4
- 最近提交时间：2026/03/24 10:31:00 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 711249442 | 2026/03/24 10:31:00 CST | python | Accepted | 0 ms | 19.2 MB |
| 709768952 | 2026/03/20 16:40:09 CST | python | Accepted | 0 ms | 19 MB |
| 709768383 | 2026/03/20 16:39:09 CST | python | Wrong Answer | N/A | N/A |
| 709768168 | 2026/03/20 16:38:49 CST | python | Accepted | 0 ms | 19.1 MB |

### 最近一次 AC 代码

```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left
```

## 163. 缺失的区间 (`missing-ranges`)

- 题目链接：https://leetcode.cn/problems/missing-ranges/
- 难度：Easy
- 标签：Array
- 总提交次数：2
- 最近提交时间：2026/02/26 10:06:05 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 700598213 | 2026/02/26 10:06:05 CST | python | Accepted | 0 ms | 19.1 MB |
| 700597941 | 2026/02/26 10:04:50 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        new_nums = [lower - 1] + nums + [upper + 1]
        missing_ranges = []
        for i in range(len(new_nums) - 1):
            curr_num = new_nums[i]
            next_num = new_nums[i + 1]
            if next_num - curr_num > 1:
                missing_ranges.append([curr_num + 1, next_num - 1])
        return missing_ranges
```

## 167. 两数之和 II - 输入有序数组 (`two-sum-ii-input-array-is-sorted`)

- 题目链接：https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/
- 难度：Medium
- 标签：Array, Two Pointers, Binary Search
- 总提交次数：4
- 最近提交时间：2026/03/17 13:36:53 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 708241345 | 2026/03/17 13:36:53 CST | python | Accepted | 3 ms | 20.5 MB |
| 702143036 | 2026/03/03 13:58:29 CST | python | Accepted | 3 ms | 20.5 MB |
| 665591574 | 2025/09/24 13:59:57 CST | python | Accepted | 3 ms | 18.2 MB |
| 665591533 | 2025/09/24 13:59:45 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left + 1, right + 1]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]
```

## 169. 多数元素 (`majority-element`)

- 题目链接：https://leetcode.cn/problems/majority-element/
- 难度：Easy
- 标签：Array, Hash Table, Divide and Conquer, Counting, Sorting
- 总提交次数：2
- 最近提交时间：2026/03/30 08:15:26 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 713356063 | 2026/03/30 08:15:26 CST | python | Accepted | 3 ms | 20.9 MB |
| 713242133 | 2026/03/29 19:19:14 CST | python | Accepted | 8 ms | 20.7 MB |

### 最近一次 AC 代码

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
                count += 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        return candidate
```

## 172. 阶乘后的零 (`factorial-trailing-zeroes`)

- 题目链接：https://leetcode.cn/problems/factorial-trailing-zeroes/
- 难度：Medium
- 标签：Math
- 总提交次数：1
- 最近提交时间：2026/04/06 17:36:00 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715651949 | 2026/04/06 17:36:00 CST | python | Accepted | 3 ms | 19.3 MB |

### 最近一次 AC 代码

```python
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n > 0:
            n //= 5
            count += n
        return count
```

## 186. 反转字符串中的单词 II (`reverse-words-in-a-string-ii`)

- 题目链接：https://leetcode.cn/problems/reverse-words-in-a-string-ii/
- 难度：Medium
- 标签：Two Pointers, String
- 总提交次数：4
- 最近提交时间：2026/02/24 12:16:19 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 700134662 | 2026/02/24 12:16:19 CST | python | Accepted | 11 ms | 24.2 MB |
| 559593730 | 2024/08/29 15:59:34 CST | python | Accepted | 50 ms | 22.3 MB |
| 558591307 | 2024/08/26 11:16:51 CST | python | Accepted | 40 ms | 22.3 MB |
| 557635809 | 2024/08/22 15:27:23 CST | python | Accepted | 51 ms | 22.3 MB |

### 最近一次 AC 代码

```python
class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(s, start, end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
        n = len(s)
        reverse(s, 0, n - 1)
        i, j = 0, 0
        while i < n:
            while s[i] == ' ':
                i += 1
            j = i
            while j < n and s[j] != ' ':
                j += 1
            reverse(s, i, j - 1)
            i = j
```

## 191. 位1的个数 (`number-of-1-bits`)

- 题目链接：https://leetcode.cn/problems/number-of-1-bits/
- 难度：Easy
- 标签：Bit Manipulation, Divide and Conquer
- 总提交次数：1
- 最近提交时间：2025/11/19 09:31:48 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 679119811 | 2025/11/19 09:31:48 CST | python | Accepted | 1 ms | 17.4 MB |

### 最近一次 AC 代码

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n = n & (n-1)
            count += 1
        return count
```

## 198. 打家劫舍 (`house-robber`)

- 题目链接：https://leetcode.cn/problems/house-robber/
- 难度：Medium
- 标签：Array, Dynamic Programming
- 总提交次数：7
- 最近提交时间：2026/02/10 10:47:10 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 697672986 | 2026/02/10 10:47:10 CST | python | Accepted | 0 ms | 19 MB |
| 697672680 | 2026/02/10 10:45:58 CST | python | Wrong Answer | N/A | N/A |
| 692497294 | 2026/01/19 18:29:21 CST | python | Accepted | 0 ms | 19.1 MB |
| 692497255 | 2026/01/19 18:29:08 CST | python | Runtime Error | N/A | N/A |
| 688685400 | 2026/01/03 10:35:20 CST | python | Accepted | 0 ms | 16.9 MB |
| 688685356 | 2026/01/03 10:34:58 CST | python | Runtime Error | N/A | N/A |
| 685096199 | 2025/12/16 12:37:11 CST | python | Accepted | 0 ms | 17.4 MB |

### 最近一次 AC 代码

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        prev_2, prev_1 = nums[0], max(nums[0], nums[1])
        for num in nums[2:]:
            curr = max(prev_1, prev_2 + num)
            prev_2, prev_1 = prev_1, curr
        return prev_1
```

## 199. 二叉树的右视图 (`binary-tree-right-side-view`)

- 题目链接：https://leetcode.cn/problems/binary-tree-right-side-view/
- 难度：Medium
- 标签：Tree, Depth-First Search, Breadth-First Search, Binary Tree
- 总提交次数：1
- 最近提交时间：2025/11/26 08:46:18 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 680724483 | 2025/11/26 08:46:18 CST | python | Accepted | 0 ms | 17.5 MB |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        dq = collections.deque([root])
        while dq:
            level_size = len(dq)
            for i in range(level_size):
                node = dq.popleft()
                if i == (level_size - 1):
                    res.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        return res
```

## 200. 岛屿数量 (`number-of-islands`)

- 题目链接：https://leetcode.cn/problems/number-of-islands/
- 难度：Medium
- 标签：Depth-First Search, Breadth-First Search, Union Find, Array, Matrix
- 总提交次数：30
- 最近提交时间：2026/04/10 09:06:41 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 716789307 | 2026/04/10 09:06:41 CST | python | Accepted | 242 ms | 21.3 MB |
| 704505274 | 2026/03/09 10:16:57 CST | python | Accepted | 229 ms | 21.2 MB |
| 687498231 | 2025/12/27 17:01:56 CST | python | Accepted | 252 ms | 19.3 MB |
| 685799863 | 2025/12/19 14:13:43 CST | python | Accepted | 249 ms | 19.5 MB |
| 685799817 | 2025/12/19 14:13:33 CST | python | Accepted | 285 ms | 19.3 MB |
| 685799783 | 2025/12/19 14:13:21 CST | python | Memory Limit Exceeded | N/A | N/A |
| 685799460 | 2025/12/19 14:11:56 CST | python | Memory Limit Exceeded | N/A | N/A |
| 685799380 | 2025/12/19 14:11:29 CST | python | Runtime Error | N/A | N/A |
| 685545081 | 2025/12/18 10:48:04 CST | python | Accepted | 238 ms | 19.6 MB |
| 685544733 | 2025/12/18 10:46:56 CST | python | Wrong Answer | N/A | N/A |
| 682411938 | 2025/12/03 16:13:06 CST | python | Accepted | 246 ms | 19.7 MB |
| 682411715 | 2025/12/03 16:12:22 CST | python | Wrong Answer | N/A | N/A |
| 682411309 | 2025/12/03 16:11:12 CST | python | Wrong Answer | N/A | N/A |
| 682411068 | 2025/12/03 16:10:30 CST | python | Wrong Answer | N/A | N/A |
| 682410854 | 2025/12/03 16:09:54 CST | python | Runtime Error | N/A | N/A |
| 680737405 | 2025/11/26 09:38:07 CST | python | Accepted | 271 ms | 19.9 MB |
| 678258934 | 2025/11/15 14:47:34 CST | python | Accepted | 246 ms | 19.7 MB |
| 678258404 | 2025/11/15 14:44:48 CST | python | Memory Limit Exceeded | N/A | N/A |
| 678258356 | 2025/11/15 14:44:31 CST | python | Runtime Error | N/A | N/A |
| 677324428 | 2025/11/11 14:07:05 CST | python | Accepted | 258 ms | 19.6 MB |
| 677323945 | 2025/11/11 14:05:04 CST | python | Memory Limit Exceeded | N/A | N/A |
| 677323245 | 2025/11/11 14:01:28 CST | python | Memory Limit Exceeded | N/A | N/A |
| 677273277 | 2025/11/11 10:14:55 CST | python | Accepted | 252 ms | 19.7 MB |
| 677273214 | 2025/11/11 10:14:40 CST | python | Runtime Error | N/A | N/A |
| 677273186 | 2025/11/11 10:14:33 CST | python | Runtime Error | N/A | N/A |
| 677268530 | 2025/11/11 09:54:20 CST | python | Accepted | 244 ms | 19.8 MB |
| 677268516 | 2025/11/11 09:54:13 CST | python | Accepted | 254 ms | 19.7 MB |
| 677268480 | 2025/11/11 09:54:02 CST | python | Accepted | 318 ms | 19.6 MB |
| 677266928 | 2025/11/11 09:46:47 CST | python | Accepted | 244 ms | 19.7 MB |
| 677266625 | 2025/11/11 09:45:14 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(r, c):
            if not (0 <= r < m and 0 <= c < n):
                return
            if grid[r][c] == '0':
                return
            grid[r][c] = '0'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)
        return res
```

## 202. 快乐数 (`happy-number`)

- 题目链接：https://leetcode.cn/problems/happy-number/
- 难度：Easy
- 标签：Hash Table, Math, Two Pointers
- 总提交次数：2
- 最近提交时间：2025/12/09 12:48:54 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 683621050 | 2025/12/09 12:48:54 CST | python | Accepted | 0 ms | 17.8 MB |
| 683620207 | 2025/12/09 12:42:27 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def isHappy(self, n: int) -> bool:
        # 数字的状态转移，要么变成1，要么变成某个不等于1的循环
        def next_num(x):
            total = 0
            while x > 0:
                digit = x % 10
                total += digit * digit
                x //= 10
            return total
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = next_num(n)
        return n == 1
```

## 204. 计数质数 (`count-primes`)

- 题目链接：https://leetcode.cn/problems/count-primes/
- 难度：Medium
- 标签：Array, Math, Enumeration, Number Theory
- 总提交次数：3
- 最近提交时间：2026/04/06 16:32:15 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715626186 | 2026/04/06 16:32:15 CST | python | Accepted | 1579 ms | 57 MB |
| 715625163 | 2026/04/06 16:29:58 CST | python | Accepted | 3357 ms | 57 MB |
| 715625111 | 2026/04/06 16:29:51 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        is_prime = [True] * n
        is_prime[0] = False
        is_prime[1] = False
        
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False
        
        return sum(is_prime)
```

## 206. 反转链表 (`reverse-linked-list`)

- 题目链接：https://leetcode.cn/problems/reverse-linked-list/
- 难度：Easy
- 标签：Recursion, Linked List
- 总提交次数：9
- 最近提交时间：2026/04/02 10:02:20 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 714446827 | 2026/04/02 10:02:20 CST | python | Accepted | 0 ms | 20.3 MB |
| 714097704 | 2026/04/01 09:44:36 CST | python | Accepted | 0 ms | 20.3 MB |
| 714097578 | 2026/04/01 09:44:07 CST | python | Wrong Answer | N/A | N/A |
| 714096181 | 2026/04/01 09:38:25 CST | python | Accepted | 0 ms | 20.2 MB |
| 714095955 | 2026/04/01 09:37:32 CST | python | Runtime Error | N/A | N/A |
| 684088781 | 2025/12/11 12:36:21 CST | python | Accepted | 3 ms | 18.7 MB |
| 684088741 | 2025/12/11 12:36:02 CST | python | Wrong Answer | N/A | N/A |
| 684074472 | 2025/12/11 11:21:14 CST | python | Accepted | 0 ms | 18.6 MB |
| 682053626 | 2025/12/02 09:04:41 CST | python | Accepted | 0 ms | 18.6 MB |

### 最近一次 AC 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = None, head
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        return pre
```

## 207. 课程表 (`course-schedule`)

- 题目链接：https://leetcode.cn/problems/course-schedule/
- 难度：Medium
- 标签：Depth-First Search, Breadth-First Search, Graph, Topological Sort
- 总提交次数：7
- 最近提交时间：2026/04/05 10:32:44 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715241249 | 2026/04/05 10:32:44 CST | python | Accepted | 3 ms | 20.3 MB |
| 680747631 | 2025/11/26 10:23:37 CST | python | Accepted | 7 ms | 18.8 MB |
| 676475278 | 2025/11/07 13:48:53 CST | python | Accepted | 0 ms | 18.7 MB |
| 676475184 | 2025/11/07 13:48:21 CST | python | Runtime Error | N/A | N/A |
| 676432739 | 2025/11/07 10:13:23 CST | python | Accepted | 0 ms | 18.7 MB |
| 676430638 | 2025/11/07 10:02:48 CST | python | Accepted | 7 ms | 18.5 MB |
| 676430554 | 2025/11/07 10:02:22 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses
        adj_list = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            in_degree[course] += 1
            adj_list[pre].append(course)
        
        dq = collections.deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                dq.append(i)
        
        course_taken = 0
        while dq:
            curr_course = dq.popleft()
            course_taken += 1
            for next_course in adj_list[curr_course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    dq.append(next_course)

        return course_taken == numCourses
```

## 208. 实现 Trie (前缀树) (`implement-trie-prefix-tree`)

- 题目链接：https://leetcode.cn/problems/implement-trie-prefix-tree/
- 难度：Medium
- 标签：Design, Trie, Hash Table, String
- 总提交次数：3
- 最近提交时间：2026/04/04 19:54:19 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715146705 | 2026/04/04 19:54:19 CST | python | Accepted | 63 ms | 33.8 MB |
| 715146657 | 2026/04/04 19:54:04 CST | python | Wrong Answer | N/A | N/A |
| 715146297 | 2026/04/04 19:52:22 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class TrieNode:
    def __init__(self):
        self.children: dict[str, "TrieNode"] = {}
        self.is_end: bool = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self._find_node(word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        return self._find_node(prefix) is not None
    
    def _find_node(self, s):
        node = self.root
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```

## 209. 长度最小的子数组 (`minimum-size-subarray-sum`)

- 题目链接：https://leetcode.cn/problems/minimum-size-subarray-sum/
- 难度：Medium
- 标签：Array, Binary Search, Prefix Sum, Sliding Window
- 总提交次数：9
- 最近提交时间：2026/03/18 14:52:18 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 708767341 | 2026/03/18 14:52:18 CST | python | Accepted | 11 ms | 30 MB |
| 708766929 | 2026/03/18 14:51:37 CST | python | Wrong Answer | N/A | N/A |
| 702521433 | 2026/03/04 13:10:37 CST | python | Accepted | 7 ms | 30.3 MB |
| 702521325 | 2026/03/04 13:10:13 CST | python | Wrong Answer | N/A | N/A |
| 702521147 | 2026/03/04 13:09:31 CST | python | Wrong Answer | N/A | N/A |
| 661348138 | 2025/09/10 15:07:04 CST | python | Accepted | 8 ms | 27.7 MB |
| 661347716 | 2025/09/10 15:06:11 CST | python | Wrong Answer | N/A | N/A |
| 659095384 | 2025/09/03 14:45:06 CST | python | Accepted | 11 ms | 27.9 MB |
| 659092759 | 2025/09/03 14:38:49 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float(inf)
        left = 0
        curr_sum = 0
        for right, r_num in enumerate(nums):
            curr_sum += r_num
            while curr_sum >= target:
                min_len = min(min_len, right - left + 1)
                curr_sum -= nums[left]
                left += 1
        return min_len if min_len != float(inf) else 0
```

## 210. 课程表 II (`course-schedule-ii`)

- 题目链接：https://leetcode.cn/problems/course-schedule-ii/
- 难度：Medium
- 标签：Depth-First Search, Breadth-First Search, Graph, Topological Sort
- 总提交次数：6
- 最近提交时间：2026/04/05 10:39:46 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715243130 | 2026/04/05 10:39:46 CST | python | Accepted | 4 ms | 20.3 MB |
| 715242717 | 2026/04/05 10:38:21 CST | python | Wrong Answer | N/A | N/A |
| 680795169 | 2025/11/26 13:59:34 CST | python | Accepted | 0 ms | 18.6 MB |
| 676627484 | 2025/11/08 10:27:33 CST | python | Accepted | 2 ms | 18.9 MB |
| 676627264 | 2025/11/08 10:26:03 CST | python | Wrong Answer | N/A | N/A |
| 676627244 | 2025/11/08 10:25:54 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        in_degree = [0] * numCourses
        adj_list = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            in_degree[course] += 1
            adj_list[pre].append(course)
        
        dq = collections.deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                dq.append(i)
        
        while dq:
            curr_course = dq.popleft()
            res.append(curr_course)
            for next_course in adj_list[curr_course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    dq.append(next_course)
        
        return res if len(res) == numCourses else []
```

## 211. 添加与搜索单词 - 数据结构设计 (`design-add-and-search-words-data-structure`)

- 题目链接：https://leetcode.cn/problems/design-add-and-search-words-data-structure/
- 难度：Medium
- 标签：Depth-First Search, Design, Trie, String
- 总提交次数：21
- 最近提交时间：2025/11/19 14:15:17 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 679189400 | 2025/11/19 14:15:17 CST | python | Accepted | 1301 ms | 64.3 MB |
| 679188922 | 2025/11/19 14:13:39 CST | python | Wrong Answer | N/A | N/A |
| 679188822 | 2025/11/19 14:13:20 CST | python | Runtime Error | N/A | N/A |
| 679188610 | 2025/11/19 14:12:36 CST | python | Runtime Error | N/A | N/A |
| 679188260 | 2025/11/19 14:11:23 CST | python | Runtime Error | N/A | N/A |
| 678250997 | 2025/11/15 14:00:26 CST | python | Accepted | 1409 ms | 64.4 MB |
| 678250819 | 2025/11/15 13:59:12 CST | python | Runtime Error | N/A | N/A |
| 678250788 | 2025/11/15 13:59:03 CST | python | Runtime Error | N/A | N/A |
| 678250518 | 2025/11/15 13:57:00 CST | python | Runtime Error | N/A | N/A |
| 678250252 | 2025/11/15 13:55:04 CST | python | Runtime Error | N/A | N/A |
| 678250210 | 2025/11/15 13:54:50 CST | python | Runtime Error | N/A | N/A |
| 678232243 | 2025/11/15 12:21:43 CST | python | Accepted | 1158 ms | 64.4 MB |
| 678232061 | 2025/11/15 12:20:12 CST | python | Runtime Error | N/A | N/A |
| 678231648 | 2025/11/15 12:16:47 CST | python | Runtime Error | N/A | N/A |
| 678231529 | 2025/11/15 12:15:50 CST | python | Runtime Error | N/A | N/A |
| 678231450 | 2025/11/15 12:15:11 CST | python | Runtime Error | N/A | N/A |
| 678231281 | 2025/11/15 12:13:52 CST | python | Runtime Error | N/A | N/A |
| 677066413 | 2025/11/10 13:59:08 CST | python | Accepted | 1213 ms | 64.3 MB |
| 677065731 | 2025/11/10 13:55:55 CST | python | Wrong Answer | N/A | N/A |
| 677018616 | 2025/11/10 10:18:33 CST | python | Accepted | 1214 ms | 64.2 MB |
| 677018551 | 2025/11/10 10:18:18 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.childs:
                node.childs[ch] = TrieNode()
            node = node.childs[ch]
        node.is_end = True
        

    def search(self, word: str) -> bool:
        def dfs(node, idx):
            if idx == len(word):
                return node.is_end
            if word[idx] == '.':
                for child in node.childs.values():
                    if dfs(child, idx + 1):
                        return True
                return False
            else:
                if word[idx] not in node.childs:
                    return False
                return dfs(node.childs[word[idx]], idx + 1)
            
        return dfs(self.root, 0)
        

class TrieNode:
    def __init__(self):
        self.childs: [str, TrieNode] = {}
        self.is_end = False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
```

## 213. 打家劫舍 II (`house-robber-ii`)

- 题目链接：https://leetcode.cn/problems/house-robber-ii/
- 难度：Medium
- 标签：Array, Dynamic Programming
- 总提交次数：4
- 最近提交时间：2026/02/10 10:56:51 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 697675577 | 2026/02/10 10:56:51 CST | python | Accepted | 0 ms | 19.2 MB |
| 692500882 | 2026/01/19 18:47:46 CST | python | Accepted | 0 ms | 19.1 MB |
| 688690654 | 2026/01/03 11:11:12 CST | python | Accepted | 0 ms | 16.9 MB |
| 688690618 | 2026/01/03 11:10:53 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_linear(nums, left, right):
            n = right - left + 1
            if n == 1:
                return nums[left]
            prev_2, prev_1 = nums[left], max(nums[left], nums[left + 1])
            for i in range(left + 2, right + 1):
                curr = max(prev_1, prev_2 + nums[i])
                prev_2, prev_1 = prev_1, curr
            return prev_1

        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        best_1 = rob_linear(nums, 0, n - 2)
        best_2 = rob_linear(nums, 1, n - 1)
        return max(best_1, best_2)
```

## 215. 数组中的第K个最大元素 (`kth-largest-element-in-an-array`)

- 题目链接：https://leetcode.cn/problems/kth-largest-element-in-an-array/
- 难度：Medium
- 标签：Array, Divide and Conquer, Quickselect, Sorting, Heap (Priority Queue)
- 总提交次数：15
- 最近提交时间：2026/04/04 16:42:59 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715102644 | 2026/04/04 16:42:59 CST | python | Accepted | 107 ms | 30.6 MB |
| 715098889 | 2026/04/04 16:31:17 CST | python | Time Limit Exceeded | N/A | N/A |
| 715098673 | 2026/04/04 16:30:39 CST | python | Runtime Error | N/A | N/A |
| 715090295 | 2026/04/04 16:05:05 CST | python | Accepted | 39 ms | 30.5 MB |
| 715089970 | 2026/04/04 16:04:01 CST | python | Runtime Error | N/A | N/A |
| 685800614 | 2025/12/19 14:17:21 CST | python | Accepted | 57 ms | 28.2 MB |
| 685800562 | 2025/12/19 14:17:04 CST | python | Accepted | 55 ms | 28.3 MB |
| 685800513 | 2025/12/19 14:16:50 CST | python | Runtime Error | N/A | N/A |
| 685542051 | 2025/12/18 10:37:23 CST | python | Accepted | 39 ms | 28.5 MB |
| 679194529 | 2025/11/19 14:32:11 CST | python | Accepted | 52 ms | 28.1 MB |
| 679194454 | 2025/11/19 14:31:57 CST | python | Runtime Error | N/A | N/A |
| 679194129 | 2025/11/19 14:30:50 CST | python | Runtime Error | N/A | N/A |
| 679193837 | 2025/11/19 14:29:54 CST | python | Runtime Error | N/A | N/A |
| 679193285 | 2025/11/19 14:28:06 CST | python | Runtime Error | N/A | N/A |
| 676636771 | 2025/11/08 11:21:35 CST | python | Accepted | 47 ms | 28.3 MB |

### 最近一次 AC 代码

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = nums[random.randint(left, right)]
            lt, gt = self._partition(nums, left, right, pivot)
            if lt <= target <= gt:
                return nums[target]
            elif target < lt:
                right = lt - 1
            else:
                left = gt + 1
    
    def _partition(self, nums, left, right, pivot):
        lt = left
        i = left
        gt = right
        while i <= gt:
            if nums[i] < pivot:
                nums[lt], nums[i] = nums[i], nums[lt]
                i += 1
                lt += 1
            elif nums[i] > pivot:
                nums[i], nums[gt] = nums[gt], nums[i]
                gt -= 1
            else:
                i += 1
        return lt, gt
```

## 216. 组合总和 III (`combination-sum-iii`)

- 题目链接：https://leetcode.cn/problems/combination-sum-iii/
- 难度：Medium
- 标签：Array, Backtracking
- 总提交次数：4
- 最近提交时间：2026/04/08 21:41:39 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 716392495 | 2026/04/08 21:41:39 CST | python | Accepted | 3 ms | 19.1 MB |
| 699290365 | 2026/02/19 13:51:14 CST | python | Accepted | 3 ms | 19.2 MB |
| 687486787 | 2025/12/27 16:14:37 CST | python | Accepted | 0 ms | 16.9 MB |
| 687486746 | 2025/12/27 16:14:27 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        path = []
        res = []
        self.path_sum = 0
        def backtrack(start_num):
            if self.path_sum == n and len(path) == k:
                res.append(list(path))
                return
            if self.path_sum > n or len(path) > k:
                return
            for num in range(start_num, 10):
                path.append(num)
                self.path_sum += num
                backtrack(num + 1)
                self.path_sum -= num
                path.pop()
        backtrack(1)
        return res
```

## 217. 存在重复元素 (`contains-duplicate`)

- 题目链接：https://leetcode.cn/problems/contains-duplicate/
- 难度：Easy
- 标签：Array, Hash Table, Sorting
- 总提交次数：2
- 最近提交时间：2025/11/27 08:35:22 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 680973718 | 2025/11/27 08:35:22 CST | python | Accepted | 10 ms | 31 MB |
| 680973655 | 2025/11/27 08:34:14 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
```

## 219. 存在重复元素 II (`contains-duplicate-ii`)

- 题目链接：https://leetcode.cn/problems/contains-duplicate-ii/
- 难度：Easy
- 标签：Array, Hash Table, Sliding Window
- 总提交次数：7
- 最近提交时间：2026/03/23 14:51:45 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 710894186 | 2026/03/23 14:51:45 CST | python | Accepted | 59 ms | 31.2 MB |
| 708739483 | 2026/03/18 13:58:31 CST | python | Accepted | 35 ms | 31.2 MB |
| 680974043 | 2025/11/27 08:40:23 CST | python | Accepted | 35 ms | 36 MB |
| 661310713 | 2025/09/10 13:07:50 CST | python | Accepted | 27 ms | 35.9 MB |
| 658557214 | 2025/09/01 21:34:38 CST | python | Accepted | 35 ms | 29.9 MB |
| 658425933 | 2025/09/01 15:37:37 CST | python | Accepted | 39 ms | 30 MB |
| 653454646 | 2025/08/16 07:27:24 CST | python | Accepted | 51 ms | 30.2 MB |

### 最近一次 AC 代码

```python
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        left = 0
        for right, r_num in enumerate(nums):
            if r_num in window:
                return True
            window.add(r_num)
            if right - left + 1 > k:
                window.remove(nums[left])
                left += 1
        return False
```

## 220. 存在重复元素 III (`contains-duplicate-iii`)

- 题目链接：https://leetcode.cn/problems/contains-duplicate-iii/
- 难度：Hard
- 标签：Array, Bucket Sort, Ordered Set, Sorting, Sliding Window
- 总提交次数：13
- 最近提交时间：2026/03/23 17:07:19 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 710980255 | 2026/03/23 17:07:19 CST | python | Accepted | 122 ms | 37.1 MB |
| 708761707 | 2026/03/18 14:42:58 CST | python | Accepted | 132 ms | 36.9 MB |
| 708761552 | 2026/03/18 14:42:41 CST | python | Runtime Error | N/A | N/A |
| 708761044 | 2026/03/18 14:41:48 CST | python | Runtime Error | N/A | N/A |
| 680991882 | 2025/11/27 10:20:15 CST | python | Accepted | 264 ms | 30.6 MB |
| 680991752 | 2025/11/27 10:19:47 CST | python | Wrong Answer | N/A | N/A |
| 661329863 | 2025/09/10 14:24:30 CST | python | Accepted | 189 ms | 36.1 MB |
| 661329780 | 2025/09/10 14:24:18 CST | python | Runtime Error | N/A | N/A |
| 661329696 | 2025/09/10 14:24:04 CST | python | Runtime Error | N/A | N/A |
| 654879014 | 2025/08/20 16:58:53 CST | python | Accepted | 135 ms | 36 MB |
| 654878768 | 2025/08/20 16:58:25 CST | python | Runtime Error | N/A | N/A |
| 654144159 | 2025/08/18 16:00:40 CST | python | Accepted | 375 ms | 30.7 MB |
| 654141063 | 2025/08/18 15:54:17 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        buckets = {}
        w = valueDiff + 1
        for i, num in enumerate(nums):
            bucket_id = num // w
            if bucket_id in buckets:
                return True
            if bucket_id - 1 in buckets and abs(buckets[bucket_id - 1] - num) <= valueDiff:
                return True
            if bucket_id + 1 in buckets and abs(buckets[bucket_id + 1] - num) <= valueDiff:
                return True
            buckets[bucket_id] = num
            if i >= indexDiff:
                old_num = nums[i - indexDiff]
                del buckets[old_num // w]
        return False
```

## 221. 最大正方形 (`maximal-square`)

- 题目链接：https://leetcode.cn/problems/maximal-square/
- 难度：Medium
- 标签：Array, Dynamic Programming, Matrix
- 总提交次数：14
- 最近提交时间：2026/02/13 14:19:45 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 698386596 | 2026/02/13 14:19:45 CST | python | Accepted | 71 ms | 32.7 MB |
| 698386458 | 2026/02/13 14:19:01 CST | python | Wrong Answer | N/A | N/A |
| 697322950 | 2026/02/08 17:52:36 CST | python | Accepted | 103 ms | 32.5 MB |
| 697322873 | 2026/02/08 17:52:18 CST | python | Wrong Answer | N/A | N/A |
| 697322800 | 2026/02/08 17:52:06 CST | python | Wrong Answer | N/A | N/A |
| 697322667 | 2026/02/08 17:51:34 CST | python | Wrong Answer | N/A | N/A |
| 696056067 | 2026/02/03 10:49:08 CST | python | Accepted | 79 ms | 32.8 MB |
| 696055806 | 2026/02/03 10:48:12 CST | python | Wrong Answer | N/A | N/A |
| 696055175 | 2026/02/03 10:46:18 CST | python | Wrong Answer | N/A | N/A |
| 695792749 | 2026/02/02 10:44:18 CST | python | Accepted | 79 ms | 32.4 MB |
| 695792705 | 2026/02/02 10:44:10 CST | python | Wrong Answer | N/A | N/A |
| 695792270 | 2026/02/02 10:42:36 CST | python | Accepted | 71 ms | 32.2 MB |
| 695790772 | 2026/02/02 10:36:48 CST | python | Wrong Answer | N/A | N/A |
| 695672585 | 2026/02/01 17:54:06 CST | python | Accepted | 84 ms | 32.7 MB |

### 最近一次 AC 代码

```python
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        max_side = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    continue
                if i == 0 or i == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                max_side = max(max_side, dp[i][j])
        return max_side ** 2
```

## 222. 完全二叉树的节点个数 (`count-complete-tree-nodes`)

- 题目链接：https://leetcode.cn/problems/count-complete-tree-nodes/
- 难度：Easy
- 标签：Bit Manipulation, Tree, Binary Search, Binary Tree
- 总提交次数：6
- 最近提交时间：2026/04/04 10:20:10 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715017589 | 2026/04/04 10:20:10 CST | python | Accepted | 0 ms | 23.4 MB |
| 715017525 | 2026/04/04 10:19:49 CST | python | Runtime Error | N/A | N/A |
| 714773558 | 2026/04/03 10:26:08 CST | python | Accepted | 0 ms | 23.6 MB |
| 714571595 | 2026/04/02 16:13:02 CST | python | Accepted | 0 ms | 23.5 MB |
| 714571269 | 2026/04/02 16:12:20 CST | python | Wrong Answer | N/A | N/A |
| 714571176 | 2026/04/02 16:12:07 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftmost_height = self._left_height(root)
        rightmost_height = self._right_height(root)
        if leftmost_height == rightmost_height:
            return 2 ** leftmost_height - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    
    def _left_height(self, node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height
    
    def _right_height(self, node):
        height = 0
        while node:
            height += 1
            node = node.right
        return height
```

## 224. 基本计算器 (`basic-calculator`)

- 题目链接：https://leetcode.cn/problems/basic-calculator/
- 难度：Hard
- 标签：Stack, Recursion, Math, String
- 总提交次数：30
- 最近提交时间：2026/03/31 08:59:22 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 713724544 | 2026/03/31 08:59:22 CST | python | Accepted | 87 ms | 21.6 MB |
| 713724358 | 2026/03/31 08:58:05 CST | python | Wrong Answer | N/A | N/A |
| 713386814 | 2026/03/30 10:39:21 CST | python | Accepted | 87 ms | 21.5 MB |
| 713385792 | 2026/03/30 10:36:56 CST | python | Wrong Answer | N/A | N/A |
| 713385289 | 2026/03/30 10:35:43 CST | python | Runtime Error | N/A | N/A |
| 713368519 | 2026/03/30 09:44:15 CST | python | Accepted | 39 ms | 20.2 MB |
| 713368251 | 2026/03/30 09:43:09 CST | python | Wrong Answer | N/A | N/A |
| 685802662 | 2025/12/19 14:26:42 CST | python | Accepted | 43 ms | 18.2 MB |
| 685802198 | 2025/12/19 14:24:34 CST | python | Wrong Answer | N/A | N/A |
| 685802024 | 2025/12/19 14:23:48 CST | python | Wrong Answer | N/A | N/A |
| 685541242 | 2025/12/18 10:34:19 CST | python | Accepted | 47 ms | 18 MB |
| 684122720 | 2025/12/11 15:13:21 CST | python | Accepted | 47 ms | 18.2 MB |
| 684122625 | 2025/12/11 15:13:04 CST | python | Wrong Answer | N/A | N/A |
| 684122399 | 2025/12/11 15:12:26 CST | python | Wrong Answer | N/A | N/A |
| 684120419 | 2025/12/11 15:06:37 CST | python | Accepted | 45 ms | 18.1 MB |
| 684119704 | 2025/12/11 15:04:23 CST | python | Accepted | 39 ms | 18.1 MB |
| 684119632 | 2025/12/11 15:04:12 CST | python | Wrong Answer | N/A | N/A |
| 684119578 | 2025/12/11 15:04:05 CST | python | Accepted | 43 ms | 18 MB |
| 684118862 | 2025/12/11 15:01:41 CST | python | Wrong Answer | N/A | N/A |
| 684118726 | 2025/12/11 15:01:14 CST | python | Wrong Answer | N/A | N/A |
| 684118637 | 2025/12/11 15:00:57 CST | python | Wrong Answer | N/A | N/A |
| 684118147 | 2025/12/11 14:59:21 CST | python | Wrong Answer | N/A | N/A |
| 683396632 | 2025/12/08 14:00:35 CST | python | Accepted | 39 ms | 18.1 MB |
| 683396439 | 2025/12/08 13:59:31 CST | python | Wrong Answer | N/A | N/A |
| 683396385 | 2025/12/08 13:59:09 CST | python | Runtime Error | N/A | N/A |
| 683394299 | 2025/12/08 13:47:43 CST | python | Accepted | 47 ms | 18.3 MB |
| 683394189 | 2025/12/08 13:47:05 CST | python | Wrong Answer | N/A | N/A |
| 683394034 | 2025/12/08 13:46:11 CST | python | Wrong Answer | N/A | N/A |
| 683364154 | 2025/12/08 11:00:20 CST | python | Accepted | 47 ms | 18 MB |
| 683363406 | 2025/12/08 10:57:53 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def calculate(self, s: str) -> int:
        def dfs(i):
            num = 0
            stack = []
            sign = '+'
            while i < len(s):
                ch = s[i]
                if ch.isdigit():
                    num = num * 10 + int(ch)
                elif ch == '(':
                    num, i = dfs(i + 1)
                
                if ch in '+-)' or i == len(s) - 1:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    num = 0
                    if ch == ')':
                        return sum(stack), i
                    sign = ch
                i += 1
            return sum(stack), i
        return dfs(0)[0]
```

## 225. 用队列实现栈 (`implement-stack-using-queues`)

- 题目链接：https://leetcode.cn/problems/implement-stack-using-queues/
- 难度：Easy
- 标签：Stack, Design, Queue
- 总提交次数：1
- 最近提交时间：2026/03/25 08:56:52 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 711655458 | 2026/03/25 08:56:52 CST | python | Accepted | 0 ms | 19.4 MB |

### 最近一次 AC 代码

```python
class MyStack:

    def __init__(self):
        self.dq = collections.deque()
        

    def push(self, x: int) -> None:
        self.dq.append(x)
        for _ in range(len(self.dq) - 1):
            self.dq.append(self.dq.popleft())
        

    def pop(self) -> int:
        return self.dq.popleft()
        

    def top(self) -> int:
        return self.dq[0]
        

    def empty(self) -> bool:
        return len(self.dq) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
```

## 226. 翻转二叉树 (`invert-binary-tree`)

- 题目链接：https://leetcode.cn/problems/invert-binary-tree/
- 难度：Easy
- 标签：Tree, Depth-First Search, Breadth-First Search, Binary Tree
- 总提交次数：7
- 最近提交时间：2026/04/05 21:57:03 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715426740 | 2026/04/05 21:57:03 CST | python | Accepted | 0 ms | 19.1 MB |
| 715426688 | 2026/04/05 21:56:53 CST | python | Wrong Answer | N/A | N/A |
| 701453737 | 2026/03/01 15:10:45 CST | python | Accepted | 0 ms | 19.2 MB |
| 701453537 | 2026/03/01 15:10:15 CST | python | Wrong Answer | N/A | N/A |
| 701453434 | 2026/03/01 15:10:00 CST | python | Runtime Error | N/A | N/A |
| 686999084 | 2025/12/25 09:16:51 CST | python | Accepted | 0 ms | 17 MB |
| 686998783 | 2025/12/25 09:14:27 CST | python | Accepted | 0 ms | 17 MB |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        left_inverted = self.invertTree(root.left)
        right_inverted = self.invertTree(root.right)
        root.left = right_inverted
        root.right = left_inverted
        return root
```

## 227. 基本计算器 II (`basic-calculator-ii`)

- 题目链接：https://leetcode.cn/problems/basic-calculator-ii/
- 难度：Medium
- 标签：Stack, Math, String
- 总提交次数：6
- 最近提交时间：2026/03/31 09:41:40 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 713732717 | 2026/03/31 09:41:40 CST | python | Accepted | 79 ms | 22 MB |
| 713732423 | 2026/03/31 09:40:24 CST | python | Wrong Answer | N/A | N/A |
| 713398430 | 2026/03/30 11:06:02 CST | python | Accepted | 56 ms | 22.2 MB |
| 713393981 | 2026/03/30 10:55:39 CST | python | Accepted | 61 ms | 22 MB |
| 713393250 | 2026/03/30 10:53:57 CST | python | Wrong Answer | N/A | N/A |
| 713393057 | 2026/03/30 10:53:29 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        stack = []
        sign = '+'
        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            if (not ch.isdigit() and ch != ' ') or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                elif sign == '/':
                    stack.append(int(stack.pop() / num))
                num = 0
                sign = ch
        return sum(stack)
```

## 230. 二叉搜索树中第 K 小的元素 (`kth-smallest-element-in-a-bst`)

- 题目链接：https://leetcode.cn/problems/kth-smallest-element-in-a-bst/
- 难度：Medium
- 标签：Tree, Depth-First Search, Binary Search Tree, Binary Tree
- 总提交次数：4
- 最近提交时间：2026/04/03 11:27:48 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 714795952 | 2026/04/03 11:27:48 CST | python | Accepted | 4 ms | 21.8 MB |
| 714795629 | 2026/04/03 11:26:53 CST | python | Runtime Error | N/A | N/A |
| 714793547 | 2026/04/03 11:21:01 CST | python | Runtime Error | N/A | N/A |
| 701745456 | 2026/03/02 13:37:28 CST | python | Accepted | 0 ms | 22 MB |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
```

## 232. 用栈实现队列 (`implement-queue-using-stacks`)

- 题目链接：https://leetcode.cn/problems/implement-queue-using-stacks/
- 难度：Easy
- 标签：Stack, Design, Queue
- 总提交次数：1
- 最近提交时间：2026/03/25 08:39:59 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 711653142 | 2026/03/25 08:39:59 CST | python | Accepted | 0 ms | 19.2 MB |

### 最近一次 AC 代码

```python
class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        

    def push(self, x: int) -> None:
        self.s1.append(x)
        

    def pop(self) -> int:
        self.peek()
        return self.s2.pop()
        

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]
        

    def empty(self) -> bool:
        return not self.s1 and not self.s2
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
```

## 234. 回文链表 (`palindrome-linked-list`)

- 题目链接：https://leetcode.cn/problems/palindrome-linked-list/
- 难度：Easy
- 标签：Stack, Recursion, Linked List, Two Pointers
- 总提交次数：3
- 最近提交时间：2026/04/01 13:39:06 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 714168864 | 2026/04/01 13:39:06 CST | python | Accepted | 54 ms | 41.7 MB |
| 714168187 | 2026/04/01 13:36:22 CST | python | Runtime Error | N/A | N/A |
| 684375581 | 2025/12/12 16:54:40 CST | python | Accepted | 36 ms | 34.1 MB |

### 最近一次 AC 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        second_half_head = self.reverse(slow)
        p1, p2 = head, second_half_head
        while p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True
    
    def reverse(self, head):
        pre, cur = None, head
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        return pre
```

## 236. 二叉树的最近公共祖先 (`lowest-common-ancestor-of-a-binary-tree`)

- 题目链接：https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/
- 难度：Medium
- 标签：Tree, Depth-First Search, Binary Tree
- 总提交次数：3
- 最近提交时间：2026/02/28 13:33:45 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 701167632 | 2026/02/28 13:33:45 CST | python | Accepted | 51 ms | 24.1 MB |
| 680522250 | 2025/11/25 12:50:41 CST | python | Accepted | 81 ms | 21.7 MB |
| 680221648 | 2025/11/24 10:00:58 CST | python | Accepted | 56 ms | 21.6 MB |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root is p or root is q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right
```

## 238. 除了自身以外数组的乘积 (`product-of-array-except-self`)

- 题目链接：https://leetcode.cn/problems/product-of-array-except-self/
- 难度：Medium
- 标签：Array, Prefix Sum
- 总提交次数：5
- 最近提交时间：2026/03/16 10:26:24 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 707679390 | 2026/03/16 10:26:24 CST | python | Accepted | 27 ms | 25.4 MB |
| 663847982 | 2025/09/18 12:43:22 CST | python | Accepted | 27 ms | 23 MB |
| 662017082 | 2025/09/12 14:28:02 CST | python | Accepted | 19 ms | 22.9 MB |
| 662006311 | 2025/09/12 13:52:49 CST | python | Accepted | 31 ms | 26.5 MB |
| 662006248 | 2025/09/12 13:52:37 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        res[0] = 1
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]
        
        right_product = 1
        for i in range(n - 1, -1, -1):
            res[i] = res[i] * right_product
            right_product *= nums[i]
        return res
```

## 239. 滑动窗口最大值 (`sliding-window-maximum`)

- 题目链接：https://leetcode.cn/problems/sliding-window-maximum/
- 难度：Hard
- 标签：Queue, Array, Sliding Window, Monotonic Queue, Heap (Priority Queue)
- 总提交次数：17
- 最近提交时间：2026/03/26 08:55:48 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 712065117 | 2026/03/26 08:55:48 CST | python | Accepted | 175 ms | 34.5 MB |
| 712065022 | 2026/03/26 08:54:53 CST | python | Wrong Answer | N/A | N/A |
| 711705636 | 2026/03/25 11:07:17 CST | python | Accepted | 164 ms | 34.8 MB |
| 680532123 | 2025/11/25 13:50:56 CST | python | Accepted | 164 ms | 30.8 MB |
| 677584425 | 2025/11/12 13:55:38 CST | python | Accepted | 163 ms | 30.9 MB |
| 677584285 | 2025/11/12 13:54:52 CST | python | Wrong Answer | N/A | N/A |
| 677584205 | 2025/11/12 13:54:31 CST | python | Runtime Error | N/A | N/A |
| 677332964 | 2025/11/11 14:36:32 CST | python | Accepted | 171 ms | 31.8 MB |
| 677332756 | 2025/11/11 14:35:55 CST | python | Wrong Answer | N/A | N/A |
| 676481534 | 2025/11/07 14:19:17 CST | python | Accepted | 196 ms | 31.6 MB |
| 676481318 | 2025/11/07 14:18:25 CST | python | Wrong Answer | N/A | N/A |
| 676480799 | 2025/11/07 14:16:16 CST | python | Wrong Answer | N/A | N/A |
| 675945726 | 2025/11/05 09:53:58 CST | python | Accepted | 163 ms | 30.9 MB |
| 675445776 | 2025/11/03 10:57:31 CST | python | Accepted | 163 ms | 30.6 MB |
| 675445017 | 2025/11/03 10:55:15 CST | python | Wrong Answer | N/A | N/A |
| 675444577 | 2025/11/03 10:53:54 CST | python | Wrong Answer | N/A | N/A |
| 675444049 | 2025/11/03 10:52:19 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        dq = collections.deque()
        for i, num in enumerate(nums):
            while dq and nums[dq[-1]] <= num:
                dq.pop()
            dq.append(i)
            if dq[0] <= i - k:
                dq.popleft()
            if i >= k - 1:
                res.append(nums[dq[0]])
        return res
```

## 240. 搜索二维矩阵 II (`search-a-2d-matrix-ii`)

- 题目链接：https://leetcode.cn/problems/search-a-2d-matrix-ii/
- 难度：Medium
- 标签：Array, Binary Search, Divide and Conquer, Matrix
- 总提交次数：6
- 最近提交时间：2026/03/19 13:56:09 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 709221780 | 2026/03/19 13:56:09 CST | python | Accepted | 138 ms | 25.2 MB |
| 703394610 | 2026/03/06 13:49:24 CST | python | Accepted | 156 ms | 25.1 MB |
| 703394343 | 2026/03/06 13:48:42 CST | python | Wrong Answer | N/A | N/A |
| 685539556 | 2025/12/18 10:27:45 CST | python | Accepted | 159 ms | 23 MB |
| 685538517 | 2025/12/18 10:23:42 CST | python | Wrong Answer | N/A | N/A |
| 685294418 | 2025/12/17 09:11:35 CST | python | Accepted | 153 ms | 23.6 MB |

### 最近一次 AC 代码

```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        m, n = 0, cols - 1
        while m < rows and n >= 0:
            curr = matrix[m][n]
            if curr == target:
                return True
            elif curr < target:
                m += 1
            else:
                n -= 1
        return False
```

## 241. 为运算表达式设计优先级 (`different-ways-to-add-parentheses`)

- 题目链接：https://leetcode.cn/problems/different-ways-to-add-parentheses/
- 难度：Medium
- 标签：Recursion, Memoization, Math, String, Dynamic Programming
- 总提交次数：1
- 最近提交时间：2026/04/11 10:34:26 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 717081859 | 2026/04/11 10:34:26 CST | python | Accepted | 0 ms | 19.2 MB |

### 最近一次 AC 代码

```python
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}
        def compute(expr):
            if expr in memo:
                return memo[expr]
            res = []
            for i, ch in enumerate(expr):
                if ch in '+-*':
                    left = compute(expr[:i])
                    right = compute(expr[i + 1:])
                    for l in left:
                        for r in right:
                            if ch == '+':
                                res.append(l + r)
                            elif ch == '-':
                                res.append(l - r)
                            else:
                                res.append(l * r)
            if not res:
                res.append(int(expr))
            memo[expr] = res
            return res
        return compute(expression)
```

## 242. 有效的字母异位词 (`valid-anagram`)

- 题目链接：https://leetcode.cn/problems/valid-anagram/
- 难度：Easy
- 标签：Hash Table, String, Sorting
- 总提交次数：1
- 最近提交时间：2026/03/29 17:51:48 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 713219162 | 2026/03/29 17:51:48 CST | python | Accepted | 9 ms | 19.4 MB |

### 最近一次 AC 代码

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = collections.defaultdict(int)
        for ch in s:
            count[ch] += 1
        
        for ch in t:
            count[ch] -= 1
            if count[ch] < 0:
                return False
        
        return True
```

## 247. 中心对称数 II (`strobogrammatic-number-ii`)

- 题目链接：https://leetcode.cn/problems/strobogrammatic-number-ii/
- 难度：Medium
- 标签：Recursion, Array, String
- 总提交次数：2
- 最近提交时间：2026/02/24 08:52:24 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 700094560 | 2026/02/24 08:52:24 CST | python | Accepted | 11 ms | 28.9 MB |
| 700094503 | 2026/02/24 08:51:36 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        def build(k):
            if k == 0:
                return ['']
            if k == 1:
                return ['0', '1', '8']
            inner_list = build(k - 2)
            res = []
            for center in inner_list:
                if k != n:
                    res.append('0' + center + '0')
                res.append('1' + center + '1')
                res.append('8' + center + '8')
                res.append('6' + center + '9')
                res.append('9' + center + '6')
            return res
        return build(n)
```

## 249. 移位字符串分组 (`group-shifted-strings`)

- 题目链接：https://leetcode.cn/problems/group-shifted-strings/
- 难度：Medium
- 标签：Array, Hash Table, String
- 总提交次数：2
- 最近提交时间：2024/09/05 08:50:42 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 561684691 | 2024/09/05 08:50:42 CST | python | Accepted | 42 ms | 16.4 MB |
| 561578027 | 2024/09/04 20:55:03 CST | python | Accepted | 36 ms | 16.6 MB |

### 最近一次 AC 代码

```python
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for input_string in strings:
            if len(input_string) == 1:
                key = ()
            else:
                key = tuple(
                    (ord(input_string[i]) - ord(input_string[i - 1])) % 26
                    for i in range(1, len(input_string))
                )
            groups[key].append(input_string)
        return list(groups.values())
```

## 250. 统计同值子树 (`count-univalue-subtrees`)

- 题目链接：https://leetcode.cn/problems/count-univalue-subtrees/
- 难度：Medium
- 标签：Tree, Depth-First Search, Binary Tree
- 总提交次数：2
- 最近提交时间：2026/02/28 11:21:59 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 701142534 | 2026/02/28 11:21:59 CST | python | Accepted | 0 ms | 19.3 MB |
| 701142374 | 2026/02/28 11:21:26 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        def is_uni(node):
            if not node:
                return True
            left_uni = is_uni(node.left)
            right_uni = is_uni(node.right)
            if not left_uni or not right_uni:
                return False
            
            if node.left and node.left.val != node.val:
                return False
            
            if node.right and node.right.val != node.val:
                return False
            
            self.count += 1
            return True
        is_uni(root)
        return self.count
```

## 252. 会议室 (`meeting-rooms`)

- 题目链接：https://leetcode.cn/problems/meeting-rooms/
- 难度：Easy
- 标签：Array, Sorting
- 总提交次数：2
- 最近提交时间：2026/02/26 10:08:15 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 700598695 | 2026/02/26 10:08:15 CST | python | Accepted | 7 ms | 20.9 MB |
| 700598578 | 2026/02/26 10:07:43 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False
        return True
```

## 253. 会议室 II (`meeting-rooms-ii`)

- 题目链接：https://leetcode.cn/problems/meeting-rooms-ii/
- 难度：Medium
- 标签：Greedy, Array, Two Pointers, Prefix Sum, Sorting, Heap (Priority Queue)
- 总提交次数：5
- 最近提交时间：2026/02/26 10:14:47 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 700600217 | 2026/02/26 10:14:47 CST | python | Accepted | 4 ms | 21.1 MB |
| 696544175 | 2026/02/05 09:46:52 CST | python | Accepted | 7 ms | 21 MB |
| 696313299 | 2026/02/04 10:32:12 CST | python | Accepted | 0 ms | 21.3 MB |
| 696312967 | 2026/02/04 10:31:03 CST | python | Wrong Answer | N/A | N/A |
| 696138724 | 2026/02/03 15:57:21 CST | python | Accepted | 3 ms | 21.2 MB |

### 最近一次 AC 代码

```python
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        min_heap = []
        for start, end in intervals:
            if min_heap and start >= min_heap[0]:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, end)
        return len(min_heap)
```

## 254. 因子的组合 (`factor-combinations`)

- 题目链接：https://leetcode.cn/problems/factor-combinations/
- 难度：Medium
- 标签：Backtracking
- 总提交次数：2
- 最近提交时间：2026/02/24 10:25:54 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 700107904 | 2026/02/24 10:25:54 CST | python | Accepted | 19 ms | 20.5 MB |
| 700107838 | 2026/02/24 10:25:37 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        path = []
        self.remian = n
        def backtrack(start_factor):
            upper = math.isqrt(self.remian)
            for f in range(start_factor, upper + 1):
                if self.remian % f != 0:
                    continue
                other = self.remian // f
                res.append(list(path) + [f, other])
                path.append(f)
                self.remian //= f
                backtrack(f)
                self.remian *= f
                path.pop()
        backtrack(2)
        return res
```

## 255. 验证二叉搜索树的前序遍历序列 (`verify-preorder-sequence-in-binary-search-tree`)

- 题目链接：https://leetcode.cn/problems/verify-preorder-sequence-in-binary-search-tree/
- 难度：Medium
- 标签：Stack, Tree, Binary Search Tree, Recursion, Array, Binary Tree, Monotonic Stack
- 总提交次数：2
- 最近提交时间：2026/03/02 14:08:34 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 701755067 | 2026/03/02 14:08:34 CST | python | Accepted | 11 ms | 20 MB |
| 701436571 | 2026/03/01 14:18:14 CST | python | Accepted | 7 ms | 20 MB |

### 最近一次 AC 代码

```python
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        lower_bound = float('-inf')
        for num in preorder:
            if num < lower_bound:
                return False
            while stack and stack[-1] < num:
                lower_bound = stack.pop()
            stack.append(num)
        return True
```

## 256. 粉刷房子 (`paint-house`)

- 题目链接：https://leetcode.cn/problems/paint-house/
- 难度：Medium
- 标签：Array, Dynamic Programming
- 总提交次数：2
- 最近提交时间：2026/02/25 08:30:30 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 700332791 | 2026/02/25 08:30:30 CST | python | Accepted | 3 ms | 19.1 MB |
| 700332742 | 2026/02/25 08:29:38 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        for i in range(1, n):
            costs[i][0] += min(costs[i-1][1], costs[i-1][2])
            costs[i][1] += min(costs[i-1][0], costs[i-1][2])
            costs[i][2] += min(costs[i-1][1], costs[i-1][0])
        return min(costs[n-1])
```

## 257. 二叉树的所有路径 (`binary-tree-paths`)

- 题目链接：https://leetcode.cn/problems/binary-tree-paths/
- 难度：Easy
- 标签：Tree, Depth-First Search, String, Backtracking, Binary Tree
- 总提交次数：1
- 最近提交时间：2026/04/07 12:16:08 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715851882 | 2026/04/07 12:16:08 CST | python | Accepted | 0 ms | 19.1 MB |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        res = []
        path = []
        def traverse(node):
            path.append(str(node.val))
            if node.left is None and node.right is None:
                res.append('->'.join(path))
            else:
                if node.left:
                    traverse(node.left)
                if node.right:
                    traverse(node.right)
            path.pop()
        traverse(root)
        return res
```

## 261. 以图判树 (`graph-valid-tree`)

- 题目链接：https://leetcode.cn/problems/graph-valid-tree/
- 难度：Medium
- 标签：Depth-First Search, Breadth-First Search, Union Find, Graph
- 总提交次数：1
- 最近提交时间：2026/04/05 11:51:03 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715265511 | 2026/04/05 11:51:03 CST | python | Accepted | 0 ms | 20.2 MB |

### 最近一次 AC 代码

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_x]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True 


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        un = UnionFind(n)
        
        for x, y in edges:
            if not un.union(x, y):
                return False
        
        return True
```

## 265. 粉刷房子 II (`paint-house-ii`)

- 题目链接：https://leetcode.cn/problems/paint-house-ii/
- 难度：Hard
- 标签：Array, Dynamic Programming
- 总提交次数：1
- 最近提交时间：2026/02/25 09:56:47 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 700342776 | 2026/02/25 09:56:47 CST | python | Accepted | 15 ms | 19.4 MB |

### 最近一次 AC 代码

```python
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n, k = len(costs), len(costs[0])
        for i in range(1, n):
            mins = heapq.nsmallest(2, [(val, idx) for idx, val in enumerate(costs[i-1])])
            min1_val, min1_idx = mins[0]
            min2_val, _ = mins[1]
            for j in range(k):
                if j == min1_idx:
                    costs[i][j] += min2_val
                else:
                    costs[i][j] += min1_val
        return min(costs[n-1])
```

## 266. 回文排列 (`palindrome-permutation`)

- 题目链接：https://leetcode.cn/problems/palindrome-permutation/
- 难度：Easy
- 标签：Bit Manipulation, Hash Table, String
- 总提交次数：1
- 最近提交时间：2024/09/01 15:43:39 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 560409120 | 2024/09/01 15:43:39 CST | python | Accepted | 41 ms | 16.4 MB |

### 最近一次 AC 代码

```python
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counts = Counter(s)
        odd_cnt = 0
        for cnt in counts.values():
            if cnt % 2 == 1:
                odd_cnt += 1
        if odd_cnt <= 1:
            return True
        else:
            return False
```

## 269. 火星词典 (`alien-dictionary`)

- 题目链接：https://leetcode.cn/problems/alien-dictionary/
- 难度：Hard
- 标签：Depth-First Search, Breadth-First Search, Graph, Topological Sort, Array, String
- 总提交次数：2
- 最近提交时间：2026/03/10 14:36:37 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 705092603 | 2026/03/10 14:36:37 CST | python | Accepted | 0 ms | 19.2 MB |
| 705092398 | 2026/03/10 14:36:13 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = {char: set() for word in words for char in word}
        indegree = {char : 0 for char in graph}
        for i in range(len(words) - 1):
            word_1 = words[i]
            word_2 = words[i + 1]
            min_len = min(len(word_1), len(word_2))
            if len(word_1) > len(word_2) and word_1[:min_len] == word_2[:min_len]:
                return ''
            for j in range(min_len):
                if word_1[j] == word_2[j]:
                    continue
                if word_2[j] not in graph[word_1[j]]:
                    graph[word_1[j]].add(word_2[j])
                    indegree[word_2[j]] += 1
                break
        dq = collections.deque()
        for char in indegree:
            if indegree[char] == 0:
                dq.append(char)
        order = []
        while dq:
            char = dq.popleft()
            order.append(char)
            for neighbor in graph[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    dq.append(neighbor)
        return ''.join(order) if len(order) == len(graph) else ''
```

## 270. 最接近的二叉搜索树值 (`closest-binary-search-tree-value`)

- 题目链接：https://leetcode.cn/problems/closest-binary-search-tree-value/
- 难度：Easy
- 标签：Tree, Depth-First Search, Binary Search Tree, Binary Search, Binary Tree
- 总提交次数：3
- 最近提交时间：2026/03/06 14:40:43 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 703417084 | 2026/03/06 14:40:43 CST | python | Accepted | 0 ms | 20.6 MB |
| 701764735 | 2026/03/02 14:33:11 CST | python | Accepted | 0 ms | 20.6 MB |
| 701762136 | 2026/03/02 14:27:20 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        curr = root
        best = root.val
        while curr:
            curr_diff = abs(curr.val - target)
            best_diff = abs(best - target)
            if curr_diff < best_diff or (curr_diff == best_diff and curr.val < best):
                best = curr.val
            if target < curr.val:
                curr = curr.left
            elif target > curr.val:
                curr = curr.right
            else:
                return curr.val
        return best
```

## 271. 字符串的编码与解码 (`encode-and-decode-strings`)

- 题目链接：https://leetcode.cn/problems/encode-and-decode-strings/
- 难度：Medium
- 标签：Design, Array, String
- 总提交次数：2
- 最近提交时间：2026/03/13 16:10:05 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 706600782 | 2026/03/13 16:10:05 CST | python | Accepted | 77 ms | 19.3 MB |
| 706599260 | 2026/03/13 16:07:52 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        parts = []
        for string in strs:
            string_len = len(string)
            parts.append(f'{string_len}#{string}')
        return ''.join(parts)
    

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        index = 0
        while index < len(s):
            sharp_index = index
            while s[sharp_index] != '#':
                sharp_index += 1
            string_len = int(s[index:sharp_index])
            string_start = sharp_index + 1
            string_end = string_start + string_len
            res.append(s[string_start:string_end])
            index = string_end
        return res

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
```

## 272. 最接近的二叉搜索树值 II (`closest-binary-search-tree-value-ii`)

- 题目链接：https://leetcode.cn/problems/closest-binary-search-tree-value-ii/
- 难度：Hard
- 标签：Stack, Tree, Depth-First Search, Binary Search Tree, Two Pointers, Binary Tree, Heap (Priority Queue)
- 总提交次数：1
- 最近提交时间：2026/03/02 14:54:40 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 701774460 | 2026/03/02 14:54:40 CST | python | Accepted | 0 ms | 20.7 MB |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        dq = collections.deque()
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if len(dq) < k:
                dq.append(node.val)
            else:
                if abs(dq[0] - target) > abs(node.val - target):
                    dq.popleft()
                    dq.append(node.val)
                else:
                    return
            inorder(node.right)
        inorder(root)
        return list(dq)
```

## 276. 栅栏涂色 (`paint-fence`)

- 题目链接：https://leetcode.cn/problems/paint-fence/
- 难度：Medium
- 标签：Dynamic Programming
- 总提交次数：2
- 最近提交时间：2026/02/25 08:23:01 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 700332444 | 2026/02/25 08:23:01 CST | python | Accepted | 0 ms | 19.2 MB |
| 700332428 | 2026/02/25 08:22:39 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        if n == 2:
            return k * k
        prev_2, prev_1 = k, k * k
        for i in range(3, n + 1):
            curr = prev_1 * (k - 1) + prev_2 * (k - 1)
            prev_2, prev_1 = prev_1, curr
        return prev_1
```

## 277. 搜寻名人 (`find-the-celebrity`)

- 题目链接：https://leetcode.cn/problems/find-the-celebrity/
- 难度：Medium
- 标签：Graph, Two Pointers, Interactive
- 总提交次数：1
- 最近提交时间：2026/03/07 20:34:27 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 703950167 | 2026/03/07 20:34:27 CST | python | Accepted | 923 ms | 19.1 MB |

### 最近一次 AC 代码

```python
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i
        for i in range(n):
            if i == candidate:
                continue
            if knows(candidate, i) or not knows(i, candidate):
                return -1
        return candidate
```

## 279. 完全平方数 (`perfect-squares`)

- 题目链接：https://leetcode.cn/problems/perfect-squares/
- 难度：Medium
- 标签：Breadth-First Search, Math, Dynamic Programming
- 总提交次数：9
- 最近提交时间：2026/02/13 14:38:16 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 698390261 | 2026/02/13 14:38:16 CST | python | Accepted | 2650 ms | 27.9 MB |
| 698389827 | 2026/02/13 14:36:20 CST | python | Wrong Answer | N/A | N/A |
| 689431659 | 2026/01/06 15:03:49 CST | python | Accepted | 2757 ms | 27.8 MB |
| 689431164 | 2026/01/06 15:02:06 CST | python | Wrong Answer | N/A | N/A |
| 689393512 | 2026/01/06 11:53:06 CST | python | Accepted | 1437 ms | 19.3 MB |
| 689393141 | 2026/01/06 11:51:34 CST | python | Wrong Answer | N/A | N/A |
| 689393048 | 2026/01/06 11:51:14 CST | python | Memory Limit Exceeded | N/A | N/A |
| 689392598 | 2026/01/06 11:49:22 CST | python | Memory Limit Exceeded | N/A | N/A |
| 689188353 | 2026/01/05 15:23:55 CST | python | Accepted | 1492 ms | 19.4 MB |

### 最近一次 AC 代码

```python
class Solution:
    def numSquares(self, n: int) -> int:
        k = 1
        squares = []
        while k ** 2 <= n:
            squares.append(k ** 2)
            k += 1
        m = len(squares)
        dp = [[n + 1] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = 0
        for i in range(1, m + 1):
            sq = squares[i - 1]
            for j in range(n + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= sq:
                    dp[i][j] = min(dp[i][j], dp[i][j - sq] + 1)
        return dp[m][n]
```

## 280. 摆动排序 (`wiggle-sort`)

- 题目链接：https://leetcode.cn/problems/wiggle-sort/
- 难度：Medium
- 标签：Greedy, Array, Sorting
- 总提交次数：7
- 最近提交时间：2026/02/23 20:49:40 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 700035529 | 2026/02/23 20:49:40 CST | python | Accepted | 0 ms | 19.6 MB |
| 700035464 | 2026/02/23 20:49:25 CST | python | Runtime Error | N/A | N/A |
| 697221580 | 2026/02/08 10:35:57 CST | python | Accepted | 3 ms | 19.7 MB |
| 697221028 | 2026/02/08 10:34:21 CST | python | Runtime Error | N/A | N/A |
| 696820803 | 2026/02/06 11:27:43 CST | python | Accepted | 3 ms | 19.8 MB |
| 558294740 | 2024/08/25 07:53:30 CST | python | Accepted | 42 ms | 17.4 MB |
| 557549307 | 2024/08/22 10:28:26 CST | python | Accepted | 37 ms | 17.3 MB |

### 最近一次 AC 代码

```python
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1):
            if (i % 2 == 0 and nums[i] > nums[i + 1]) or (i % 2 == 1 and nums[i] < nums[i + 1]):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
```

## 281. 锯齿迭代器 (`zigzag-iterator`)

- 题目链接：https://leetcode.cn/problems/zigzag-iterator/
- 难度：Medium
- 标签：Design, Queue, Array, Iterator
- 总提交次数：1
- 最近提交时间：2026/03/13 16:26:20 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 706611947 | 2026/03/13 16:26:20 CST | python | Accepted | 64 ms | 19.4 MB |

### 最近一次 AC 代码

```python
class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.dq = collections.deque()
        if v1:
            self.dq.append((v1, 0))
        if v2:
            self.dq.append((v2, 0))        

    def next(self) -> int:
        arr, index = self.dq.popleft()
        val = arr[index]
        if index + 1 < len(arr):
            self.dq.append((arr, index + 1))
        return val

    def hasNext(self) -> bool:
        return bool(self.dq)
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
```

## 283. 移动零 (`move-zeroes`)

- 题目链接：https://leetcode.cn/problems/move-zeroes/
- 难度：Easy
- 标签：Array, Two Pointers
- 总提交次数：2
- 最近提交时间：2026/03/23 10:10:29 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 710782948 | 2026/03/23 10:10:29 CST | python | Accepted | 3 ms | 20.4 MB |
| 708220939 | 2026/03/17 12:28:01 CST | python | Accepted | 7 ms | 20.3 MB |

### 最近一次 AC 代码

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
        for i in range(slow, len(nums)):
            nums[i] = 0
```

## 286. 墙与门 (`walls-and-gates`)

- 题目链接：https://leetcode.cn/problems/walls-and-gates/
- 难度：Medium
- 标签：Breadth-First Search, Array, Matrix
- 总提交次数：1
- 最近提交时间：2026/03/10 10:15:52 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 704978660 | 2026/03/10 10:15:52 CST | python | Accepted | 25 ms | 21.7 MB |

### 最近一次 AC 代码

```python
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return
        rows, cols = len(rooms), len(rooms[0])
        dq = collections.deque()
        inf = 2147483647
        for row in range(rows):
            for col in range(cols):
                if rooms[row][col] == 0:
                    dq.append((row, col))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while dq:
            row, col = dq.popleft()
            for dr, dc in directions:
                next_row, next_col = row + dr, col + dc
                if not (0 <= next_row < rows and 0 <= next_col < cols):
                    continue
                if rooms[next_row][next_col] != inf:
                    continue
                rooms[next_row][next_col] = rooms[row][col] + 1
                dq.append((next_row, next_col))
```

## 287. 寻找重复数 (`find-the-duplicate-number`)

- 题目链接：https://leetcode.cn/problems/find-the-duplicate-number/
- 难度：Medium
- 标签：Bit Manipulation, Array, Two Pointers, Binary Search
- 总提交次数：3
- 最近提交时间：2026/04/01 08:53:47 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 714087718 | 2026/04/01 08:53:47 CST | python | Accepted | 29 ms | 33 MB |
| 714087710 | 2026/04/01 08:53:40 CST | python | Runtime Error | N/A | N/A |
| 713825285 | 2026/03/31 14:29:34 CST | python | Accepted | 43 ms | 32.9 MB |

### 最近一次 AC 代码

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
```

## 290. 单词规律 (`word-pattern`)

- 题目链接：https://leetcode.cn/problems/word-pattern/
- 难度：Easy
- 标签：Hash Table, String
- 总提交次数：1
- 最近提交时间：2026/03/27 21:24:47 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 712688095 | 2026/03/27 21:24:47 CST | python | Accepted | 0 ms | 19.3 MB |

### 最近一次 AC 代码

```python
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        char_to_word = {}
        word_to_char = {}
        for ch, word in zip(pattern, words):
            if ch in char_to_word and char_to_word[ch] != word:
                return False
            if word in word_to_char and word_to_char[word] != ch:
                return False
            char_to_word[ch] = word
            word_to_char[word] = ch
        return True
```

## 292. Nim 游戏 (`nim-game`)

- 题目链接：https://leetcode.cn/problems/nim-game/
- 难度：Easy
- 标签：Brainteaser, Math, Game Theory
- 总提交次数：1
- 最近提交时间：2026/04/06 16:40:15 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715629556 | 2026/04/06 16:40:15 CST | python | Accepted | 0 ms | 19.2 MB |

### 最近一次 AC 代码

```python
class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0
```

## 295. 数据流的中位数 (`find-median-from-data-stream`)

- 题目链接：https://leetcode.cn/problems/find-median-from-data-stream/
- 难度：Hard
- 标签：Design, Two Pointers, Data Stream, Sorting, Heap (Priority Queue)
- 总提交次数：7
- 最近提交时间：2026/04/04 18:42:49 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715133063 | 2026/04/04 18:42:49 CST | python | Accepted | 297 ms | 41.3 MB |
| 678449721 | 2025/11/16 15:18:37 CST | python | Accepted | 225 ms | 40.6 MB |
| 678449167 | 2025/11/16 15:16:40 CST | python | Wrong Answer | N/A | N/A |
| 678277990 | 2025/11/15 16:09:50 CST | python | Accepted | 195 ms | 40.1 MB |
| 678277257 | 2025/11/15 16:06:39 CST | python | Runtime Error | N/A | N/A |
| 678277170 | 2025/11/15 16:06:18 CST | python | Runtime Error | N/A | N/A |
| 678277102 | 2025/11/15 16:05:59 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))
        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
```

## 297. 二叉树的序列化与反序列化 (`serialize-and-deserialize-binary-tree`)

- 题目链接：https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/
- 难度：Hard
- 标签：Tree, Depth-First Search, Breadth-First Search, Design, String, Binary Tree
- 总提交次数：4
- 最近提交时间：2026/04/07 10:52:56 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715823725 | 2026/04/07 10:52:56 CST | python | Accepted | 106 ms | 22.9 MB |
| 701694221 | 2026/03/02 11:15:19 CST | python | Accepted | 86 ms | 23.1 MB |
| 687241037 | 2025/12/26 10:58:06 CST | python | Accepted | 88 ms | 21.6 MB |
| 687240877 | 2025/12/26 10:57:32 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return 'null'
        left_str = self.serialize(root.left)
        right_str = self.serialize(root.right)
        return f'{root.val},{left_str},{right_str}'
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        strs = iter(data.split(','))
        def _build():
            val = next(strs)
            if val == 'null':
                return None
            node = TreeNode(val)
            node.left = _build()
            node.right = _build()
            return node
        return _build()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
```

## 298. 二叉树最长连续序列 (`binary-tree-longest-consecutive-sequence`)

- 题目链接：https://leetcode.cn/problems/binary-tree-longest-consecutive-sequence/
- 难度：Medium
- 标签：Tree, Depth-First Search, Binary Tree
- 总提交次数：2
- 最近提交时间：2026/03/01 10:53:05 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 701384316 | 2026/03/01 10:53:05 CST | python | Accepted | 15 ms | 22.9 MB |
| 701384165 | 2026/03/01 10:52:37 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.max_len = 0
        def dfs(node):
            if not node:
                return 0
            curr = 1
            left_len = dfs(node.left)
            right_len = dfs(node.right)

            if node.left and node.left.val == node.val + 1:
                curr = max(curr, left_len + 1)
            
            if node.right and node.right.val == node.val + 1:
                curr = max(curr, right_len + 1)
            
            self.max_len = max(self.max_len, curr)
            return curr
        dfs(root)
        return self.max_len
```

## 300. 最长递增子序列 (`longest-increasing-subsequence`)

- 题目链接：https://leetcode.cn/problems/longest-increasing-subsequence/
- 难度：Medium
- 标签：Array, Binary Search, Dynamic Programming
- 总提交次数：15
- 最近提交时间：2026/04/13 09:08:02 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 717595644 | 2026/04/13 09:08:02 CST | python | Accepted | 3 ms | 19.6 MB |
| 717595546 | 2026/04/13 09:07:19 CST | python | Runtime Error | N/A | N/A |
| 717595143 | 2026/04/13 09:04:15 CST | python | Accepted | 1227 ms | 19.1 MB |
| 702854930 | 2026/03/05 08:38:37 CST | python | Accepted | 3 ms | 19.5 MB |
| 697658709 | 2026/02/10 09:36:54 CST | python | Accepted | 1323 ms | 19.2 MB |
| 697428699 | 2026/02/09 10:01:28 CST | python | Accepted | 1227 ms | 19.1 MB |
| 695565257 | 2026/02/01 10:12:50 CST | python | Accepted | 1243 ms | 19.4 MB |
| 688071418 | 2025/12/30 13:47:04 CST | python | Accepted | 3 ms | 17.7 MB |
| 688071315 | 2025/12/30 13:46:31 CST | python | Runtime Error | N/A | N/A |
| 688071276 | 2025/12/30 13:46:17 CST | python | Runtime Error | N/A | N/A |
| 688042807 | 2025/12/30 11:10:20 CST | python | Accepted | 2064 ms | 17.2 MB |
| 685803653 | 2025/12/19 14:31:00 CST | python | Accepted | 2177 ms | 17.4 MB |
| 685537283 | 2025/12/18 10:18:54 CST | python | Accepted | 1978 ms | 17.1 MB |
| 685537070 | 2025/12/18 10:18:02 CST | python | Wrong Answer | N/A | N/A |
| 682069640 | 2025/12/02 10:20:03 CST | python | Accepted | 1855 ms | 18 MB |

### 最近一次 AC 代码

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for x in nums:
            pos = bisect.bisect_left(tails, x)
            if pos == len(tails):
                tails.append(x)
            else:
                tails[pos] = x
        return len(tails)
```

## 303. 区域和检索 - 数组不可变 (`range-sum-query-immutable`)

- 题目链接：https://leetcode.cn/problems/range-sum-query-immutable/
- 难度：Easy
- 标签：Design, Array, Prefix Sum
- 总提交次数：3
- 最近提交时间：2026/03/15 18:35:30 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 707480504 | 2026/03/15 18:35:30 CST | python | Accepted | 7 ms | 22.5 MB |
| 661616160 | 2025/09/11 10:56:46 CST | python | Accepted | 3 ms | 21.4 MB |
| 661615954 | 2025/09/11 10:56:23 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class NumArray:

    def __init__(self, nums: List[int]):
        self.pre_sum = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            self.pre_sum[i] = self.pre_sum[i - 1] + nums[i - 1]      

    def sumRange(self, left: int, right: int) -> int:
        return self.pre_sum[right + 1] - self.pre_sum[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
```

## 304. 二维区域和检索 - 矩阵不可变 (`range-sum-query-2d-immutable`)

- 题目链接：https://leetcode.cn/problems/range-sum-query-2d-immutable/
- 难度：Medium
- 标签：Design, Array, Matrix, Prefix Sum
- 总提交次数：13
- 最近提交时间：2026/03/16 09:01:49 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 707649988 | 2026/03/16 09:01:49 CST | python | Accepted | 121 ms | 32.8 MB |
| 707649765 | 2026/03/16 09:00:22 CST | python | Wrong Answer | N/A | N/A |
| 707649749 | 2026/03/16 09:00:15 CST | python | Runtime Error | N/A | N/A |
| 707649594 | 2026/03/16 08:59:11 CST | python | Runtime Error | N/A | N/A |
| 661930600 | 2025/09/12 09:42:52 CST | python | Accepted | 100 ms | 30.7 MB |
| 661915426 | 2025/09/12 08:16:57 CST | python | Accepted | 130 ms | 30.7 MB |
| 661913849 | 2025/09/12 07:36:58 CST | python | Wrong Answer | N/A | N/A |
| 661913833 | 2025/09/12 07:36:11 CST | python | Wrong Answer | N/A | N/A |
| 661913795 | 2025/09/12 07:34:48 CST | python | Wrong Answer | N/A | N/A |
| 661913792 | 2025/09/12 07:34:40 CST | python | Runtime Error | N/A | N/A |
| 661666526 | 2025/09/11 13:46:54 CST | python | Accepted | 113 ms | 30.7 MB |
| 661665131 | 2025/09/11 13:41:31 CST | python | Wrong Answer | N/A | N/A |
| 661664134 | 2025/09/11 13:37:21 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        if not m * n:
            return
        self.pre_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.pre_sum[i][j] = self.pre_sum[i - 1][j] + self.pre_sum[i][j - 1] + matrix[i - 1][j - 1] - self.pre_sum[i - 1][j - 1]        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.pre_sum[row2 + 1][col2 + 1] - self.pre_sum[row2 + 1][col1] - self.pre_sum[row1][col2 + 1] + self.pre_sum[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
```

## 305. 岛屿数量 II (`number-of-islands-ii`)

- 题目链接：https://leetcode.cn/problems/number-of-islands-ii/
- 难度：Hard
- 标签：Union Find, Array, Hash Table
- 总提交次数：2
- 最近提交时间：2026/03/09 15:26:05 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 704640168 | 2026/03/09 15:26:05 CST | python | Accepted | 84 ms | 23 MB |
| 704637865 | 2026/03/09 15:22:04 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.size = [1] * size
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return False
        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a
        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]
        return True


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        union_find = UnionFind(m * n)
        land = set()
        res = []
        island_count = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def get_id(row, col):
            return row * n + col
        for row, col in positions:
            if (row, col) in land:
                res.append(island_count)
                continue
            land.add((row, col))
            island_count += 1
            curr_id = get_id(row, col)
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if not (0 <= new_row < m and 0 <= new_col < n):
                    continue
                if (new_row, new_col) not in land:
                    continue
                neighbor_id = get_id(new_row, new_col)
                if union_find.union(curr_id, neighbor_id):
                    island_count -= 1
            res.append(island_count)
        return res
```

## 310. 最小高度树 (`minimum-height-trees`)

- 题目链接：https://leetcode.cn/problems/minimum-height-trees/
- 难度：Medium
- 标签：Depth-First Search, Breadth-First Search, Graph, Topological Sort
- 总提交次数：9
- 最近提交时间：2026/04/05 20:17:34 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715397627 | 2026/04/05 20:17:34 CST | python | Accepted | 46 ms | 27.2 MB |
| 715396859 | 2026/04/05 20:14:33 CST | python | Wrong Answer | N/A | N/A |
| 715396810 | 2026/04/05 20:14:22 CST | python | Runtime Error | N/A | N/A |
| 686561523 | 2025/12/23 10:58:57 CST | python | Accepted | 39 ms | 25.1 MB |
| 686561423 | 2025/12/23 10:58:39 CST | python | Runtime Error | N/A | N/A |
| 686358000 | 2025/12/22 14:27:08 CST | python | Accepted | 47 ms | 25.2 MB |
| 686356763 | 2025/12/22 14:22:07 CST | python | Accepted | 47 ms | 24.7 MB |
| 686355483 | 2025/12/22 14:17:00 CST | python | Wrong Answer | N/A | N/A |
| 686355416 | 2025/12/22 14:16:44 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        adj_list = collections.defaultdict(list)
        in_degree = [0] * n
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
            in_degree[u] += 1
            in_degree[v] += 1
        dq = collections.deque()
        for i in range(n):
            if in_degree[i] == 1:
                dq.append(i)
        remaining = n
        while remaining > 2:
            sz = len(dq)
            remaining -= sz
            for _ in range(sz):
                leaf = dq.popleft()
                for neighbor in adj_list[leaf]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 1:
                        dq.append(neighbor)
        return list(dq)
```

## 311. 稀疏矩阵的乘法 (`sparse-matrix-multiplication`)

- 题目链接：https://leetcode.cn/problems/sparse-matrix-multiplication/
- 难度：Medium
- 标签：Array, Hash Table, Matrix
- 总提交次数：1
- 最近提交时间：2026/03/10 16:17:17 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 705159406 | 2026/03/10 16:17:17 CST | python | Accepted | 0 ms | 19.1 MB |

### 最近一次 AC 代码

```python
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m = len(mat1)
        k = len(mat1[0])
        n = len(mat2[0])
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for t in range(k):
                if mat1[i][t] == 0:
                    continue
                for j in range(n):
                    if mat2[t][j] == 0:
                        continue
                    res[i][j] += mat1[i][t] * mat2[t][j]
        return res
```

## 312. 戳气球 (`burst-balloons`)

- 题目链接：https://leetcode.cn/problems/burst-balloons/
- 难度：Hard
- 标签：Array, Dynamic Programming
- 总提交次数：4
- 最近提交时间：2026/02/14 14:40:18 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 698579228 | 2026/02/14 14:40:18 CST | python | Accepted | 1855 ms | 21.8 MB |
| 691543121 | 2026/01/15 15:48:19 CST | python | Accepted | 1984 ms | 21.8 MB |
| 691215849 | 2026/01/14 10:39:45 CST | python | Accepted | 2087 ms | 22.1 MB |
| 690958340 | 2026/01/13 10:41:32 CST | python | Accepted | 1744 ms | 21.7 MB |

### 最近一次 AC 代码

```python
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        vals = [1] + nums + [1]
        n = len(vals)
        dp = [[0] * n for _ in range(n)]
        for gap in range(2, n):
            for i in range(0, n - gap):
                j = i + gap
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + vals[i] * vals[k] * vals[j])
        return dp[0][n - 1]
```

## 314. 二叉树的垂直遍历 (`binary-tree-vertical-order-traversal`)

- 题目链接：https://leetcode.cn/problems/binary-tree-vertical-order-traversal/
- 难度：Medium
- 标签：Tree, Depth-First Search, Breadth-First Search, Hash Table, Binary Tree, Sorting
- 总提交次数：3
- 最近提交时间：2026/03/03 08:39:03 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 702041182 | 2026/03/03 08:39:03 CST | python | Accepted | 0 ms | 19.2 MB |
| 702041063 | 2026/03/03 08:37:52 CST | python | Wrong Answer | N/A | N/A |
| 702041007 | 2026/03/03 08:37:20 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        column_tabel = collections.defaultdict(list)
        dq = collections.deque([(root, 0)])
        min_col, max_col = 0, 0
        while dq:
            node, col = dq.popleft()
            if node:
                column_tabel[col].append(node.val)
                min_col = min(min_col, col)
                max_col = max(max_col, col)
                if node.left:
                    dq.append((node.left, col - 1))
                if node.right:
                    dq.append((node.right, col + 1))
        return [column_tabel[x] for x in range(min_col, max_col + 1)]
```

## 317. 离建筑物最近的距离 (`shortest-distance-from-all-buildings`)

- 题目链接：https://leetcode.cn/problems/shortest-distance-from-all-buildings/
- 难度：Hard
- 标签：Breadth-First Search, Array, Matrix
- 总提交次数：6
- 最近提交时间：2026/03/10 11:30:28 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 705021957 | 2026/03/10 11:30:28 CST | python | Accepted | 2722 ms | 19.5 MB |
| 705020109 | 2026/03/10 11:27:24 CST | python | Memory Limit Exceeded | N/A | N/A |
| 705019963 | 2026/03/10 11:27:08 CST | python | Runtime Error | N/A | N/A |
| 705019851 | 2026/03/10 11:26:57 CST | python | Runtime Error | N/A | N/A |
| 705019664 | 2026/03/10 11:26:39 CST | python | Runtime Error | N/A | N/A |
| 705019517 | 2026/03/10 11:26:24 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dist_sum = [[0] * cols for _ in range(rows)]
        reach_count = [[0] * cols for _ in range(rows)]
        buildings_count = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def bfs(start_row, start_col):
            visited = [[False] * cols for _ in range(rows)]
            dq = collections.deque([(start_row, start_col, 0)])
            visited[start_row][start_col] = True
            while dq:
                row, col, dist = dq.popleft()
                for dr, dc in directions:
                    next_row, next_col = row + dr, col + dc
                    if not (0 <= next_row < rows and 0 <= next_col < cols):
                        continue
                    if visited[next_row][next_col]:
                        continue
                    if grid[next_row][next_col] != 0:
                        continue
                    visited[next_row][next_col] = True
                    dist_sum[next_row][next_col] += dist + 1
                    reach_count[next_row][next_col] += 1
                    dq.append((next_row, next_col, dist + 1))
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    buildings_count += 1
                    bfs(row, col)
        res = float('inf')
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0 and reach_count[row][col] == buildings_count:
                    res = min(res, dist_sum[row][col])
        
        return res if res != float('inf') else -1
```

## 319. 灯泡开关 (`bulb-switcher`)

- 题目链接：https://leetcode.cn/problems/bulb-switcher/
- 难度：Medium
- 标签：Brainteaser, Math
- 总提交次数：1
- 最近提交时间：2026/04/06 16:52:17 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715634604 | 2026/04/06 16:52:17 CST | python | Accepted | 0 ms | 19.1 MB |

### 最近一次 AC 代码

```python
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(n ** 0.5)
```

## 322. 零钱兑换 (`coin-change`)

- 题目链接：https://leetcode.cn/problems/coin-change/
- 难度：Medium
- 标签：Breadth-First Search, Array, Dynamic Programming
- 总提交次数：26
- 最近提交时间：2026/04/12 11:35:29 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 717358171 | 2026/04/12 11:35:29 CST | python | Accepted | 523 ms | 19.5 MB |
| 717357861 | 2026/04/12 11:34:24 CST | python | Wrong Answer | N/A | N/A |
| 693089291 | 2026/01/21 21:27:07 CST | python | Accepted | 715 ms | 20.8 MB |
| 690126195 | 2026/01/09 12:42:53 CST | python | Accepted | 695 ms | 20.8 MB |
| 690126090 | 2026/01/09 12:41:58 CST | python | Wrong Answer | N/A | N/A |
| 689705689 | 2026/01/07 16:14:49 CST | python | Accepted | 711 ms | 21.2 MB |
| 689704752 | 2026/01/07 16:12:12 CST | python | Wrong Answer | N/A | N/A |
| 689428293 | 2026/01/06 14:53:06 CST | python | Accepted | 691 ms | 21 MB |
| 689426380 | 2026/01/06 14:47:12 CST | python | Wrong Answer | N/A | N/A |
| 689425621 | 2026/01/06 14:44:45 CST | python | Accepted | 695 ms | 21.1 MB |
| 689425407 | 2026/01/06 14:44:03 CST | python | Wrong Answer | N/A | N/A |
| 689424976 | 2026/01/06 14:42:34 CST | python | Wrong Answer | N/A | N/A |
| 689388748 | 2026/01/06 11:35:08 CST | python | Accepted | 403 ms | 19.3 MB |
| 689388574 | 2026/01/06 11:34:34 CST | python | Wrong Answer | N/A | N/A |
| 689182947 | 2026/01/05 15:08:00 CST | python | Accepted | 895 ms | 17.5 MB |
| 689182236 | 2026/01/05 15:05:52 CST | python | Runtime Error | N/A | N/A |
| 689182118 | 2026/01/05 15:05:33 CST | python | Runtime Error | N/A | N/A |
| 688555794 | 2026/01/02 14:05:23 CST | python | Accepted | 825 ms | 17.3 MB |
| 688034761 | 2025/12/30 10:47:48 CST | python | Accepted | 803 ms | 17.6 MB |
| 688034687 | 2025/12/30 10:47:29 CST | python | Wrong Answer | N/A | N/A |
| 685806051 | 2025/12/19 14:40:15 CST | python | Accepted | 759 ms | 17.7 MB |
| 685805869 | 2025/12/19 14:39:34 CST | python | Wrong Answer | N/A | N/A |
| 685535973 | 2025/12/18 10:13:26 CST | python | Accepted | 735 ms | 17.3 MB |
| 685535748 | 2025/12/18 10:12:29 CST | python | Wrong Answer | N/A | N/A |
| 677068809 | 2025/11/10 14:10:57 CST | python | Accepted | 771 ms | 17.9 MB |
| 676814884 | 2025/11/09 10:48:35 CST | python | Accepted | 755 ms | 18.1 MB |

### 最近一次 AC 代码

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for target in range(1, amount + 1):
            for coin in coins:
                if target >= coin:
                    dp[target] = min(dp[target], dp[target - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
```

## 323. 无向图中连通分量的数目 (`number-of-connected-components-in-an-undirected-graph`)

- 题目链接：https://leetcode.cn/problems/number-of-connected-components-in-an-undirected-graph/
- 难度：Medium
- 标签：Depth-First Search, Breadth-First Search, Union Find, Graph
- 总提交次数：1
- 最近提交时间：2026/03/09 10:08:51 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 704501718 | 2026/03/09 10:08:51 CST | python | Accepted | 3 ms | 20.6 MB |

### 最近一次 AC 代码

```python
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [False] * n
        count = 0

        def dfs(node):
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)

        for node in range(n):
            if visited[node]:
                continue
            count += 1
            dfs(node)

        return count
```

## 329. 矩阵中的最长递增路径 (`longest-increasing-path-in-a-matrix`)

- 题目链接：https://leetcode.cn/problems/longest-increasing-path-in-a-matrix/
- 难度：Hard
- 标签：Depth-First Search, Breadth-First Search, Graph, Topological Sort, Memoization, Array, Dynamic Programming, Matrix
- 总提交次数：6
- 最近提交时间：2026/02/08 11:39:18 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 697238889 | 2026/02/08 11:39:18 CST | python | Accepted | 155 ms | 35.7 MB |
| 696049813 | 2026/02/03 10:28:51 CST | python | Accepted | 147 ms | 35.7 MB |
| 696049767 | 2026/02/03 10:28:40 CST | python | Runtime Error | N/A | N/A |
| 695804981 | 2026/02/02 11:26:37 CST | python | Accepted | 155 ms | 35.6 MB |
| 695788590 | 2026/02/02 10:27:37 CST | python | Accepted | 152 ms | 35.7 MB |
| 695788460 | 2026/02/02 10:27:04 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            max_len = 1
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    max_len = max(max_len, 1 + dfs(ni, nj))
            memo[(i, j)] = max_len
            return max_len
        
        return max(dfs(i, j) for i in range(m) for j in range(n))
```

## 333. 最大二叉搜索子树 (`largest-bst-subtree`)

- 题目链接：https://leetcode.cn/problems/largest-bst-subtree/
- 难度：Medium
- 标签：Tree, Depth-First Search, Binary Search Tree, Dynamic Programming, Binary Tree
- 总提交次数：2
- 最近提交时间：2026/02/28 12:33:05 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 701158219 | 2026/02/28 12:33:05 CST | python | Accepted | 3 ms | 20.7 MB |
| 701158124 | 2026/02/28 12:32:27 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        self.max_size = 0
        def dfs(node):
            if not node:
                return True, 0, float('inf'), float('-inf')
            l_bst, l_size, l_min, l_max = dfs(node.left)
            r_bst, r_size, r_min, r_max = dfs(node.right)
            if l_bst and r_bst and l_max < node.val < r_min:
                curr_size = l_size + r_size + 1
                curr_min = min(l_min, node.val)
                curr_max = max(r_max, node.val)
                self.max_size = max(self.max_size, curr_size)
                return True, curr_size, curr_min, curr_max
            else:
                return False, 0, 0, 0
        dfs(root)
        return self.max_size
```

## 337. 打家劫舍 III (`house-robber-iii`)

- 题目链接：https://leetcode.cn/problems/house-robber-iii/
- 难度：Medium
- 标签：Tree, Depth-First Search, Dynamic Programming, Binary Tree
- 总提交次数：5
- 最近提交时间：2026/02/12 14:07:27 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 698170935 | 2026/02/12 14:07:27 CST | python | Accepted | 0 ms | 20.6 MB |
| 698170727 | 2026/02/12 14:06:30 CST | python | Wrong Answer | N/A | N/A |
| 692558318 | 2026/01/19 22:12:09 CST | python | Accepted | 3 ms | 20.7 MB |
| 688692839 | 2026/01/03 11:25:11 CST | python | Accepted | 11 ms | 18.2 MB |
| 688692777 | 2026/01/03 11:24:50 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0, 0
            left_rob, left_skip = dfs(node.left)
            right_rob, right_skip = dfs(node.right)

            curr_rob = left_skip + right_skip + node.val
            curr_skip = max(left_rob, left_skip) + max(right_rob, right_skip)
            return curr_rob, curr_skip
        root_rob, root_skip = dfs(root)
        return max(root_rob, root_skip)
```

## 340. 至多包含 K 个不同字符的最长子串 (`longest-substring-with-at-most-k-distinct-characters`)

- 题目链接：https://leetcode.cn/problems/longest-substring-with-at-most-k-distinct-characters/
- 难度：Medium
- 标签：Hash Table, String, Sliding Window
- 总提交次数：2
- 最近提交时间：2024/08/30 20:03:51 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 559954569 | 2024/08/30 20:03:51 CST | python | Accepted | 67 ms | 16.4 MB |
| 559896943 | 2024/08/30 16:24:50 CST | python | Accepted | 71 ms | 16.4 MB |

### 最近一次 AC 代码

```python
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left = 0
        char_map = {}
        max_len = 0
        for right in range(len(s)):
            right_char = s[right]
            if right_char in char_map:
                char_map[right_char] += 1
            else:
                char_map[right_char] = 1
            if len(char_map) > k:
                left_char = s[left]
                char_map[left_char] -= 1
                if char_map[left_char] == 0:
                    del char_map[left_char]
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len
```

## 343. 整数拆分 (`integer-break`)

- 题目链接：https://leetcode.cn/problems/integer-break/
- 难度：Medium
- 标签：Math, Dynamic Programming
- 总提交次数：3
- 最近提交时间：2026/01/30 11:29:31 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 695152069 | 2026/01/30 11:29:31 CST | python | Accepted | 0 ms | 19 MB |
| 695151958 | 2026/01/30 11:29:10 CST | python | Wrong Answer | N/A | N/A |
| 694952613 | 2026/01/29 14:58:56 CST | python | Accepted | 0 ms | 18.9 MB |

### 最近一次 AC 代码

```python
class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2: return 1
        if n == 3: return 2
        if n == 4: return 4
        # 不能拆 1，尽量拆 3
        # n == 5 时 3 * 2 > 2 * 2 * 1
        # n == 6 时 3 * 3 > 2 * 2 * 2
        # n == 7 时 3 * 4 > 2 * 2 * 2 * 1
        if n % 3 == 0:
            return 3 ** (n // 3)
        elif n % 3 == 1:
            return 3 ** (n // 3 - 1) * 4
        else:
            return 3 ** (n // 3) * 2
```

## 344. 反转字符串 (`reverse-string`)

- 题目链接：https://leetcode.cn/problems/reverse-string/
- 难度：Easy
- 标签：Two Pointers, String
- 总提交次数：1
- 最近提交时间：2026/03/17 14:54:37 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 708280886 | 2026/03/17 14:54:37 CST | python | Accepted | 8 ms | 23.2 MB |

### 最近一次 AC 代码

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        left, right = 0, n - 1
        while left < right:
            tmp = s[left]
            s[left] = s[right]
            s[right] = tmp
            left += 1
            right -= 1
```

## 346. 数据流中的移动平均值 (`moving-average-from-data-stream`)

- 题目链接：https://leetcode.cn/problems/moving-average-from-data-stream/
- 难度：Easy
- 标签：Design, Queue, Array, Data Stream
- 总提交次数：2
- 最近提交时间：2026/03/11 15:10:30 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 705606023 | 2026/03/11 15:10:30 CST | python | Accepted | 7 ms | 22 MB |
| 705605271 | 2026/03/11 15:09:25 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.deque = collections.deque()
        self.window_sum = 0

    def next(self, val: int) -> float:
        self.deque.append(val)
        self.window_sum += val
        if len(self.deque) > self.size:
            removed = self.deque.popleft()
            self.window_sum -= removed
        return self.window_sum / len(self.deque)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
```

## 347. 前 K 个高频元素 (`top-k-frequent-elements`)

- 题目链接：https://leetcode.cn/problems/top-k-frequent-elements/
- 难度：Medium
- 标签：Array, Hash Table, Divide and Conquer, Bucket Sort, Counting, Quickselect, Sorting, Heap (Priority Queue)
- 总提交次数：5
- 最近提交时间：2026/04/04 18:21:13 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715128969 | 2026/04/04 18:21:13 CST | python | Accepted | 4 ms | 22.6 MB |
| 715128614 | 2026/04/04 18:19:27 CST | python | Wrong Answer | N/A | N/A |
| 676706680 | 2025/11/08 17:24:42 CST | python | Accepted | 4 ms | 21 MB |
| 676706407 | 2025/11/08 17:23:35 CST | python | Runtime Error | N/A | N/A |
| 676706168 | 2025/11/08 17:22:40 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = collections.Counter(nums)
        min_heap = []
        for num, freq in freq_map.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, (freq, num))
            else:
                if freq > min_heap[0][0]:
                    heapq.heapreplace(min_heap, (freq, num))
        return [num for _, num in min_heap]
```

## 348. 设计井字棋 (`design-tic-tac-toe`)

- 题目链接：https://leetcode.cn/problems/design-tic-tac-toe/
- 难度：Medium
- 标签：Design, Array, Hash Table, Matrix, Simulation
- 总提交次数：1
- 最近提交时间：2026/03/13 14:00:27 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 706523903 | 2026/03/13 14:00:27 CST | python | Accepted | 88 ms | 21.3 MB |

### 最近一次 AC 代码

```python
class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.anti_diag = 0        

    def move(self, row: int, col: int, player: int) -> int:
        add = 1 if player == 1 else -1
        self.rows[row] += add
        self.cols[col] += add
        if row == col:
            self.diag += add
        if row + col == self.n - 1:
            self.anti_diag += add
        if (
            abs(self.rows[row]) == self.n
            or abs(self.cols[col]) == self.n
            or abs(self.diag) == self.n
            or abs(self.anti_diag) == self.n
        ):
            return player
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
```

## 353. 贪吃蛇 (`design-snake-game`)

- 题目链接：https://leetcode.cn/problems/design-snake-game/
- 难度：Medium
- 标签：Design, Queue, Array, Hash Table, Simulation
- 总提交次数：2
- 最近提交时间：2026/03/13 15:10:40 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 706561898 | 2026/03/13 15:10:40 CST | python | Accepted | 193 ms | 21.1 MB |
| 706561740 | 2026/03/13 15:10:25 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = food
        self.food_index = 0
        self.score = 0

        self.snake = collections.deque([(0, 0)])
        self.occupied = set({(0, 0)})

        self.directions = {
            "U": (-1, 0),
            "D": (1, 0),
            "L": (0, -1),
            "R": (0, 1)
        }

    def move(self, direction: str) -> int:
        head_row, head_col = self.snake[0]
        delta_row, delta_col = self.directions[direction]
        new_row, new_col = head_row + delta_row, head_col + delta_col
        new_head = (new_row, new_col)
        if not(0 <= new_row < self.height and 0 <= new_col < self.width):
            return -1
        is_eating = (
            self.food_index < len(self.food)
            and new_row == self.food[self.food_index][0]
            and new_col == self.food[self.food_index][1]
        )
        if not is_eating:
            tail = self.snake[-1]
            self.occupied.remove(tail)
        if new_head in self.occupied:
            return -1
        self.snake.appendleft(new_head)
        self.occupied.add(new_head)

        if is_eating:
            self.food_index += 1
            self.score += 1
        else:
            self.snake.pop()
        
        return self.score
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
```

## 354. 俄罗斯套娃信封问题 (`russian-doll-envelopes`)

- 题目链接：https://leetcode.cn/problems/russian-doll-envelopes/
- 难度：Hard
- 标签：Array, Binary Search, Dynamic Programming, Sorting
- 总提交次数：7
- 最近提交时间：2026/04/13 10:17:39 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 717611353 | 2026/04/13 10:17:39 CST | python | Accepted | 156 ms | 53.8 MB |
| 702864508 | 2026/03/05 09:32:44 CST | python | Accepted | 131 ms | 53.7 MB |
| 695567314 | 2026/02/01 10:25:28 CST | python | Time Limit Exceeded | N/A | N/A |
| 688092535 | 2025/12/30 15:13:03 CST | python | Accepted | 160 ms | 50.6 MB |
| 688092487 | 2025/12/30 15:12:53 CST | python | Runtime Error | N/A | N/A |
| 688092392 | 2025/12/30 15:12:31 CST | python | Runtime Error | N/A | N/A |
| 688092168 | 2025/12/30 15:11:48 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        tails = []
        for _, h in envelopes:
            pos = bisect.bisect_left(tails, h)
            if pos == len(tails):
                tails.append(h)
            else:
                tails[pos] = h
        return len(tails)
```

## 355. 设计推特 (`design-twitter`)

- 题目链接：https://leetcode.cn/problems/design-twitter/
- 难度：Medium
- 标签：Design, Hash Table, Linked List, Heap (Priority Queue)
- 总提交次数：7
- 最近提交时间：2026/04/04 15:45:46 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715084235 | 2026/04/04 15:45:46 CST | python | Accepted | 5 ms | 28.3 MB |
| 715084023 | 2026/04/04 15:45:08 CST | python | Accepted | 0 ms | 28.1 MB |
| 715083981 | 2026/04/04 15:44:59 CST | python | Accepted | 19 ms | 28.2 MB |
| 715083711 | 2026/04/04 15:44:05 CST | python | Wrong Answer | N/A | N/A |
| 715082974 | 2026/04/04 15:41:46 CST | python | Wrong Answer | N/A | N/A |
| 715082737 | 2026/04/04 15:40:56 CST | python | Runtime Error | N/A | N/A |
| 715082670 | 2026/04/04 15:40:44 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.following = collections.defaultdict(set)
        self.tweets = collections.defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.tweets[userId].append((self.timestamp, tweetId))
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        max_heap = []
        users = set(self.following[userId])
        users.add(userId)
        for uid in users:
            tweets = self.tweets[uid]
            if tweets:
                idx = len(tweets) - 1
                timestamp, tweet_id = tweets[idx]
                heapq.heappush(max_heap, (-timestamp, tweet_id, uid, idx))
        
        while max_heap and len(res) < 10:
            _, tweet_id, uid, idx = heapq.heappop(max_heap)
            res.append(tweet_id)
            if idx > 0:
                pre_timestamp, pre_tweet = self.tweets[uid][idx - 1]
                heapq.heappush(max_heap, (-pre_timestamp, pre_tweet, uid, idx - 1))

        return res       


    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId == followerId:
            return
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.following[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
```

## 358. K 距离间隔重排字符串 (`rearrange-string-k-distance-apart`)

- 题目链接：https://leetcode.cn/problems/rearrange-string-k-distance-apart/
- 难度：Hard
- 标签：Greedy, Hash Table, String, Counting, Sorting, Heap (Priority Queue)
- 总提交次数：1
- 最近提交时间：2026/03/12 14:59:55 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 706082902 | 2026/03/12 14:59:55 CST | python | Accepted | 47 ms | 20.5 MB |

### 最近一次 AC 代码

```python
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1:
            return s
        counter = collections.Counter(s)
        max_heap = [(-count, char) for char, count in counter.items()]
        heapq.heapify(max_heap)

        cooldown = collections.deque()
        res = []
        for index in range(len(s)):
            while cooldown and cooldown[0][0] <= index:
                _, neg_count, char = cooldown.popleft()
                heapq.heappush(max_heap, (neg_count, char))
            
            if not max_heap:
                return ''
            
            neg_count, char = heapq.heappop(max_heap)
            res.append(char)
            remaining = -neg_count - 1
            
            if remaining > 0:
                cooldown.append((index + k, -remaining, char))
        
        return ''.join(res)
```

## 363. 矩形区域不超过 K 的最大数值和 (`max-sum-of-rectangle-no-larger-than-k`)

- 题目链接：https://leetcode.cn/problems/max-sum-of-rectangle-no-larger-than-k/
- 难度：Hard
- 标签：Array, Binary Search, Matrix, Ordered Set, Prefix Sum
- 总提交次数：5
- 最近提交时间：2026/03/05 14:33:01 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 702979353 | 2026/03/05 14:33:01 CST | python | Accepted | 935 ms | 19.7 MB |
| 697884248 | 2026/02/11 08:38:59 CST | python | Accepted | 855 ms | 19.9 MB |
| 697884230 | 2026/02/11 08:38:39 CST | python | Runtime Error | N/A | N/A |
| 697669016 | 2026/02/10 10:31:37 CST | python | Accepted | 879 ms | 20 MB |
| 697500975 | 2026/02/09 15:21:42 CST | python | Accepted | 872 ms | 20 MB |

### 最近一次 AC 代码

```python
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        max_sum = float('-inf')
        for top in range(m):
            col_sum = [0] * n
            for bottom in range(top, m):
                for j in range(n):
                    col_sum[j] += matrix[bottom][j]
                pre_sum = 0
                sorted_prefix = [0]
                for num in col_sum:
                    pre_sum += num
                    target = pre_sum - k
                    idx = bisect.bisect_left(sorted_prefix, target)
                    if idx < len(sorted_prefix):
                        max_sum = max(max_sum, pre_sum - sorted_prefix[idx])
                    bisect.insort(sorted_prefix, pre_sum)
        return max_sum
```

## 365. 水壶问题 (`water-and-jug-problem`)

- 题目链接：https://leetcode.cn/problems/water-and-jug-problem/
- 难度：Medium
- 标签：Depth-First Search, Breadth-First Search, Math
- 总提交次数：3
- 最近提交时间：2025/12/24 09:31:53 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 686774473 | 2025/12/24 09:31:53 CST | python | Accepted | 0 ms | 17.1 MB |
| 686774400 | 2025/12/24 09:31:25 CST | python | Wrong Answer | N/A | N/A |
| 686773346 | 2025/12/24 09:24:47 CST | python | Accepted | 0 ms | 17.3 MB |

### 最近一次 AC 代码

```python
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if target > x + y:
            return False
        return target % math.gcd(x, y) == 0
```

## 366. 寻找二叉树的叶子节点 (`find-leaves-of-binary-tree`)

- 题目链接：https://leetcode.cn/problems/find-leaves-of-binary-tree/
- 难度：Medium
- 标签：Tree, Depth-First Search, Binary Tree
- 总提交次数：2
- 最近提交时间：2026/02/28 10:18:02 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 701124742 | 2026/02/28 10:18:02 CST | python | Accepted | 0 ms | 19.1 MB |
| 701124576 | 2026/02/28 10:17:15 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def get_height(node):
            if not node:
                return -1
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            curr_height = 1 + max(left_height, right_height)
            if len(res) == curr_height:
                res.append([])
            res[curr_height].append(node.val)
            return curr_height
        get_height(root)
        return res
```

## 368. 最大整除子集 (`largest-divisible-subset`)

- 题目链接：https://leetcode.cn/problems/largest-divisible-subset/
- 难度：Medium
- 标签：Array, Math, Dynamic Programming, Sorting
- 总提交次数：14
- 最近提交时间：2026/02/14 10:55:59 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 698543692 | 2026/02/14 10:55:59 CST | python | Accepted | 171 ms | 19.3 MB |
| 698543585 | 2026/02/14 10:55:33 CST | python | Wrong Answer | N/A | N/A |
| 698543435 | 2026/02/14 10:54:51 CST | python | Runtime Error | N/A | N/A |
| 697938803 | 2026/02/11 13:39:56 CST | python | Accepted | 171 ms | 19.4 MB |
| 697938587 | 2026/02/11 13:38:40 CST | python | Memory Limit Exceeded | N/A | N/A |
| 696534589 | 2026/02/05 07:52:39 CST | python | Accepted | 171 ms | 19.2 MB |
| 696534578 | 2026/02/05 07:52:08 CST | python | Wrong Answer | N/A | N/A |
| 696534569 | 2026/02/05 07:51:17 CST | python | Wrong Answer | N/A | N/A |
| 696359563 | 2026/02/04 13:51:08 CST | python | Accepted | 175 ms | 19.4 MB |
| 696359218 | 2026/02/04 13:49:30 CST | python | Wrong Answer | N/A | N/A |
| 696031564 | 2026/02/03 09:05:55 CST | python | Accepted | 175 ms | 19.4 MB |
| 695831524 | 2026/02/02 13:51:54 CST | python | Accepted | 171 ms | 19.4 MB |
| 695563770 | 2026/02/01 10:01:56 CST | python | Accepted | 171 ms | 19.2 MB |
| 695563224 | 2026/02/01 09:57:25 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n
        parents = [-1] * n
        best_len = 1
        best_end = 0
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parents[i] = j
            if dp[i] > best_len:
                best_len = dp[i]
                best_end = i
        res = []
        idx = best_end
        while idx != -1:
            res.append(nums[idx])
            idx = parents[idx]
        return res
```

## 369. 给单链表加一 (`plus-one-linked-list`)

- 题目链接：https://leetcode.cn/problems/plus-one-linked-list/
- 难度：Medium
- 标签：Linked List, Math
- 总提交次数：1
- 最近提交时间：2026/03/11 16:45:11 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 705673417 | 2026/03/11 16:45:11 CST | python | Accepted | 0 ms | 19.2 MB |

### 最近一次 AC 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        last_not_nine = dummy
        curr = head
        while curr:
            if curr.val != 9:
                last_not_nine = curr
            curr = curr.next
        last_not_nine.val += 1
        curr = last_not_nine.next
        while curr:
            curr.val = 0
            curr = curr.next
        if dummy.val == 1:
            return dummy
        return dummy.next
```

## 370. 区间加法 (`range-addition`)

- 题目链接：https://leetcode.cn/problems/range-addition/
- 难度：Medium
- 标签：Array, Prefix Sum
- 总提交次数：5
- 最近提交时间：2026/03/23 08:48:40 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 710762131 | 2026/03/23 08:48:40 CST | python | Accepted | 10 ms | 24.2 MB |
| 710762016 | 2026/03/23 08:47:52 CST | python | Runtime Error | N/A | N/A |
| 707793857 | 2026/03/16 14:55:22 CST | python | Accepted | 15 ms | 24.5 MB |
| 707793030 | 2026/03/16 14:54:05 CST | python | Wrong Answer | N/A | N/A |
| 707792860 | 2026/03/16 14:53:50 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Difference:
    def __init__(self, nums):
        assert len(nums) > 0
        self.diff = [0] * len(nums)
        self.diff[0] = nums[0]
        for i in range(len(nums)):
            self.diff[i] = nums[i] - nums[i - 1]
    
    def increasement(self, i, j, val):
        self.diff[i] += val
        if j + 1 < len(self.diff):
            self.diff[j + 1] -= val
    
    def result(self):
        res = [0] * len(self.diff)
        res[0] = self.diff[0]
        for i in range(1, len(self.diff)):
            res[i] = self.diff[i] + res[i - 1]
        return res

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        nums = [0] * length
        diff = Difference(nums)
        for i, j, val in updates:
            diff.increasement(i, j, val)
        return diff.result()
```

## 372. 超级次方 (`super-pow`)

- 题目链接：https://leetcode.cn/problems/super-pow/
- 难度：Medium
- 标签：Math, Divide and Conquer
- 总提交次数：1
- 最近提交时间：2026/04/06 21:22:53 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715720184 | 2026/04/06 21:22:53 CST | python | Accepted | 15 ms | 19.1 MB |

### 最近一次 AC 代码

```python
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        mod = 1337
        a %= mod
        res = 1
        for digit in b:
            res = ((res ** 10) % mod) * ((a ** digit) % mod) % mod
        return res
```

## 373. 查找和最小的 K 对数字 (`find-k-pairs-with-smallest-sums`)

- 题目链接：https://leetcode.cn/problems/find-k-pairs-with-smallest-sums/
- 难度：Medium
- 标签：Array, Heap (Priority Queue)
- 总提交次数：5
- 最近提交时间：2026/03/31 13:52:26 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 713812304 | 2026/03/31 13:52:26 CST | python | Accepted | 179 ms | 50.2 MB |
| 713812206 | 2026/03/31 13:52:05 CST | python | Runtime Error | N/A | N/A |
| 713811821 | 2026/03/31 13:50:46 CST | python | Runtime Error | N/A | N/A |
| 683834261 | 2025/12/10 10:49:15 CST | python | Accepted | 79 ms | 34 MB |
| 647890938 | 2025/07/29 08:10:26 CST | python | Accepted | 87 ms | 33.7 MB |

### 最近一次 AC 代码

```python
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        min_heap = []
        m, n = len(nums1), len(nums2)
        for r in range(m):
            heapq.heappush(min_heap, (nums1[r] + nums2[0], r, 0))

        while min_heap:
            _, r, c = heapq.heappop(min_heap)
            res.append([nums1[r], nums2[c]])
            if len(res) == k:
                return res
            if c + 1 < n:
                heapq.heappush(min_heap, (nums1[r] + nums2[c + 1], r, c + 1))
        
        return []
```

## 375. 猜数字大小 II (`guess-number-higher-or-lower-ii`)

- 题目链接：https://leetcode.cn/problems/guess-number-higher-or-lower-ii/
- 难度：Medium
- 标签：Math, Dynamic Programming, Game Theory
- 总提交次数：4
- 最近提交时间：2026/02/14 15:19:10 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 698587040 | 2026/02/14 15:19:10 CST | python | Accepted | 955 ms | 19.9 MB |
| 698586645 | 2026/02/14 15:17:19 CST | python | Wrong Answer | N/A | N/A |
| 692273898 | 2026/01/18 20:45:01 CST | python | Accepted | 1273 ms | 19.9 MB |
| 692074046 | 2026/01/17 22:18:20 CST | python | Accepted | 991 ms | 19.9 MB |

### 最近一次 AC 代码

```python
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 2) for _ in range(n + 2)]
        for gap in range(1, n):
            for i in range(1, n - gap + 1):
                j = i + gap
                dp[i][j] = float('inf')
                for k in range(i, j + 1):
                    worst = k + max(dp[i][k - 1], dp[k + 1][j])
                    dp[i][j] = min(dp[i][j], worst)
        return dp[1][n]
```

## 377. 组合总和 Ⅳ (`combination-sum-iv`)

- 题目链接：https://leetcode.cn/problems/combination-sum-iv/
- 难度：Medium
- 标签：Array, Dynamic Programming
- 总提交次数：6
- 最近提交时间：2026/02/13 14:47:44 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 698392235 | 2026/02/13 14:47:44 CST | python | Accepted | 54 ms | 19.2 MB |
| 693092804 | 2026/01/21 21:38:44 CST | python | Accepted | 66 ms | 19.2 MB |
| 690109806 | 2026/01/09 11:17:08 CST | python | Accepted | 67 ms | 19.1 MB |
| 690109005 | 2026/01/09 11:14:24 CST | python | Wrong Answer | N/A | N/A |
| 689443001 | 2026/01/06 15:36:12 CST | python | Accepted | 77 ms | 19 MB |
| 689193569 | 2026/01/05 15:39:15 CST | python | Accepted | 55 ms | 19.2 MB |

### 最近一次 AC 代码

```python
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for t in range(1, target + 1):
            for num in nums:
                if t >= num:
                    dp[t] += dp[t - num]
        return dp[target]
```

## 378. 有序矩阵中第 K 小的元素 (`kth-smallest-element-in-a-sorted-matrix`)

- 题目链接：https://leetcode.cn/problems/kth-smallest-element-in-a-sorted-matrix/
- 难度：Medium
- 标签：Array, Binary Search, Matrix, Sorting, Heap (Priority Queue)
- 总提交次数：10
- 最近提交时间：2026/04/04 14:49:38 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715067934 | 2026/04/04 14:49:38 CST | python | Accepted | 3 ms | 22.6 MB |
| 715067235 | 2026/04/04 14:46:58 CST | python | Wrong Answer | N/A | N/A |
| 703296811 | 2026/03/06 09:36:40 CST | python | Accepted | 3 ms | 22.7 MB |
| 703296745 | 2026/03/06 09:36:27 CST | python | Runtime Error | N/A | N/A |
| 702510930 | 2026/03/04 12:25:45 CST | python | Accepted | 0 ms | 22.8 MB |
| 702492925 | 2026/03/04 11:31:16 CST | python | Accepted | 23 ms | 22.5 MB |
| 683830456 | 2025/12/10 10:36:17 CST | python | Accepted | 31 ms | 20.9 MB |
| 683830390 | 2025/12/10 10:36:03 CST | python | Runtime Error | N/A | N/A |
| 683830301 | 2025/12/10 10:35:47 CST | python | Runtime Error | N/A | N/A |
| 647586206 | 2025/07/28 09:24:58 CST | python | Accepted | 35 ms | 20.8 MB |

### 最近一次 AC 代码

```python
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def _less_than_count(x):
            cnt = 0
            rows, cols = n - 1, 0
            while rows >= 0 and cols < n:
                if matrix[rows][cols] <= x:
                    cnt += (rows + 1)
                    cols += 1
                else:
                    rows -= 1
            return cnt

        left, right = matrix[0][0], matrix[n - 1][n - 1]
        while left < right:
            mid = left + (right - left) // 2
            if _less_than_count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left
```

## 380. O(1) 时间插入、删除和获取随机元素 (`insert-delete-getrandom-o1`)

- 题目链接：https://leetcode.cn/problems/insert-delete-getrandom-o1/
- 难度：Medium
- 标签：Design, Array, Hash Table, Math, Randomized
- 总提交次数：1
- 最近提交时间：2025/11/18 10:07:26 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 678866242 | 2025/11/18 10:07:26 CST | python | Accepted | 153 ms | 56.6 MB |

### 最近一次 AC 代码

```python
class RandomizedSet:

    def __init__(self):
        self.vals = []
        self.vals_to_index = {}
        

    def insert(self, val: int) -> bool:
        if val in self.vals_to_index:
            return False
        self.vals.append(val)
        self.vals_to_index[val] = len(self.vals) - 1
        return True


    def remove(self, val: int) -> bool:
        if not self.vals or val not in self.vals_to_index:
            return False
        idx_to_remove = self.vals_to_index[val]
        last_val = self.vals[-1]
        if val != last_val:
            self.vals[idx_to_remove] = last_val
            self.vals_to_index[last_val] = idx_to_remove
        self.vals.pop()
        del self.vals_to_index[val]
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.vals)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
```

## 381. O(1) 时间插入、删除和获取随机元素 - 允许重复 (`insert-delete-getrandom-o1-duplicates-allowed`)

- 题目链接：https://leetcode.cn/problems/insert-delete-getrandom-o1-duplicates-allowed/
- 难度：Hard
- 标签：Design, Array, Hash Table, Math, Randomized
- 总提交次数：8
- 最近提交时间：2025/11/18 11:11:34 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 678886454 | 2025/11/18 11:11:34 CST | python | Accepted | 124 ms | 72.6 MB |
| 678885415 | 2025/11/18 11:08:19 CST | python | Wrong Answer | N/A | N/A |
| 678884452 | 2025/11/18 11:05:25 CST | python | Accepted | 125 ms | 72.5 MB |
| 678883802 | 2025/11/18 11:03:42 CST | python | Accepted | 158 ms | 72.6 MB |
| 678883313 | 2025/11/18 11:02:06 CST | python | Runtime Error | N/A | N/A |
| 678882301 | 2025/11/18 10:59:03 CST | python | Accepted | 149 ms | 72.6 MB |
| 678880816 | 2025/11/18 10:54:39 CST | python | Wrong Answer | N/A | N/A |
| 678879700 | 2025/11/18 10:51:22 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class RandomizedCollection:

    def __init__(self):
        self.vals: list[int] = []
        self.vals_to_idx: dict[int, set] = collections.defaultdict(set)
        

    def insert(self, val: int) -> bool:
        exist = val not in self.vals_to_idx
        self.vals.append(val)
        self.vals_to_idx[val].add(len(self.vals) - 1)
        return exist        


    def remove(self, val: int) -> bool:
        if val not in self.vals_to_idx:
            return False
        idx_to_remove = self.vals_to_idx[val].pop()
        last_idx = len(self.vals) - 1
        last_val = self.vals[last_idx]
        if idx_to_remove != last_idx:
            self.vals[idx_to_remove] = last_val
            self.vals_to_idx[last_val].add(idx_to_remove)
            self.vals_to_idx[last_val].discard(last_idx)
        self.vals.pop()
        if not self.vals_to_idx[val]:
            del self.vals_to_idx[val]
        return True


    def getRandom(self) -> int:
        return random.choice(self.vals)

        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
```

## 382. 链表随机节点 (`linked-list-random-node`)

- 题目链接：https://leetcode.cn/problems/linked-list-random-node/
- 难度：Medium
- 标签：Reservoir Sampling, Linked List, Math, Randomized
- 总提交次数：3
- 最近提交时间：2026/03/24 11:16:44 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 711274247 | 2026/03/24 11:16:44 CST | python | Accepted | 43 ms | 23.1 MB |
| 709984405 | 2026/03/21 09:56:07 CST | python | Accepted | 39 ms | 23.3 MB |
| 709841757 | 2026/03/20 19:34:39 CST | python | Accepted | 39 ms | 23.1 MB |

### 最近一次 AC 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        res = 0
        count = 0
        node = self.head
        while node:
            count += 1
            if random.randint(1, count) == 1:
                res = node.val
            node = node.next
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
```

## 384. 打乱数组 (`shuffle-an-array`)

- 题目链接：https://leetcode.cn/problems/shuffle-an-array/
- 难度：Medium
- 标签：Design, Array, Math, Randomized
- 总提交次数：5
- 最近提交时间：2026/03/24 11:22:50 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 711277501 | 2026/03/24 11:22:50 CST | python | Accepted | 40 ms | 22.5 MB |
| 709982803 | 2026/03/21 09:49:33 CST | python | Accepted | 20 ms | 22.4 MB |
| 709982678 | 2026/03/21 09:49:06 CST | python | Runtime Error | N/A | N/A |
| 709838210 | 2026/03/20 19:24:44 CST | python | Accepted | 30 ms | 22.4 MB |
| 709838080 | 2026/03/20 19:24:19 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums
        

    def shuffle(self) -> List[int]:
        shuffled = self.nums[:]
        n = len(shuffled)
        for i in range(n):
            j = random.randint(i, n - 1)
            shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
        return shuffled
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
```

## 387. 字符串中的第一个唯一字符 (`first-unique-character-in-a-string`)

- 题目链接：https://leetcode.cn/problems/first-unique-character-in-a-string/
- 难度：Easy
- 标签：Queue, Hash Table, String, Counting
- 总提交次数：1
- 最近提交时间：2026/03/29 19:12:51 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 713240476 | 2026/03/29 19:12:51 CST | python | Accepted | 49 ms | 19.8 MB |

### 最近一次 AC 代码

```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        for i, ch in enumerate(s):
            if count[ch] == 1:
                return i
        return -1
```

## 392. 判断子序列 (`is-subsequence`)

- 题目链接：https://leetcode.cn/problems/is-subsequence/
- 难度：Easy
- 标签：Two Pointers, String, Dynamic Programming
- 总提交次数：3
- 最近提交时间：2026/03/24 10:07:27 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 711238644 | 2026/03/24 10:07:27 CST | python | Accepted | 4 ms | 19.1 MB |
| 709223661 | 2026/03/19 14:00:58 CST | python | Accepted | 0 ms | 19.2 MB |
| 685341508 | 2025/12/17 12:47:42 CST | python | Accepted | 0 ms | 17.4 MB |

### 最近一次 AC 代码

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        i = 0
        n = len(s)
        for ch in t:
            if i < n and s[i] == ch:
                i += 1
                if i == n:
                    return True
        return False
```

## 394. 字符串解码 (`decode-string`)

- 题目链接：https://leetcode.cn/problems/decode-string/
- 难度：Medium
- 标签：Stack, Recursion, String
- 总提交次数：5
- 最近提交时间：2026/03/28 09:36:21 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 712758294 | 2026/03/28 09:36:21 CST | python | Accepted | 0 ms | 19.1 MB |
| 712432835 | 2026/03/27 08:09:18 CST | python | Accepted | 0 ms | 19.1 MB |
| 712094916 | 2026/03/26 10:39:51 CST | python | Accepted | 0 ms | 19.2 MB |
| 712094664 | 2026/03/26 10:39:21 CST | python | Wrong Answer | N/A | N/A |
| 712094589 | 2026/03/26 10:39:12 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def decodeString(self, s: str) -> str:
        curr = ''
        num = 0
        stack = []
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '[':
                stack.append((curr, num))
                curr = ''
                num = 0
            elif ch == ']':
                prev_str, repeat = stack.pop()
                curr = prev_str + repeat * curr
            else:
                curr += ch
        return curr
```

## 395. 至少有 K 个重复字符的最长子串 (`longest-substring-with-at-least-k-repeating-characters`)

- 题目链接：https://leetcode.cn/problems/longest-substring-with-at-least-k-repeating-characters/
- 难度：Medium
- 标签：Hash Table, String, Divide and Conquer, Sliding Window
- 总提交次数：10
- 最近提交时间：2026/03/23 17:17:37 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 710986688 | 2026/03/23 17:17:37 CST | python | Accepted | 47 ms | 19.1 MB |
| 708780453 | 2026/03/18 15:13:34 CST | python | Accepted | 43 ms | 19.1 MB |
| 708780026 | 2026/03/18 15:12:53 CST | python | Wrong Answer | N/A | N/A |
| 661395750 | 2025/09/10 16:41:27 CST | python | Accepted | 55 ms | 17.8 MB |
| 661391803 | 2025/09/10 16:33:58 CST | python | Wrong Answer | N/A | N/A |
| 661391600 | 2025/09/10 16:33:35 CST | python | Runtime Error | N/A | N/A |
| 655480630 | 2025/08/22 14:29:23 CST | python | Accepted | 47 ms | 17.4 MB |
| 655479443 | 2025/08/22 14:25:52 CST | python | Wrong Answer | N/A | N/A |
| 655479093 | 2025/08/22 14:24:51 CST | python | Time Limit Exceeded | N/A | N/A |
| 655479008 | 2025/08/22 14:24:38 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        max_len = 0
        for h in range(1, 27):
            left = 0
            valid_count = uniq_count = 0
            window = collections.defaultdict(int)
            for right, r_char in enumerate(s):
                if window[r_char] == 0:
                    uniq_count += 1
                window[r_char] += 1
                if window[r_char] == k:
                    valid_count += 1
                while uniq_count > h:
                    l_char = s[left]
                    if window[l_char] == k:
                        valid_count -= 1
                    window[l_char] -= 1
                    if window[l_char] == 0:
                        uniq_count -= 1
                    left += 1
                if uniq_count == h and valid_count == h:
                    max_len = max(max_len, right - left + 1)
        return max_len
```

## 398. 随机数索引 (`random-pick-index`)

- 题目链接：https://leetcode.cn/problems/random-pick-index/
- 难度：Medium
- 标签：Reservoir Sampling, Hash Table, Math, Randomized
- 总提交次数：6
- 最近提交时间：2026/03/24 11:26:32 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 711279362 | 2026/03/24 11:26:32 CST | python | Accepted | 35 ms | 29.2 MB |
| 709985256 | 2026/03/21 09:59:36 CST | python | Accepted | 47 ms | 29.4 MB |
| 709847841 | 2026/03/20 19:50:23 CST | python | Accepted | 41 ms | 29.3 MB |
| 709846522 | 2026/03/20 19:47:06 CST | python | Time Limit Exceeded | N/A | N/A |
| 709846025 | 2026/03/20 19:45:56 CST | python | Time Limit Exceeded | N/A | N/A |
| 709845953 | 2026/03/20 19:45:44 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:

    def __init__(self, nums: List[int]):
        self.indices = collections.defaultdict(list)
        for i, num in enumerate(nums):
            self.indices[num].append(i)
        

    def pick(self, target: int) -> int:
        return random.choice(self.indices[target])
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
```

## 399. 除法求值 (`evaluate-division`)

- 题目链接：https://leetcode.cn/problems/evaluate-division/
- 难度：Medium
- 标签：Depth-First Search, Breadth-First Search, Union Find, Graph, Array, String, Shortest Path
- 总提交次数：6
- 最近提交时间：2025/12/24 11:53:45 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 686810043 | 2025/12/24 11:53:45 CST | python | Accepted | 0 ms | 17.1 MB |
| 686809821 | 2025/12/24 11:52:33 CST | python | Runtime Error | N/A | N/A |
| 686109127 | 2025/12/21 09:16:28 CST | python | Accepted | 0 ms | 17.1 MB |
| 686108989 | 2025/12/21 09:13:46 CST | python | Runtime Error | N/A | N/A |
| 685935148 | 2025/12/20 09:41:33 CST | python | Accepted | 0 ms | 17.2 MB |
| 685934954 | 2025/12/20 09:39:30 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(dict)
        for (a, b), c in zip(equations, values):
            graph[a][b] = c
            graph[b][a] = 1.0 / c
        
        def bfs(start, end):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            dq = collections.deque([(start, 1.0)])
            visited = {start}
            while dq:
                curr, val = dq.popleft()
                if curr == end:
                    return val
                for next_node, weight in graph[curr].items():
                    if next_node not in visited:
                        visited.add(next_node)
                        dq.append((next_node, val * weight))
            return -1.0

        res = []
        for x, y in queries:
            res.append(bfs(x, y))
        return res
```

## 402. 移掉 K 位数字 (`remove-k-digits`)

- 题目链接：https://leetcode.cn/problems/remove-k-digits/
- 难度：Medium
- 标签：Stack, Greedy, String, Monotonic Stack
- 总提交次数：4
- 最近提交时间：2026/03/27 08:49:26 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 712436315 | 2026/03/27 08:49:26 CST | python | Accepted | 18 ms | 20.5 MB |
| 712436206 | 2026/03/27 08:48:29 CST | python | Wrong Answer | N/A | N/A |
| 712143829 | 2026/03/26 13:09:14 CST | python | Accepted | 20 ms | 20.4 MB |
| 712143613 | 2026/03/26 13:08:21 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for ch in num:
            while k > 0 and stack and stack[-1] > ch:
                stack.pop()
                k -= 1
            stack.append(ch)
        if k > 0:
            stack = stack[:-k]
        res = ''.join(stack).lstrip('0')
        return res if res else '0'
```

## 410. 分割数组的最大值 (`split-array-largest-sum`)

- 题目链接：https://leetcode.cn/problems/split-array-largest-sum/
- 难度：Hard
- 标签：Greedy, Array, Binary Search, Dynamic Programming, Prefix Sum
- 总提交次数：2
- 最近提交时间：2026/03/24 09:57:23 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 711234640 | 2026/03/24 09:57:23 CST | python | Accepted | 0 ms | 19.2 MB |
| 709170603 | 2026/03/19 11:30:22 CST | python | Accepted | 0 ms | 19.1 MB |

### 最近一次 AC 代码

```python
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def can_split(max_sum):
            groups = 1
            curr = 0
            for num in nums:
                if curr + num > max_sum:
                    groups += 1
                    curr = num
                else:
                    curr += num
            return groups <= k
        left, right = max(nums), sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            if can_split(mid):
                right = mid
            else:
                left = mid + 1
        return left
```

## 416. 分割等和子集 (`partition-equal-subset-sum`)

- 题目链接：https://leetcode.cn/problems/partition-equal-subset-sum/
- 难度：Medium
- 标签：Array, Dynamic Programming
- 总提交次数：9
- 最近提交时间：2026/04/13 11:04:38 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 717628188 | 2026/04/13 11:04:38 CST | python | Accepted | 1283 ms | 34.3 MB |
| 717627738 | 2026/04/13 11:03:32 CST | python | Runtime Error | N/A | N/A |
| 692929024 | 2026/01/21 11:49:37 CST | python | Accepted | 1286 ms | 34.4 MB |
| 689125662 | 2026/01/05 10:56:07 CST | python | Accepted | 1247 ms | 32.2 MB |
| 689125533 | 2026/01/05 10:55:42 CST | python | Wrong Answer | N/A | N/A |
| 688917782 | 2026/01/04 14:10:16 CST | python | Accepted | 1159 ms | 32.2 MB |
| 688530396 | 2026/01/02 11:30:11 CST | python | Accepted | 1111 ms | 32.2 MB |
| 688451649 | 2026/01/01 18:00:59 CST | python | Accepted | 1127 ms | 32.1 MB |
| 688450338 | 2026/01/01 17:50:45 CST | python | Accepted | 1179 ms | 32.1 MB |

### 最近一次 AC 代码

```python
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        n = len(nums)
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            num = nums[i - 1]
            for j in range(target + 1):
                dp[i][j] = dp[i - 1][j] or (j >= num and dp[i - 1][j - num])
        return dp[n][target]
```

## 417. 太平洋大西洋水流问题 (`pacific-atlantic-water-flow`)

- 题目链接：https://leetcode.cn/problems/pacific-atlantic-water-flow/
- 难度：Medium
- 标签：Depth-First Search, Breadth-First Search, Array, Matrix
- 总提交次数：9
- 最近提交时间：2025/12/24 15:37:48 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 686856860 | 2025/12/24 15:37:48 CST | python | Accepted | 41 ms | 18.4 MB |
| 686856730 | 2025/12/24 15:37:20 CST | python | Runtime Error | N/A | N/A |
| 686651058 | 2025/12/23 17:00:11 CST | python | Accepted | 39 ms | 18.3 MB |
| 686650683 | 2025/12/23 16:59:03 CST | python | Wrong Answer | N/A | N/A |
| 686650221 | 2025/12/23 16:57:38 CST | python | Wrong Answer | N/A | N/A |
| 686649838 | 2025/12/23 16:56:23 CST | python | Wrong Answer | N/A | N/A |
| 686649608 | 2025/12/23 16:55:39 CST | python | Wrong Answer | N/A | N/A |
| 686649435 | 2025/12/23 16:55:09 CST | python | Runtime Error | N/A | N/A |
| 686649283 | 2025/12/23 16:54:43 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
        m, n = len(heights), len(heights[0])
        def bfs(dq, reachable):
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            while dq:
                r, c = dq.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue
                    if (nr, nc) in reachable or heights[nr][nc] < heights[r][c]:
                        continue
                    reachable.add((nr, nc))
                    dq.append((nr, nc))
        pacific_q = collections.deque()
        pacific_reachable = set()
        for r in range(m):
            pacific_q.append((r, 0))
            pacific_reachable.add((r, 0))
        for c in range(1, n):
            pacific_q.append((0, c))
            pacific_reachable.add((0, c))
        bfs(pacific_q, pacific_reachable)

        atlantic_q = collections.deque()
        atlantic_reachable = set()
        for r in range(m):
            atlantic_q.append((r, n-1))
            atlantic_reachable.add((r, n-1))
        for c in range(n-1):
            atlantic_q.append((m-1, c))
            atlantic_reachable.add((m-1, c))
        bfs(atlantic_q, atlantic_reachable)

        res = []
        for r in range(m):
            for c in range(n):
                if (r, c) in pacific_reachable and (r, c) in atlantic_reachable:
                    res.append([r, c])
        return res
```

## 422. 有效的单词方块 (`valid-word-square`)

- 题目链接：https://leetcode.cn/problems/valid-word-square/
- 难度：Easy
- 标签：Array, Matrix
- 总提交次数：2
- 最近提交时间：2026/03/10 15:24:15 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 705122749 | 2026/03/10 15:24:15 CST | python | Accepted | 19 ms | 19.6 MB |
| 705122136 | 2026/03/10 15:23:20 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for i in range(len(words)):
            for j in range(len(words[i])):
                if j >= len(words):
                    return False
                if i >= len(words[j]):
                    return False
                if words[i][j] != words[j][i]:
                    return False
        return True
```

## 424. 替换后的最长重复字符 (`longest-repeating-character-replacement`)

- 题目链接：https://leetcode.cn/problems/longest-repeating-character-replacement/
- 难度：Medium
- 标签：Hash Table, String, Sliding Window
- 总提交次数：10
- 最近提交时间：2026/03/23 14:47:01 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 710891497 | 2026/03/23 14:47:01 CST | python | Accepted | 75 ms | 19.5 MB |
| 708737373 | 2026/03/18 13:53:24 CST | python | Accepted | 71 ms | 19.5 MB |
| 700643589 | 2026/02/26 13:13:34 CST | python | Accepted | 72 ms | 19.4 MB |
| 679380595 | 2025/11/20 09:30:02 CST | python | Accepted | 103 ms | 17.6 MB |
| 663040591 | 2025/09/15 21:47:55 CST | python | Accepted | 149 ms | 17.9 MB |
| 661275344 | 2025/09/10 11:07:18 CST | python | Accepted | 123 ms | 17.9 MB |
| 661264580 | 2025/09/10 10:43:23 CST | python | Accepted | 83 ms | 17.7 MB |
| 661264449 | 2025/09/10 10:43:06 CST | python | Wrong Answer | N/A | N/A |
| 661261800 | 2025/09/10 10:37:06 CST | python | Wrong Answer | N/A | N/A |
| 653150313 | 2025/08/15 07:45:22 CST | python | Accepted | 131 ms | 17.9 MB |

### 最近一次 AC 代码

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_freq = 0
        freq_map = collections.defaultdict(int)
        left = 0
        res = 0
        for right, r_char in enumerate(s):
            freq_map[r_char] += 1
            max_freq = max(max_freq, freq_map[r_char])
            if right - left + 1 - max_freq > k:
                freq_map[s[left]] -= 1
                left += 1
            res = right - left + 1
        return res
```

## 429. N 叉树的层序遍历 (`n-ary-tree-level-order-traversal`)

- 题目链接：https://leetcode.cn/problems/n-ary-tree-level-order-traversal/
- 难度：Medium
- 标签：Tree, Breadth-First Search
- 总提交次数：4
- 最近提交时间：2026/04/02 13:09:05 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 714504844 | 2026/04/02 13:09:05 CST | python | Accepted | 63 ms | 20.8 MB |
| 700857777 | 2026/02/27 09:45:53 CST | python | Accepted | 70 ms | 20.7 MB |
| 684720800 | 2025/12/14 17:41:04 CST | python | Accepted | 59 ms | 19 MB |
| 684720764 | 2025/12/14 17:40:54 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        dq = collections.deque([root])
        res = []
        while dq:
            sz = len(dq)
            level_vals = []
            for _ in range(sz):
                node = dq.popleft()
                level_vals.append(node.val)
                for child in node.children:
                    dq.append(child)
            res.append(level_vals)
        return res
```

## 433. 最小基因变化 (`minimum-genetic-mutation`)

- 题目链接：https://leetcode.cn/problems/minimum-genetic-mutation/
- 难度：Medium
- 标签：Breadth-First Search, Hash Table, String
- 总提交次数：6
- 最近提交时间：2025/12/23 11:30:40 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 686570343 | 2025/12/23 11:30:40 CST | python | Accepted | 0 ms | 17 MB |
| 686570298 | 2025/12/23 11:30:31 CST | python | Runtime Error | N/A | N/A |
| 686570276 | 2025/12/23 11:30:26 CST | python | Runtime Error | N/A | N/A |
| 686373151 | 2025/12/22 15:19:45 CST | python | Accepted | 0 ms | 17.1 MB |
| 686373081 | 2025/12/22 15:19:30 CST | python | Runtime Error | N/A | N/A |
| 686373034 | 2025/12/22 15:19:19 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)
        dq = collections.deque([(startGene, 0)])
        visited = {startGene}
        ch_list = ['A', 'C', 'G', 'T']
        while dq:
            curr_gene, steps = dq.popleft()
            if curr_gene == endGene:
                return steps
            for i in range(8):
                for ch in ch_list:
                    if curr_gene[i] == ch:
                        continue
                    new_gene = curr_gene[:i] + ch + curr_gene[i+1:]
                    if new_gene in bank_set and new_gene not in visited:
                        visited.add(new_gene)
                        dq.append((new_gene, steps + 1))
        return -1
```

## 435. 无重叠区间 (`non-overlapping-intervals`)

- 题目链接：https://leetcode.cn/problems/non-overlapping-intervals/
- 难度：Medium
- 标签：Greedy, Array, Dynamic Programming, Sorting
- 总提交次数：3
- 最近提交时间：2026/02/05 08:44:39 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 696536684 | 2026/02/05 08:44:39 CST | python | Accepted | 87 ms | 47.9 MB |
| 696325977 | 2026/02/04 11:13:14 CST | python | Accepted | 119 ms | 48.3 MB |
| 696120517 | 2026/02/03 15:09:44 CST | python | Accepted | 75 ms | 48.2 MB |

### 最近一次 AC 代码

```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        del_cnt = 0
        pre_end = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= pre_end:
                pre_end = end
            else:
                del_cnt += 1
        return del_cnt
```

## 438. 找到字符串中所有字母异位词 (`find-all-anagrams-in-a-string`)

- 题目链接：https://leetcode.cn/problems/find-all-anagrams-in-a-string/
- 难度：Medium
- 标签：Hash Table, String, Sliding Window
- 总提交次数：23
- 最近提交时间：2026/03/18 10:08:48 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 708643936 | 2026/03/18 10:08:48 CST | python | Accepted | 39 ms | 19.9 MB |
| 700399482 | 2026/02/25 14:13:42 CST | python | Accepted | 38 ms | 19.9 MB |
| 681294113 | 2025/11/28 14:38:26 CST | python | Accepted | 39 ms | 18.2 MB |
| 681294050 | 2025/11/28 14:38:14 CST | python | Runtime Error | N/A | N/A |
| 681292454 | 2025/11/28 14:32:11 CST | python | Accepted | 35 ms | 18.1 MB |
| 681292140 | 2025/11/28 14:30:57 CST | python | Wrong Answer | N/A | N/A |
| 681291779 | 2025/11/28 14:29:34 CST | python | Runtime Error | N/A | N/A |
| 681291741 | 2025/11/28 14:29:26 CST | python | Runtime Error | N/A | N/A |
| 663185043 | 2025/09/16 12:36:00 CST | python | Accepted | 39 ms | 18.2 MB |
| 663184987 | 2025/09/16 12:35:34 CST | python | Wrong Answer | N/A | N/A |
| 663109495 | 2025/09/16 08:42:08 CST | python | Accepted | 39 ms | 18.2 MB |
| 663109471 | 2025/09/16 08:41:55 CST | python | Runtime Error | N/A | N/A |
| 663109284 | 2025/09/16 08:40:21 CST | python | Accepted | 39 ms | 18.2 MB |
| 663109265 | 2025/09/16 08:40:13 CST | python | Wrong Answer | N/A | N/A |
| 660896937 | 2025/09/09 10:18:34 CST | python | Accepted | 45 ms | 18.4 MB |
| 660896828 | 2025/09/09 10:18:20 CST | python | Runtime Error | N/A | N/A |
| 660895002 | 2025/09/09 10:13:54 CST | python | Wrong Answer | N/A | N/A |
| 658784183 | 2025/09/02 16:05:53 CST | python | Accepted | 55 ms | 18.4 MB |
| 658782294 | 2025/09/02 16:01:58 CST | python | Wrong Answer | N/A | N/A |
| 658778152 | 2025/09/02 15:53:40 CST | python | Wrong Answer | N/A | N/A |
| 658777014 | 2025/09/02 15:51:22 CST | python | Wrong Answer | N/A | N/A |
| 658774437 | 2025/09/02 15:46:09 CST | python | Wrong Answer | N/A | N/A |
| 650942994 | 2025/08/08 08:04:25 CST | python | Accepted | 39 ms | 18.1 MB |

### 最近一次 AC 代码

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = collections.Counter(p)
        window = collections.defaultdict(int)
        valid = 0
        left = 0
        res = []
        for right, r_char in enumerate(s):
            if r_char in need:
                window[r_char] += 1
                if window[r_char] == need[r_char]:
                    valid += 1
            if right >= len(p) - 1:
                if valid == len(need):
                    res.append(left)
                l_char = s[left]
                if l_char in need:
                    if window[l_char] == need[l_char]:
                        valid -= 1
                    window[l_char] -= 1
                left += 1
        return res
```

## 439. 三元表达式解析器 (`ternary-expression-parser`)

- 题目链接：https://leetcode.cn/problems/ternary-expression-parser/
- 难度：Medium
- 标签：Stack, Recursion, String
- 总提交次数：2
- 最近提交时间：2026/03/11 10:41:09 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 705480151 | 2026/03/11 10:41:09 CST | python | Accepted | 11 ms | 19.3 MB |
| 705476894 | 2026/03/11 10:35:41 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = []
        n = len(expression)
        for i in range(n - 1, -1, -1):
            char = expression[i]
            if i + 1 < n and expression[i + 1] == '?':
                true_expr = stack.pop()
                stack.pop()
                false_expr = stack.pop()
                if char == 'T':
                    stack.append(true_expr)
                else:
                    stack.append(false_expr)
            elif char != '?':
                stack.append(char)
        return stack[-1]
```

## 445. 两数相加 II (`add-two-numbers-ii`)

- 题目链接：https://leetcode.cn/problems/add-two-numbers-ii/
- 难度：Medium
- 标签：Stack, Linked List, Math
- 总提交次数：5
- 最近提交时间：2026/04/01 08:50:42 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 714087360 | 2026/04/01 08:50:42 CST | python | Accepted | 7 ms | 19.1 MB |
| 713819798 | 2026/03/31 14:15:48 CST | python | Accepted | 7 ms | 19 MB |
| 683847253 | 2025/12/10 11:31:13 CST | python | Accepted | 8 ms | 17.6 MB |
| 683847079 | 2025/12/10 11:30:35 CST | python | Memory Limit Exceeded | N/A | N/A |
| 648208272 | 2025/07/30 08:09:25 CST | python | Accepted | 3 ms | 17.8 MB |

### 最近一次 AC 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stk_1 = []
        stk_2 = []
        curr_1, curr_2 = l1, l2
        while curr_1:
            stk_1.append(curr_1.val)
            curr_1 = curr_1.next
        while curr_2:
            stk_2.append(curr_2.val)
            curr_2 = curr_2.next
        
        head = None
        carry = 0
        while stk_1 or stk_2 or carry:
            l1_val = stk_1.pop() if stk_1 else 0
            l2_val = stk_2.pop() if stk_2 else 0
            total = l1_val + l2_val + carry
            new_val = total % 10
            carry = total // 10
            new_node = ListNode(new_val)
            new_node.next = head
            head = new_node
        return head
```

## 450. 删除二叉搜索树中的节点 (`delete-node-in-a-bst`)

- 题目链接：https://leetcode.cn/problems/delete-node-in-a-bst/
- 难度：Medium
- 标签：Tree, Binary Search Tree, Binary Tree
- 总提交次数：8
- 最近提交时间：2026/04/04 10:58:54 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715025402 | 2026/04/04 10:58:54 CST | python | Accepted | 3 ms | 21.9 MB |
| 715024457 | 2026/04/04 10:54:35 CST | python | Runtime Error | N/A | N/A |
| 715024263 | 2026/04/04 10:53:44 CST | python | Runtime Error | N/A | N/A |
| 715024110 | 2026/04/04 10:53:01 CST | python | Runtime Error | N/A | N/A |
| 714848113 | 2026/04/03 15:03:50 CST | python | Accepted | 0 ms | 22 MB |
| 714847605 | 2026/04/03 15:02:30 CST | python | Wrong Answer | N/A | N/A |
| 714847239 | 2026/04/03 15:01:29 CST | python | Runtime Error | N/A | N/A |
| 714847156 | 2026/04/03 15:01:16 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        successor = self._get_min(root.right)
        root.val = successor.val
        root.right = self.deleteNode(root.right, successor.val)
        return root
    
    def _get_min(self, node):
        while node.left:
            node = node.left
        return node
```

## 452. 用最少数量的箭引爆气球 (`minimum-number-of-arrows-to-burst-balloons`)

- 题目链接：https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/
- 难度：Medium
- 标签：Greedy, Array, Sorting
- 总提交次数：4
- 最近提交时间：2026/02/05 08:58:38 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 696537699 | 2026/02/05 08:58:38 CST | python | Accepted | 87 ms | 52.6 MB |
| 696321039 | 2026/02/04 10:57:06 CST | python | Accepted | 76 ms | 52.7 MB |
| 696129343 | 2026/02/03 15:32:21 CST | python | Accepted | 90 ms | 52.5 MB |
| 696129183 | 2026/02/03 15:31:57 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        n = len(points)
        arrows_cnt = 1
        arrows_pos = points[0][1]
        for start, end in points[1:]:
            if start > arrows_pos:
                arrows_cnt += 1
                arrows_pos = end
        return arrows_cnt
```

## 460. LFU 缓存 (`lfu-cache`)

- 题目链接：https://leetcode.cn/problems/lfu-cache/
- 难度：Hard
- 标签：Design, Hash Table, Linked List, Doubly-Linked List
- 总提交次数：7
- 最近提交时间：2025/11/15 11:20:49 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 678223370 | 2025/11/15 11:20:49 CST | python | Accepted | 151 ms | 78.6 MB |
| 678223223 | 2025/11/15 11:20:02 CST | python | Wrong Answer | N/A | N/A |
| 678222542 | 2025/11/15 11:16:32 CST | python | Wrong Answer | N/A | N/A |
| 678222358 | 2025/11/15 11:15:32 CST | python | Runtime Error | N/A | N/A |
| 678221954 | 2025/11/15 11:13:15 CST | python | Runtime Error | N/A | N/A |
| 678221867 | 2025/11/15 11:12:49 CST | python | Runtime Error | N/A | N/A |
| 678076125 | 2025/11/14 14:32:42 CST | python | Accepted | 140 ms | 78.4 MB |

### 最近一次 AC 代码

```python
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key2value = {}
        self.key2freq = {}
        self.freq2keys = defaultdict(OrderedDict)
        self.min_freq = 0
        

    def get(self, key: int) -> int:
        if key not in self.key2value:
            return -1
        self.increase_freq(key)
        return self.key2value[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.key2value:
            self.key2value[key] = value
            self.increase_freq(key)
            return
        if len(self.key2value) >= self.capacity:
            self.evict_one()
        self.key2value[key] = value
        self.key2freq[key] = 1
        self.freq2keys[1][key] = None
        self.min_freq = 1


    def evict_one(self):
        key_to_del, _ = self.freq2keys[self.min_freq].popitem(last=False)
        del self.key2value[key_to_del]
        del self.key2freq[key_to_del]
    

    def increase_freq(self, key):
        freq = self.key2freq.get(key)
        del self.freq2keys[freq][key]
        if not self.freq2keys[freq]:
            if freq == self.min_freq:
                self.min_freq = freq+1
        new_freq = freq+1
        self.key2freq[key] = new_freq
        self.freq2keys[new_freq][key] = None        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
```

## 474. 一和零 (`ones-and-zeroes`)

- 题目链接：https://leetcode.cn/problems/ones-and-zeroes/
- 难度：Medium
- 标签：Array, String, Dynamic Programming
- 总提交次数：20
- 最近提交时间：2026/02/13 15:20:19 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 698399776 | 2026/02/13 15:20:19 CST | python | Accepted | 1951 ms | 73.5 MB |
| 698399403 | 2026/02/13 15:18:52 CST | python | Wrong Answer | N/A | N/A |
| 692963622 | 2026/01/21 14:40:23 CST | python | Accepted | 2431 ms | 73.4 MB |
| 692963485 | 2026/01/21 14:39:55 CST | python | Wrong Answer | N/A | N/A |
| 692963036 | 2026/01/21 14:38:22 CST | python | Wrong Answer | N/A | N/A |
| 692962388 | 2026/01/21 14:36:21 CST | python | Wrong Answer | N/A | N/A |
| 690137706 | 2026/01/09 14:00:24 CST | python | Accepted | 2079 ms | 73.4 MB |
| 690137308 | 2026/01/09 13:58:24 CST | python | Wrong Answer | N/A | N/A |
| 689169043 | 2026/01/05 14:23:53 CST | python | Accepted | 2700 ms | 70.5 MB |
| 689166957 | 2026/01/05 14:16:25 CST | python | Wrong Answer | N/A | N/A |
| 689166516 | 2026/01/05 14:14:48 CST | python | Wrong Answer | N/A | N/A |
| 689166360 | 2026/01/05 14:14:04 CST | python | Runtime Error | N/A | N/A |
| 688956719 | 2026/01/04 16:12:16 CST | python | Accepted | 2379 ms | 71.5 MB |
| 688956262 | 2026/01/04 16:10:46 CST | python | Wrong Answer | N/A | N/A |
| 688955957 | 2026/01/04 16:09:45 CST | python | Wrong Answer | N/A | N/A |
| 688955397 | 2026/01/04 16:08:13 CST | python | Runtime Error | N/A | N/A |
| 688955122 | 2026/01/04 16:07:28 CST | python | Runtime Error | N/A | N/A |
| 688856919 | 2026/01/04 09:46:02 CST | python | Accepted | 1587 ms | 17.5 MB |
| 688851147 | 2026/01/04 08:56:25 CST | python | Accepted | 2427 ms | 71.7 MB |
| 688851086 | 2026/01/04 08:55:49 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        k = len(strs)
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(k + 1)]
        for t in range(1, k + 1):
            curr = strs[t - 1]
            zero_cnt = curr.count('0')
            one_cnt = curr.count('1')
            for i in range(m + 1):
                for j in range(n + 1):
                    dp[t][i][j] = dp[t - 1][i][j]
                    if i >= zero_cnt and j >= one_cnt:
                        dp[t][i][j] = max(dp[t][i][j], dp[t - 1][i - zero_cnt][j - one_cnt] + 1)
        return dp[k][m][n]
```

## 484. 寻找排列 (`find-permutation`)

- 题目链接：https://leetcode.cn/problems/find-permutation/
- 难度：Medium
- 标签：Stack, Greedy, Array, String
- 总提交次数：3
- 最近提交时间：2026/03/11 12:29:45 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 705533802 | 2026/03/11 12:29:45 CST | python | Accepted | 9 ms | 20 MB |
| 705533723 | 2026/03/11 12:29:29 CST | python | Runtime Error | N/A | N/A |
| 705533699 | 2026/03/11 12:29:24 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def findPermutation(self, s: str) -> List[int]:
        n = len(s)
        res = list(range(1, n + 2))
        i = 0
        while i < n:
            if s[i] == 'I':
                i += 1
                continue
            start = i
            while i < n and s[i] == 'D':
                i += 1
            end = i
            while start < end:
                res[start], res[end] = res[end], res[start]
                start += 1
                end -= 1
        return res
```

## 487. 最大连续1的个数 II (`max-consecutive-ones-ii`)

- 题目链接：https://leetcode.cn/problems/max-consecutive-ones-ii/
- 难度：Medium
- 标签：Array, Dynamic Programming, Sliding Window
- 总提交次数：4
- 最近提交时间：2026/02/26 11:43:22 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 700627014 | 2026/02/26 11:43:22 CST | python | Accepted | 15 ms | 19.5 MB |
| 698166938 | 2026/02/12 13:46:48 CST | python | Accepted | 23 ms | 19.6 MB |
| 560058675 | 2024/08/31 11:06:49 CST | python | Accepted | 69 ms | 16.6 MB |
| 559905033 | 2024/08/30 16:43:46 CST | python | Accepted | 89 ms | 16.5 MB |

### 最近一次 AC 代码

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = 0
        prev_zero = -1
        left = 0
        for right, num in enumerate(nums):
            if num == 0:
                left = prev_zero + 1
                prev_zero = right
            max_len = max(max_len, right - left + 1)
        return max_len
```

## 490. 迷宫 (`the-maze`)

- 题目链接：https://leetcode.cn/problems/the-maze/
- 难度：Medium
- 标签：Depth-First Search, Breadth-First Search, Array, Matrix
- 总提交次数：2
- 最近提交时间：2026/03/09 16:41:49 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 704696099 | 2026/03/09 16:41:49 CST | python | Accepted | 23 ms | 19.7 MB |
| 704695818 | 2026/03/09 16:41:24 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        rows, cols = len(maze), len(maze[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def rolls(row, col, dr, dc):
            while (
                0 <= row + dr < rows
                and 0 <= col + dc < cols
                and maze[row + dr][col + dc] == 0
            ):
                row = row + dr
                col = col + dc
            return row, col
        
        dq = collections.deque([tuple(start)])
        visited =  {tuple(start)}
        while dq:
            row, col = dq.popleft()
            if [row, col] == destination:
                return True
            for dr, dc in directions:
                next_row, next_col = rolls(row, col, dr, dc)
                if (next_row, next_col) not in visited:
                    visited.add((next_row, next_col))
                    dq.append((next_row, next_col))
        return False
```

## 491. 非递减子序列 (`non-decreasing-subsequences`)

- 题目链接：https://leetcode.cn/problems/non-decreasing-subsequences/
- 难度：Medium
- 标签：Bit Manipulation, Array, Hash Table, Backtracking
- 总提交次数：9
- 最近提交时间：2026/04/09 10:12:24 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 716476947 | 2026/04/09 10:12:24 CST | python | Accepted | 19 ms | 24.6 MB |
| 716476794 | 2026/04/09 10:11:56 CST | python | Wrong Answer | N/A | N/A |
| 716476762 | 2026/04/09 10:11:49 CST | python | Runtime Error | N/A | N/A |
| 699298018 | 2026/02/19 14:47:46 CST | python | Accepted | 19 ms | 24.7 MB |
| 699297982 | 2026/02/19 14:47:31 CST | python | Runtime Error | N/A | N/A |
| 687824502 | 2025/12/29 11:26:41 CST | python | Accepted | 15 ms | 22.6 MB |
| 687650727 | 2025/12/28 15:03:36 CST | python | Accepted | 19 ms | 22.7 MB |
| 687650500 | 2025/12/28 15:02:35 CST | python | Wrong Answer | N/A | N/A |
| 687649044 | 2025/12/28 14:55:19 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        layer_used = set()
        n = len(nums)
        def backtrack(start_idx):
            if len(path) >= 2:
                res.append(list(path))
            layer_used = set()
            for i in range(start_idx, n):
                if nums[i] in layer_used:
                    continue
                if path and path[-1] > nums[i]:
                    continue
                layer_used.add(nums[i])
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()
        backtrack(0)
        return res
```

## 494. 目标和 (`target-sum`)

- 题目链接：https://leetcode.cn/problems/target-sum/
- 难度：Medium
- 标签：Array, Dynamic Programming, Backtracking
- 总提交次数：14
- 最近提交时间：2026/02/13 15:09:42 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 698397153 | 2026/02/13 15:09:42 CST | python | Accepted | 39 ms | 19.3 MB |
| 692956867 | 2026/01/21 14:17:03 CST | python | Accepted | 35 ms | 19.1 MB |
| 692956381 | 2026/01/21 14:15:13 CST | python | Runtime Error | N/A | N/A |
| 690100695 | 2026/01/09 10:44:44 CST | python | Accepted | 39 ms | 19.1 MB |
| 690100624 | 2026/01/09 10:44:29 CST | python | Runtime Error | N/A | N/A |
| 689750237 | 2026/01/07 19:02:45 CST | python | Accepted | 51 ms | 19.1 MB |
| 689750010 | 2026/01/07 19:01:29 CST | python | Wrong Answer | N/A | N/A |
| 689162895 | 2026/01/05 13:59:31 CST | python | Accepted | 39 ms | 17.3 MB |
| 688950081 | 2026/01/04 15:52:50 CST | python | Accepted | 43 ms | 17.1 MB |
| 688949719 | 2026/01/04 15:51:47 CST | python | Runtime Error | N/A | N/A |
| 688949676 | 2026/01/04 15:51:40 CST | python | Runtime Error | N/A | N/A |
| 688678035 | 2026/01/03 08:59:16 CST | python | Accepted | 39 ms | 17.1 MB |
| 688677989 | 2026/01/03 08:58:07 CST | python | Runtime Error | N/A | N/A |
| 688677956 | 2026/01/03 08:57:14 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total:
            return 0
        if (total + target) % 2 == 1:
            return 0
        need = (target + total) // 2
        n = len(nums)
        dp = [[0] * (need + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            num = nums[i - 1]
            for j in range(need + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= num:
                    dp[i][j] += dp[i - 1][j - num]
        return dp[n][need]
```

## 496. 下一个更大元素 I (`next-greater-element-i`)

- 题目链接：https://leetcode.cn/problems/next-greater-element-i/
- 难度：Easy
- 标签：Stack, Array, Hash Table, Monotonic Stack
- 总提交次数：1
- 最近提交时间：2026/03/25 09:55:10 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 711671387 | 2026/03/25 09:55:10 CST | python | Accepted | 4 ms | 19.1 MB |

### 最近一次 AC 代码

```python
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        for num in nums2:
            while stack and stack[-1] < num:
                smaller = stack.pop()
                next_greater[smaller] = num
            stack.append(num)
        return [next_greater.get(num, -1) for num in nums1]
```

## 499. 迷宫 III (`the-maze-iii`)

- 题目链接：https://leetcode.cn/problems/the-maze-iii/
- 难度：Hard
- 标签：Depth-First Search, Breadth-First Search, Graph, Array, String, Matrix, Shortest Path, Heap (Priority Queue)
- 总提交次数：1
- 最近提交时间：2026/03/09 19:22:51 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 704773240 | 2026/03/09 19:22:51 CST | python | Accepted | 3 ms | 19.3 MB |

### 最近一次 AC 代码

```python
class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        rows, cols = len(maze), len(maze[0])
        directions = [
            (1, 0, 'd'),
            (0, -1, 'l'),
            (0, 1, 'r'),
            (-1, 0, 'u')
        ]
        hole_pos = tuple(hole)
        def roll(row, col, dr, dc):
            distance = 0
            while (
                0 <= row + dr < rows
                and 0 <= col + dc < cols
                and maze[row + dr][col + dc] == 0
            ):
                row += dr
                col += dc
                distance += 1
                if (row, col) == hole_pos:
                    break
            return  row, col, distance
    
        start_pos = tuple(ball)
        heap = [(0, '', start_pos[0], start_pos[1])]
        best = {start_pos: (0, '')}
        while heap:
            curr_dist, curr_path, row, col = heapq.heappop(heap)
            if (row, col) == hole_pos:
                return curr_path
            if best[(row, col)] > (curr_dist, curr_path):
                continue
            for dr, dc, move_char in directions:
                next_row, next_col, move_dist = roll(row, col, dr, dc)
                if move_dist == 0:
                    continue
                new_dist = curr_dist + move_dist
                new_path = curr_path + move_char
                next_pos = (next_row, next_col)
                new_state = (new_dist, new_path)
                if next_pos not in best or new_state < best[next_pos]:
                    best[next_pos] = new_state
                    heapq.heappush(heap, (new_dist, new_path, next_row, next_col))
        return 'impossible'
```

## 503. 下一个更大元素 II (`next-greater-element-ii`)

- 题目链接：https://leetcode.cn/problems/next-greater-element-ii/
- 难度：Medium
- 标签：Stack, Array, Monotonic Stack
- 总提交次数：5
- 最近提交时间：2026/03/26 08:43:52 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 712063762 | 2026/03/26 08:43:52 CST | python | Accepted | 19 ms | 20.9 MB |
| 712063742 | 2026/03/26 08:43:40 CST | python | Runtime Error | N/A | N/A |
| 712063693 | 2026/03/26 08:43:07 CST | python | Runtime Error | N/A | N/A |
| 712063575 | 2026/03/26 08:41:52 CST | python | Runtime Error | N/A | N/A |
| 711677548 | 2026/03/25 10:11:24 CST | python | Accepted | 19 ms | 21 MB |

### 最近一次 AC 代码

```python
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []
        for i in range(2 * n):
            idx = i % n
            while stack and nums[stack[-1]] < nums[idx]:
                res[stack[-1]] = nums[idx]
                stack.pop()
            if i < n:
                stack.append(idx)
        return res
```

## 505. 迷宫 II (`the-maze-ii`)

- 题目链接：https://leetcode.cn/problems/the-maze-ii/
- 难度：Medium
- 标签：Depth-First Search, Breadth-First Search, Graph, Array, Matrix, Shortest Path, Heap (Priority Queue)
- 总提交次数：3
- 最近提交时间：2026/03/09 18:35:25 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 704755191 | 2026/03/09 18:35:25 CST | python | Accepted | 35 ms | 19.7 MB |
| 704754008 | 2026/03/09 18:31:51 CST | python | Wrong Answer | N/A | N/A |
| 704753291 | 2026/03/09 18:29:45 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def rolls(row, col, dr, dc):
            distance = 0
            while (
                0 <= row + dr < rows
                and 0 <= col + dc < cols
                and maze[row + dr][col + dc] == 0
            ):
                row += dr
                col += dc
                distance += 1
            return row, col, distance
        start_pos = tuple(start)
        destination_pos = tuple(destination)
        heap = [(0, start_pos[0], start_pos[1])]
        dist = {start_pos: 0}
        while heap:
            curr_dist, row, col = heapq.heappop(heap)
            if (row, col) == destination_pos:
                return curr_dist
            if curr_dist > dist[(row, col)]:
                continue
            for dr, dc in directions:
                new_row, new_col, move_dist = rolls(row, col, dr, dc)
                new_dist = curr_dist + move_dist
                if new_dist < dist.get((new_row, new_col), float('inf')):
                    dist[(new_row, new_col)] = new_dist
                    heapq.heappush(heap, (new_dist, new_row, new_col))
        return -1
```

## 509. 斐波那契数 (`fibonacci-number`)

- 题目链接：https://leetcode.cn/problems/fibonacci-number/
- 难度：Easy
- 标签：Recursion, Memoization, Math, Dynamic Programming
- 总提交次数：3
- 最近提交时间：2026/04/12 11:20:37 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 717353706 | 2026/04/12 11:20:37 CST | python | Accepted | 0 ms | 19.1 MB |
| 717353469 | 2026/04/12 11:19:49 CST | python | Accepted | 0 ms | 19 MB |
| 688024382 | 2025/12/30 10:06:39 CST | python | Accepted | 0 ms | 16.9 MB |

### 最近一次 AC 代码

```python
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        prev_2, prev_1 = 0, 1
        for _ in range(2, n + 1):
            prev_2, prev_1 = prev_1, prev_1 + prev_2
        return prev_1
```

## 515. 在每个树行中找最大值 (`find-largest-value-in-each-tree-row`)

- 题目链接：https://leetcode.cn/problems/find-largest-value-in-each-tree-row/
- 难度：Medium
- 标签：Tree, Depth-First Search, Breadth-First Search, Binary Tree
- 总提交次数：1
- 最近提交时间：2025/12/20 18:24:27 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 686027519 | 2025/12/20 18:24:27 CST | python | Accepted | 7 ms | 18.4 MB |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        dq = collections.deque([root])
        while dq:
            sz = len(dq)
            level_max = float('-inf')
            for _ in range(sz):
                node = dq.popleft()
                level_max = max(level_max, node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            res.append(level_max)
        return res
```

## 516. 最长回文子序列 (`longest-palindromic-subsequence`)

- 题目链接：https://leetcode.cn/problems/longest-palindromic-subsequence/
- 难度：Medium
- 标签：String, Dynamic Programming
- 总提交次数：12
- 最近提交时间：2026/02/14 14:14:23 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 698574619 | 2026/02/14 14:14:23 CST | python | Accepted | 551 ms | 35.2 MB |
| 694940963 | 2026/01/29 14:22:38 CST | python | Accepted | 559 ms | 34.9 MB |
| 693292552 | 2026/01/22 17:18:14 CST | python | Accepted | 551 ms | 35.3 MB |
| 693292267 | 2026/01/22 17:17:24 CST | python | Wrong Answer | N/A | N/A |
| 693292199 | 2026/01/22 17:17:13 CST | python | Runtime Error | N/A | N/A |
| 692361482 | 2026/01/19 10:32:52 CST | python | Accepted | 551 ms | 35 MB |
| 691197353 | 2026/01/14 09:15:09 CST | python | Accepted | 557 ms | 35 MB |
| 690994600 | 2026/01/13 13:13:04 CST | python | Accepted | 539 ms | 35.2 MB |
| 690994572 | 2026/01/13 13:12:55 CST | python | Runtime Error | N/A | N/A |
| 690994503 | 2026/01/13 13:12:31 CST | python | Runtime Error | N/A | N/A |
| 690711245 | 2026/01/12 10:58:35 CST | python | Accepted | 583 ms | 34.9 MB |
| 688523909 | 2026/01/02 10:45:06 CST | python | Accepted | 759 ms | 32.7 MB |

### 最近一次 AC 代码

```python
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]
```

## 518. 零钱兑换 II (`coin-change-ii`)

- 题目链接：https://leetcode.cn/problems/coin-change-ii/
- 难度：Medium
- 标签：Array, Dynamic Programming
- 总提交次数：11
- 最近提交时间：2026/04/13 11:51:48 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 717644783 | 2026/04/13 11:51:48 CST | python | Accepted | 527 ms | 63.8 MB |
| 698393174 | 2026/02/13 14:51:55 CST | python | Accepted | 439 ms | 64 MB |
| 693091118 | 2026/01/21 21:33:03 CST | python | Accepted | 542 ms | 63.8 MB |
| 689707827 | 2026/01/07 16:20:29 CST | python | Accepted | 475 ms | 64.2 MB |
| 689707749 | 2026/01/07 16:20:16 CST | python | Runtime Error | N/A | N/A |
| 689421576 | 2026/01/06 14:30:49 CST | python | Accepted | 447 ms | 64.2 MB |
| 689414665 | 2026/01/06 14:03:30 CST | python | Accepted | 171 ms | 19.5 MB |
| 689136599 | 2026/01/05 11:29:51 CST | python | Accepted | 435 ms | 61.8 MB |
| 688943221 | 2026/01/04 15:31:48 CST | python | Accepted | 522 ms | 62 MB |
| 688564942 | 2026/01/02 15:01:19 CST | python | Accepted | 443 ms | 62 MB |
| 688559918 | 2026/01/02 14:32:59 CST | python | Accepted | 179 ms | 17.5 MB |

### 最近一次 AC 代码

```python
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            coin = coins[i - 1]
            for j in range(amount + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= coin:
                    dp[i][j] += dp[i][j - coin]
        return dp[n][amount]
```

## 523. 连续的子数组和 (`continuous-subarray-sum`)

- 题目链接：https://leetcode.cn/problems/continuous-subarray-sum/
- 难度：Medium
- 标签：Array, Hash Table, Math, Prefix Sum
- 总提交次数：10
- 最近提交时间：2026/03/22 17:45:19 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 710583571 | 2026/03/22 17:45:19 CST | python | Accepted | 62 ms | 38.8 MB |
| 710582926 | 2026/03/22 17:43:58 CST | python | Wrong Answer | N/A | N/A |
| 707711717 | 2026/03/16 11:25:24 CST | python | Accepted | 60 ms | 39 MB |
| 707709099 | 2026/03/16 11:21:05 CST | python | Wrong Answer | N/A | N/A |
| 707708228 | 2026/03/16 11:19:32 CST | python | Wrong Answer | N/A | N/A |
| 707707572 | 2026/03/16 11:18:23 CST | python | Wrong Answer | N/A | N/A |
| 663710370 | 2025/09/17 21:37:45 CST | python | Accepted | 87 ms | 37.1 MB |
| 663709889 | 2025/09/17 21:36:20 CST | python | Wrong Answer | N/A | N/A |
| 663709780 | 2025/09/17 21:36:02 CST | python | Wrong Answer | N/A | N/A |
| 662218715 | 2025/09/13 09:34:03 CST | python | Accepted | 67 ms | 37.4 MB |

### 最近一次 AC 代码

```python
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder_map = {0 : -1}
        pre_sum = 0
        for i, num in enumerate(nums):
            pre_sum += num
            remainder = pre_sum % k
            if remainder in remainder_map:
                if i - remainder_map[remainder] >= 2:
                    return True
            else:
                remainder_map[remainder] = i
        return False
```

## 525. 连续数组 (`contiguous-array`)

- 题目链接：https://leetcode.cn/problems/contiguous-array/
- 难度：Medium
- 标签：Array, Hash Table, Prefix Sum
- 总提交次数：11
- 最近提交时间：2026/03/16 11:02:09 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 707698454 | 2026/03/16 11:02:09 CST | python | Accepted | 75 ms | 24.7 MB |
| 707697844 | 2026/03/16 11:01:07 CST | python | Wrong Answer | N/A | N/A |
| 707697623 | 2026/03/16 11:00:44 CST | python | Wrong Answer | N/A | N/A |
| 663976102 | 2025/09/18 18:59:53 CST | python | Accepted | 115 ms | 23 MB |
| 663975731 | 2025/09/18 18:58:12 CST | python | Wrong Answer | N/A | N/A |
| 662212277 | 2025/09/13 08:23:57 CST | python | Accepted | 105 ms | 23 MB |
| 662212265 | 2025/09/13 08:23:46 CST | python | Runtime Error | N/A | N/A |
| 662053307 | 2025/09/12 15:53:52 CST | python | Accepted | 153 ms | 23.5 MB |
| 662053043 | 2025/09/12 15:53:17 CST | python | Runtime Error | N/A | N/A |
| 662051824 | 2025/09/12 15:50:30 CST | python | Wrong Answer | N/A | N/A |
| 662051475 | 2025/09/12 15:49:44 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_len = 0
        sum_to_index = {0 : -1}
        pre_sum = 0
        for i, num in enumerate(nums):
            if num == 0:
                pre_sum += -1
            else:
                pre_sum += 1
            if pre_sum in sum_to_index:
                max_len = max(max_len, i - sum_to_index[pre_sum])
            else:
                sum_to_index[pre_sum] = i
        return max_len
```

## 526. 优美的排列 (`beautiful-arrangement`)

- 题目链接：https://leetcode.cn/problems/beautiful-arrangement/
- 难度：Medium
- 标签：Bit Manipulation, Array, Dynamic Programming, Backtracking, Bitmask
- 总提交次数：3
- 最近提交时间：2026/02/20 21:50:03 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 699516572 | 2026/02/20 21:50:03 CST | python | Accepted | 639 ms | 19.1 MB |
| 687818610 | 2025/12/29 11:05:26 CST | python | Accepted | 717 ms | 17 MB |
| 687818550 | 2025/12/29 11:05:14 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def countArrangement(self, n: int) -> int:
        res = 0
        used = [False] * (n + 1)
        def backtrack(pos):
            nonlocal res
            if pos == n + 1:
                res += 1
                return
            for x in range(1, n + 1):
                if used[x]:
                    continue
                if x % pos != 0 and pos % x != 0:
                    continue
                used[x] = True
                backtrack(pos + 1)
                used[x] = False
        backtrack(1)
        return res
```

## 528. 按权重随机选择 (`random-pick-with-weight`)

- 题目链接：https://leetcode.cn/problems/random-pick-with-weight/
- 难度：Medium
- 标签：Array, Math, Binary Search, Prefix Sum, Randomized
- 总提交次数：4
- 最近提交时间：2026/03/24 11:08:14 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 711269288 | 2026/03/24 11:08:14 CST | python | Accepted | 43 ms | 24 MB |
| 709981050 | 2026/03/21 09:41:43 CST | python | Accepted | 46 ms | 24.3 MB |
| 709832246 | 2026/03/20 19:06:07 CST | python | Accepted | 54 ms | 24.3 MB |
| 709832082 | 2026/03/20 19:05:32 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        self.total = 0
        for weight in w:
            self.total += weight
            self.prefix.append(self.total)

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        return bisect.bisect_left(self.prefix, target)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
```

## 531. 孤独像素 I (`lonely-pixel-i`)

- 题目链接：https://leetcode.cn/problems/lonely-pixel-i/
- 难度：Medium
- 标签：Array, Hash Table, Matrix
- 总提交次数：3
- 最近提交时间：2026/03/10 15:36:29 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 705130645 | 2026/03/10 15:36:29 CST | python | Accepted | 25 ms | 22.8 MB |
| 705130257 | 2026/03/10 15:35:53 CST | python | Time Limit Exceeded | N/A | N/A |
| 705130134 | 2026/03/10 15:35:43 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        if not picture or not picture[0]:
            return 0
        m, n = len(picture), len(picture[0])
        row_count = [0] * m
        col_count = [0] * n
        for i in range(m):
            for j in range(n):
                if picture[i][j] == 'B':
                    row_count[i] += 1
                    col_count[j] += 1
        lonely_count = 0
        for i in range(m):
            for j in range(n):
                if (
                    picture[i][j] == 'B'
                    and row_count[i] == 1
                    and col_count[j] == 1
                ):
                    lonely_count += 1
        return lonely_count
```

## 538. 把二叉搜索树转换为累加树 (`convert-bst-to-greater-tree`)

- 题目链接：https://leetcode.cn/problems/convert-bst-to-greater-tree/
- 难度：Medium
- 标签：Tree, Depth-First Search, Binary Search Tree, Binary Tree
- 总提交次数：1
- 最近提交时间：2026/04/03 11:39:31 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 714799754 | 2026/04/03 11:39:31 CST | python | Accepted | 3 ms | 21.1 MB |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.sum = 0
        def traverse(root):
            if not root:
                return 
            traverse(root.right)
            self.sum += root.val
            root.val = self.sum
            traverse(root.left)
        traverse(root)
        return root
```

## 542. 01 矩阵 (`01-matrix`)

- 题目链接：https://leetcode.cn/problems/01-matrix/
- 难度：Medium
- 标签：Breadth-First Search, Array, Dynamic Programming, Matrix
- 总提交次数：5
- 最近提交时间：2025/12/24 15:12:30 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 686848662 | 2025/12/24 15:12:30 CST | python | Accepted | 111 ms | 19.8 MB |
| 686848413 | 2025/12/24 15:11:45 CST | python | Wrong Answer | N/A | N/A |
| 686625937 | 2025/12/23 15:44:29 CST | python | Accepted | 109 ms | 19.6 MB |
| 686625695 | 2025/12/23 15:43:43 CST | python | Wrong Answer | N/A | N/A |
| 686625623 | 2025/12/23 15:43:29 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return []
        m, n = len(mat), len(mat[0])
        res = [[-1] * n for _ in range(m)]
        dq = collections.deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    res[i][j] = 0
                    dq.append((i, j))
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while dq:
            r, c = dq.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                if res[nr][nc] == -1:
                    res[nr][nc] = res[r][c] + 1
                    dq.append((nr, nc))
        return res
```

## 543. 二叉树的直径 (`diameter-of-binary-tree`)

- 题目链接：https://leetcode.cn/problems/diameter-of-binary-tree/
- 难度：Easy
- 标签：Tree, Depth-First Search, Binary Tree
- 总提交次数：8
- 最近提交时间：2026/04/03 10:03:11 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 714766734 | 2026/04/03 10:03:11 CST | python | Accepted | 0 ms | 22.1 MB |
| 714553235 | 2026/04/02 15:33:15 CST | python | Accepted | 0 ms | 22.1 MB |
| 701127847 | 2026/02/28 10:31:00 CST | python | Accepted | 3 ms | 22.1 MB |
| 684865017 | 2025/12/15 13:37:14 CST | python | Accepted | 1 ms | 20.4 MB |
| 684864961 | 2025/12/15 13:36:53 CST | python | Runtime Error | N/A | N/A |
| 684838180 | 2025/12/15 11:06:25 CST | python | Accepted | 8 ms | 20.4 MB |
| 684837653 | 2025/12/15 11:04:37 CST | python | Wrong Answer | N/A | N/A |
| 684837522 | 2025/12/15 11:04:07 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        def get_height(node):
            if not node:
                return 0
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            self.max_diameter = max(self.max_diameter, left_height + right_height)
            return max(left_height, right_height) + 1
        get_height(root)
        return self.max_diameter
```

## 545. 二叉树的边界 (`boundary-of-binary-tree`)

- 题目链接：https://leetcode.cn/problems/boundary-of-binary-tree/
- 难度：Medium
- 标签：Tree, Depth-First Search, Binary Tree
- 总提交次数：4
- 最近提交时间：2026/03/01 14:57:37 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 701449186 | 2026/03/01 14:57:37 CST | python | Accepted | 3 ms | 20 MB |
| 701449049 | 2026/03/01 14:57:11 CST | python | Wrong Answer | N/A | N/A |
| 701447324 | 2026/03/01 14:53:26 CST | python | Runtime Error | N/A | N/A |
| 701447274 | 2026/03/01 14:53:16 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = [root.val]
        def is_leaf(node):
            return node and not node.left and not node.right
        
        def get_left_boundry(node):
            while node:
                if is_leaf(node):
                    break
                res.append(node.val)
                if node.left:
                    node = node.left
                else:
                    node = node.right
        
        def get_leaves(node):
            if not node:
                return
            if is_leaf(node):
                if node is not root:
                    res.append(node.val)
            else:
                get_leaves(node.left)
                get_leaves(node.right)
        
        def get_right_boundry(node):
            stack = []
            while node:
                if is_leaf(node):
                    break
                stack.append(node.val)
                if node.right:
                    node = node.right
                else:
                    node = node.left
            while stack:
                res.append(stack.pop())
        
        get_left_boundry(root.left)
        get_leaves(root)
        get_right_boundry(root.right)

        return res
```

## 549. 二叉树最长连续序列 II (`binary-tree-longest-consecutive-sequence-ii`)

- 题目链接：https://leetcode.cn/problems/binary-tree-longest-consecutive-sequence-ii/
- 难度：Medium
- 标签：Tree, Depth-First Search, Binary Tree
- 总提交次数：2
- 最近提交时间：2026/02/28 14:18:32 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 701177866 | 2026/02/28 14:18:32 CST | python | Accepted | 7 ms | 20 MB |
| 701177761 | 2026/02/28 14:18:11 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        self.max_len = 0
        def dfs(node):  # 返回以当前节点为起点的最长递增路径和最长递减路径
            if not node:
                return 0, 0
            inc, dec = 1, 1
            left_inc, left_dec = dfs(node.left)
            right_inc, right_dec = dfs(node.right)
            if node.left:
                if node.val == node.left.val - 1:
                    inc = max(inc, left_inc + 1)
                elif node.val == node.left.val + 1:
                    dec = max(dec, left_dec + 1)
            if node.right:
                if node.val == node.right.val - 1:
                    inc = max(inc, right_inc + 1)
                elif node.val == node.right.val + 1:
                    dec = max(dec, right_dec + 1)
            self.max_len = max(self.max_len, inc + dec - 1)
            return inc, dec
        dfs(root)
        return self.max_len
```

## 560. 和为 K 的子数组 (`subarray-sum-equals-k`)

- 题目链接：https://leetcode.cn/problems/subarray-sum-equals-k/
- 难度：Medium
- 标签：Array, Hash Table, Prefix Sum
- 总提交次数：7
- 最近提交时间：2026/03/16 13:51:52 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 707761259 | 2026/03/16 13:51:52 CST | python | Accepted | 39 ms | 22 MB |
| 707761174 | 2026/03/16 13:51:39 CST | python | Runtime Error | N/A | N/A |
| 682385489 | 2025/12/03 14:53:42 CST | python | Accepted | 47 ms | 20.1 MB |
| 682385328 | 2025/12/03 14:53:10 CST | python | Wrong Answer | N/A | N/A |
| 663592105 | 2025/09/17 15:58:48 CST | python | Accepted | 30 ms | 20 MB |
| 663591836 | 2025/09/17 15:58:15 CST | python | Wrong Answer | N/A | N/A |
| 662224766 | 2025/09/13 10:06:15 CST | python | Accepted | 27 ms | 20.1 MB |

### 最近一次 AC 代码

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = 0
        pre_sum_map = collections.defaultdict(int)
        pre_sum_map[0] = 1
        cnt = 0
        for num in nums:
            pre_sum += num
            target = pre_sum - k
            if target in pre_sum_map:
                cnt += pre_sum_map.get(target)
            pre_sum_map[pre_sum] += 1
        return cnt
```

## 563. 二叉树的坡度 (`binary-tree-tilt`)

- 题目链接：https://leetcode.cn/problems/binary-tree-tilt/
- 难度：Easy
- 标签：Tree, Depth-First Search, Binary Tree
- 总提交次数：1
- 最近提交时间：2026/02/28 11:35:24 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 701146418 | 2026/02/28 11:35:24 CST | python | Accepted | 4 ms | 20.2 MB |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.total_tile = 0
        def get_sum(node):
            if not node:
                return 0
            left_sum = get_sum(node.left)
            right_sum = get_sum(node.right)
            self.total_tile += abs(left_sum - right_sum)
            return node.val + left_sum + right_sum
        get_sum(root)
        return self.total_tile
```

## 566. 重塑矩阵 (`reshape-the-matrix`)

- 题目链接：https://leetcode.cn/problems/reshape-the-matrix/
- 难度：Easy
- 标签：Array, Matrix, Simulation
- 总提交次数：1
- 最近提交时间：2026/03/19 12:24:21 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 709194141 | 2026/03/19 12:24:21 CST | python | Accepted | 0 ms | 19.7 MB |

### 最近一次 AC 代码

```python
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        res = [[0] * c for _ in range(r)]
        for idx in range(m * n):
            old_row = idx // n
            old_col = idx % n
            new_row = idx // c
            new_col = idx % c
            res[new_row][new_col] = mat[old_row][old_col]
        return res
```

## 567. 字符串的排列 (`permutation-in-string`)

- 题目链接：https://leetcode.cn/problems/permutation-in-string/
- 难度：Medium
- 标签：Hash Table, Two Pointers, String, Sliding Window
- 总提交次数：9
- 最近提交时间：2026/03/18 10:02:24 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 708641226 | 2026/03/18 10:02:24 CST | python | Accepted | 15 ms | 19.3 MB |
| 700401631 | 2026/02/25 14:22:12 CST | python | Accepted | 23 ms | 19.1 MB |
| 700401345 | 2026/02/25 14:21:10 CST | python | Wrong Answer | N/A | N/A |
| 660867188 | 2025/09/09 08:31:19 CST | python | Accepted | 23 ms | 17.9 MB |
| 660797800 | 2025/09/08 22:02:13 CST | python | Accepted | 27 ms | 17.9 MB |
| 660793399 | 2025/09/08 21:51:50 CST | python | Wrong Answer | N/A | N/A |
| 660789212 | 2025/09/08 21:42:02 CST | python | Wrong Answer | N/A | N/A |
| 660782710 | 2025/09/08 21:27:10 CST | python | Wrong Answer | N/A | N/A |
| 650625014 | 2025/08/07 09:27:20 CST | python | Accepted | 27 ms | 17.6 MB |

### 最近一次 AC 代码

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = collections.Counter(s1)
        window = collections.defaultdict(int)
        left = 0
        valid = 0
        for right, r_char in enumerate(s2):
            if r_char in need:
                window[r_char] += 1
                if window[r_char] == need[r_char]:
                    valid += 1
            if right >= len(s1) - 1:
                if valid == len(need):
                    return True
                l_char = s2[left]
                if l_char in need:
                    if window[l_char] == need[l_char]:
                        valid -= 1
                    window[l_char] -= 1
                left += 1
        return False
```

## 582. 杀掉进程 (`kill-process`)

- 题目链接：https://leetcode.cn/problems/kill-process/
- 难度：Medium
- 标签：Tree, Depth-First Search, Breadth-First Search, Array, Hash Table
- 总提交次数：2
- 最近提交时间：2026/03/08 19:48:07 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 704329885 | 2026/03/08 19:48:07 CST | python | Accepted | 35 ms | 30 MB |
| 704329770 | 2026/03/08 19:47:52 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        child_map = collections.defaultdict(list)
        for child, parent in zip(pid, ppid):
            child_map[parent].append(child)
        
        res = []
        dq = collections.deque([kill])
        while dq:
            node = dq.popleft()
            res.append(node)
            for child in child_map[node]:
                dq.append(child)
        
        return res
```

## 583. 两个字符串的删除操作 (`delete-operation-for-two-strings`)

- 题目链接：https://leetcode.cn/problems/delete-operation-for-two-strings/
- 难度：Medium
- 标签：String, Dynamic Programming
- 总提交次数：13
- 最近提交时间：2026/02/11 13:46:20 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 697939972 | 2026/02/11 13:46:20 CST | python | Accepted | 79 ms | 21 MB |
| 693288309 | 2026/01/22 17:06:30 CST | python | Accepted | 79 ms | 21 MB |
| 692457774 | 2026/01/19 16:25:05 CST | python | Accepted | 99 ms | 21.1 MB |
| 692457156 | 2026/01/19 16:23:38 CST | python | Wrong Answer | N/A | N/A |
| 690695170 | 2026/01/12 09:55:39 CST | python | Accepted | 79 ms | 21 MB |
| 690694897 | 2026/01/12 09:54:20 CST | python | Wrong Answer | N/A | N/A |
| 690694867 | 2026/01/12 09:54:10 CST | python | Runtime Error | N/A | N/A |
| 690694803 | 2026/01/12 09:53:50 CST | python | Wrong Answer | N/A | N/A |
| 688515358 | 2026/01/02 09:10:11 CST | python | Accepted | 139 ms | 19 MB |
| 685329263 | 2025/12/17 11:31:49 CST | python | Accepted | 137 ms | 19.4 MB |
| 685328807 | 2025/12/17 11:30:08 CST | python | Wrong Answer | N/A | N/A |
| 685328628 | 2025/12/17 11:29:23 CST | python | Wrong Answer | N/A | N/A |
| 685328370 | 2025/12/17 11:28:30 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return m + n - 2 * dp[m][n]
```

## 588. 设计内存文件系统 (`design-in-memory-file-system`)

- 题目链接：https://leetcode.cn/problems/design-in-memory-file-system/
- 难度：Hard
- 标签：Design, Trie, Hash Table, String, Sorting
- 总提交次数：1
- 最近提交时间：2026/03/12 11:10:29 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 705985434 | 2026/03/12 11:10:29 CST | python | Accepted | 3 ms | 19.8 MB |

### 最近一次 AC 代码

```python
class TrieNode:
    def __init__(self):
        self.children: Dict[str, "TrieNode"] = {}
        self.is_file: bool = False
        self.content: str = ''


class FileSystem:

    def __init__(self):
        self.root = TrieNode()
    

    def _traverse(self, parts, create):
        node = self.root
        for part in parts:
            if part not in node.children:
                if not create:
                    raise FileNotFoundError(f'Path not found: {'.'.join(parts)}')
                node.children[part] = TrieNode()
            node = node.children[part]
        return node

    
    def _split_path(self, path):
        return [part for part in path.split('/') if part]
        

    def ls(self, path: str) -> List[str]:
        if path == '/':
            return sorted(self.root.children.keys())
        parts = self._split_path(path)
        node = self._traverse(parts, False)

        if node.is_file:
            return [parts[-1]]
        
        return sorted(node.children.keys())


    def mkdir(self, path: str) -> None:
        parts = self._split_path(path)
        self._traverse(parts, True)
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        parts = self._split_path(filePath)
        node = self._traverse(parts, True)
        node.is_file = True
        node.content += content
        

    def readContentFromFile(self, filePath: str) -> str:
        parts = self._split_path(filePath)
        node = self._traverse(parts, False)
        return node.content
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
```

## 589. N 叉树的前序遍历 (`n-ary-tree-preorder-traversal`)

- 题目链接：https://leetcode.cn/problems/n-ary-tree-preorder-traversal/
- 难度：Easy
- 标签：Stack, Tree, Depth-First Search
- 总提交次数：5
- 最近提交时间：2026/04/02 13:00:11 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 714503044 | 2026/04/02 13:00:11 CST | python | Accepted | 69 ms | 20.6 MB |
| 701376402 | 2026/03/01 10:27:32 CST | python | Accepted | 62 ms | 20.6 MB |
| 701375896 | 2026/03/01 10:25:17 CST | python | Accepted | 55 ms | 20.7 MB |
| 684727215 | 2025/12/14 18:16:39 CST | python | Accepted | 56 ms | 18.8 MB |
| 684721873 | 2025/12/14 17:46:17 CST | python | Accepted | 53 ms | 19.2 MB |

### 最近一次 AC 代码

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            node =  stack.pop()
            res.append(node.val)
            for child in node.children[::-1]:
                stack.append(child)
        return res
```

## 590. N 叉树的后序遍历 (`n-ary-tree-postorder-traversal`)

- 题目链接：https://leetcode.cn/problems/n-ary-tree-postorder-traversal/
- 难度：Easy
- 标签：Stack, Tree, Depth-First Search
- 总提交次数：3
- 最近提交时间：2026/04/02 13:06:11 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 714504244 | 2026/04/02 13:06:11 CST | python | Accepted | 55 ms | 20.8 MB |
| 684742878 | 2025/12/14 19:53:53 CST | python | Accepted | 57 ms | 19 MB |
| 684742227 | 2025/12/14 19:50:32 CST | python | Accepted | 41 ms | 19.2 MB |

### 最近一次 AC 代码

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            for child in node.children:
                stack.append(child)
        return res[::-1]
```

## 604. 迭代压缩字符串 (`design-compressed-string-iterator`)

- 题目链接：https://leetcode.cn/problems/design-compressed-string-iterator/
- 难度：Easy
- 标签：Design, Array, String, Iterator
- 总提交次数：4
- 最近提交时间：2026/03/13 15:40:24 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 706581113 | 2026/03/13 15:40:24 CST | python | Accepted | 0 ms | 19.3 MB |
| 706579615 | 2026/03/13 15:38:13 CST | python | Wrong Answer | N/A | N/A |
| 706579489 | 2026/03/13 15:38:00 CST | python | Wrong Answer | N/A | N/A |
| 706579358 | 2026/03/13 15:37:48 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class StringIterator:

    def __init__(self, compressedString: str):
        self.s = compressedString
        self.index = 0
        self.curr_char = ''
        self.curr_count = 0
        
    
    def _load_next_group(self):
        if self.index >= len(self.s):
            return
        self.curr_char = self.s[self.index]
        self.index += 1

        count = 0
        while self.index < len(self.s) and self.s[self.index].isdigit():
            count = count * 10 + int(self.s[self.index])
            self.index += 1
        self.curr_count = count


    def next(self) -> str:
        if not self.hasNext():
            return ' '
        if self.curr_count == 0:
            self._load_next_group()
        self.curr_count -= 1
        return self.curr_char
        

    def hasNext(self) -> bool:
        return self.curr_count > 0 or self.index < len(self.s)
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
```

## 616. 给字符串添加加粗标签 (`add-bold-tag-in-string`)

- 题目链接：https://leetcode.cn/problems/add-bold-tag-in-string/
- 难度：Medium
- 标签：Trie, Array, Hash Table, String, String Matching
- 总提交次数：2
- 最近提交时间：2026/02/26 09:58:04 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 700596514 | 2026/02/26 09:58:04 CST | python | Accepted | 31 ms | 19.5 MB |
| 700596479 | 2026/02/26 09:57:54 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        n = len(s)
        is_bold = [False] * n
        end = 0
        for i in range(n):
            for word in words:
                if s.startswith(word, i):
                    end = max(end, i + len(word))
            if end > i:
                is_bold[i] = True
        
        res = []
        for i in range(n):
            if is_bold[i] and (i == 0 or not is_bold[i-1]):
                res.append('<b>')
            res.append(s[i])
            if is_bold[i] and (i == n - 1 or not is_bold[i+1]):
                res.append('</b>')
        return ''.join(res)
```

## 622. 设计循环队列 (`design-circular-queue`)

- 题目链接：https://leetcode.cn/problems/design-circular-queue/
- 难度：Medium
- 标签：Design, Queue, Array, Linked List
- 总提交次数：1
- 最近提交时间：2026/03/24 13:46:14 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 711323185 | 2026/03/24 13:46:14 CST | python | Accepted | 8 ms | 19.8 MB |

### 最近一次 AC 代码

```python
class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.data = [0] * k
        self.size = 0
        self.head = 0


    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        tail_index = (self.head + self.size) % self.capacity
        self.data[tail_index] = value
        self.size += 1
        return True
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.data[self.head]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        tail_index = (self.head + self.size - 1) % self.capacity
        return self.data[tail_index]
        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.size == self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
```

## 624. 数组列表中的最大距离 (`maximum-distance-in-arrays`)

- 题目链接：https://leetcode.cn/problems/maximum-distance-in-arrays/
- 难度：Medium
- 标签：Greedy, Array
- 总提交次数：6
- 最近提交时间：2026/02/23 18:45:13 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 700012951 | 2026/02/23 18:45:13 CST | python | Accepted | 40 ms | 34.5 MB |
| 696568820 | 2026/02/05 11:16:33 CST | python | Accepted | 31 ms | 34.7 MB |
| 696568350 | 2026/02/05 11:15:03 CST | python | Runtime Error | N/A | N/A |
| 558294473 | 2024/08/25 07:42:12 CST | python | Accepted | 162 ms | 32.8 MB |
| 557540686 | 2024/08/22 10:03:47 CST | python | Accepted | 163 ms | 32.9 MB |
| 557537095 | 2024/08/22 09:52:32 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        max_val = arrays[0][-1]
        min_val = arrays[0][0]
        max_distance = 0
        for array in arrays[1:]:
            max_distance = max(max_distance, abs(max_val - array[0]))
            max_distance = max(max_distance, abs(min_val - array[-1]))
            max_val = max(max_val, array[-1])
            min_val = min(min_val, array[0])
        return max_distance
```

## 637. 二叉树的层平均值 (`average-of-levels-in-binary-tree`)

- 题目链接：https://leetcode.cn/problems/average-of-levels-in-binary-tree/
- 难度：Easy
- 标签：Tree, Depth-First Search, Breadth-First Search, Binary Tree
- 总提交次数：1
- 最近提交时间：2025/12/20 18:28:29 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 686028063 | 2025/12/20 18:28:29 CST | python | Accepted | 3 ms | 18.8 MB |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        res = []
        dq = collections.deque([root])
        while dq:
            sz = len(dq)
            total = 0
            for _ in range(sz):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
                total += node.val
            res.append(total / sz)
        return res
```

## 641. 设计循环双端队列 (`design-circular-deque`)

- 题目链接：https://leetcode.cn/problems/design-circular-deque/
- 难度：Medium
- 标签：Design, Queue, Array, Linked List
- 总提交次数：1
- 最近提交时间：2026/03/24 13:58:11 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 711327679 | 2026/03/24 13:58:11 CST | python | Accepted | 8 ms | 19.9 MB |

### 最近一次 AC 代码

```python
class MyCircularDeque:

    def __init__(self, k: int):
        self.dq = collections.deque()
        self.capacity = k
        

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.dq.appendleft(value)
        return True
        

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.dq.append(value)
        return True
        

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.dq.popleft()
        return True
        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.dq.pop()
        return True
        

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.dq[0]
        

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.dq[-1]
        

    def isEmpty(self) -> bool:
        return len(self.dq) == 0 
        

    def isFull(self) -> bool:
        return len(self.dq) == self.capacity        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
```

## 642. 设计搜索自动补全系统 (`design-search-autocomplete-system`)

- 题目链接：https://leetcode.cn/problems/design-search-autocomplete-system/
- 难度：Hard
- 标签：Depth-First Search, Design, Trie, String, Data Stream, Sorting, Heap (Priority Queue)
- 总提交次数：2
- 最近提交时间：2026/03/12 12:26:18 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 706019108 | 2026/03/12 12:26:18 CST | python | Accepted | 167 ms | 26 MB |
| 706018938 | 2026/03/12 12:25:37 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class TrieNode:
    def __init__(self):
        self.children: Dict[str, "TrieNode"] = {}
        self.sentences: Set[str] = set()

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.sentence_to_count = collections.defaultdict(int)
        self.curr_input = []
        for sentence, count in zip(sentences, times):
            self.sentence_to_count[sentence] = count
            self._insert(sentence)
    
    def _insert(self, sentence):
        node = self.root
        for ch in sentence:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.sentences.add(sentence)

    def _search_prefix(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node
        

    def input(self, c: str) -> List[str]:
        if c == '#':
            sentence = ''.join(self.curr_input)
            self.sentence_to_count[sentence] += 1
            self._insert(sentence)
            self.curr_input = []
            return []
        self.curr_input.append(c)
        prefix = ''.join(self.curr_input)
        node = self._search_prefix(prefix)
        if not node:
            return []
        candidates = list(node.sentences)
        candidates.sort(key=lambda s: (-self.sentence_to_count[s], s))
        return candidates[:3]       


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
```

## 643. 子数组最大平均数 I (`maximum-average-subarray-i`)

- 题目链接：https://leetcode.cn/problems/maximum-average-subarray-i/
- 难度：Easy
- 标签：Array, Sliding Window
- 总提交次数：8
- 最近提交时间：2026/02/25 14:05:36 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 700397604 | 2026/02/25 14:05:36 CST | python | Accepted | 91 ms | 28.7 MB |
| 658560994 | 2025/09/01 21:44:01 CST | python | Accepted | 176 ms | 27 MB |
| 658560019 | 2025/09/01 21:41:31 CST | python | Wrong Answer | N/A | N/A |
| 658559348 | 2025/09/01 21:39:48 CST | python | Wrong Answer | N/A | N/A |
| 658404145 | 2025/09/01 14:49:24 CST | python | Accepted | 124 ms | 26.9 MB |
| 658396244 | 2025/09/01 14:30:06 CST | python | Accepted | 165 ms | 27 MB |
| 658393766 | 2025/09/01 14:23:13 CST | python | Wrong Answer | N/A | N/A |
| 658393270 | 2025/09/01 14:21:45 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = -float('inf')
        max_sum = 0
        left = 0
        for right, r_num in enumerate(nums):
            max_sum += r_num
            if right >= k - 1:
                max_avg = max(max_avg, max_sum / k)
                max_sum -= nums[left]
                left += 1
        return max_avg if max_avg != -float('inf') else 0
```

## 644. 子数组最大平均数 II (`maximum-average-subarray-ii`)

- 题目链接：https://leetcode.cn/problems/maximum-average-subarray-ii/
- 难度：Hard
- 标签：Array, Binary Search, Prefix Sum
- 总提交次数：3
- 最近提交时间：2026/03/04 10:35:21 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 702465098 | 2026/03/04 10:35:21 CST | python | Accepted | 705 ms | 20.6 MB |
| 702464923 | 2026/03/04 10:35:00 CST | python | Runtime Error | N/A | N/A |
| 702464711 | 2026/03/04 10:34:34 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        def check(avg):
            curr_sum = 0
            for i in range(k):
                curr_sum += nums[i] - avg
            if curr_sum >= 0:
                return True
            
            pre_sum = 0
            min_pre_sum = 0
            for i in range(k, len(nums)):
                curr_sum += nums[i] - avg
                pre_sum += nums[i - k] - avg
                min_pre_sum = min(min_pre_sum, pre_sum)
                if curr_sum - min_pre_sum >= 0:
                    return True
            return False
        
        left, right = min(nums), max(nums)
        while right - left > 1e-5:
            mid = (left + right) / 2
            if check(mid):
                left = mid
            else:
                right = mid
        return left
```

## 647. 回文子串 (`palindromic-substrings`)

- 题目链接：https://leetcode.cn/problems/palindromic-substrings/
- 难度：Medium
- 标签：Two Pointers, String, Dynamic Programming
- 总提交次数：1
- 最近提交时间：2026/01/19 11:03:25 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 692370758 | 2026/01/19 11:03:25 CST | python | Accepted | 107 ms | 19.3 MB |

### 最近一次 AC 代码

```python
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        def expand_around_center(left, right):
            cnt = 0
            while left >= 0 and right < n and s[left] == s[right]:
                cnt += 1
                left -= 1
                right += 1
            return cnt
        for i in range(n):
            res += expand_around_center(i, i)
            res += expand_around_center(i, i + 1)
        return res
```

## 651. 四个键的键盘 (`4-keys-keyboard`)

- 题目链接：https://leetcode.cn/problems/4-keys-keyboard/
- 难度：Medium
- 标签：Math, Dynamic Programming
- 总提交次数：2
- 最近提交时间：2026/02/25 10:39:50 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 700353195 | 2026/02/25 10:39:50 CST | python | Accepted | 3 ms | 19 MB |
| 700351646 | 2026/02/25 10:34:22 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def maxA(self, n: int) -> int:
        dp = [i for i in range(n + 1)]
        for i in range(1, n + 1):
            # 到第 j 步时是准备开始做递增的基准
            for j in range(1, i - 2):
                curr = dp[j] + dp[j] * (i - (j + 2))
                dp[i] = max(dp[i], curr)
        return dp[n]
```

## 652. 寻找重复的子树 (`find-duplicate-subtrees`)

- 题目链接：https://leetcode.cn/problems/find-duplicate-subtrees/
- 难度：Medium
- 标签：Tree, Depth-First Search, Hash Table, Binary Tree
- 总提交次数：5
- 最近提交时间：2026/02/28 13:57:12 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 701172483 | 2026/02/28 13:57:12 CST | python | Accepted | 3 ms | 20.4 MB |
| 687227531 | 2025/12/26 10:04:20 CST | python | Accepted | 99 ms | 17.9 MB |
| 687226782 | 2025/12/26 10:00:37 CST | python | Wrong Answer | N/A | N/A |
| 687226006 | 2025/12/26 09:57:00 CST | python | Accepted | 55 ms | 17.6 MB |
| 687225920 | 2025/12/26 09:56:33 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        res = []
        subtree_count = collections.defaultdict(int)
        def _get_subtree_key(node):
            if not node:
                return None
            left_key = _get_subtree_key(node.left)
            right_key = _get_subtree_key(node.right)
            curr_key = (node.val, left_key, right_key)
            if subtree_count.get(curr_key) == 1:
                res.append(node)
            subtree_count[curr_key] += 1
            return curr_key
        _get_subtree_key(root)
        return res
```

## 654. 最大二叉树 (`maximum-binary-tree`)

- 题目链接：https://leetcode.cn/problems/maximum-binary-tree/
- 难度：Medium
- 标签：Stack, Tree, Array, Divide and Conquer, Binary Tree, Monotonic Stack
- 总提交次数：10
- 最近提交时间：2026/04/06 22:07:35 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715736477 | 2026/04/06 22:07:35 CST | python | Accepted | 7 ms | 19.6 MB |
| 715736239 | 2026/04/06 22:06:52 CST | python | Time Limit Exceeded | N/A | N/A |
| 701684368 | 2026/03/02 10:53:28 CST | python | Accepted | 5 ms | 19.4 MB |
| 701684261 | 2026/03/02 10:53:11 CST | python | Runtime Error | N/A | N/A |
| 701683981 | 2026/03/02 10:52:28 CST | python | Runtime Error | N/A | N/A |
| 701474198 | 2026/03/01 16:05:33 CST | python | Accepted | 15 ms | 19.5 MB |
| 701473751 | 2026/03/01 16:04:22 CST | python | Wrong Answer | N/A | N/A |
| 701473653 | 2026/03/01 16:04:05 CST | python | Runtime Error | N/A | N/A |
| 687054683 | 2025/12/25 13:58:58 CST | python | Accepted | 24 ms | 17.5 MB |
| 687044800 | 2025/12/25 12:49:31 CST | python | Accepted | 42 ms | 17.7 MB |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []
        for num in nums:
            node = TreeNode(num)
            while stack and stack[-1].val < num:
                node.left = stack.pop()
            if stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0] if stack else None
```

## 658. 找到 K 个最接近的元素 (`find-k-closest-elements`)

- 题目链接：https://leetcode.cn/problems/find-k-closest-elements/
- 难度：Medium
- 标签：Array, Two Pointers, Binary Search, Sorting, Sliding Window, Heap (Priority Queue)
- 总提交次数：8
- 最近提交时间：2026/03/24 10:26:11 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 711246969 | 2026/03/24 10:26:11 CST | python | Accepted | 0 ms | 20.4 MB |
| 711246475 | 2026/03/24 10:25:13 CST | python | Wrong Answer | N/A | N/A |
| 711246052 | 2026/03/24 10:24:18 CST | python | Wrong Answer | N/A | N/A |
| 709710012 | 2026/03/20 15:03:49 CST | python | Accepted | 0 ms | 20.6 MB |
| 709679085 | 2026/03/20 14:00:49 CST | python | Runtime Error | N/A | N/A |
| 709674836 | 2026/03/20 13:49:22 CST | python | Runtime Error | N/A | N/A |
| 709652976 | 2026/03/20 12:28:33 CST | python | Accepted | 0 ms | 20.4 MB |
| 709261980 | 2026/03/19 15:08:18 CST | python | Accepted | 0 ms | 20.3 MB |

### 最近一次 AC 代码

```python
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k
        while left < right:
            mid = left + (right - left) // 2
            # 比较 [mid, mid + k - 1] 和 [mid + 1, mid + k] 哪个区间更好
            # 只需比较 arr[mid] 和 arr[mid + k]哪个离 x 更近
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left + k]
```

## 662. 二叉树最大宽度 (`maximum-width-of-binary-tree`)

- 题目链接：https://leetcode.cn/problems/maximum-width-of-binary-tree/
- 难度：Medium
- 标签：Tree, Depth-First Search, Breadth-First Search, Binary Tree
- 总提交次数：9
- 最近提交时间：2026/04/05 16:34:33 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715339643 | 2026/04/05 16:34:33 CST | python | Accepted | 3 ms | 20 MB |
| 700869932 | 2026/02/27 10:36:25 CST | python | Accepted | 5 ms | 19.9 MB |
| 700869869 | 2026/02/27 10:36:12 CST | python | Runtime Error | N/A | N/A |
| 686306952 | 2025/12/22 10:21:20 CST | python | Accepted | 3 ms | 17.8 MB |
| 686306863 | 2025/12/22 10:20:57 CST | python | Runtime Error | N/A | N/A |
| 686121579 | 2025/12/21 10:49:54 CST | python | Accepted | 7 ms | 18.1 MB |
| 686018682 | 2025/12/20 17:29:28 CST | python | Accepted | 3 ms | 17.8 MB |
| 686018593 | 2025/12/20 17:28:59 CST | python | Wrong Answer | N/A | N/A |
| 686018344 | 2025/12/20 17:27:55 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_width = 0
        dq = collections.deque([(root, 1)])
        while dq:
            sz = len(dq)
            first_idx = dq[0][1]
            last_idx = dq[-1][1]
            for _ in range(sz):
                node, idx = dq.popleft()
                if node.left:
                    dq.append((node.left, idx * 2))
                if node.right:
                    dq.append((node.right, idx * 2 + 1))
            max_width = max(max_width, last_idx - first_idx + 1)
        return max_width
```

## 673. 最长递增子序列的个数 (`number-of-longest-increasing-subsequence`)

- 题目链接：https://leetcode.cn/problems/number-of-longest-increasing-subsequence/
- 难度：Medium
- 标签：Binary Indexed Tree, Segment Tree, Array, Dynamic Programming
- 总提交次数：4
- 最近提交时间：2026/02/14 10:25:55 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 698538011 | 2026/02/14 10:25:55 CST | python | Accepted | 467 ms | 19.3 MB |
| 697886218 | 2026/02/11 09:06:25 CST | python | Accepted | 459 ms | 19.3 MB |
| 697659535 | 2026/02/10 09:42:31 CST | python | Accepted | 463 ms | 19.5 MB |
| 697441410 | 2026/02/09 10:58:13 CST | python | Accepted | 467 ms | 19.2 MB |

### 最近一次 AC 代码

```python
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp_len = [1] * n
        dp_cnt = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp_len[j] + 1 > dp_len[i]:
                        dp_len[i] = dp_len[j] + 1
                        dp_cnt[i] = dp_cnt[j]
                    elif dp_len[j] + 1 == dp_len[i]:
                        dp_cnt[i] += dp_cnt[j]
        res = 0
        best_len = max(dp_len)
        for i in range(n):
            if dp_len[i] == best_len:
                res += dp_cnt[i]
        return res
```

## 674. 最长连续递增序列 (`longest-continuous-increasing-subsequence`)

- 题目链接：https://leetcode.cn/problems/longest-continuous-increasing-subsequence/
- 难度：Easy
- 标签：Array
- 总提交次数：2
- 最近提交时间：2026/02/11 10:07:29 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 697894964 | 2026/02/11 10:07:29 CST | python | Accepted | 3 ms | 20.2 MB |
| 697891531 | 2026/02/11 09:48:16 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_len = 1
        curr_len = 1
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                curr_len += 1
            else:
                curr_len = 1
            max_len = max(max_len, curr_len)
        return max_len
```

## 694. 不同岛屿的数量 (`number-of-distinct-islands`)

- 题目链接：https://leetcode.cn/problems/number-of-distinct-islands/
- 难度：Medium
- 标签：Depth-First Search, Breadth-First Search, Union Find, Array, Hash Table, Matrix, Sorting, Hash Function
- 总提交次数：2
- 最近提交时间：2026/04/10 13:13:18 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 716858957 | 2026/04/10 13:13:18 CST | python | Accepted | 33 ms | 20.6 MB |
| 687619700 | 2025/12/28 11:52:06 CST | python | Accepted | 27 ms | 17.6 MB |

### 最近一次 AC 代码

```python
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        shapes = set()
        def dfs(r, c, base_r, base_c, shape):
            if not (0 <= r < m and 0 <= c < n):
                return
            if grid[r][c] == 0:
                return
            grid[r][c] = 0
            shape.append((r - base_r, c - base_c))
            dfs(r + 1, c, base_r, base_c, shape)
            dfs(r - 1, c, base_r, base_c, shape)
            dfs(r, c + 1, base_r, base_c, shape)
            dfs(r, c - 1, base_r, base_c, shape)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    shape = []
                    dfs(i, j, i, j, shape)
                    shapes.add(tuple(shape))

        return len(shapes)
```

## 695. 岛屿的最大面积 (`max-area-of-island`)

- 题目链接：https://leetcode.cn/problems/max-area-of-island/
- 难度：Medium
- 标签：Depth-First Search, Breadth-First Search, Union Find, Array, Matrix
- 总提交次数：4
- 最近提交时间：2026/04/10 12:12:54 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 716844059 | 2026/04/10 12:12:54 CST | python | Accepted | 16 ms | 20.4 MB |
| 716843618 | 2026/04/10 12:10:28 CST | python | Time Limit Exceeded | N/A | N/A |
| 716843599 | 2026/04/10 12:10:22 CST | python | Runtime Error | N/A | N/A |
| 687593768 | 2025/12/28 09:54:33 CST | python | Accepted | 8 ms | 17.7 MB |

### 最近一次 AC 代码

```python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(r, c):
            if not (0 <= r < m and 0 <= c < n):
                return 0
            if grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1) + 1
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        
        return res
```

## 700. 二叉搜索树中的搜索 (`search-in-a-binary-search-tree`)

- 题目链接：https://leetcode.cn/problems/search-in-a-binary-search-tree/
- 难度：Easy
- 标签：Tree, Binary Search Tree, Binary Tree
- 总提交次数：2
- 最近提交时间：2026/04/03 14:03:10 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 714828162 | 2026/04/03 14:03:10 CST | python | Accepted | 0 ms | 20.9 MB |
| 714828005 | 2026/04/03 14:02:32 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root
        while curr:
            if curr.val == val:
                return curr
            elif val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return None
```

## 701. 二叉搜索树中的插入操作 (`insert-into-a-binary-search-tree`)

- 题目链接：https://leetcode.cn/problems/insert-into-a-binary-search-tree/
- 难度：Medium
- 标签：Tree, Binary Search Tree, Binary Tree
- 总提交次数：2
- 最近提交时间：2026/04/04 10:45:23 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715022442 | 2026/04/04 10:45:23 CST | python | Accepted | 3 ms | 21 MB |
| 714829912 | 2026/04/03 14:09:47 CST | python | Accepted | 0 ms | 21 MB |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        curr = root
        while curr:
            if val < curr.val:
                if not curr.left:
                    curr.left = TreeNode(val)
                    return root
                curr = curr.left
            else:
                if not curr.right:
                    curr.right = TreeNode(val)
                    return root
                curr = curr.right
```

## 703. 数据流中的第 K 大元素 (`kth-largest-element-in-a-stream`)

- 题目链接：https://leetcode.cn/problems/kth-largest-element-in-a-stream/
- 难度：Easy
- 标签：Tree, Design, Binary Search Tree, Binary Tree, Data Stream, Heap (Priority Queue)
- 总提交次数：2
- 最近提交时间：2026/04/04 17:25:54 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715115696 | 2026/04/04 17:25:54 CST | python | Accepted | 15 ms | 25.1 MB |
| 715115635 | 2026/04/04 17:25:42 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        for num in nums:
            heapq.heappush(self.min_heap, num)
            if len(self.min_heap) > k:
                heapq.heappop(self.min_heap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
```

## 704. 二分查找 (`binary-search`)

- 题目链接：https://leetcode.cn/problems/binary-search/
- 难度：Easy
- 标签：Array, Binary Search
- 总提交次数：2
- 最近提交时间：2026/03/03 13:36:42 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 702136125 | 2026/03/03 13:36:42 CST | python | Accepted | 11 ms | 20.3 MB |
| 666185368 | 2025/09/26 14:27:06 CST | python | Accepted | 0 ms | 18.5 MB |

### 最近一次 AC 代码

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left += 1
            elif nums[mid] > target:
                right -= 1
            else:
                return mid
        return -1
```

## 708. 循环有序列表的插入 (`insert-into-a-sorted-circular-linked-list`)

- 题目链接：https://leetcode.cn/problems/insert-into-a-sorted-circular-linked-list/
- 难度：Medium
- 标签：Linked List
- 总提交次数：2
- 最近提交时间：2026/03/11 16:20:40 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 705655711 | 2026/03/11 16:20:40 CST | python | Accepted | 52 ms | 20.1 MB |
| 705653963 | 2026/03/11 16:18:15 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            new_node = Node(insertVal)
            new_node.next = new_node
            return new_node
        
        curr = head
        while True:
            next_node = curr.next
            if curr.val <= insertVal <= next_node.val:
                break
            if curr.val > next_node.val:
                if curr.val <= insertVal or insertVal <= next_node.val:
                    break
            curr = next_node
            if curr == head:
                break
        new_node = Node(insertVal, curr.next)
        curr.next = new_node
        return head
```

## 712. 两个字符串的最小ASCII删除和 (`minimum-ascii-delete-sum-for-two-strings`)

- 题目链接：https://leetcode.cn/problems/minimum-ascii-delete-sum-for-two-strings/
- 难度：Medium
- 标签：String, Dynamic Programming
- 总提交次数：9
- 最近提交时间：2026/04/13 12:31:14 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 717652333 | 2026/04/13 12:31:14 CST | python | Accepted | 315 ms | 23.5 MB |
| 697942690 | 2026/02/11 13:59:37 CST | python | Accepted | 275 ms | 23.6 MB |
| 692434801 | 2026/01/19 15:24:47 CST | python | Accepted | 305 ms | 23.4 MB |
| 692434236 | 2026/01/19 15:23:22 CST | python | Wrong Answer | N/A | N/A |
| 690706247 | 2026/01/12 10:41:32 CST | python | Accepted | 267 ms | 23.3 MB |
| 690705580 | 2026/01/12 10:39:03 CST | python | Wrong Answer | N/A | N/A |
| 688519000 | 2026/01/02 10:03:57 CST | python | Accepted | 439 ms | 21.1 MB |
| 688518924 | 2026/01/02 10:03:06 CST | python | Wrong Answer | N/A | N/A |
| 688518909 | 2026/01/02 10:02:54 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    del_s1 = dp[i - 1][j] + ord(s1[i - 1])
                    del_s2 = dp[i][j - 1] + ord(s2[j - 1])
                    dp[i][j] = min(del_s1, del_s2)
        return dp[m][n]
```

## 713. 乘积小于 K 的子数组 (`subarray-product-less-than-k`)

- 题目链接：https://leetcode.cn/problems/subarray-product-less-than-k/
- 难度：Medium
- 标签：Array, Binary Search, Prefix Sum, Sliding Window
- 总提交次数：18
- 最近提交时间：2026/03/23 14:24:49 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 710879856 | 2026/03/23 14:24:49 CST | python | Accepted | 34 ms | 22.1 MB |
| 710879763 | 2026/03/23 14:24:37 CST | python | Runtime Error | N/A | N/A |
| 708673516 | 2026/03/18 11:04:07 CST | python | Accepted | 51 ms | 21.9 MB |
| 703486718 | 2026/03/06 16:38:04 CST | python | Accepted | 79 ms | 21.7 MB |
| 703485927 | 2026/03/06 16:36:35 CST | python | Accepted | 80 ms | 21.9 MB |
| 703485594 | 2026/03/06 16:35:56 CST | python | Runtime Error | N/A | N/A |
| 703485439 | 2026/03/06 16:35:39 CST | python | Runtime Error | N/A | N/A |
| 663319518 | 2025/09/16 18:46:00 CST | python | Accepted | 83 ms | 19.5 MB |
| 663319434 | 2025/09/16 18:45:40 CST | python | Runtime Error | N/A | N/A |
| 663318591 | 2025/09/16 18:41:49 CST | python | Runtime Error | N/A | N/A |
| 660987884 | 2025/09/09 14:48:15 CST | python | Accepted | 67 ms | 19.5 MB |
| 660985429 | 2025/09/09 14:42:38 CST | python | Runtime Error | N/A | N/A |
| 660981830 | 2025/09/09 14:34:11 CST | python | Wrong Answer | N/A | N/A |
| 660978517 | 2025/09/09 14:26:06 CST | python | Wrong Answer | N/A | N/A |
| 652483240 | 2025/08/13 09:16:20 CST | python | Accepted | 67 ms | 19.5 MB |
| 652483130 | 2025/08/13 09:15:56 CST | python | Runtime Error | N/A | N/A |
| 652474201 | 2025/08/13 07:57:21 CST | python | Wrong Answer | N/A | N/A |
| 652474128 | 2025/08/13 07:55:14 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        count = 0
        left = 0
        product = 1
        for right, r_num in enumerate(nums):
            product *= r_num
            while product >= k:
                product //= nums[left]
                left += 1
            count += (right - left + 1)
        return count
```

## 718. 最长重复子数组 (`maximum-length-of-repeated-subarray`)

- 题目链接：https://leetcode.cn/problems/maximum-length-of-repeated-subarray/
- 难度：Medium
- 标签：Array, Binary Search, Dynamic Programming, Sliding Window, Hash Function, Rolling Hash
- 总提交次数：12
- 最近提交时间：2026/03/04 13:03:14 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 702519577 | 2026/03/04 13:03:14 CST | python | Accepted | 1317 ms | 43.4 MB |
| 702519446 | 2026/03/04 13:02:45 CST | python | Wrong Answer | N/A | N/A |
| 702519415 | 2026/03/04 13:02:38 CST | python | Runtime Error | N/A | N/A |
| 702519198 | 2026/03/04 13:01:43 CST | python | Wrong Answer | N/A | N/A |
| 697944427 | 2026/02/11 14:08:07 CST | python | Accepted | 1307 ms | 43.5 MB |
| 697944355 | 2026/02/11 14:07:50 CST | python | Runtime Error | N/A | N/A |
| 697241592 | 2026/02/08 11:50:17 CST | python | Accepted | 1326 ms | 43.7 MB |
| 696051593 | 2026/02/03 10:34:47 CST | python | Accepted | 1431 ms | 43.5 MB |
| 696051514 | 2026/02/03 10:34:33 CST | python | Wrong Answer | N/A | N/A |
| 696051059 | 2026/02/03 10:33:02 CST | python | Wrong Answer | N/A | N/A |
| 695799752 | 2026/02/02 11:08:16 CST | python | Accepted | 1477 ms | 43.6 MB |
| 695649487 | 2026/02/01 16:30:21 CST | python | Accepted | 1422 ms | 43.5 MB |

### 最近一次 AC 代码

```python
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_len = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    max_len = max(max_len, dp[i][j])
                else:
                    dp[i][j] = 0
        return max_len
```

## 721. 账户合并 (`accounts-merge`)

- 题目链接：https://leetcode.cn/problems/accounts-merge/
- 难度：Medium
- 标签：Depth-First Search, Breadth-First Search, Union Find, Array, Hash Table, String, Sorting
- 总提交次数：5
- 最近提交时间：2026/03/09 10:53:56 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 704524163 | 2026/03/09 10:53:56 CST | python | Accepted | 27 ms | 22.6 MB |
| 704523968 | 2026/03/09 10:53:34 CST | python | Runtime Error | N/A | N/A |
| 686800092 | 2025/12/24 11:15:34 CST | python | Accepted | 31 ms | 20.3 MB |
| 686799996 | 2025/12/24 11:15:17 CST | python | Runtime Error | N/A | N/A |
| 686799647 | 2025/12/24 11:14:00 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj_list = collections.defaultdict(list)
        emails_to_name = {}
        for account in accounts:
            name = account[0]
            emails = account[1:]
            if not emails:
                continue
            first_email = emails[0]
            emails_to_name[first_email] = name
            for email in emails[1:]:
                 adj_list[email].append(first_email)
                 adj_list[first_email].append(email)
                 emails_to_name[email] = name
        
        res = []
        visited = set()
        for email in emails_to_name:
            if not email in visited:
                dq = collections.deque([email])
                visited.add(email)
                emails_in_group = []
                while dq:
                    e = dq.popleft()
                    emails_in_group.append(e)
                    for neighbor in adj_list[e]:
                        if neighbor not in visited:
                            dq.append(neighbor)
                            visited.add(neighbor)
                emails_in_group.sort()
                name = emails_to_name[email]
                res.append([name] + emails_in_group)

        return res
```

## 723. 粉碎糖果 (`candy-crush`)

- 题目链接：https://leetcode.cn/problems/candy-crush/
- 难度：Medium
- 标签：Array, Two Pointers, Matrix, Simulation
- 总提交次数：2
- 最近提交时间：2026/03/10 18:25:04 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 705234834 | 2026/03/10 18:25:04 CST | python | Accepted | 38 ms | 19.4 MB |
| 705234589 | 2026/03/10 18:24:25 CST | python | Time Limit Exceeded | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        rows, cols = len(board), len(board[0])
        while True:
            crushed = False
            for i in range(rows):
                for j in range(cols - 2):
                    value = abs(board[i][j])
                    if (
                        value != 0
                        and value == abs(board[i][j + 1])
                        and value == abs(board[i][j + 2])
                    ):
                        board[i][j] = -value
                        board[i][j + 1] = -value
                        board[i][j + 2] = -value
                        crushed = True
            for i in range(rows - 2):
                for j in range(cols):
                    value = abs(board[i][j])
                    if (
                        value != 0
                        and value == abs(board[i + 1][j])
                        and value == abs(board[i + 2][j])
                    ):
                        board[i][j] = -value
                        board[i + 1][j] = -value
                        board[i + 2][j] = -value
                        crushed = True
            if not crushed:
                return board

            for j in range(cols):
                write_row = rows - 1
                for i in range(rows - 1, -1, -1):
                    if board[i][j] > 0:
                        board[write_row][j] = board[i][j]
                        write_row -= 1
                for i in range(write_row, -1, -1):
                    board[i][j] = 0
```

## 724. 寻找数组的中心下标 (`find-pivot-index`)

- 题目链接：https://leetcode.cn/problems/find-pivot-index/
- 难度：Easy
- 标签：Array, Prefix Sum
- 总提交次数：5
- 最近提交时间：2026/03/17 08:25:10 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 708126504 | 2026/03/17 08:25:10 CST | python | Accepted | 16 ms | 19.9 MB |
| 707671447 | 2026/03/16 10:08:56 CST | python | Accepted | 16 ms | 20 MB |
| 661717474 | 2025/09/11 15:53:00 CST | python | Accepted | 3 ms | 18.3 MB |
| 661692568 | 2025/09/11 15:00:04 CST | python | Accepted | 11 ms | 18.3 MB |
| 661683743 | 2025/09/11 14:41:04 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        pre_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]
        for i in range(n):
            left_sum = pre_sum[i] - pre_sum[0]  # nums[0..i-1]的和
            right_sum = pre_sum[n] - pre_sum[i+1]  # nums[i+1..n-1]的和
            if left_sum == right_sum:
                return i
        return -1
```

## 729. 我的日程安排表 I (`my-calendar-i`)

- 题目链接：https://leetcode.cn/problems/my-calendar-i/
- 难度：Medium
- 标签：Design, Segment Tree, Array, Binary Search, Ordered Set
- 总提交次数：11
- 最近提交时间：2026/03/30 08:28:27 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 713356827 | 2026/03/30 08:28:27 CST | python | Accepted | 24 ms | 20.1 MB |
| 713248196 | 2026/03/29 19:40:21 CST | python | Accepted | 23 ms | 20.2 MB |
| 713248035 | 2026/03/29 19:39:51 CST | python | Wrong Answer | N/A | N/A |
| 713247981 | 2026/03/29 19:39:40 CST | python | Runtime Error | N/A | N/A |
| 713247755 | 2026/03/29 19:38:54 CST | python | Runtime Error | N/A | N/A |
| 713247719 | 2026/03/29 19:38:48 CST | python | Runtime Error | N/A | N/A |
| 713247681 | 2026/03/29 19:38:40 CST | python | Runtime Error | N/A | N/A |
| 703447941 | 2026/03/06 15:34:57 CST | python | Accepted | 31 ms | 20 MB |
| 703447814 | 2026/03/06 15:34:43 CST | python | Runtime Error | N/A | N/A |
| 703447646 | 2026/03/06 15:34:27 CST | python | Runtime Error | N/A | N/A |
| 680972490 | 2025/11/27 08:10:44 CST | python | Accepted | 24 ms | 18.6 MB |

### 最近一次 AC 代码

```python
class MyCalendar:

    def __init__(self):
        self.calendar = []
        

    def book(self, startTime: int, endTime: int) -> bool:
        idx = bisect.bisect_left(self.calendar, (startTime, endTime))
        if idx > 0:
            pre_start, pre_end = self.calendar[idx - 1]
            if startTime < pre_end:
                return False
        if idx < len(self.calendar):
            next_start, next_end = self.calendar[idx]
            if endTime > next_start:
                return False
        self.calendar.insert(idx, (startTime, endTime))
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)
```

## 734. 句子相似性 (`sentence-similarity`)

- 题目链接：https://leetcode.cn/problems/sentence-similarity/
- 难度：Easy
- 标签：Array, Hash Table, String
- 总提交次数：1
- 最近提交时间：2024/09/03 14:58:41 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 561073224 | 2024/09/03 14:58:41 CST | python | Accepted | 38 ms | 16.4 MB |

### 最近一次 AC 代码

```python
class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        similar_set = set()
        for x, y in similarPairs:
            similar_set.add((x, y))
            similar_set.add((y, x))
        for x, y in zip(sentence1, sentence2):
            if len(x) != len(y) and (x, y) not in similar_set:
                return False
        return True
```

## 739. 每日温度 (`daily-temperatures`)

- 题目链接：https://leetcode.cn/problems/daily-temperatures/
- 难度：Medium
- 标签：Stack, Array, Monotonic Stack
- 总提交次数：8
- 最近提交时间：2026/03/26 08:49:52 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 712064433 | 2026/03/26 08:49:52 CST | python | Accepted | 111 ms | 27.5 MB |
| 711683535 | 2026/03/25 10:25:03 CST | python | Accepted | 88 ms | 28.3 MB |
| 711682841 | 2026/03/25 10:23:28 CST | python | Runtime Error | N/A | N/A |
| 711682748 | 2026/03/25 10:23:16 CST | python | Runtime Error | N/A | N/A |
| 678225302 | 2025/11/15 11:31:56 CST | python | Accepted | 95 ms | 26 MB |
| 678225268 | 2025/11/15 11:31:43 CST | python | Runtime Error | N/A | N/A |
| 678036799 | 2025/11/14 11:04:23 CST | python | Accepted | 91 ms | 26.4 MB |
| 678036389 | 2025/11/14 11:02:50 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []
        for i, num in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < num:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return res
```

## 740. 删除并获得点数 (`delete-and-earn`)

- 题目链接：https://leetcode.cn/problems/delete-and-earn/
- 难度：Medium
- 标签：Array, Hash Table, Dynamic Programming
- 总提交次数：8
- 最近提交时间：2026/02/11 08:25:49 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 697883660 | 2026/02/11 08:25:49 CST | python | Accepted | 7 ms | 20.5 MB |
| 697681323 | 2026/02/10 11:17:06 CST | python | Accepted | 0 ms | 20.4 MB |
| 695370931 | 2026/01/31 11:12:28 CST | python | Accepted | 0 ms | 20.2 MB |
| 695370693 | 2026/01/31 11:11:12 CST | python | Wrong Answer | N/A | N/A |
| 694938002 | 2026/01/29 14:12:09 CST | python | Accepted | 2 ms | 20.4 MB |
| 694607367 | 2026/01/28 09:30:01 CST | python | Accepted | 3 ms | 20.3 MB |
| 694426081 | 2026/01/27 15:05:00 CST | python | Accepted | 3 ms | 20.2 MB |
| 692923056 | 2026/01/21 11:28:32 CST | python | Accepted | 3 ms | 20.2 MB |

### 最近一次 AC 代码

```python
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        max_num = max(nums)
        points = [0] * (max_num + 1)
        for num in nums:
            points[num] += num
        prev_2, prev_1 = points[0], points[1]
        for point in points[2:]:
            curr = max(prev_1, prev_2 + point)
            prev_2, prev_1 = prev_1, curr
        return prev_1
```

## 743. 网络延迟时间 (`network-delay-time`)

- 题目链接：https://leetcode.cn/problems/network-delay-time/
- 难度：Medium
- 标签：Depth-First Search, Breadth-First Search, Graph, Shortest Path, Heap (Priority Queue)
- 总提交次数：1
- 最近提交时间：2026/04/06 11:25:21 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715536866 | 2026/04/06 11:25:21 CST | python | Accepted | 354 ms | 21 MB |

### 最近一次 AC 代码

```python
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        dist = [float('inf')] *  (n + 1)
        dist[k] = 0
        min_heap = [(0, k)]
        while min_heap:
            curr_dist, u = heapq.heappop(min_heap)
            for v, w in graph[u]:
                new_dist = curr_dist + w
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(min_heap, (new_dist, v))
        max_dist = max(dist[1:])
        return max_dist if max_dist != float('inf') else -1
```

## 752. 打开转盘锁 (`open-the-lock`)

- 题目链接：https://leetcode.cn/problems/open-the-lock/
- 难度：Medium
- 标签：Breadth-First Search, Array, Hash Table, String
- 总提交次数：9
- 最近提交时间：2026/04/05 19:06:43 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715381782 | 2026/04/05 19:06:43 CST | python | Accepted | 419 ms | 20.1 MB |
| 686551236 | 2025/12/23 10:22:13 CST | python | Accepted | 411 ms | 18.6 MB |
| 686550920 | 2025/12/23 10:20:59 CST | python | Wrong Answer | N/A | N/A |
| 686549776 | 2025/12/23 10:16:24 CST | python | Wrong Answer | N/A | N/A |
| 686549723 | 2025/12/23 10:16:08 CST | python | Runtime Error | N/A | N/A |
| 686315108 | 2025/12/22 10:53:55 CST | python | Accepted | 399 ms | 18.8 MB |
| 686315012 | 2025/12/22 10:53:33 CST | python | Wrong Answer | N/A | N/A |
| 686204735 | 2025/12/21 17:34:34 CST | python | Accepted | 325 ms | 18.3 MB |
| 686204424 | 2025/12/21 17:33:02 CST | python | Memory Limit Exceeded | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        start = '0000'
        deadends_set = set(deadends)
        if start in deadends_set:
            return -1
        if start == target:
            return 0
        dq = collections.deque([(start, 0)])
        visited = {start}
        while dq:
            curr_state, steps = dq.popleft()
            if curr_state == target:
                return steps
            for idx in range(4):
                digit = int(curr_state[idx])
                for move in [1, -1]:
                    new_digit = (digit + move + 10) % 10
                    new_state = curr_state[:idx] + str(new_digit) + curr_state[idx+1:]
                    if new_state in deadends_set:
                        continue
                    if new_state not in visited:
                        visited.add(new_state)
                        dq.append((new_state, steps + 1))
        return -1
```

## 760. 找出变位映射 (`find-anagram-mappings`)

- 题目链接：https://leetcode.cn/problems/find-anagram-mappings/
- 难度：Easy
- 标签：Array, Hash Table
- 总提交次数：1
- 最近提交时间：2024/09/01 15:08:24 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 560397298 | 2024/09/01 15:08:24 CST | python | Accepted | 38 ms | 16.3 MB |

### 最近一次 AC 代码

```python
class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        index_map = {num: i for i, num in enumerate(nums2)}
        ret = [index_map[num] for num in nums1]
        return ret
```

## 772. 基本计算器 III (`basic-calculator-iii`)

- 题目链接：https://leetcode.cn/problems/basic-calculator-iii/
- 难度：Hard
- 标签：Stack, Recursion, Math, String
- 总提交次数：6
- 最近提交时间：2026/03/31 09:52:45 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 713735662 | 2026/03/31 09:52:45 CST | python | Accepted | 7 ms | 19.1 MB |
| 713383359 | 2026/03/30 10:30:48 CST | python | Accepted | 4 ms | 19.4 MB |
| 713382201 | 2026/03/30 10:27:48 CST | python | Wrong Answer | N/A | N/A |
| 713382136 | 2026/03/30 10:27:39 CST | python | Runtime Error | N/A | N/A |
| 705597677 | 2026/03/11 14:57:58 CST | python | Accepted | 3 ms | 19.2 MB |
| 705596963 | 2026/03/11 14:56:52 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def calculate(self, s: str) -> int:
        def dfs(i):
            num = 0
            stack = []
            sign = '+'
            while i < len(s):
                ch  = s[i]
                if ch.isdigit():
                    num = num * 10 + int(ch)
                elif ch == '(':
                    num, i = dfs(i + 1)
                if (not ch.isdigit() and ch != ' ') or i == len(s) - 1:
                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)
                    elif sign == '*':
                        stack.append(stack.pop() * num)
                    elif sign == '/':
                        stack.append(int(stack.pop() / num))
                    num = 0
                    if ch == ')':
                        return sum(stack), i
                    sign = ch
                i += 1
            return sum(stack), i
        return dfs(0)[0]
```

## 773. 滑动谜题 (`sliding-puzzle`)

- 题目链接：https://leetcode.cn/problems/sliding-puzzle/
- 难度：Hard
- 标签：Breadth-First Search, Memoization, Array, Dynamic Programming, Backtracking, Matrix
- 总提交次数：14
- 最近提交时间：2026/04/05 17:32:07 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715359514 | 2026/04/05 17:32:07 CST | python | Accepted | 3 ms | 19.3 MB |
| 715359354 | 2026/04/05 17:31:34 CST | python | Memory Limit Exceeded | N/A | N/A |
| 715358911 | 2026/04/05 17:30:07 CST | python | Runtime Error | N/A | N/A |
| 715358854 | 2026/04/05 17:29:57 CST | python | Runtime Error | N/A | N/A |
| 715358811 | 2026/04/05 17:29:49 CST | python | Runtime Error | N/A | N/A |
| 715358687 | 2026/04/05 17:29:24 CST | python | Runtime Error | N/A | N/A |
| 686547819 | 2025/12/23 10:06:50 CST | python | Accepted | 9 ms | 17.1 MB |
| 686547769 | 2025/12/23 10:06:34 CST | python | Runtime Error | N/A | N/A |
| 686312214 | 2025/12/22 10:42:30 CST | python | Accepted | 7 ms | 17.2 MB |
| 686311770 | 2025/12/22 10:40:48 CST | python | Wrong Answer | N/A | N/A |
| 686145771 | 2025/12/21 12:54:52 CST | python | Accepted | 7 ms | 17.1 MB |
| 686145136 | 2025/12/21 12:49:46 CST | python | Accepted | 7 ms | 17.4 MB |
| 686144982 | 2025/12/21 12:48:22 CST | python | Wrong Answer | N/A | N/A |
| 686144820 | 2025/12/21 12:47:13 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = ''.join(str(num) for row in board for num in row)
        target = '123450'
        dq = collections.deque([(start, 0)])
        visited = {start}
        # 0 1 2
        # 3 4 5
        neighbors = [
            [1, 3],
            [0, 2, 4],
            [1, 5],
            [0, 4],
            [1, 3, 5],
            [2, 4]
        ]
        while dq:
            curr_state, steps = dq.popleft()
            if curr_state == target:
                return steps
            zero_idx = curr_state.index('0')
            for neighbor in neighbors[zero_idx]:
                state_list = list(curr_state)
                state_list[neighbor], state_list[zero_idx] = state_list[zero_idx], state_list[neighbor]
                new_state = ''.join(state_list)
                if new_state not in visited:
                    visited.add(new_state)
                    dq.append((new_state, steps + 1))
        return -1
```

## 785. 判断二分图 (`is-graph-bipartite`)

- 题目链接：https://leetcode.cn/problems/is-graph-bipartite/
- 难度：Medium
- 标签：Depth-First Search, Breadth-First Search, Union Find, Graph
- 总提交次数：3
- 最近提交时间：2026/04/05 09:41:07 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715233225 | 2026/04/05 09:41:07 CST | python | Accepted | 0 ms | 19.7 MB |
| 715232996 | 2026/04/05 09:39:04 CST | python | Wrong Answer | N/A | N/A |
| 715232945 | 2026/04/05 09:38:40 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [0] * n
        for start in range(n):
            if colors[start] != 0:
                continue
            dq = collections.deque([start])
            colors[start] = 1
            while dq:
                node = dq.popleft()
                for neighbor in graph[node]:
                    if colors[neighbor] == 0:
                        colors[neighbor] = -colors[node]
                        dq.append(neighbor)
                    elif colors[node] == colors[neighbor]:
                        return False
        return True
```

## 787. K 站中转内最便宜的航班 (`cheapest-flights-within-k-stops`)

- 题目链接：https://leetcode.cn/problems/cheapest-flights-within-k-stops/
- 难度：Medium
- 标签：Depth-First Search, Breadth-First Search, Graph, Dynamic Programming, Shortest Path, Heap (Priority Queue)
- 总提交次数：1
- 最近提交时间：2026/04/06 16:16:41 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715619843 | 2026/04/06 16:16:41 CST | python | Accepted | 19 ms | 20.7 MB |

### 最近一次 AC 代码

```python
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, price in flights:
            graph[u].append((v, price))
        max_edges = k + 1
        best = [[float('inf')] * (max_edges + 1) for _ in range(n)]
        best[src][0] = 0
        min_heap = [(0, src, 0)]
        while min_heap:
            cost, city, steps = heapq.heappop(min_heap)
            if cost > best[city][steps]:
                continue
            if city == dst:
                return cost
            if steps == max_edges:
                continue
            for neighbor, price in graph[city]:
                new_cost = cost + price
                new_steps = steps + 1
                if new_cost < best[neighbor][new_steps]:
                    best[neighbor][new_steps] = new_cost
                    heapq.heappush(min_heap, (new_cost, neighbor, new_steps))
        return -1
```

## 792. 匹配子序列的单词数 (`number-of-matching-subsequences`)

- 题目链接：https://leetcode.cn/problems/number-of-matching-subsequences/
- 难度：Medium
- 标签：Trie, Array, Hash Table, String, Binary Search, Dynamic Programming, Sorting
- 总提交次数：14
- 最近提交时间：2026/03/24 10:13:38 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 711241204 | 2026/03/24 10:13:38 CST | python | Accepted | 283 ms | 23 MB |
| 709236410 | 2026/03/19 14:28:23 CST | python | Accepted | 271 ms | 22.7 MB |
| 702948183 | 2026/03/05 13:11:17 CST | python | Accepted | 266 ms | 22.9 MB |
| 702947877 | 2026/03/05 13:10:07 CST | python | Runtime Error | N/A | N/A |
| 702947734 | 2026/03/05 13:09:36 CST | python | Accepted | 277 ms | 22.5 MB |
| 702946680 | 2026/03/05 13:05:37 CST | python | Runtime Error | N/A | N/A |
| 702946391 | 2026/03/05 13:04:31 CST | python | Runtime Error | N/A | N/A |
| 702946101 | 2026/03/05 13:03:28 CST | python | Wrong Answer | N/A | N/A |
| 702946003 | 2026/03/05 13:03:07 CST | python | Runtime Error | N/A | N/A |
| 702920691 | 2026/03/05 11:36:38 CST | python | Accepted | 231 ms | 20.6 MB |
| 685808226 | 2025/12/19 14:49:01 CST | python | Accepted | 243 ms | 19.1 MB |
| 685534452 | 2025/12/18 10:06:50 CST | python | Accepted | 231 ms | 18.7 MB |
| 685352240 | 2025/12/17 13:57:39 CST | python | Accepted | 243 ms | 19.4 MB |
| 682358570 | 2025/12/03 12:41:07 CST | python | Accepted | 255 ms | 19.2 MB |

### 最近一次 AC 代码

```python
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        positions_map = collections.defaultdict(list)
        for i, ch in enumerate(s):
            positions_map[ch].append(i)
        count = 0
        for word in words:
            is_sub = True
            match_index = -1
            for ch in word:
                positions = positions_map[ch]
                idx = bisect.bisect_right(positions, match_index)
                if idx < len(positions):
                    match_index = positions[idx]
                else:
                    is_sub = False
                    break
            if is_sub:
                count += 1
        return count
```

## 841. 钥匙和房间 (`keys-and-rooms`)

- 题目链接：https://leetcode.cn/problems/keys-and-rooms/
- 难度：Medium
- 标签：Depth-First Search, Breadth-First Search, Graph
- 总提交次数：6
- 最近提交时间：2026/04/05 21:21:39 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715415929 | 2026/04/05 21:21:39 CST | python | Accepted | 3 ms | 19.4 MB |
| 686563496 | 2025/12/23 11:05:49 CST | python | Accepted | 0 ms | 17.4 MB |
| 686363780 | 2025/12/22 14:48:09 CST | python | Accepted | 0 ms | 17.5 MB |
| 686363724 | 2025/12/22 14:47:57 CST | python | Runtime Error | N/A | N/A |
| 686363209 | 2025/12/22 14:46:08 CST | python | Runtime Error | N/A | N/A |
| 686362722 | 2025/12/22 14:44:20 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        dq = collections.deque([0])
        visited[0] = True
        while dq:
            room = dq.popleft()
            for next_room in rooms[room]:
                if not visited[next_room]:
                    visited[next_room] = True
                    dq.append(next_room)
        for v in visited:
            if not v:
                return False
        return True
```

## 852. 山脉数组的峰顶索引 (`peak-index-in-a-mountain-array`)

- 题目链接：https://leetcode.cn/problems/peak-index-in-a-mountain-array/
- 难度：Medium
- 标签：Array, Binary Search
- 总提交次数：1
- 最近提交时间：2026/03/20 16:45:51 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 709772505 | 2026/03/20 16:45:51 CST | python | Accepted | 0 ms | 31.1 MB |

### 最近一次 AC 代码

```python
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] > arr[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left
```

## 853. 车队 (`car-fleet`)

- 题目链接：https://leetcode.cn/problems/car-fleet/
- 难度：Medium
- 标签：Stack, Array, Sorting, Monotonic Stack
- 总提交次数：4
- 最近提交时间：2026/03/28 09:27:41 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 712757065 | 2026/03/28 09:27:41 CST | python | Accepted | 151 ms | 40.9 MB |
| 712757039 | 2026/03/28 09:27:26 CST | python | Runtime Error | N/A | N/A |
| 712454796 | 2026/03/27 10:11:37 CST | python | Accepted | 147 ms | 40.9 MB |
| 712454391 | 2026/03/27 10:10:27 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        count = 0
        last_time = 0.0
        for pos, spd in cars:
            time = (target - pos) / spd
            if time > last_time:
                count += 1
                last_time = time
        return count
```

## 863. 二叉树中所有距离为 K 的结点 (`all-nodes-distance-k-in-binary-tree`)

- 题目链接：https://leetcode.cn/problems/all-nodes-distance-k-in-binary-tree/
- 难度：Medium
- 标签：Tree, Depth-First Search, Breadth-First Search, Hash Table, Binary Tree
- 总提交次数：9
- 最近提交时间：2026/04/05 19:58:04 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715392794 | 2026/04/05 19:58:04 CST | python | Accepted | 66 ms | 19.6 MB |
| 715392648 | 2026/04/05 19:57:28 CST | python | Runtime Error | N/A | N/A |
| 702065960 | 2026/03/03 10:19:22 CST | python | Accepted | 47 ms | 19.5 MB |
| 702065840 | 2026/03/03 10:19:06 CST | python | Runtime Error | N/A | N/A |
| 702065643 | 2026/03/03 10:18:37 CST | python | Runtime Error | N/A | N/A |
| 686556267 | 2025/12/23 10:41:25 CST | python | Accepted | 43 ms | 17.4 MB |
| 686556222 | 2025/12/23 10:41:15 CST | python | Runtime Error | N/A | N/A |
| 686337845 | 2025/12/22 12:46:36 CST | python | Accepted | 44 ms | 17.4 MB |
| 686337806 | 2025/12/22 12:46:19 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not root:
            return []
        stack = [(root, None)]
        adj_list = collections.defaultdict(list)
        while stack:
            node, parent = stack.pop()
            if parent:
                adj_list[parent].append(node)
                adj_list[node].append(parent)
            if node.left:
                stack.append((node.left, node))
            if node.right:
                stack.append((node.right, node))

        dq = collections.deque([(target, 0)])
        res = []
        visited = {target}
        while dq:
            node, dist = dq.popleft()
            if dist == k:
                res.append(node.val)
            if dist > k:
                break
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dq.append((neighbor, dist + 1))
        return res
```

## 867. 转置矩阵 (`transpose-matrix`)

- 题目链接：https://leetcode.cn/problems/transpose-matrix/
- 难度：Easy
- 标签：Array, Matrix, Simulation
- 总提交次数：1
- 最近提交时间：2026/03/17 16:46:56 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 708360129 | 2026/03/17 16:46:56 CST | python | Accepted | 0 ms | 19.7 MB |

### 最近一次 AC 代码

```python
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        res = [[0] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                res[j][i] = matrix[i][j]
        return res
```

## 873. 最长的斐波那契子序列的长度 (`length-of-longest-fibonacci-subsequence`)

- 题目链接：https://leetcode.cn/problems/length-of-longest-fibonacci-subsequence/
- 难度：Medium
- 标签：Array, Hash Table, Dynamic Programming
- 总提交次数：3
- 最近提交时间：2026/02/14 10:37:49 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 698540211 | 2026/02/14 10:37:49 CST | python | Accepted | 697 ms | 26.6 MB |
| 697913815 | 2026/02/11 11:23:01 CST | python | Accepted | 791 ms | 26.7 MB |
| 697905714 | 2026/02/11 10:52:53 CST | python | Accepted | 759 ms | 26.7 MB |

### 最近一次 AC 代码

```python
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[2] * n for _ in range(n)]
        val_to_idx = {v : i for i, v in enumerate(arr)}
        res = 0
        for i in range(2, n):
            for j in range(i):
                target = arr[i] - arr[j]
                if target < arr[j] and target in val_to_idx:
                    k = val_to_idx[target]
                    dp[i][j] = dp[j][k] + 1
                    res = max(res, dp[i][j])
        return res
```

## 875. 爱吃香蕉的珂珂 (`koko-eating-bananas`)

- 题目链接：https://leetcode.cn/problems/koko-eating-bananas/
- 难度：Medium
- 标签：Array, Binary Search
- 总提交次数：9
- 最近提交时间：2026/03/24 09:01:33 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 711218410 | 2026/03/24 09:01:33 CST | python | Accepted | 151 ms | 20.6 MB |
| 709713503 | 2026/03/20 15:09:50 CST | python | Accepted | 295 ms | 20.6 MB |
| 709713413 | 2026/03/20 15:09:42 CST | python | Accepted | 295 ms | 20.4 MB |
| 709652515 | 2026/03/20 12:26:17 CST | python | Accepted | 299 ms | 20.4 MB |
| 709136661 | 2026/03/19 10:30:54 CST | python | Accepted | 303 ms | 20.4 MB |
| 702433908 | 2026/03/04 08:41:05 CST | python | Accepted | 147 ms | 20.6 MB |
| 677070601 | 2025/11/10 14:18:31 CST | python | Accepted | 147 ms | 18.8 MB |
| 676899501 | 2025/11/09 17:13:42 CST | python | Accepted | 139 ms | 19 MB |
| 666681185 | 2025/09/28 14:56:32 CST | python | Accepted | 178 ms | 19 MB |

### 最近一次 AC 代码

```python
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(speed):
            time_cost = 0
            for pile in piles:
                time_cost += ceil(pile / speed)
            return time_cost <= h
        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if can_finish(mid):
                right = mid
            else:
                left = mid + 1
        return left
```

## 876. 链表的中间结点 (`middle-of-the-linked-list`)

- 题目链接：https://leetcode.cn/problems/middle-of-the-linked-list/
- 难度：Easy
- 标签：Linked List, Two Pointers
- 总提交次数：4
- 最近提交时间：2026/03/31 11:08:13 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 713766186 | 2026/03/31 11:08:13 CST | python | Accepted | 0 ms | 19 MB |
| 713765511 | 2026/03/31 11:06:52 CST | python | Wrong Answer | N/A | N/A |
| 683640550 | 2025/12/09 14:33:43 CST | python | Accepted | 4 ms | 17.3 MB |
| 645916376 | 2025/07/22 07:26:34 CST | python | Accepted | 0 ms | 17.7 MB |

### 最近一次 AC 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
```

## 877. 石子游戏 (`stone-game`)

- 题目链接：https://leetcode.cn/problems/stone-game/
- 难度：Medium
- 标签：Array, Math, Dynamic Programming, Game Theory
- 总提交次数：1
- 最近提交时间：2026/04/06 16:48:16 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715632900 | 2026/04/06 16:48:16 CST | python | Accepted | 0 ms | 19.1 MB |

### 最近一次 AC 代码

```python
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
```

## 886. 可能的二分法 (`possible-bipartition`)

- 题目链接：https://leetcode.cn/problems/possible-bipartition/
- 难度：Medium
- 标签：Depth-First Search, Breadth-First Search, Union Find, Graph
- 总提交次数：3
- 最近提交时间：2026/04/05 09:51:51 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715234532 | 2026/04/05 09:51:51 CST | python | Accepted | 31 ms | 22.5 MB |
| 715234482 | 2026/04/05 09:51:29 CST | python | Wrong Answer | N/A | N/A |
| 715234447 | 2026/04/05 09:51:13 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n + 1)]
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        colors = [0] * (n + 1)
        for start in range(1, n + 1):
            if colors[start] != 0:
                continue
            dq = collections.deque([start])
            colors[start] = 1
            while dq:
                node = dq.popleft()
                for neighbor in graph[node]:
                    if colors[neighbor] == 0:
                        colors[neighbor] = -colors[node]
                        dq.append(neighbor)
                    elif colors[neighbor] == colors[node]:
                        return False
        return True
```

## 889. 根据前序和后序遍历构造二叉树 (`construct-binary-tree-from-preorder-and-postorder-traversal`)

- 题目链接：https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-postorder-traversal/
- 难度：Medium
- 标签：Tree, Array, Hash Table, Divide and Conquer, Binary Tree
- 总提交次数：11
- 最近提交时间：2026/04/07 10:34:51 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715816159 | 2026/04/07 10:34:51 CST | python | Accepted | 0 ms | 19.5 MB |
| 715815026 | 2026/04/07 10:32:06 CST | python | Wrong Answer | N/A | N/A |
| 701676567 | 2026/03/02 10:34:47 CST | python | Accepted | 0 ms | 19.3 MB |
| 687107324 | 2025/12/25 17:00:14 CST | python | Accepted | 4 ms | 17.2 MB |
| 687098281 | 2025/12/25 16:34:21 CST | python | Accepted | 0 ms | 17.5 MB |
| 687098153 | 2025/12/25 16:33:58 CST | python | Runtime Error | N/A | N/A |
| 687097996 | 2025/12/25 16:33:31 CST | python | Runtime Error | N/A | N/A |
| 687097106 | 2025/12/25 16:30:36 CST | python | Runtime Error | N/A | N/A |
| 687096251 | 2025/12/25 16:27:55 CST | python | Runtime Error | N/A | N/A |
| 687095515 | 2025/12/25 16:25:41 CST | python | Runtime Error | N/A | N/A |
| 687095451 | 2025/12/25 16:25:30 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(postorder)
        post_map = {val : idx for idx, val in enumerate(postorder)}
        def _build(pre_start, pre_end, post_start, post_end):
            if pre_start >= pre_end or post_start >= post_end:
                return
            root_val = preorder[pre_start]
            root = TreeNode(root_val)
            if pre_end - pre_start == 1:
                return root
            left_root_val = preorder[pre_start + 1]
            left_root_idx = post_map.get(left_root_val)
            size = left_root_idx - post_start + 1
            root.left = _build(pre_start + 1, pre_start + 1 + size, post_start, post_start + size)
            root.right = _build(pre_start + 1 + size, pre_end, post_start + size, post_end - 1)
            return root
        return _build(0, n, 0, n)
```

## 901. 股票价格跨度 (`online-stock-span`)

- 题目链接：https://leetcode.cn/problems/online-stock-span/
- 难度：Medium
- 标签：Stack, Design, Data Stream, Monotonic Stack
- 总提交次数：8
- 最近提交时间：2026/03/28 09:33:13 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 712757851 | 2026/03/28 09:33:13 CST | python | Accepted | 143 ms | 23.9 MB |
| 712757816 | 2026/03/28 09:33:02 CST | python | Runtime Error | N/A | N/A |
| 712437542 | 2026/03/27 08:59:06 CST | python | Accepted | 66 ms | 23.9 MB |
| 712135622 | 2026/03/26 12:29:31 CST | python | Accepted | 156 ms | 23.6 MB |
| 712135572 | 2026/03/26 12:29:20 CST | python | Runtime Error | N/A | N/A |
| 712135538 | 2026/03/26 12:29:11 CST | python | Runtime Error | N/A | N/A |
| 712135498 | 2026/03/26 12:28:58 CST | python | Runtime Error | N/A | N/A |
| 712135458 | 2026/03/26 12:28:46 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            _, pre_span = self.stack.pop()
            span += pre_span
        self.stack.append((price, span))
        return span       


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
```

## 904. 水果成篮 (`fruit-into-baskets`)

- 题目链接：https://leetcode.cn/problems/fruit-into-baskets/
- 难度：Medium
- 标签：Array, Hash Table, Sliding Window
- 总提交次数：3
- 最近提交时间：2026/02/26 11:34:16 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 700624306 | 2026/02/26 11:34:16 CST | python | Accepted | 171 ms | 25.5 MB |
| 700622995 | 2026/02/26 11:29:51 CST | python | Wrong Answer | N/A | N/A |
| 660572954 | 2025/09/08 11:48:39 CST | python | Accepted | 212 ms | 23.2 MB |

### 最近一次 AC 代码

```python
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window = {}
        max_len = 0
        left = 0
        for right, r_num in enumerate(fruits):
            if r_num in window:
                window[r_num] += 1
            else:
                window[r_num] = 1
            if len(window) > 2:
                l_num = fruits[left]
                window[l_num] -= 1
                if window[l_num] == 0:
                    del window[l_num]
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len
```

## 918. 环形子数组的最大和 (`maximum-sum-circular-subarray`)

- 题目链接：https://leetcode.cn/problems/maximum-sum-circular-subarray/
- 难度：Medium
- 标签：Queue, Array, Divide and Conquer, Dynamic Programming, Monotonic Queue
- 总提交次数：6
- 最近提交时间：2026/02/10 08:49:16 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 697654169 | 2026/02/10 08:49:16 CST | python | Accepted | 50 ms | 23.9 MB |
| 697452832 | 2026/02/09 11:40:42 CST | python | Accepted | 44 ms | 23.9 MB |
| 690985161 | 2026/01/13 12:14:45 CST | python | Accepted | 57 ms | 23.9 MB |
| 690985018 | 2026/01/13 12:13:45 CST | python | Wrong Answer | N/A | N/A |
| 690775961 | 2026/01/12 15:10:03 CST | python | Accepted | 67 ms | 23.9 MB |
| 690775439 | 2026/01/12 15:08:36 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = max_sum = max_so_far = min_sum = min_so_far = nums[0]
        for num in nums[1:]:
            total += num
            max_so_far = max(num, num + max_so_far)
            max_sum = max(max_sum, max_so_far)
            min_so_far = min(num, num + min_so_far)
            min_sum = min(min_sum, min_so_far)
        if max_sum < 0:
            return max_sum
        return max(max_sum, total - min_sum)
```

## 919. 完全二叉树插入器 (`complete-binary-tree-inserter`)

- 题目链接：https://leetcode.cn/problems/complete-binary-tree-inserter/
- 难度：Medium
- 标签：Tree, Breadth-First Search, Design, Binary Tree
- 总提交次数：7
- 最近提交时间：2026/02/27 13:14:28 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 700909147 | 2026/02/27 13:14:28 CST | python | Accepted | 3 ms | 20 MB |
| 700909051 | 2026/02/27 13:13:59 CST | python | Wrong Answer | N/A | N/A |
| 686535337 | 2025/12/23 08:47:50 CST | python | Accepted | 3 ms | 18 MB |
| 686535206 | 2025/12/23 08:46:05 CST | python | Wrong Answer | N/A | N/A |
| 686290045 | 2025/12/22 08:41:23 CST | python | Accepted | 0 ms | 18.2 MB |
| 686289999 | 2025/12/22 08:40:31 CST | python | Wrong Answer | N/A | N/A |
| 686289953 | 2025/12/22 08:39:46 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.candidate_parents = collections.deque()
        dq = collections.deque([root])
        while dq:
            node = dq.popleft()
            if not node.left or not node.right:
                self.candidate_parents.append(node)
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)

    def insert(self, val: int) -> int:
        new_node = TreeNode(val = val)
        parent = self.candidate_parents[0]
        if not parent.left:
            parent.left = new_node
        else:
            parent.right = new_node
            self.candidate_parents.popleft()
        self.candidate_parents.append(new_node)
        return parent.val
        

    def get_root(self) -> Optional[TreeNode]:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
```

## 931. 下降路径最小和 (`minimum-falling-path-sum`)

- 题目链接：https://leetcode.cn/problems/minimum-falling-path-sum/
- 难度：Medium
- 标签：Array, Dynamic Programming, Matrix
- 总提交次数：8
- 最近提交时间：2026/04/13 10:33:10 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 717616492 | 2026/04/13 10:33:10 CST | python | Accepted | 15 ms | 20.1 MB |
| 717616409 | 2026/04/13 10:32:55 CST | python | Runtime Error | N/A | N/A |
| 717616323 | 2026/04/13 10:32:44 CST | python | Runtime Error | N/A | N/A |
| 717616290 | 2026/04/13 10:32:38 CST | python | Runtime Error | N/A | N/A |
| 698384845 | 2026/02/13 14:09:50 CST | python | Accepted | 12 ms | 19.7 MB |
| 688140053 | 2025/12/30 17:52:37 CST | python | Accepted | 23 ms | 17.7 MB |
| 688139892 | 2025/12/30 17:51:51 CST | python | Runtime Error | N/A | N/A |
| 688128988 | 2025/12/30 17:10:22 CST | python | Accepted | 24 ms | 17.9 MB |

### 最近一次 AC 代码

```python
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0] * n for _ in range(n)]
        for j in range(n):
            dp[0][j] = matrix[0][j]
        for i in range(1, n):
            for j in range(n):
                best_above = dp[i - 1][j]
                if j - 1 >= 0:
                    best_above = min(best_above, dp[i - 1][j - 1])
                if j + 1 < n:
                    best_above = min(best_above, dp[i - 1][j + 1])
                dp[i][j] = matrix[i][j] + best_above
        return min(dp[n - 1])
```

## 933. 最近的请求次数 (`number-of-recent-calls`)

- 题目链接：https://leetcode.cn/problems/number-of-recent-calls/
- 难度：Easy
- 标签：Design, Queue, Data Stream
- 总提交次数：1
- 最近提交时间：2026/03/26 11:03:42 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 712105731 | 2026/03/26 11:03:42 CST | python | Accepted | 122 ms | 23.8 MB |

### 最近一次 AC 代码

```python
class RecentCounter:

    def __init__(self):
        self.dq = collections.deque()
        

    def ping(self, t: int) -> int:
        self.dq.append(t)
        while self.dq and self.dq[0] < t - 3000:
            self.dq.popleft()
        return len(self.dq)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
```

## 940. 不同的子序列 II (`distinct-subsequences-ii`)

- 题目链接：https://leetcode.cn/problems/distinct-subsequences-ii/
- 难度：Hard
- 标签：String, Dynamic Programming
- 总提交次数：10
- 最近提交时间：2026/02/14 13:57:52 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 698571999 | 2026/02/14 13:57:52 CST | python | Accepted | 11 ms | 19.3 MB |
| 698571979 | 2026/02/14 13:57:44 CST | python | Runtime Error | N/A | N/A |
| 694618250 | 2026/01/28 10:23:09 CST | python | Accepted | 7 ms | 19 MB |
| 694618206 | 2026/01/28 10:22:58 CST | python | Runtime Error | N/A | N/A |
| 694337356 | 2026/01/27 09:22:23 CST | python | Accepted | 7 ms | 19.1 MB |
| 694146468 | 2026/01/26 14:37:54 CST | python | Accepted | 4 ms | 19.3 MB |
| 694146181 | 2026/01/26 14:36:57 CST | python | Runtime Error | N/A | N/A |
| 694139096 | 2026/01/26 14:11:28 CST | python | Accepted | 11 ms | 19.3 MB |
| 694138840 | 2026/01/26 14:10:20 CST | python | Runtime Error | N/A | N/A |
| 694138729 | 2026/01/26 14:09:55 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        counts = [0] * 26
        mod = 10 ** 9 + 7
        total = 0
        for c in s:
            idx = ord(c) - ord('a')
            new_end = total + 1
            total = total - counts[idx] + new_end
            counts[idx] = new_end
        return total % mod
```

## 950. 按递增顺序显示卡牌 (`reveal-cards-in-increasing-order`)

- 题目链接：https://leetcode.cn/problems/reveal-cards-in-increasing-order/
- 难度：Medium
- 标签：Queue, Array, Sorting, Simulation
- 总提交次数：2
- 最近提交时间：2026/03/31 08:22:16 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 713720842 | 2026/03/31 08:22:16 CST | python | Accepted | 0 ms | 19.4 MB |
| 713422885 | 2026/03/30 12:21:03 CST | python | Accepted | 3 ms | 19.3 MB |

### 最近一次 AC 代码

```python
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        dq = collections.deque()
        for card in reversed(deck):
            if dq:
                dq.appendleft(dq.pop())
            dq.appendleft(card)
        return list(dq)
```

## 958. 二叉树的完全性检验 (`check-completeness-of-a-binary-tree`)

- 题目链接：https://leetcode.cn/problems/check-completeness-of-a-binary-tree/
- 难度：Medium
- 标签：Tree, Breadth-First Search, Binary Tree
- 总提交次数：3
- 最近提交时间：2026/04/05 16:39:33 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715341437 | 2026/04/05 16:39:33 CST | python | Accepted | 0 ms | 19.3 MB |
| 700900336 | 2026/02/27 12:17:47 CST | python | Accepted | 0 ms | 19 MB |
| 686051592 | 2025/12/20 21:00:49 CST | python | Accepted | 4 ms | 17.1 MB |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        dq = collections.deque([root])
        is_end = False
        while dq:
            node = dq.popleft()
            if node is None:
                is_end = True
            else:
                if is_end:
                    return False
                dq.append(node.left)
                dq.append(node.right)
        return True
```

## 967. 连续差相同的数字 (`numbers-with-same-consecutive-differences`)

- 题目链接：https://leetcode.cn/problems/numbers-with-same-consecutive-differences/
- 难度：Medium
- 标签：Breadth-First Search, Backtracking
- 总提交次数：3
- 最近提交时间：2026/02/22 16:55:37 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 699807116 | 2026/02/22 16:55:37 CST | python | Accepted | 7 ms | 19.5 MB |
| 687646331 | 2025/12/28 14:42:05 CST | python | Accepted | 8 ms | 17.6 MB |
| 687646310 | 2025/12/28 14:41:59 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []
        path_sum = 0
        pos = 0
        def backtrack():
            nonlocal path_sum, pos
            if pos == n:
                res.append(path_sum)
                return
            for x in range(10):
                if pos == 0 and x == 0:
                    continue
                if pos > 0 and abs(path_sum % 10 - x) != k:
                    continue
                pos += 1
                path_sum = path_sum * 10 + x
                backtrack()
                path_sum //= 10
                pos -= 1
        backtrack()
        return res
```

## 974. 和可被 K 整除的子数组 (`subarray-sums-divisible-by-k`)

- 题目链接：https://leetcode.cn/problems/subarray-sums-divisible-by-k/
- 难度：Medium
- 标签：Array, Hash Table, Prefix Sum
- 总提交次数：2
- 最近提交时间：2026/03/16 14:19:38 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 707773498 | 2026/03/16 14:19:38 CST | python | Accepted | 39 ms | 23.2 MB |
| 662237835 | 2025/09/13 10:56:07 CST | python | Accepted | 23 ms | 20.6 MB |

### 最近一次 AC 代码

```python
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pre_sum = 0
        remainder_map = collections.defaultdict(int)
        remainder_map[0] = 1
        count = 0
        for num in nums:
            pre_sum += num
            remainder = pre_sum % k
            if remainder in remainder_map:
                count += remainder_map.get(remainder)
            remainder_map[remainder] += 1
        return count
```

## 977. 有序数组的平方 (`squares-of-a-sorted-array`)

- 题目链接：https://leetcode.cn/problems/squares-of-a-sorted-array/
- 难度：Easy
- 标签：Array, Two Pointers, Sorting
- 总提交次数：2
- 最近提交时间：2026/03/17 16:11:37 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 708334093 | 2026/03/17 16:11:37 CST | python | Accepted | 12 ms | 20.7 MB |
| 665835843 | 2025/09/25 10:29:55 CST | python | Accepted | 15 ms | 19.5 MB |

### 最近一次 AC 代码

```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        left, right = 0, n - 1
        tail = n - 1
        while left <= right:
            left_sq = nums[left] ** 2
            right_sq = nums[right] ** 2
            if left_sq < right_sq:
                res[tail] = right_sq
                right -= 1
            else:
                res[tail] = left_sq
                left += 1
            tail -= 1
        return res
```

## 980. 不同路径 III (`unique-paths-iii`)

- 题目链接：https://leetcode.cn/problems/unique-paths-iii/
- 难度：Hard
- 标签：Bit Manipulation, Array, Backtracking, Matrix
- 总提交次数：6
- 最近提交时间：2026/04/09 10:30:13 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 716482925 | 2026/04/09 10:30:13 CST | python | Accepted | 31 ms | 19.4 MB |
| 716482594 | 2026/04/09 10:29:19 CST | python | Time Limit Exceeded | N/A | N/A |
| 716482514 | 2026/04/09 10:29:04 CST | python | Runtime Error | N/A | N/A |
| 716482432 | 2026/04/09 10:28:50 CST | python | Runtime Error | N/A | N/A |
| 699792780 | 2026/02/22 15:51:43 CST | python | Accepted | 15 ms | 19.4 MB |
| 687798042 | 2025/12/29 10:42:39 CST | python | Accepted | 18 ms | 17 MB |

### 最近一次 AC 代码

```python
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        total_valid = 0
        m, n = len(grid), len(grid[0])
        start_r, start_c = 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start_r, start_c = i, j
                    total_valid += 1
                elif grid[i][j] != -1:
                    total_valid += 1
        self.res = 0
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        def backtrack(r, c, remain):
            if not (0 <= r < m and 0 <= c < n):
                return
            if grid[r][c] == -1:
                return
            if remain == 1 and grid[r][c] == 2:
                self.res += 1
                return
            for dr, dc in directions:
                origin = grid[r][c]
                grid[r][c] = -1
                remain -= 1
                nr, nc = r + dr, c + dc
                backtrack(nr, nc, remain)
                remain += 1
                grid[r][c] = origin
        backtrack(start_r, start_c, total_valid)
        return self.res
```

## 981. 基于时间的键值存储 (`time-based-key-value-store`)

- 题目链接：https://leetcode.cn/problems/time-based-key-value-store/
- 难度：Medium
- 标签：Design, Hash Table, String, Binary Search
- 总提交次数：9
- 最近提交时间：2026/03/06 15:13:59 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 703435499 | 2026/03/06 15:13:59 CST | python | Accepted | 57 ms | 64.6 MB |
| 677582859 | 2025/11/12 13:47:26 CST | python | Accepted | 60 ms | 70.1 MB |
| 677582815 | 2025/11/12 13:47:11 CST | python | Runtime Error | N/A | N/A |
| 675691048 | 2025/11/04 10:16:58 CST | python | Accepted | 58 ms | 69.3 MB |
| 675690741 | 2025/11/04 10:15:55 CST | python | Wrong Answer | N/A | N/A |
| 675690658 | 2025/11/04 10:15:37 CST | python | Runtime Error | N/A | N/A |
| 675690530 | 2025/11/04 10:15:09 CST | python | Runtime Error | N/A | N/A |
| 675319848 | 2025/11/02 17:36:22 CST | python | Accepted | 71 ms | 70.2 MB |
| 675319745 | 2025/11/02 17:35:53 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class TimeMap:

    def __init__(self):
        self.ts = collections.defaultdict(list)
        self.vals = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.ts[key].append(timestamp)
        self.vals[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.ts:
            return ''
        idx = bisect.bisect_right(self.ts[key], timestamp) - 1
        if idx >= 0:
            return self.vals[key][idx]
        return ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
```

## 983. 最低票价 (`minimum-cost-for-tickets`)

- 题目链接：https://leetcode.cn/problems/minimum-cost-for-tickets/
- 难度：Medium
- 标签：Array, Dynamic Programming
- 总提交次数：13
- 最近提交时间：2026/01/28 09:55:32 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 694611820 | 2026/01/28 09:55:32 CST | python | Accepted | 3 ms | 19.1 MB |
| 694414033 | 2026/01/27 14:30:12 CST | python | Accepted | 0 ms | 19 MB |
| 694413950 | 2026/01/27 14:29:56 CST | python | Runtime Error | N/A | N/A |
| 692818265 | 2026/01/20 21:28:57 CST | python | Accepted | 0 ms | 19.1 MB |
| 690135038 | 2026/01/09 13:46:19 CST | python | Accepted | 0 ms | 18.9 MB |
| 690134990 | 2026/01/09 13:46:04 CST | python | Runtime Error | N/A | N/A |
| 689696298 | 2026/01/07 15:58:40 CST | python | Accepted | 0 ms | 19.2 MB |
| 689695675 | 2026/01/07 15:56:47 CST | python | Wrong Answer | N/A | N/A |
| 689695454 | 2026/01/07 15:56:08 CST | python | Wrong Answer | N/A | N/A |
| 689695397 | 2026/01/07 15:55:54 CST | python | Runtime Error | N/A | N/A |
| 689354777 | 2026/01/06 09:38:43 CST | python | Accepted | 5 ms | 19.3 MB |
| 689354712 | 2026/01/06 09:38:18 CST | python | Runtime Error | N/A | N/A |
| 689354608 | 2026/01/06 09:37:47 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        travel_days = set(days)
        last_day = days[-1]
        dp = [0] * (last_day + 1)
        for day in range(1, last_day + 1):
            if day not in travel_days:
                dp[day] = dp[day - 1]
                continue
            cost_1 = dp[day - 1] + costs[0]
            cost_7 = dp[max(0, day - 7)] + costs[1]
            cost_30 = dp[max(0, day - 30)] + costs[2]
            dp[day] = min(cost_1, cost_7, cost_30)
        return dp[last_day]
```

## 987. 二叉树的垂序遍历 (`vertical-order-traversal-of-a-binary-tree`)

- 题目链接：https://leetcode.cn/problems/vertical-order-traversal-of-a-binary-tree/
- 难度：Hard
- 标签：Tree, Depth-First Search, Breadth-First Search, Hash Table, Binary Tree, Sorting
- 总提交次数：3
- 最近提交时间：2026/03/03 09:57:33 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 702057662 | 2026/03/03 09:57:33 CST | python | Accepted | 0 ms | 19.3 MB |
| 702057551 | 2026/03/03 09:57:15 CST | python | Wrong Answer | N/A | N/A |
| 702057023 | 2026/03/03 09:55:45 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        nodes = []
        def dfs(node, row, col):
            if not node:
                return
            nodes.append((col, row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)
        dfs(root, 0, 0)
        nodes.sort()
        if not nodes:
            return []
        res = []
        curr_col_vals = []
        last_col = nodes[0][0]
        for col, row, val in nodes:
            if col != last_col:
                res.append(curr_col_vals)
                curr_col_vals = []
                last_col = col
            curr_col_vals.append(val)
        res.append(curr_col_vals)
        return res
```

## 990. 等式方程的可满足性 (`satisfiability-of-equality-equations`)

- 题目链接：https://leetcode.cn/problems/satisfiability-of-equality-equations/
- 难度：Medium
- 标签：Union Find, Graph, Array, String
- 总提交次数：2
- 最近提交时间：2026/04/05 15:42:50 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715320836 | 2026/04/05 15:42:50 CST | python | Accepted | 4 ms | 19.2 MB |
| 715320545 | 2026/04/05 15:41:59 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind(26)
        for equation in equations:
            if equation[1:3] == '==':
                x = ord(equation[0]) - ord('a')
                y = ord(equation[3]) - ord('a')
                uf.union(x, y)
        for equation in equations:
            if equation[1:3] == '!=':
                x = ord(equation[0]) - ord('a')
                y = ord(equation[3]) - ord('a')
                if uf.find(x) == uf.find(y):
                    return False
        return True
```

## 994. 腐烂的橘子 (`rotting-oranges`)

- 题目链接：https://leetcode.cn/problems/rotting-oranges/
- 难度：Medium
- 标签：Breadth-First Search, Array, Matrix
- 总提交次数：7
- 最近提交时间：2025/12/24 14:07:57 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 686830054 | 2025/12/24 14:07:57 CST | python | Accepted | 3 ms | 16.9 MB |
| 686829025 | 2025/12/24 14:02:47 CST | python | Wrong Answer | N/A | N/A |
| 686828993 | 2025/12/24 14:02:38 CST | python | Runtime Error | N/A | N/A |
| 686595330 | 2025/12/23 14:02:52 CST | python | Accepted | 3 ms | 17.2 MB |
| 686594532 | 2025/12/23 13:59:02 CST | python | Wrong Answer | N/A | N/A |
| 686594381 | 2025/12/23 13:58:16 CST | python | Wrong Answer | N/A | N/A |
| 686594233 | 2025/12/23 13:57:29 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dq = collections.deque()
        fresh = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    dq.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        minutes = 0
        while dq and fresh > 0:
            sz = len(dq)
            for _ in range(sz):
                r, c = dq.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if not 0 <= nr < m or not 0 <= nc < n:
                        continue
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        dq.append((nr, nc))
            minutes += 1
        return minutes if fresh == 0 else -1
```

## 1004. 最大连续1的个数 III (`max-consecutive-ones-iii`)

- 题目链接：https://leetcode.cn/problems/max-consecutive-ones-iii/
- 难度：Medium
- 标签：Array, Binary Search, Prefix Sum, Sliding Window
- 总提交次数：5
- 最近提交时间：2026/03/18 11:44:51 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 708696589 | 2026/03/18 11:44:51 CST | python | Accepted | 63 ms | 21.9 MB |
| 700642190 | 2026/02/26 13:05:03 CST | python | Accepted | 52 ms | 21.9 MB |
| 661008148 | 2025/09/09 15:30:52 CST | python | Accepted | 150 ms | 19.9 MB |
| 652815826 | 2025/08/14 07:48:12 CST | python | Accepted | 83 ms | 20.1 MB |
| 652815748 | 2025/08/14 07:45:27 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero_counts = 0
        left = 0
        max_len = 0
        for right, r_num in enumerate(nums):
            if r_num == 0:
                zero_counts += 1
            if zero_counts > k:
                if nums[left] == 0:
                    zero_counts -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len
```

## 1011. 在 D 天内送达包裹的能力 (`capacity-to-ship-packages-within-d-days`)

- 题目链接：https://leetcode.cn/problems/capacity-to-ship-packages-within-d-days/
- 难度：Medium
- 标签：Array, Binary Search
- 总提交次数：4
- 最近提交时间：2026/03/24 09:34:53 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 711226933 | 2026/03/24 09:34:53 CST | python | Accepted | 215 ms | 23.7 MB |
| 709154997 | 2026/03/19 11:03:13 CST | python | Accepted | 207 ms | 23.5 MB |
| 709154888 | 2026/03/19 11:03:02 CST | python | Runtime Error | N/A | N/A |
| 709154178 | 2026/03/19 11:01:49 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(capacity):
            used_days = 1
            curr = 0
            for weight in weights:
                if curr + weight > capacity:
                    used_days += 1
                    curr = weight
                else:
                    curr += weight
            return used_days <= days
        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            if can_ship(mid):
                right = mid
            else:
                left = mid + 1
        return left
```

## 1020. 飞地的数量 (`number-of-enclaves`)

- 题目链接：https://leetcode.cn/problems/number-of-enclaves/
- 难度：Medium
- 标签：Depth-First Search, Breadth-First Search, Union Find, Array, Matrix
- 总提交次数：4
- 最近提交时间：2026/04/10 11:13:44 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 716826826 | 2026/04/10 11:13:44 CST | python | Accepted | 159 ms | 32.9 MB |
| 687623996 | 2025/12/28 12:16:49 CST | python | Accepted | 131 ms | 27.9 MB |
| 687623856 | 2025/12/28 12:15:59 CST | python | Accepted | 131 ms | 28 MB |
| 687623822 | 2025/12/28 12:15:43 CST | python | Accepted | 131 ms | 28.2 MB |

### 最近一次 AC 代码

```python
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(r, c):
            if not (0 <= r < m and 0 <= c < n):
                return 0
            if grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1) + 1
        
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        
        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)

        res = 0
        
        for i in range(m):
            for j in range(n):
                res += dfs(i, j)
        
        return res
```

## 1022. 从根到叶的二进制数之和 (`sum-of-root-to-leaf-binary-numbers`)

- 题目链接：https://leetcode.cn/problems/sum-of-root-to-leaf-binary-numbers/
- 难度：Easy
- 标签：Tree, Depth-First Search, Binary Tree
- 总提交次数：1
- 最近提交时间：2026/04/07 12:38:40 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715855972 | 2026/04/07 12:38:40 CST | python | Accepted | 0 ms | 19.3 MB |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        total = 0
        def traverse(node, cur):
            cur = cur * 2 + node.val
            nonlocal total
            if node.left is None and node.right is None:
                total += cur
                return 
            if node.left:
                traverse(node.left, cur)
            if node.right:
                traverse(node.right, cur)
        traverse(root, 0)
        return total
```

## 1024. 视频拼接 (`video-stitching`)

- 题目链接：https://leetcode.cn/problems/video-stitching/
- 难度：Medium
- 标签：Greedy, Array, Dynamic Programming
- 总提交次数：8
- 最近提交时间：2026/02/12 11:19:19 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 698137650 | 2026/02/12 11:19:19 CST | python | Accepted | 0 ms | 19.1 MB |
| 696556856 | 2026/02/05 10:37:35 CST | python | Accepted | 0 ms | 19 MB |
| 696556757 | 2026/02/05 10:37:15 CST | python | Time Limit Exceeded | N/A | N/A |
| 696307857 | 2026/02/04 10:12:05 CST | python | Accepted | 0 ms | 19.2 MB |
| 696307651 | 2026/02/04 10:11:15 CST | python | Time Limit Exceeded | N/A | N/A |
| 696307564 | 2026/02/04 10:10:52 CST | python | Runtime Error | N/A | N/A |
| 696302941 | 2026/02/04 09:49:44 CST | python | Accepted | 0 ms | 19.3 MB |
| 696153513 | 2026/02/03 16:36:26 CST | python | Accepted | 0 ms | 19 MB |

### 最近一次 AC 代码

```python
class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort()
        n = len(clips)
        end = 0
        farthest = 0
        cnt = 0
        i = 0
        while end < time:
            while i < n and clips[i][0] <= end:
                farthest = max(farthest, clips[i][1])
                i += 1
            if farthest == end:
                return -1
            cnt += 1
            end = farthest
        return cnt
```

## 1027. 最长等差数列 (`longest-arithmetic-subsequence`)

- 题目链接：https://leetcode.cn/problems/longest-arithmetic-subsequence/
- 难度：Medium
- 标签：Array, Hash Table, Binary Search, Dynamic Programming
- 总提交次数：8
- 最近提交时间：2026/03/05 13:55:34 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 702962015 | 2026/03/05 13:55:34 CST | python | Accepted | 1187 ms | 28.7 MB |
| 702961764 | 2026/03/05 13:54:54 CST | python | Wrong Answer | N/A | N/A |
| 702961554 | 2026/03/05 13:54:17 CST | python | Runtime Error | N/A | N/A |
| 702961486 | 2026/03/05 13:54:04 CST | python | Runtime Error | N/A | N/A |
| 698542225 | 2026/02/14 10:48:34 CST | python | Accepted | 1187 ms | 28.4 MB |
| 698541998 | 2026/02/14 10:47:22 CST | python | Wrong Answer | N/A | N/A |
| 697915224 | 2026/02/11 11:28:04 CST | python | Accepted | 1202 ms | 28.7 MB |
| 697915150 | 2026/02/11 11:27:50 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[2] * n for _ in range (n)]
        res = 2
        for i in range(n):
            exists = {}
            for j in range(i):
                diff = nums[i] - nums[j]
                target = nums[j] - diff
                if target in exists:
                    dp[i][j] = dp[j][exists[target]] + 1
                    res = max(res, dp[i][j])
                exists[nums[j]] = j
        return res
```

## 1038. 从二叉搜索树到更大和树 (`binary-search-tree-to-greater-sum-tree`)

- 题目链接：https://leetcode.cn/problems/binary-search-tree-to-greater-sum-tree/
- 难度：Medium
- 标签：Tree, Depth-First Search, Binary Search Tree, Binary Tree
- 总提交次数：2
- 最近提交时间：2026/04/03 12:25:52 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 714809903 | 2026/04/03 12:25:52 CST | python | Accepted | 0 ms | 19 MB |
| 714809793 | 2026/04/03 12:25:13 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.sum = 0
        def traverse(root):
            if not root:
                return 
            traverse(root.right)
            self.sum += root.val
            root.val = self.sum
            traverse(root.left)
        traverse(root)
        return root
```

## 1039. 多边形三角剖分的最低得分 (`minimum-score-triangulation-of-polygon`)

- 题目链接：https://leetcode.cn/problems/minimum-score-triangulation-of-polygon/
- 难度：Medium
- 标签：Array, Dynamic Programming
- 总提交次数：5
- 最近提交时间：2026/02/14 14:56:38 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 698582385 | 2026/02/14 14:56:38 CST | python | Accepted | 27 ms | 19.1 MB |
| 691545385 | 2026/01/15 15:54:38 CST | python | Accepted | 27 ms | 19.2 MB |
| 691219456 | 2026/01/14 10:51:31 CST | python | Accepted | 23 ms | 19.4 MB |
| 691217821 | 2026/01/14 10:46:16 CST | python | Wrong Answer | N/A | N/A |
| 690982337 | 2026/01/13 11:58:36 CST | python | Accepted | 27 ms | 19.3 MB |

### 最近一次 AC 代码

```python
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]
        for gap in range(2, n):
            for i in range(0, n - gap):
                j = i + gap
                dp[i][j] = float('inf')
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + values[i] * values[k] * values[j])
        return dp[0][n - 1]
```

## 1049. 最后一块石头的重量 II (`last-stone-weight-ii`)

- 题目链接：https://leetcode.cn/problems/last-stone-weight-ii/
- 难度：Medium
- 标签：Array, Dynamic Programming
- 总提交次数：14
- 最近提交时间：2026/02/13 15:03:32 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 698395685 | 2026/02/13 15:03:32 CST | python | Accepted | 11 ms | 19.4 MB |
| 692959044 | 2026/01/21 14:24:33 CST | python | Accepted | 14 ms | 19.5 MB |
| 689739542 | 2026/01/07 18:01:42 CST | python | Accepted | 11 ms | 19.4 MB |
| 689739154 | 2026/01/07 18:00:01 CST | python | Wrong Answer | N/A | N/A |
| 689738988 | 2026/01/07 17:59:20 CST | python | Wrong Answer | N/A | N/A |
| 689130497 | 2026/01/05 11:10:22 CST | python | Accepted | 7 ms | 17.2 MB |
| 689130386 | 2026/01/05 11:10:01 CST | python | Wrong Answer | N/A | N/A |
| 688920552 | 2026/01/04 14:21:29 CST | python | Accepted | 10 ms | 17.6 MB |
| 688753427 | 2026/01/03 17:05:39 CST | python | Accepted | 11 ms | 17.2 MB |
| 688749224 | 2026/01/03 16:47:42 CST | python | Wrong Answer | N/A | N/A |
| 688680236 | 2026/01/03 09:43:14 CST | python | Accepted | 7 ms | 17.3 MB |
| 688680186 | 2026/01/03 09:42:28 CST | python | Wrong Answer | N/A | N/A |
| 688680155 | 2026/01/03 09:42:09 CST | python | Wrong Answer | N/A | N/A |
| 688680098 | 2026/01/03 09:41:16 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        n = len(stones)
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            stone = stones[i - 1]
            for j in range(target + 1):
                dp[i][j] = dp[i - 1][j] or (j >= stone and dp[i - 1][j - stone])
        for best in range(target, -1, -1):
            if dp[n][best]:
                return total - 2 * best
```

## 1055. 形成字符串的最短路径 (`shortest-way-to-form-string`)

- 题目链接：https://leetcode.cn/problems/shortest-way-to-form-string/
- 难度：Medium
- 标签：Greedy, Two Pointers, String, Binary Search
- 总提交次数：10
- 最近提交时间：2026/03/05 13:40:26 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 702956769 | 2026/03/05 13:40:26 CST | python | Accepted | 0 ms | 19.1 MB |
| 700146380 | 2026/02/24 13:07:58 CST | python | Accepted | 3 ms | 19.1 MB |
| 697933718 | 2026/02/11 13:09:15 CST | python | Accepted | 0 ms | 19.1 MB |
| 697229339 | 2026/02/08 11:03:00 CST | python | Accepted | 4 ms | 19.3 MB |
| 696810388 | 2026/02/06 10:56:23 CST | python | Accepted | 4 ms | 19.3 MB |
| 696809971 | 2026/02/06 10:55:04 CST | python | Wrong Answer | N/A | N/A |
| 559599404 | 2024/08/29 16:11:54 CST | python | Accepted | 35 ms | 16.3 MB |
| 558898069 | 2024/08/27 11:46:55 CST | python | Accepted | 31 ms | 16.6 MB |
| 558125974 | 2024/08/24 12:40:57 CST | python | Time Limit Exceeded | N/A | N/A |
| 557856548 | 2024/08/23 10:46:26 CST | python | Accepted | 44 ms | 16.5 MB |

### 最近一次 AC 代码

```python
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        source_map = collections.defaultdict(list)
        for idx, s in enumerate(source):
            source_map[s].append(idx)
        rounds = 1
        curr_pos = -1
        for ch in target:
            if ch not in source_map:
                return -1
            positions = source_map[ch]
            pos = bisect.bisect_right(positions, curr_pos)
            if pos == len(positions):
                rounds += 1
                curr_pos = positions[0]
            else:
                curr_pos = positions[pos]
        return rounds
```

## 1056. 易混淆数 (`confusing-number`)

- 题目链接：https://leetcode.cn/problems/confusing-number/
- 难度：Easy
- 标签：Math
- 总提交次数：4
- 最近提交时间：2026/02/23 20:57:13 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 700037239 | 2026/02/23 20:57:13 CST | python | Accepted | 0 ms | 19 MB |
| 558297166 | 2024/08/25 08:55:47 CST | python | Accepted | 43 ms | 16.2 MB |
| 557561141 | 2024/08/22 10:58:17 CST | python | Accepted | 32 ms | 16.2 MB |
| 557557351 | 2024/08/22 10:49:28 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def confusingNumber(self, n: int) -> bool:
        rotate_map = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        num_str = str(n)
        new_str = ''
        for c in num_str[::-1]:
            if c not in rotate_map:
                return False
            new_str += rotate_map.get(c)
        return new_str != num_str
```

## 1057. 校园自行车分配 (`campus-bikes`)

- 题目链接：https://leetcode.cn/problems/campus-bikes/
- 难度：Medium
- 标签：Array, Sorting, Heap (Priority Queue)
- 总提交次数：1
- 最近提交时间：2026/03/12 14:35:56 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 706068266 | 2026/03/12 14:35:56 CST | python | Accepted | 977 ms | 157.6 MB |

### 最近一次 AC 代码

```python
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        pairs = []
        worker_count = len(workers)
        bikes_count = len(bikes)
        for woker_id in range(worker_count):
            wx, wy = workers[woker_id]
            for bike_id in range(bikes_count):
                bx, by = bikes[bike_id]
                distance = abs(wx - bx) + abs(wy - by)
                pairs.append((distance, woker_id, bike_id))
        
        pairs.sort()
        res = [-1] * worker_count
        assigned_worker = 0
        used_bike = set()
        for _, woker_id, bike_id in pairs:
            if res[woker_id] != -1:
                continue
            if bike_id in used_bike:
                continue
            used_bike.add(bike_id)
            res[woker_id] = bike_id
            assigned_worker += 1
            if assigned_worker == worker_count:
                break
        return res
```

## 1059. 从起点到终点的所有路径 (`all-paths-from-source-lead-to-destination`)

- 题目链接：https://leetcode.cn/problems/all-paths-from-source-lead-to-destination/
- 难度：Medium
- 标签：Graph, Topological Sort
- 总提交次数：2
- 最近提交时间：2026/03/09 13:01:14 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 704572673 | 2026/03/09 13:01:14 CST | python | Accepted | 7 ms | 23.3 MB |
| 704572617 | 2026/03/09 13:01:03 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]
        for start, end in edges:
            graph[start].append(end)
        if graph[destination]:
            return False
        state = [0] * n 

        def dfs(node):
            if state[node] == 1:
                return False
            if state[node] == 2:
                return True
            
            if not graph[node]:
                return node == destination
            
            state[node] = 1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            state[node] = 2
            return True
        
        return dfs(source)
```

## 1060. 有序数组中的缺失元素 (`missing-element-in-sorted-array`)

- 题目链接：https://leetcode.cn/problems/missing-element-in-sorted-array/
- 难度：Medium
- 标签：Array, Binary Search
- 总提交次数：1
- 最近提交时间：2026/03/03 15:30:42 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 702187157 | 2026/03/03 15:30:42 CST | python | Accepted | 0 ms | 24.6 MB |

### 最近一次 AC 代码

```python
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def missing_count(i):
            return nums[i] - nums[0] - i
        total_missing = missing_count(n - 1)
        if k > total_missing:
            return nums[-1] + (k - total_missing)
        
        left, right = 0, n - 1
        while left < right:
            mid = left + (right - left) // 2
            if missing_count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        
        pre_missing = missing_count(left - 1)
        return nums[left - 1] + (k - pre_missing)
```

## 1086. 前五科的均分 (`high-five`)

- 题目链接：https://leetcode.cn/problems/high-five/
- 难度：Easy
- 标签：Array, Hash Table, Sorting, Heap (Priority Queue)
- 总提交次数：2
- 最近提交时间：2026/03/12 13:59:05 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 706050376 | 2026/03/12 13:59:05 CST | python | Accepted | 4 ms | 19.7 MB |
| 706050082 | 2026/03/12 13:58:29 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        students_score = collections.defaultdict(list)
        for student_id, score in items:
            heapq.heappush(students_score[student_id], score)
            if len(students_score[student_id]) > 5:
                heapq.heappop(students_score[student_id])
        res = []
        for student_id in sorted(students_score):
            high_five_sum = sum(students_score[student_id])
            res.append([student_id, high_five_sum // 5])
        return res
```

## 1087. 花括号展开 (`brace-expansion`)

- 题目链接：https://leetcode.cn/problems/brace-expansion/
- 难度：Medium
- 标签：Stack, Breadth-First Search, String, Backtracking, Sorting
- 总提交次数：4
- 最近提交时间：2026/02/24 10:55:51 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 700115198 | 2026/02/24 10:55:51 CST | python | Accepted | 0 ms | 19.6 MB |
| 700114664 | 2026/02/24 10:53:49 CST | python | Wrong Answer | N/A | N/A |
| 700114620 | 2026/02/24 10:53:38 CST | python | Runtime Error | N/A | N/A |
| 700114542 | 2026/02/24 10:53:22 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def expand(self, s: str) -> List[str]:
        groups = []
        n = len(s)
        i = 0
        while i < n:
            if s[i] == '{':
                j = s.find('}', i)
                groups.append(sorted(s[i+1 : j].split(',')))
                i = j + 1
            else:
                groups.append([s[i]])
                i += 1
        res = []
        path = []
        def backtrack(group_index):
            if group_index == len(groups):
                res.append(''.join(path))
                return
            for ch in groups[group_index]:
                path.append(ch)
                backtrack(group_index + 1)
                path.pop()
        backtrack(0)
        return res
```

## 1091. 二进制矩阵中的最短路径 (`shortest-path-in-binary-matrix`)

- 题目链接：https://leetcode.cn/problems/shortest-path-in-binary-matrix/
- 难度：Medium
- 标签：Breadth-First Search, Array, Matrix
- 总提交次数：15
- 最近提交时间：2026/04/05 21:49:49 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715424490 | 2026/04/05 21:49:49 CST | python | Accepted | 128 ms | 19.4 MB |
| 715424040 | 2026/04/05 21:48:23 CST | python | Memory Limit Exceeded | N/A | N/A |
| 715423997 | 2026/04/05 21:48:14 CST | python | Runtime Error | N/A | N/A |
| 715423919 | 2026/04/05 21:47:58 CST | python | Runtime Error | N/A | N/A |
| 686875671 | 2025/12/24 16:18:35 CST | python | Accepted | 117 ms | 17.5 MB |
| 686875493 | 2025/12/24 16:18:06 CST | python | Accepted | 119 ms | 17.4 MB |
| 686875417 | 2025/12/24 16:17:52 CST | python | Wrong Answer | N/A | N/A |
| 686875374 | 2025/12/24 16:17:44 CST | python | Runtime Error | N/A | N/A |
| 686875342 | 2025/12/24 16:17:39 CST | python | Runtime Error | N/A | N/A |
| 686575736 | 2025/12/23 11:53:57 CST | python | Accepted | 135 ms | 17.4 MB |
| 686575589 | 2025/12/23 11:53:11 CST | python | Wrong Answer | N/A | N/A |
| 686394326 | 2025/12/22 16:13:40 CST | python | Accepted | 131 ms | 17.8 MB |
| 686393593 | 2025/12/22 16:11:20 CST | python | Wrong Answer | N/A | N/A |
| 686393098 | 2025/12/22 16:09:40 CST | python | Wrong Answer | N/A | N/A |
| 686393055 | 2025/12/22 16:09:31 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        if n == 1:
            return 1
        dq = collections.deque([(0, 0, 1)])
        directions = [
            [-1, -1], [-1, 0], [-1, 1],
            [0, -1], [0, 1],
            [1, -1], [1, 0], [1, 1]
        ]
        while dq:
            r, c, dist = dq.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < n) or not (0 <= nc < n):
                    continue
                if grid[nr][nc] == 1:
                    continue
                if nr == nc == n - 1:
                    return dist + 1
                dq.append((nr, nc, dist + 1))
                grid[nr][nc] = 1
        return -1
```

## 1094. 拼车 (`car-pooling`)

- 题目链接：https://leetcode.cn/problems/car-pooling/
- 难度：Medium
- 标签：Array, Prefix Sum, Sorting, Simulation, Heap (Priority Queue)
- 总提交次数：3
- 最近提交时间：2026/03/23 09:23:40 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 710768474 | 2026/03/23 09:23:40 CST | python | Accepted | 3 ms | 19.5 MB |
| 707813369 | 2026/03/16 15:24:25 CST | python | Accepted | 7 ms | 19.4 MB |
| 707812659 | 2026/03/16 15:23:29 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Difference:
    def __init__(self, nums):
        self.diff = [0] * len(nums)
        self.diff[0] = nums[0]
        for i in range(1, len(self.diff)):
            self.diff[i] = nums[i] - nums[i - 1]
    
    def increasement(self, i, j, val):
        self.diff[i] += val
        if j + 1 < len(self.diff):
            self.diff[j + 1] -= val
    
    def result(self):
        res = [0] * len(self.diff)
        res[0] = self.diff[0]
        for i in range(1, len(res)):
            res[i] = self.diff[i] + res[i - 1]
        return res


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        res = [0] * 1000
        df = Difference(res)
        for trip in trips:
            i = trip[1]
            j = trip[2] - 1
            val = trip[0]
            df.increasement(i, j, val)
        for cnt in df.result():
            if cnt > capacity:
                return False
        return True
```

## 1100. 长度为 K 的无重复字符子串 (`find-k-length-substrings-with-no-repeated-characters`)

- 题目链接：https://leetcode.cn/problems/find-k-length-substrings-with-no-repeated-characters/
- 难度：Medium
- 标签：Hash Table, String, Sliding Window
- 总提交次数：3
- 最近提交时间：2026/02/25 14:29:56 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 700403667 | 2026/02/25 14:29:56 CST | python | Accepted | 7 ms | 19.3 MB |
| 560184965 | 2024/08/31 19:59:31 CST | python | Accepted | 45 ms | 16.2 MB |
| 559940061 | 2024/08/30 18:43:16 CST | python | Accepted | 45 ms | 16.5 MB |

### 最近一次 AC 代码

```python
class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        res = 0
        left = 0
        char_set = set()
        for right, r_char in enumerate(s):
            while r_char in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(r_char)
            if right - left + 1 == k:
                res += 1
                char_set.remove(s[left])
                left += 1
        return res
```

## 1104. 二叉树寻路 (`path-in-zigzag-labelled-binary-tree`)

- 题目链接：https://leetcode.cn/problems/path-in-zigzag-labelled-binary-tree/
- 难度：Medium
- 标签：Tree, Math, Binary Tree
- 总提交次数：10
- 最近提交时间：2026/03/01 10:35:48 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 701378954 | 2026/03/01 10:35:48 CST | python | Accepted | 0 ms | 19.1 MB |
| 701378759 | 2026/03/01 10:35:13 CST | python | Wrong Answer | N/A | N/A |
| 700902263 | 2026/02/27 12:29:55 CST | python | Accepted | 0 ms | 19 MB |
| 686553600 | 2025/12/23 10:31:24 CST | python | Accepted | 0 ms | 16.9 MB |
| 686553526 | 2025/12/23 10:31:04 CST | python | Wrong Answer | N/A | N/A |
| 686316642 | 2025/12/22 10:59:17 CST | python | Accepted | 0 ms | 17 MB |
| 686316362 | 2025/12/22 10:58:19 CST | python | Runtime Error | N/A | N/A |
| 686110627 | 2025/12/21 09:39:55 CST | python | Accepted | 0 ms | 17 MB |
| 686110577 | 2025/12/21 09:39:06 CST | python | Wrong Answer | N/A | N/A |
| 686012064 | 2025/12/20 16:57:30 CST | python | Accepted | 0 ms | 16.8 MB |

### 最近一次 AC 代码

```python
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        res = []
        while label:
            res.append(label)
            level = int(math.log2(label))
            level_start = 1 << level
            level_end = (1 << (level + 1)) - 1
            label = (level_start + level_end - label) // 2
        return res[::-1]
```

## 1109. 航班预订统计 (`corporate-flight-bookings`)

- 题目链接：https://leetcode.cn/problems/corporate-flight-bookings/
- 难度：Medium
- 标签：Array, Prefix Sum
- 总提交次数：9
- 最近提交时间：2026/03/16 15:09:26 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 707803181 | 2026/03/16 15:09:26 CST | python | Accepted | 46 ms | 30.4 MB |
| 664516892 | 2025/09/20 18:56:25 CST | python | Accepted | 47 ms | 28.4 MB |
| 664516692 | 2025/09/20 18:55:15 CST | python | Runtime Error | N/A | N/A |
| 664516362 | 2025/09/20 18:53:12 CST | python | Runtime Error | N/A | N/A |
| 664516223 | 2025/09/20 18:52:25 CST | python | Runtime Error | N/A | N/A |
| 664198003 | 2025/09/19 14:49:49 CST | python | Accepted | 51 ms | 28.3 MB |
| 664197883 | 2025/09/19 14:49:30 CST | python | Runtime Error | N/A | N/A |
| 664197682 | 2025/09/19 14:48:55 CST | python | Accepted | 47 ms | 28.4 MB |
| 664197412 | 2025/09/19 14:48:11 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Difference:
    def __init__(self, nums):
        assert len(nums) > 0
        self.diff = [0] * len(nums)
        self.diff[0] = nums[0]
        for i in range(1, len(self.diff)):
            self.diff[i] = nums[i] - nums[i - 1]
    
    def increament(self, i, j, val):
        self.diff[i] += val
        if j + 1 < len(self.diff):
            self.diff[j + 1] -= val
    
    def result(self):
        res = [0] * len(self.diff)
        res[0] = self.diff[0]
        for i in range(1, len(res)):
            res[i] = self.diff[i] + res[i - 1]
        return res

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * n
        df = Difference(res)
        for booking in bookings:
            i = booking[0] - 1
            j = booking[1] - 1
            val = booking[2]
            df.increament(i, j, val)
        return df.result()
```

## 1114. 按序打印 (`print-in-order`)

- 题目链接：https://leetcode.cn/problems/print-in-order/
- 难度：Easy
- 标签：Concurrency
- 总提交次数：4
- 最近提交时间：2025/11/17 17:10:12 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 678720642 | 2025/11/17 17:10:12 CST | python | Accepted | 55 ms | 18 MB |
| 678719832 | 2025/11/17 17:08:53 CST | python | Time Limit Exceeded | N/A | N/A |
| 678467020 | 2025/11/16 16:26:53 CST | python | Accepted | 52 ms | 17.9 MB |
| 678466871 | 2025/11/16 16:26:23 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Foo:
    def __init__(self):
        self.second_sem = threading.Semaphore(0)
        self.third_sem = threading.Semaphore(0)


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.second_sem.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.second_sem.acquire()
        
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.third_sem.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.third_sem.acquire()
        
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
```

## 1117. H2O 生成 (`building-h2o`)

- 题目链接：https://leetcode.cn/problems/building-h2o/
- 难度：Medium
- 标签：Concurrency
- 总提交次数：4
- 最近提交时间：2025/11/17 17:05:49 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 678718743 | 2025/11/17 17:05:49 CST | python | Accepted | 49 ms | 17.9 MB |
| 678609794 | 2025/11/17 10:43:00 CST | python | Accepted | 54 ms | 18.1 MB |
| 678606634 | 2025/11/17 10:32:52 CST | python | Accepted | 57 ms | 17.9 MB |
| 678602532 | 2025/11/17 10:18:25 CST | python | Time Limit Exceeded | N/A | N/A |

### 最近一次 AC 代码

```python
class H2O:
    def __init__(self):
        self.barrier = threading.Barrier(3)
        self.h_sem = threading.Semaphore(2)
        self.o_sem = threading.Semaphore(1)


    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.h_sem.acquire()
        self.barrier.wait()
        
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.h_sem.release()


    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.o_sem.acquire()
        self.barrier.wait()
        
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.o_sem.release()
```

## 1120. 子树的最大平均值 (`maximum-average-subtree`)

- 题目链接：https://leetcode.cn/problems/maximum-average-subtree/
- 难度：Medium
- 标签：Tree, Depth-First Search, Binary Tree
- 总提交次数：1
- 最近提交时间：2026/02/28 12:22:16 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 701156614 | 2026/02/28 12:22:16 CST | python | Accepted | 0 ms | 21.1 MB |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.max_avg = 0
        def dfs(node):
            if not node:
                return 0, 0
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            curr_sum = left_sum + right_sum + node.val
            curr_count = left_count + right_count + 1
            self.max_avg = max(self.max_avg, curr_sum / curr_count)
            return curr_sum, curr_count
        dfs(root)
        return self.max_avg
```

## 1124. 表现良好的最长时间段 (`longest-well-performing-interval`)

- 题目链接：https://leetcode.cn/problems/longest-well-performing-interval/
- 难度：Medium
- 标签：Stack, Array, Hash Table, Prefix Sum, Monotonic Stack
- 总提交次数：7
- 最近提交时间：2026/03/22 21:27:21 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 710673366 | 2026/03/22 21:27:21 CST | python | Accepted | 19 ms | 19.6 MB |
| 710673261 | 2026/03/22 21:27:11 CST | python | Runtime Error | N/A | N/A |
| 707769042 | 2026/03/16 14:10:23 CST | python | Accepted | 24 ms | 19.8 MB |
| 707768194 | 2026/03/16 14:08:32 CST | python | Wrong Answer | N/A | N/A |
| 662484189 | 2025/09/14 09:06:03 CST | python | Accepted | 19 ms | 18.1 MB |
| 662484166 | 2025/09/14 09:05:51 CST | python | Accepted | 31 ms | 18.2 MB |
| 662484097 | 2025/09/14 09:05:12 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        pre_sum = 0
        pre_sum_map = {}
        max_len = 0
        for i, hour in enumerate(hours):
            pre_sum += 1 if hour > 8 else -1
            if pre_sum > 0:
                max_len = max(max_len, i + 1)
            else:
                target = pre_sum - 1
                if target in pre_sum_map:
                    max_len = max(max_len, i - pre_sum_map[target])
            if pre_sum not in pre_sum_map:
                pre_sum_map[pre_sum] = i
        return max_len
```

## 1133. 最大唯一数 (`largest-unique-number`)

- 题目链接：https://leetcode.cn/problems/largest-unique-number/
- 难度：Easy
- 标签：Array, Hash Table, Sorting
- 总提交次数：1
- 最近提交时间：2024/09/05 09:21:16 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 561691562 | 2024/09/05 09:21:16 CST | python | Accepted | 30 ms | 16.7 MB |

### 最近一次 AC 代码

```python
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counts_dict = Counter(nums)
        uniq_nums = [num for num in counts_dict if counts_dict[num] == 1]
        if not uniq_nums:
            return -1
        return max(uniq_nums)
```

## 1134. 阿姆斯特朗数 (`armstrong-number`)

- 题目链接：https://leetcode.cn/problems/armstrong-number/
- 难度：Easy
- 标签：Math
- 总提交次数：1
- 最近提交时间：2026/03/13 18:18:08 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 706673420 | 2026/03/13 18:18:08 CST | python | Accepted | 0 ms | 19 MB |

### 最近一次 AC 代码

```python
class Solution:
    def isArmstrong(self, n: int) -> bool:
        power = len(str(n))
        origin = n
        total = 0
        while n > 0:
            digit = n % 10
            total += digit ** power
            n //= 10
        return total == origin
```

## 1135. 最低成本连通所有城市 (`connecting-cities-with-minimum-cost`)

- 题目链接：https://leetcode.cn/problems/connecting-cities-with-minimum-cost/
- 难度：Medium
- 标签：Union Find, Graph, Minimum Spanning Tree, Heap (Priority Queue)
- 总提交次数：1
- 最近提交时间：2026/04/05 12:07:05 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715269393 | 2026/04/05 12:07:05 CST | python | Accepted | 38 ms | 24.6 MB |

### 最近一次 AC 代码

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True


class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        connections.sort(key=lambda x: x[2])
        uf = UnionFind(n + 1)
        min_cost = 0
        edges = 0
        for x, y, cost in connections:
            if uf.union(x, y):
                min_cost += cost
                edges += 1
                if edges == n - 1:
                    return min_cost
        return -1
```

## 1136. 并行课程 (`parallel-courses`)

- 题目链接：https://leetcode.cn/problems/parallel-courses/
- 难度：Medium
- 标签：Graph, Topological Sort
- 总提交次数：1
- 最近提交时间：2026/03/09 15:47:21 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 704654518 | 2026/03/09 15:47:21 CST | python | Accepted | 15 ms | 21.1 MB |

### 最近一次 AC 代码

```python
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n + 1)]
        indegree = [0] * (n + 1)
        for pre_course, next_course in relations:
            adj_list[pre_course].append(next_course)
            indegree[next_course] += 1
        
        dq = collections.deque()
        for course in range(1, n + 1):
            if indegree[course] == 0:
                dq.append(course)
        
        semesters = 0
        studied_count = 0
        while dq:
            sz = len(dq)
            semesters += 1
            for _ in range(sz):
                course = dq.popleft()
                studied_count += 1
                for next_course in adj_list[course]:
                    indegree[next_course] -= 1
                    if indegree[next_course] == 0:
                        dq.append(next_course)
        return semesters if studied_count == n else -1
```

## 1143. 最长公共子序列 (`longest-common-subsequence`)

- 题目链接：https://leetcode.cn/problems/longest-common-subsequence/
- 难度：Medium
- 标签：String, Dynamic Programming
- 总提交次数：10
- 最近提交时间：2026/04/13 12:23:06 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 717650977 | 2026/04/13 12:23:06 CST | python | Accepted | 359 ms | 43.7 MB |
| 692426247 | 2026/01/19 15:01:09 CST | python | Accepted | 347 ms | 43.6 MB |
| 690693605 | 2026/01/12 09:47:25 CST | python | Accepted | 351 ms | 43.7 MB |
| 688515050 | 2026/01/02 09:02:20 CST | python | Accepted | 491 ms | 41.4 MB |
| 685810610 | 2025/12/19 14:58:47 CST | python | Accepted | 507 ms | 41.4 MB |
| 685810059 | 2025/12/19 14:56:32 CST | python | Wrong Answer | N/A | N/A |
| 685533196 | 2025/12/18 10:00:23 CST | python | Accepted | 526 ms | 41.6 MB |
| 685325987 | 2025/12/17 11:19:58 CST | python | Accepted | 503 ms | 41.9 MB |
| 682063112 | 2025/12/02 09:54:29 CST | python | Accepted | 499 ms | 42 MB |
| 682062863 | 2025/12/02 09:53:23 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]
```

## 1150. 检查一个数是否在数组中占绝大多数 (`check-if-a-number-is-majority-element-in-a-sorted-array`)

- 题目链接：https://leetcode.cn/problems/check-if-a-number-is-majority-element-in-a-sorted-array/
- 难度：Easy
- 标签：Array, Binary Search
- 总提交次数：1
- 最近提交时间：2026/03/03 13:53:01 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 702141182 | 2026/03/03 13:53:01 CST | python | Accepted | 0 ms | 19.2 MB |

### 最近一次 AC 代码

```python
class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        if n == 0:
            return False
        left_bound = bisect.bisect_left(nums, target)
        if left_bound == n or nums[left_bound] != target:
            return False
        check_idx = left_bound + n // 2
        return check_idx < n and nums[check_idx] == target
```

## 1155. 掷骰子等于目标和的方法数 (`number-of-dice-rolls-with-target-sum`)

- 题目链接：https://leetcode.cn/problems/number-of-dice-rolls-with-target-sum/
- 难度：Medium
- 标签：Dynamic Programming
- 总提交次数：10
- 最近提交时间：2026/02/13 15:29:09 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 698401915 | 2026/02/13 15:29:09 CST | python | Accepted | 255 ms | 19.7 MB |
| 693284238 | 2026/01/22 16:57:04 CST | python | Accepted | 251 ms | 19.5 MB |
| 693283987 | 2026/01/22 16:56:21 CST | python | Wrong Answer | N/A | N/A |
| 690117546 | 2026/01/09 11:44:19 CST | python | Accepted | 274 ms | 19.5 MB |
| 690117288 | 2026/01/09 11:43:16 CST | python | Wrong Answer | N/A | N/A |
| 689474273 | 2026/01/06 17:02:44 CST | python | Accepted | 203 ms | 19.2 MB |
| 689474067 | 2026/01/06 17:02:07 CST | python | Wrong Answer | N/A | N/A |
| 689473957 | 2026/01/06 17:01:47 CST | python | Runtime Error | N/A | N/A |
| 689473829 | 2026/01/06 17:01:23 CST | python | Runtime Error | N/A | N/A |
| 689459442 | 2026/01/06 16:21:16 CST | python | Accepted | 319 ms | 19.5 MB |

### 最近一次 AC 代码

```python
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        mod = 10 ** 9 + 7
        for i in range(1, n + 1):
            for j in range(target + 1):
                total = 0
                for x in range(1, min(k, j) + 1):
                    total += dp[i - 1][j - x]
                dp[i][j] = total % mod
        return dp[n][target]
```

## 1161. 最大层内元素和 (`maximum-level-sum-of-a-binary-tree`)

- 题目链接：https://leetcode.cn/problems/maximum-level-sum-of-a-binary-tree/
- 难度：Medium
- 标签：Tree, Depth-First Search, Breadth-First Search, Binary Tree
- 总提交次数：3
- 最近提交时间：2026/02/27 10:11:14 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 700863308 | 2026/02/27 10:11:14 CST | python | Accepted | 21 ms | 22.6 MB |
| 686124246 | 2025/12/21 11:01:30 CST | python | Accepted | 15 ms | 21.1 MB |
| 686054588 | 2025/12/20 21:16:32 CST | python | Accepted | 18 ms | 21.2 MB |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        dq = collections.deque([root])
        level = 1
        max_level = 1
        max_level_sum = float('-inf')
        while dq:
            sz = len(dq)
            level_sum = 0
            for _ in range(sz):
                node = dq.popleft()
                level_sum += node.val
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            if level_sum > max_level_sum:
                max_level_sum = level_sum
                max_level = level
            level += 1
        return max_level
```

## 1165. 单行键盘 (`single-row-keyboard`)

- 题目链接：https://leetcode.cn/problems/single-row-keyboard/
- 难度：Easy
- 标签：Hash Table, String
- 总提交次数：1
- 最近提交时间：2024/09/04 19:53:25 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 561554939 | 2024/09/04 19:53:25 CST | python | Accepted | 40 ms | 16.5 MB |

### 最近一次 AC 代码

```python
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        char_idx_map = {char: idx for idx, char in enumerate(keyboard)}
        time_cost = 0
        current_pos = 0

        for s in word:
            update_pos = char_idx_map.get(s)
            time_cost += abs(update_pos - current_pos)
            current_pos = update_pos
        
        return time_cost
```

## 1167. 连接木棍的最低费用 (`minimum-cost-to-connect-sticks`)

- 题目链接：https://leetcode.cn/problems/minimum-cost-to-connect-sticks/
- 难度：Medium
- 标签：Greedy, Array, Heap (Priority Queue)
- 总提交次数：2
- 最近提交时间：2026/03/12 14:09:28 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 706054867 | 2026/03/12 14:09:28 CST | python | Accepted | 79 ms | 20.1 MB |
| 706054786 | 2026/03/12 14:09:16 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        if len(sticks) == 1:
            return 0
        total_cost = 0
        heapq.heapify(sticks)
        while len(sticks) > 1:
            first = heapq.heappop(sticks)
            second = heapq.heappop(sticks)
            merged = first + second
            total_cost += merged
            heapq.heappush(sticks, merged)
        return total_cost
```

## 1180. 统计只含单一字母的子串 (`count-substrings-with-only-one-distinct-letter`)

- 题目链接：https://leetcode.cn/problems/count-substrings-with-only-one-distinct-letter/
- 难度：Easy
- 标签：Math, String
- 总提交次数：2
- 最近提交时间：2026/03/13 18:39:58 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 706680472 | 2026/03/13 18:39:58 CST | python | Accepted | 0 ms | 18.9 MB |
| 706680341 | 2026/03/13 18:39:34 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def countLetters(self, s: str) -> int:
        total = 0
        count = 0
        for i, ch in enumerate(s):
            if i > 0 and ch == s[i - 1]:
                count += 1
            else:
                count = 1
            total += count
        return total
```

## 1197. 进击的骑士 (`minimum-knight-moves`)

- 题目链接：https://leetcode.cn/problems/minimum-knight-moves/
- 难度：Medium
- 标签：Breadth-First Search
- 总提交次数：1
- 最近提交时间：2026/03/10 09:56:30 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 704970113 | 2026/03/10 09:56:30 CST | python | Accepted | 695 ms | 31 MB |

### 最近一次 AC 代码

```python
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        directions = [
            (2, 1),
            (2, -1),
            (-2, 1),
            (-2, -1),
            (1, 2),
            (1, -2),
            (-1, 2),
            (-1, -2)
        ]
        dq = collections.deque([(0, 0, 0)])
        visited = {(0, 0)}
        while dq:
            row, col, steps = dq.popleft()
            if (row, col) == (x, y):
                return steps
            for dr, dc in directions:
                next_row, next_col = row + dr, col + dc
                if (next_row, next_col) in visited:
                    continue
                if next_row < -2 or next_col < -2:
                    continue
                visited.add((next_row, next_col))
                dq.append((next_row, next_col, steps + 1))
        return -1
```

## 1198. 找出所有行中最小公共元素 (`find-smallest-common-element-in-all-rows`)

- 题目链接：https://leetcode.cn/problems/find-smallest-common-element-in-all-rows/
- 难度：Medium
- 标签：Array, Hash Table, Binary Search, Counting, Matrix
- 总提交次数：9
- 最近提交时间：2026/03/06 14:21:02 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 703407396 | 2026/03/06 14:21:02 CST | python | Accepted | 31 ms | 38.9 MB |
| 562322393 | 2024/09/07 08:49:18 CST | python | Accepted | 64 ms | 37.9 MB |
| 562322376 | 2024/09/07 08:49:01 CST | python | Accepted | 60 ms | 37.9 MB |
| 562202747 | 2024/09/06 17:24:26 CST | python | Accepted | 43 ms | 38.1 MB |
| 562202598 | 2024/09/06 17:24:04 CST | python | Accepted | 55 ms | 38.1 MB |
| 562202476 | 2024/09/06 17:23:45 CST | python | Accepted | 47 ms | 38.1 MB |
| 562201088 | 2024/09/06 17:20:08 CST | python | Accepted | 106 ms | 54.9 MB |
| 562200701 | 2024/09/06 17:19:04 CST | python | Accepted | 52 ms | 37.9 MB |
| 562190547 | 2024/09/06 16:54:43 CST | python | Accepted | 86 ms | 38 MB |

### 最近一次 AC 代码

```python
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        row_count = len(mat)
        counts = collections.defaultdict(int)
        for row in mat:
            for num in row:
                counts[num] += 1
        for num in mat[0]:
            if counts[num] == row_count:
                return num
        return -1
```

## 1214. 查找两棵二叉搜索树之和 (`two-sum-bsts`)

- 题目链接：https://leetcode.cn/problems/two-sum-bsts/
- 难度：Medium
- 标签：Stack, Tree, Depth-First Search, Binary Search Tree, Two Pointers, Binary Search, Binary Tree
- 总提交次数：4
- 最近提交时间：2026/03/06 14:54:47 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 703424838 | 2026/03/06 14:54:47 CST | python | Accepted | 0 ms | 21.7 MB |
| 703424650 | 2026/03/06 14:54:27 CST | python | Runtime Error | N/A | N/A |
| 703424083 | 2026/03/06 14:53:27 CST | python | Wrong Answer | N/A | N/A |
| 701785417 | 2026/03/02 15:17:17 CST | python | Accepted | 7 ms | 21.7 MB |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        if not root1 or not root2:
            return False
        s1 = []
        s2 = []
        def push_left(node):
            while node:
                s1.append(node)
                node = node.left
        def push_right(node):
            while node:
                s2.append(node)
                node = node.right
        push_left(root1)
        push_right(root2)
        while s1 and s2:
            val1 = s1[-1].val
            val2 = s2[-1].val
            if val1 + val2 == target:
                return True
            if val1 + val2 < target:
                node = s1.pop()
                push_left(node.right)
            else:
                node = s2.pop()
                push_right(node.left)
        return False
```

## 1228. 等差数列中缺失的数字 (`missing-number-in-arithmetic-progression`)

- 题目链接：https://leetcode.cn/problems/missing-number-in-arithmetic-progression/
- 难度：Easy
- 标签：Array, Math
- 总提交次数：1
- 最近提交时间：2026/03/03 15:39:56 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 702192455 | 2026/03/03 15:39:56 CST | python | Accepted | 0 ms | 19.3 MB |

### 最近一次 AC 代码

```python
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)
        diff = (arr[-1] - arr[0]) // n
        left, right = 0, n - 1
        while left < right:
            mid = left + (right - left) // 2
            expect = arr[0] + mid * diff
            if expect == arr[mid]:
                left = mid + 1
            else:
                right = mid
        return arr[0] + left * diff
```

## 1231. 分享巧克力 (`divide-chocolate`)

- 题目链接：https://leetcode.cn/problems/divide-chocolate/
- 难度：Hard
- 标签：Array, Binary Search
- 总提交次数：2
- 最近提交时间：2026/03/04 09:57:34 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 702450119 | 2026/03/04 09:57:34 CST | python | Accepted | 47 ms | 20.3 MB |
| 702450033 | 2026/03/04 09:57:17 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        people = k + 1
        total = sum(sweetness)
        def can_make(min_sweet):
            count = 0
            acc = 0
            for s in sweetness:
                acc += s
                if acc >= min_sweet:
                    count += 1
                    acc = 0
                    if count >= people:
                        return True
            return False
        
        left, right = 1, total // people
        while left < right:
            mid = left + (right - left + 1) // 2
            if can_make(mid):
                left = mid
            else:
                right = mid - 1
        return left
```

## 1235. 规划兼职工作 (`maximum-profit-in-job-scheduling`)

- 题目链接：https://leetcode.cn/problems/maximum-profit-in-job-scheduling/
- 难度：Hard
- 标签：Array, Binary Search, Dynamic Programming, Sorting
- 总提交次数：7
- 最近提交时间：2026/03/05 09:56:36 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 702871909 | 2026/03/05 09:56:36 CST | python | Accepted | 107 ms | 32.2 MB |
| 697332374 | 2026/02/08 18:40:38 CST | python | Accepted | 108 ms | 32.1 MB |
| 697332101 | 2026/02/08 18:39:14 CST | python | Wrong Answer | N/A | N/A |
| 696335960 | 2026/02/04 11:44:34 CST | python | Accepted | 105 ms | 32.1 MB |
| 696030054 | 2026/02/03 08:50:28 CST | python | Accepted | 99 ms | 32.6 MB |
| 695844194 | 2026/02/02 14:41:41 CST | python | Accepted | 95 ms | 32 MB |
| 695843930 | 2026/02/02 14:40:52 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(endTime, startTime, profit))
        end_times = [job[0] for job in jobs]
        n = len(end_times)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            end, start, pro = jobs[i - 1]
            pre_jobs = bisect.bisect_right(end_times, start, 0, i)
            dp[i] = max(dp[i - 1], dp[pre_jobs] + pro)
        return dp[n]
```

## 1236. 网络爬虫 (`web-crawler`)

- 题目链接：https://leetcode.cn/problems/web-crawler/
- 难度：Medium
- 标签：Depth-First Search, Breadth-First Search, String, Interactive
- 总提交次数：2
- 最近提交时间：2026/03/09 13:47:00 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 704587609 | 2026/03/09 13:47:00 CST | python | Accepted | 194 ms | 25.7 MB |
| 704587367 | 2026/03/09 13:46:25 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def get_host(url):
            return url.split('/')[2]
        target_host = get_host(startUrl)
        visited = {startUrl}
        dq = collections.deque([startUrl])
        while dq:
            curr_url = dq.popleft()
            for next_url in htmlParser.getUrls(curr_url):
                if get_host(next_url) != target_host:
                    continue
                if next_url in visited:
                    continue
                visited.add(next_url)
                dq.append(next_url)
        return list(visited)
```

## 1254. 统计封闭岛屿的数目 (`number-of-closed-islands`)

- 题目链接：https://leetcode.cn/problems/number-of-closed-islands/
- 难度：Medium
- 标签：Depth-First Search, Breadth-First Search, Union Find, Array, Matrix
- 总提交次数：2
- 最近提交时间：2026/04/10 10:45:28 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 716814311 | 2026/04/10 10:45:28 CST | python | Accepted | 15 ms | 19.8 MB |
| 687588717 | 2025/12/28 08:53:44 CST | python | Accepted | 15 ms | 17.6 MB |

### 最近一次 AC 代码

```python
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(r, c):
            if not (0 <= r < m and 0 <= c < n):
                return
            if grid[r][c] == 1:
                return
            grid[r][c] = 1
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        
        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    res += 1
                    dfs(i, j)
        
        return res
```

## 1259. 不相交的握手 (`handshakes-that-dont-cross`)

- 题目链接：https://leetcode.cn/problems/handshakes-that-dont-cross/
- 难度：Hard
- 标签：Math, Dynamic Programming
- 总提交次数：3
- 最近提交时间：2026/02/25 11:08:24 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 700361336 | 2026/02/25 11:08:24 CST | python | Accepted | 223 ms | 19 MB |
| 700361068 | 2026/02/25 11:07:30 CST | python | Wrong Answer | N/A | N/A |
| 700360862 | 2026/02/25 11:06:49 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        pairs = numPeople // 2
        mod = 10 ** 9 + 7
        dp = [0] * (pairs + 1)
        dp[0] = 1
        for i in range(1, pairs + 1):
            for j in range(i):
                left_counts = dp[j]
                right_counts = dp[i - 1 - j]
                dp[i] = (dp[i] + left_counts * right_counts) % mod
        return dp[pairs]
```

## 1260. 二维网格迁移 (`shift-2d-grid`)

- 题目链接：https://leetcode.cn/problems/shift-2d-grid/
- 难度：Easy
- 标签：Array, Matrix, Simulation
- 总提交次数：2
- 最近提交时间：2026/03/23 13:53:39 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 710866436 | 2026/03/23 13:53:39 CST | python | Accepted | 3 ms | 19.4 MB |
| 708355157 | 2026/03/17 16:40:23 CST | python | Accepted | 3 ms | 19.5 MB |

### 最近一次 AC 代码

```python
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                idx = i * n + j
                new_idx = (idx + k) % total
                new_i = new_idx // n
                new_j = new_idx % n
                res[new_i][new_j] = grid[i][j]
        return res
```

## 1265. 逆序打印不可变链表 (`print-immutable-linked-list-in-reverse`)

- 题目链接：https://leetcode.cn/problems/print-immutable-linked-list-in-reverse/
- 难度：Medium
- 标签：Stack, Recursion, Linked List, Two Pointers
- 总提交次数：1
- 最近提交时间：2026/03/11 17:18:10 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 705696780 | 2026/03/11 17:18:10 CST | python | Accepted | 42 ms | 19.4 MB |

### 最近一次 AC 代码

```python
# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        def dfs(node):
            if not node:
                return
            dfs(node.getNext())
            node.printValue()
        dfs(head)
```

## 1272. 删除区间 (`remove-interval`)

- 题目链接：https://leetcode.cn/problems/remove-interval/
- 难度：Medium
- 标签：Array
- 总提交次数：1
- 最近提交时间：2026/02/26 09:43:33 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 700593666 | 2026/02/26 09:43:33 CST | python | Accepted | 4 ms | 23.9 MB |

### 最近一次 AC 代码

```python
class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        remove_start, remove_end = toBeRemoved
        res = []
        for start, end in intervals:
            if start < remove_start:
                res.append([start, min(end, remove_start)])
            if end > remove_end:
                res.append([max(start, remove_end), end])
        return res
```

## 1302. 层数最深叶子节点的和 (`deepest-leaves-sum`)

- 题目链接：https://leetcode.cn/problems/deepest-leaves-sum/
- 难度：Medium
- 标签：Tree, Depth-First Search, Breadth-First Search, Binary Tree
- 总提交次数：1
- 最近提交时间：2025/12/20 21:24:02 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 686056097 | 2025/12/20 21:24:02 CST | python | Accepted | 15 ms | 19.9 MB |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        dq = collections.deque([root])
        while dq:
            sz = len(dq)
            level_sum = 0
            for _ in range(sz):
                node = dq.popleft()
                level_sum += node.val
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        return level_sum
```

## 1306. 跳跃游戏 III (`jump-game-iii`)

- 题目链接：https://leetcode.cn/problems/jump-game-iii/
- 难度：Medium
- 标签：Depth-First Search, Breadth-First Search, Array
- 总提交次数：3
- 最近提交时间：2025/12/23 11:11:30 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 686565106 | 2025/12/23 11:11:30 CST | python | Accepted | 13 ms | 22.4 MB |
| 686368102 | 2025/12/22 15:02:53 CST | python | Accepted | 7 ms | 22.5 MB |
| 686367985 | 2025/12/22 15:02:31 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0:
            return True
        n = len(arr)
        visited = [False] * n
        dq = collections.deque([start])
        visited[start] = True
        while dq:
            pos = dq.popleft()
            if arr[pos] == 0:
                return True
            for next_pos in [pos - arr[pos], pos + arr[pos]]:
                if 0 <= next_pos < n and not visited[next_pos]:
                    visited[next_pos] = True
                    dq.append(next_pos)
        return False
```

## 1312. 让字符串成为回文串的最少插入次数 (`minimum-insertion-steps-to-make-a-string-palindrome`)

- 题目链接：https://leetcode.cn/problems/minimum-insertion-steps-to-make-a-string-palindrome/
- 难度：Hard
- 标签：String, Dynamic Programming
- 总提交次数：2
- 最近提交时间：2026/01/12 11:04:54 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 690713229 | 2026/01/12 11:04:54 CST | python | Accepted | 187 ms | 20.9 MB |
| 688527691 | 2026/01/02 11:11:57 CST | python | Accepted | 327 ms | 18.5 MB |

### 最近一次 AC 代码

```python
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
        return n - dp[0][n - 1]
```

## 1314. 矩阵区域和 (`matrix-block-sum`)

- 题目链接：https://leetcode.cn/problems/matrix-block-sum/
- 难度：Medium
- 标签：Array, Matrix, Prefix Sum
- 总提交次数：4
- 最近提交时间：2026/03/16 09:53:30 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 707663219 | 2026/03/16 09:53:30 CST | python | Accepted | 12 ms | 20.3 MB |
| 707662870 | 2026/03/16 09:52:38 CST | python | Runtime Error | N/A | N/A |
| 661940425 | 2025/09/12 10:11:43 CST | python | Accepted | 24 ms | 18.7 MB |
| 661940310 | 2025/09/12 10:11:25 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class NumMatrix:
    def __init__(self, matrix):
        m, n = len(matrix), len(matrix[0])
        if not m * n:
            return
        self.pre_sum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.pre_sum[i][j] = self.pre_sum[i - 1][j] + self.pre_sum[i][j - 1] + matrix[i - 1][j - 1] - self.pre_sum[i - 1][j - 1]
    
    def sub_sum(self, x1, y1, x2, y2):
        return self.pre_sum[x2 + 1][y2 + 1] - self.pre_sum[x1][y2 + 1] - self.pre_sum[x2 + 1][y1] + self.pre_sum[x1][y1]


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        res = [[0] * n for _ in range(m)]
        num_matrix = NumMatrix(mat)
        for i in range(m):
            for j in range(n):
                x1 = max(i - k, 0)
                y1 = max(j - k, 0)
                x2 = min(i + k, m - 1)
                y2 = min(j + k, n - 1)
                res[i][j] = num_matrix.sub_sum(x1, y1, x2, y2)
        return res
```

## 1329. 将矩阵按对角线排序 (`sort-the-matrix-diagonally`)

- 题目链接：https://leetcode.cn/problems/sort-the-matrix-diagonally/
- 难度：Medium
- 标签：Array, Matrix, Sorting
- 总提交次数：2
- 最近提交时间：2026/03/23 13:51:07 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 710865478 | 2026/03/23 13:51:07 CST | python | Accepted | 7 ms | 19.5 MB |
| 708342884 | 2026/03/17 16:23:50 CST | python | Accepted | 4 ms | 19.5 MB |

### 最近一次 AC 代码

```python
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        diag = collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                diag[i - j].append(mat[i][j])
        for vals in diag.values():
            vals.sort(reverse=True)
        for i in range(m):
            for j in range(n):
                mat[i][j] = diag[i - j].pop()
        return mat
```

## 1352. 最后 K 个数的乘积 (`product-of-the-last-k-numbers`)

- 题目链接：https://leetcode.cn/problems/product-of-the-last-k-numbers/
- 难度：Medium
- 标签：Design, Array, Math, Data Stream, Prefix Sum
- 总提交次数：4
- 最近提交时间：2026/03/22 17:34:52 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 710578618 | 2026/03/22 17:34:52 CST | python | Accepted | 36 ms | 33.1 MB |
| 707689342 | 2026/03/16 10:45:48 CST | python | Accepted | 36 ms | 33.1 MB |
| 707689173 | 2026/03/16 10:45:30 CST | python | Runtime Error | N/A | N/A |
| 662028263 | 2025/09/12 14:56:13 CST | python | Accepted | 55 ms | 31.2 MB |

### 最近一次 AC 代码

```python
class ProductOfNumbers:

    def __init__(self):
        self.pre_product = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.pre_product = [1]
            return
        self.pre_product.append(self.pre_product[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.pre_product):
            return 0
        return self.pre_product[-1] // self.pre_product[-1-k]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
```

## 1388. 3n 块披萨 (`pizza-with-3n-slices`)

- 题目链接：https://leetcode.cn/problems/pizza-with-3n-slices/
- 难度：Hard
- 标签：Greedy, Array, Dynamic Programming, Heap (Priority Queue)
- 总提交次数：8
- 最近提交时间：2026/02/14 15:49:30 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 698593859 | 2026/02/14 15:49:30 CST | python | Accepted | 119 ms | 20.4 MB |
| 698593800 | 2026/02/14 15:49:13 CST | python | Runtime Error | N/A | N/A |
| 698593756 | 2026/02/14 15:49:03 CST | python | Runtime Error | N/A | N/A |
| 697883520 | 2026/02/11 08:22:48 CST | python | Accepted | 107 ms | 20.4 MB |
| 697714424 | 2026/02/10 14:13:51 CST | python | Accepted | 115 ms | 19.9 MB |
| 697714062 | 2026/02/10 14:12:02 CST | python | Wrong Answer | N/A | N/A |
| 697713854 | 2026/02/10 14:11:00 CST | python | Wrong Answer | N/A | N/A |
| 697713562 | 2026/02/10 14:09:40 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        def max_side_no_adj(nums, k):
            n = len(nums)
            dp = [[0] * (k + 1) for _ in range(n + 1)]
            for i in range(1, n + 1):
                for j in range(1, k + 1):
                    dp[i][j] = dp[i - 1][j]
                    if i >= 2:
                        dp[i][j] = max(dp[i][j], dp[i - 2][j - 1] + nums[i - 1])
                    else:
                        if j == 1:
                            dp[i][j] = max(dp[i][j], nums[0])
            return dp[n][k]

        k = len(slices) // 3
        best_1 = max_side_no_adj(slices[:-1], k)
        best_2 = max_side_no_adj(slices[1:], k)
        return max(best_1, best_2)
```

## 1396. 设计地铁系统 (`design-underground-system`)

- 题目链接：https://leetcode.cn/problems/design-underground-system/
- 难度：Medium
- 标签：Design, Hash Table, String
- 总提交次数：1
- 最近提交时间：2025/11/19 10:42:20 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 679141368 | 2025/11/19 10:42:20 CST | python | Accepted | 55 ms | 28.6 MB |

### 最近一次 AC 代码

```python
class UndergroundSystem:

    def __init__(self):
        # 用于记录乘客的在途信息，key是乘客id，value是(start_station, start_time)
        self.in_map = {}
        # 用于记录两站之间的总耗时和乘车次数，key 是(start_station, end_station)，value 是(total_time, count)
        self.stats = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.in_map[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.in_map.pop(id)
        duration = t - start_time
        key = (start_station, stationName)
        total_time, count = self.stats.get(key, (0, 0))
        self.stats[key] = (total_time + duration, count + 1)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, count = self.stats.get((startStation, endStation))
        return total_time / count
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
```

## 1426. 数元素 (`counting-elements`)

- 题目链接：https://leetcode.cn/problems/counting-elements/
- 难度：Easy
- 标签：Array, Hash Table
- 总提交次数：1
- 最近提交时间：2024/09/06 08:55:28 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 562030512 | 2024/09/06 08:55:28 CST | python | Accepted | 40 ms | 16.5 MB |

### 最近一次 AC 代码

```python
class Solution:
    def countElements(self, arr: List[int]) -> int:
        num_set = set(arr)
        cnt = 0
        for num in arr:
            if num + 1 in num_set:
                cnt += 1
        return cnt
```

## 1427. 字符串的左右移 (`perform-string-shifts`)

- 题目链接：https://leetcode.cn/problems/perform-string-shifts/
- 难度：Easy
- 标签：Array, Math, String
- 总提交次数：9
- 最近提交时间：2026/02/23 21:38:41 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 700046797 | 2026/02/23 21:38:41 CST | python | Accepted | 0 ms | 19.1 MB |
| 700045651 | 2026/02/23 21:33:34 CST | python | Accepted | 0 ms | 19.3 MB |
| 700045438 | 2026/02/23 21:32:42 CST | python | Wrong Answer | N/A | N/A |
| 700045278 | 2026/02/23 21:32:03 CST | python | Wrong Answer | N/A | N/A |
| 700044775 | 2026/02/23 21:29:50 CST | python | Wrong Answer | N/A | N/A |
| 700044551 | 2026/02/23 21:28:50 CST | python | Wrong Answer | N/A | N/A |
| 700042038 | 2026/02/23 21:17:45 CST | python | Wrong Answer | N/A | N/A |
| 557579271 | 2024/08/22 11:41:44 CST | python | Accepted | 36 ms | 16.5 MB |
| 557576027 | 2024/08/22 11:34:02 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        total_shift = 0
        for direction, amount in shift:
            if direction == 0:
                total_shift -= amount
            elif direction == 1:
                total_shift += amount
        n = len(s)
        final_shift = total_shift % n
        return s[-final_shift:] + s[:-final_shift] if final_shift else s
```

## 1429. 第一个唯一数字 (`first-unique-number`)

- 题目链接：https://leetcode.cn/problems/first-unique-number/
- 难度：Medium
- 标签：Design, Queue, Array, Hash Table, Data Stream
- 总提交次数：2
- 最近提交时间：2026/03/11 15:42:08 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 705627979 | 2026/03/11 15:42:08 CST | python | Accepted | 574 ms | 60.3 MB |
| 705625328 | 2026/03/11 15:38:36 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.dq = collections.deque()
        self.count = collections.defaultdict(int)
        for num in nums:
            self.add(num)

    def showFirstUnique(self) -> int:
        while self.dq and self.count[self.dq[0]] > 1:
            self.dq.popleft()
        return self.dq[0] if self.dq else -1
        

    def add(self, value: int) -> None:
        self.dq.append(value)
        self.count[value] += 1
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
```

## 1474. 删除链表 M 个节点之后的 N 个节点 (`delete-n-nodes-after-m-nodes-of-a-linked-list`)

- 题目链接：https://leetcode.cn/problems/delete-n-nodes-after-m-nodes-of-a-linked-list/
- 难度：Easy
- 标签：Linked List
- 总提交次数：1
- 最近提交时间：2026/03/11 15:55:50 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 705638012 | 2026/03/11 15:55:50 CST | python | Accepted | 0 ms | 21.5 MB |

### 最近一次 AC 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        curr = head
        while curr:
            for _ in range(1, m):
                if not curr:
                    return head
                curr = curr.next
            if not curr:
                break
            to_delete = curr.next
            for _ in range(n):
                if not to_delete:
                    break
                to_delete = to_delete.next
            curr.next = to_delete
            curr = to_delete
        return head
```

## 1490. 克隆 N 叉树 (`clone-n-ary-tree`)

- 题目链接：https://leetcode.cn/problems/clone-n-ary-tree/
- 难度：Medium
- 标签：Tree, Depth-First Search, Breadth-First Search, Hash Table
- 总提交次数：1
- 最近提交时间：2026/03/03 11:11:09 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 702090400 | 2026/03/03 11:11:09 CST | python | Accepted | 66 ms | 22.2 MB |

### 最近一次 AC 代码

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return None
        new_root = Node(root.val)
        new_root.children = [self.cloneTree(child) for child in root.children]
        return new_root
```

## 1506. 找到 N 叉树的根节点 (`find-root-of-n-ary-tree`)

- 题目链接：https://leetcode.cn/problems/find-root-of-n-ary-tree/
- 难度：Medium
- 标签：Bit Manipulation, Tree, Depth-First Search, Hash Table
- 总提交次数：1
- 最近提交时间：2026/03/03 11:04:22 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 702087090 | 2026/03/03 11:04:22 CST | python | Accepted | 106 ms | 31.1 MB |

### 最近一次 AC 代码

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        xor_num = 0
        for node in tree:
            xor_num ^= node.val
            for child in node.children:
                xor_num ^= child.val
        for node in tree:
            if node.val == xor_num:
                return node
        return None
```

## 1514. 概率最大的路径 (`path-with-maximum-probability`)

- 题目链接：https://leetcode.cn/problems/path-with-maximum-probability/
- 难度：Medium
- 标签：Graph, Array, Shortest Path, Heap (Priority Queue)
- 总提交次数：3
- 最近提交时间：2026/04/06 15:08:44 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715592110 | 2026/04/06 15:08:44 CST | python | Accepted | 87 ms | 29.7 MB |
| 715591906 | 2026/04/06 15:08:14 CST | python | Wrong Answer | N/A | N/A |
| 715591497 | 2026/04/06 15:07:10 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = collections.defaultdict(list)
        for (u, v), prob in zip(edges, succProb):
            graph[u].append((v, prob))
            graph[v].append((u, prob))
        best = [0.0] * n
        best[start_node] = 1.0

        max_heap = [(-1.0, start_node)]
        while max_heap:
            neg_prob, u = heapq.heappop(max_heap)
            curr_prob = -neg_prob
            if curr_prob < best[u]:
                continue
            if u == end_node:
                return curr_prob
            for v, edge_prob in graph[u]:
                new_prob = curr_prob * edge_prob
                if new_prob > best[v]:
                    best[v] = new_prob
                    heapq.heappush(max_heap, (-new_prob, v))
        return 0.0
```

## 1522. N 叉树的直径 (`diameter-of-n-ary-tree`)

- 题目链接：https://leetcode.cn/problems/diameter-of-n-ary-tree/
- 难度：Medium
- 标签：Tree, Depth-First Search
- 总提交次数：1
- 最近提交时间：2026/02/28 10:42:59 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 701131046 | 2026/02/28 10:42:59 CST | python | Accepted | 62 ms | 20.6 MB |

### 最近一次 AC 代码

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        self.max_diameter = 0
        def get_height(node):
            if not node:
                return 0
            max1 = max2 = 0
            for child in node.children:
                height = get_height(child)
                if height > max1:
                    max2 = max1
                    max1 = height
                elif height > max2:
                    max2 = height
            self.max_diameter = max(self.max_diameter, max1 + max2)
            return max1 + 1
        get_height(root)
        return self.max_diameter
```

## 1533. 找到最大整数的索引 (`find-the-index-of-the-large-integer`)

- 题目链接：https://leetcode.cn/problems/find-the-index-of-the-large-integer/
- 难度：Medium
- 标签：Array, Binary Search, Interactive
- 总提交次数：5
- 最近提交时间：2026/03/04 08:09:39 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 702431714 | 2026/03/04 08:09:39 CST | python | Accepted | 177 ms | 57.2 MB |
| 702431705 | 2026/03/04 08:09:24 CST | python | Runtime Error | N/A | N/A |
| 702162054 | 2026/03/03 14:43:43 CST | python | Accepted | 164 ms | 56.9 MB |
| 702161359 | 2026/03/03 14:42:18 CST | python | Wrong Answer | N/A | N/A |
| 702160797 | 2026/03/03 14:41:03 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        left, right = 0, reader.length() - 1
        while left < right:
            length = right - left + 1
            if length % 2 == 0:
                mid = left + length // 2 - 1
                cmp = reader.compareSub(left, mid, mid + 1, right)
                if cmp > 0:
                    right = mid
                else:
                    left = mid + 1
            else:
                mid = left + length // 2
                cmp = reader.compareSub(left, mid - 1, mid + 1, right)
                if cmp == 0:
                    return mid
                if cmp > 0:
                    right = mid - 1
                else:
                    left = mid + 1
        return left
```

## 1547. 切棍子的最小成本 (`minimum-cost-to-cut-a-stick`)

- 题目链接：https://leetcode.cn/problems/minimum-cost-to-cut-a-stick/
- 难度：Hard
- 标签：Array, Dynamic Programming, Sorting
- 总提交次数：4
- 最近提交时间：2026/02/14 15:29:55 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 698589347 | 2026/02/14 15:29:55 CST | python | Accepted | 307 ms | 19.5 MB |
| 691846442 | 2026/01/16 19:41:17 CST | python | Accepted | 275 ms | 19.4 MB |
| 691259259 | 2026/01/14 14:02:50 CST | python | Accepted | 271 ms | 19.4 MB |
| 691259070 | 2026/01/14 14:02:03 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        pos = [0] + sorted(cuts) + [n]
        m = len(pos)
        dp = [[0] * m for _ in range(m)]
        for gap in range(2, m):
            for i in range(0, m - gap):
                j = i + gap
                cost = pos[j] - pos[i]
                dp[i][j] = float('inf')
                for k in range(i + 1, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j] + cost)
        return dp[0][m - 1]
```

## 1584. 连接所有点的最小费用 (`min-cost-to-connect-all-points`)

- 题目链接：https://leetcode.cn/problems/min-cost-to-connect-all-points/
- 难度：Medium
- 标签：Union Find, Graph, Array, Minimum Spanning Tree
- 总提交次数：1
- 最近提交时间：2026/04/05 15:14:30 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715311214 | 2026/04/05 15:14:30 CST | python | Accepted | 299 ms | 19.3 MB |

### 最近一次 AC 代码

```python
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        in_mst = [False] * n
        min_dist = [float('inf')] * n

        min_dist[0] = 0
        total_cost = 0

        for _ in range(n):
            u = -1
            for i in range(n):
                if not in_mst[i] and (u == -1 or min_dist[i] < min_dist[u]):
                    u = i
            in_mst[u] = True
            total_cost += min_dist[u]

            x1, y1 = points[u]
            for j in range(n):
                if not in_mst[j]:
                    x2, y2 = points[j]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    if dist < min_dist[j]:
                        min_dist[j] = dist
        return total_cost
```

## 1593. 拆分字符串使唯一子字符串的数目最大 (`split-a-string-into-the-max-number-of-unique-substrings`)

- 题目链接：https://leetcode.cn/problems/split-a-string-into-the-max-number-of-unique-substrings/
- 难度：Medium
- 标签：Hash Table, String, Backtracking
- 总提交次数：4
- 最近提交时间：2026/02/22 13:54:07 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 699771394 | 2026/02/22 13:54:07 CST | python | Accepted | 119 ms | 19.5 MB |
| 699771351 | 2026/02/22 13:53:49 CST | python | Runtime Error | N/A | N/A |
| 682783742 | 2025/12/05 09:12:54 CST | python | Accepted | 171 ms | 17.5 MB |
| 682783327 | 2025/12/05 09:09:30 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        best = 0
        used = set()
        def backtrack(start_index, count):
            nonlocal best
            if start_index == n:
                best = max(best, count)
                return
            for end_index in range(start_index + 1, n + 1):
                sub_string = s[start_index : end_index]
                if sub_string in used:
                    continue
                used.add(sub_string)
                backtrack(end_index, count + 1)
                used.remove(sub_string)
        backtrack(0, 0)
        return best
```

## 1609. 奇偶树 (`even-odd-tree`)

- 题目链接：https://leetcode.cn/problems/even-odd-tree/
- 难度：Medium
- 标签：Tree, Breadth-First Search, Binary Tree
- 总提交次数：7
- 最近提交时间：2026/02/27 11:00:41 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 700877334 | 2026/02/27 11:00:41 CST | python | Accepted | 50 ms | 56 MB |
| 700875345 | 2026/02/27 10:54:21 CST | python | Wrong Answer | N/A | N/A |
| 700874627 | 2026/02/27 10:52:06 CST | python | Wrong Answer | N/A | N/A |
| 686126615 | 2025/12/21 11:11:56 CST | python | Accepted | 55 ms | 43.6 MB |
| 686060039 | 2025/12/20 21:44:12 CST | python | Accepted | 51 ms | 43.6 MB |
| 686059998 | 2025/12/20 21:44:02 CST | python | Runtime Error | N/A | N/A |
| 686059368 | 2025/12/20 21:40:47 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        level = 0
        dq = collections.deque([root])
        while dq:
            if level % 2 == 0:
                prev = float('-inf')
            else:
                prev = float('inf')
            sz = len(dq)
            for _ in range(sz):
                node = dq.popleft()
                if level % 2 == 0:
                    if node.val % 2 == 0 or node.val <= prev:
                        return False
                else:
                    if node.val % 2 == 1 or node.val >= prev:
                        return False
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
                prev = node.val
            level += 1
        return True
```

## 1631. 最小体力消耗路径 (`path-with-minimum-effort`)

- 题目链接：https://leetcode.cn/problems/path-with-minimum-effort/
- 难度：Medium
- 标签：Depth-First Search, Breadth-First Search, Union Find, Array, Binary Search, Matrix, Heap (Priority Queue)
- 总提交次数：3
- 最近提交时间：2026/04/06 14:50:44 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715585492 | 2026/04/06 14:50:44 CST | python | Accepted | 243 ms | 20.5 MB |
| 715585262 | 2026/04/06 14:49:59 CST | python | Time Limit Exceeded | N/A | N/A |
| 715585208 | 2026/04/06 14:49:50 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        dist = [[float('inf')] * cols for _ in range(rows)]
        dist[0][0] = 0
        min_heap = [(0, 0, 0)]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while min_heap:
            curr_effort, x, y = heapq.heappop(min_heap)
            if curr_effort > dist[x][y]:
                continue
            if x == rows - 1 and y == cols - 1:
                return curr_effort
            for dr, dc in directions:
                nx, ny = x + dr, y + dc
                if 0 <= nx < rows and 0 <= ny < cols:
                    edge_cost = abs(heights[x][y] - heights[nx][ny])
                    new_effort = max(curr_effort, edge_cost)
                    if new_effort < dist[nx][ny]:
                        dist[nx][ny] = new_effort
                        heapq.heappush(min_heap, (new_effort, nx, ny))
        return 0
```

## 1658. 将 x 减到 0 的最小操作数 (`minimum-operations-to-reduce-x-to-zero`)

- 题目链接：https://leetcode.cn/problems/minimum-operations-to-reduce-x-to-zero/
- 难度：Medium
- 标签：Array, Hash Table, Binary Search, Prefix Sum, Sliding Window
- 总提交次数：13
- 最近提交时间：2026/03/18 10:50:06 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 708664852 | 2026/03/18 10:50:06 CST | python | Accepted | 67 ms | 30.6 MB |
| 708664785 | 2026/03/18 10:49:59 CST | python | Runtime Error | N/A | N/A |
| 708662606 | 2026/03/18 10:46:13 CST | python | Accepted | 81 ms | 30.9 MB |
| 708662445 | 2026/03/18 10:45:54 CST | python | Runtime Error | N/A | N/A |
| 700648913 | 2026/02/26 13:41:47 CST | python | Accepted | 101 ms | 30.4 MB |
| 660962304 | 2025/09/09 13:33:31 CST | python | Accepted | 97 ms | 28.6 MB |
| 660962242 | 2025/09/09 13:33:15 CST | python | Runtime Error | N/A | N/A |
| 660962117 | 2025/09/09 13:32:43 CST | python | Wrong Answer | N/A | N/A |
| 660956388 | 2025/09/09 13:06:44 CST | python | Wrong Answer | N/A | N/A |
| 660956350 | 2025/09/09 13:06:29 CST | python | Wrong Answer | N/A | N/A |
| 660955477 | 2025/09/09 13:02:06 CST | python | Wrong Answer | N/A | N/A |
| 652125693 | 2025/08/12 09:02:17 CST | python | Accepted | 116 ms | 28.8 MB |
| 652125177 | 2025/08/12 08:58:41 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target < 0:
            return -1
        max_len = float('-inf')
        left = 0
        curr_sum = 0
        for right, r_num in enumerate(nums):
            curr_sum += r_num
            while curr_sum > target:
                curr_sum -= nums[left]
                left += 1
            if curr_sum == target:
                max_len = max(max_len, right - left + 1)
        return len(nums) - max_len if max_len != float('-inf') else -1
```

## 1700. 无法吃午餐的学生数量 (`number-of-students-unable-to-eat-lunch`)

- 题目链接：https://leetcode.cn/problems/number-of-students-unable-to-eat-lunch/
- 难度：Easy
- 标签：Stack, Queue, Array, Simulation
- 总提交次数：1
- 最近提交时间：2026/03/29 21:53:46 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 713296010 | 2026/03/29 21:53:46 CST | python | Accepted | 0 ms | 19 MB |

### 最近一次 AC 代码

```python
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = [0, 0]
        for student in students:
            count[student] += 1
        remaining = len(students)
        for sandwich in sandwiches:
            if count[sandwich] == 0:
                return remaining
            remaining -= 1
            count[sandwich] -= 1
        return 0
```

## 1721. 交换链表中的节点 (`swapping-nodes-in-a-linked-list`)

- 题目链接：https://leetcode.cn/problems/swapping-nodes-in-a-linked-list/
- 难度：Medium
- 标签：Linked List, Two Pointers
- 总提交次数：1
- 最近提交时间：2025/12/12 15:59:26 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 684359733 | 2025/12/12 15:59:26 CST | python | Accepted | 35 ms | 39.4 MB |

### 最近一次 AC 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        front = head
        for _ in range(k - 1):
            front = front.next
        # front 先走 k-1 步后，离链表的最后一个节点还有 n - k 步
        first = front
        second = head
        while front.next:
            front = front.next
            second = second.next
        # 此时 second 正好落在了第 n - k + 1 个节点，就是倒数第 k 个节点
        first.val, second.val = second.val, first.val
        return head
```

## 1802. 有界数组中指定下标处的最大值 (`maximum-value-at-a-given-index-in-a-bounded-array`)

- 题目链接：https://leetcode.cn/problems/maximum-value-at-a-given-index-in-a-bounded-array/
- 难度：Medium
- 标签：Greedy, Math, Binary Search
- 总提交次数：11
- 最近提交时间：2026/03/04 11:16:32 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 702485515 | 2026/03/04 11:16:32 CST | python | Accepted | 3 ms | 19.1 MB |
| 702485272 | 2026/03/04 11:15:59 CST | python | Wrong Answer | N/A | N/A |
| 697216503 | 2026/02/08 10:09:42 CST | python | Accepted | 0 ms | 19.4 MB |
| 697021502 | 2026/02/07 10:26:37 CST | python | Accepted | 0 ms | 19.3 MB |
| 696852606 | 2026/02/06 14:10:53 CST | python | Accepted | 2 ms | 19.1 MB |
| 696852561 | 2026/02/06 14:10:42 CST | python | Wrong Answer | N/A | N/A |
| 696852434 | 2026/02/06 14:10:08 CST | python | Accepted | 4 ms | 19.2 MB |
| 696851807 | 2026/02/06 14:07:35 CST | python | Wrong Answer | N/A | N/A |
| 696851516 | 2026/02/06 14:06:22 CST | python | Wrong Answer | N/A | N/A |
| 684334228 | 2025/12/12 14:27:01 CST | python | Accepted | 3 ms | 17.5 MB |
| 684333813 | 2025/12/12 14:25:23 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def side_sum(peak, side_len):
            if peak > side_len:
                return (peak - side_len + peak - 1) * side_len / 2
            dec_len = peak - 1
            dec_sum = (1 + peak - 1) * dec_len / 2
            ones = side_len - dec_len
            return ones + dec_sum

        def min_total_sum(peak):
            left_len = index
            right_len = n - index - 1
            return peak + side_sum(peak, left_len) + side_sum(peak, right_len)

        def feasible(peak):
            return min_total_sum(peak) <= maxSum

        left, right = 1, maxSum - (n - 1)
        while left < right:
            mid = left + (right - left + 1) // 2
            if feasible(mid):
                left = mid
            else:
                right = mid - 1
        return left
```

## 1804. 实现 Trie （前缀树） II (`implement-trie-ii-prefix-tree`)

- 题目链接：https://leetcode.cn/problems/implement-trie-ii-prefix-tree/
- 难度：Medium
- 标签：Design, Trie, Hash Table, String
- 总提交次数：2
- 最近提交时间：2026/04/04 20:10:53 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715150291 | 2026/04/04 20:10:53 CST | python | Accepted | 125 ms | 32.8 MB |
| 715150213 | 2026/04/04 20:10:31 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class TrieNode:
    def __init__(self):
        self.children: dict[str, "TrieNode"] = {}
        self.pass_count = 0
        self.end_count = 0
 
class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.pass_count += 1
        node.end_count += 1

    def countWordsEqualTo(self, word: str) -> int:
        node = self._find_node(word)
        if node is None:
            return 0
        return node.end_count

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self._find_node(prefix)
        if node is None:
            return 0
        return node.pass_count
        

    def erase(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children[ch]
            node.pass_count -= 1
        node.end_count -= 1

    def _find_node(self, s):
        node = self.root
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)
```

## 1836. 从未排序的链表中移除重复元素 (`remove-duplicates-from-an-unsorted-linked-list`)

- 题目链接：https://leetcode.cn/problems/remove-duplicates-from-an-unsorted-linked-list/
- 难度：Medium
- 标签：Hash Table, Linked List
- 总提交次数：1
- 最近提交时间：2025/12/10 10:05:56 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 683822342 | 2025/12/10 10:05:56 CST | python | Accepted | 217 ms | 49.3 MB |

### 最近一次 AC 代码

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: Optional[ListNode]) -> Optional[ListNode]:
        freq: list[int, int] = collections.defaultdict(int)
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        while curr:
            freq[curr.val] += 1
            curr = curr.next
        
        curr = head
        while curr:
            if freq[curr.val] > 1:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        
        return dummy.next
```

## 1905. 统计子岛屿 (`count-sub-islands`)

- 题目链接：https://leetcode.cn/problems/count-sub-islands/
- 难度：Medium
- 标签：Depth-First Search, Breadth-First Search, Union Find, Array, Matrix
- 总提交次数：2
- 最近提交时间：2026/04/10 12:41:08 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 716853500 | 2026/04/10 12:41:08 CST | python | Accepted | 413 ms | 30.9 MB |
| 687602631 | 2025/12/28 10:47:59 CST | python | Accepted | 377 ms | 27.9 MB |

### 最近一次 AC 代码

```python
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])
        def dfs(grid, r, c):
            if not (0 <= r < m and 0 <= c < n):
                return
            if grid[r][c] == 0:
                return
            grid[r][c] = 0
            dfs(grid, r + 1, c)
            dfs(grid, r - 1, c)
            dfs(grid, r, c + 1)
            dfs(grid, r, c - 1)
        
        for i in range(m):
            for j in range(n):
                if grid1[i][j] == 0 and grid2[i][j] == 1:
                    dfs(grid2, i, j)
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    res += 1
                    dfs(grid2, i, j)
        
        return res
```

## 1926. 迷宫中离入口最近的出口 (`nearest-exit-from-entrance-in-maze`)

- 题目链接：https://leetcode.cn/problems/nearest-exit-from-entrance-in-maze/
- 难度：Medium
- 标签：Breadth-First Search, Array, Matrix
- 总提交次数：6
- 最近提交时间：2026/04/05 21:33:24 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715419633 | 2026/04/05 21:33:24 CST | python | Accepted | 75 ms | 20.4 MB |
| 715419554 | 2026/04/05 21:33:06 CST | python | Runtime Error | N/A | N/A |
| 686863840 | 2025/12/24 15:58:51 CST | python | Accepted | 58 ms | 18.9 MB |
| 686572677 | 2025/12/23 11:40:00 CST | python | Accepted | 59 ms | 18.8 MB |
| 686383037 | 2025/12/22 15:51:28 CST | python | Accepted | 55 ms | 19.1 MB |
| 686380255 | 2025/12/22 15:42:29 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        start, end = entrance
        dq = collections.deque([(start, end, 0)])
        maze[start][end] = '+'
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while dq:
            r, c, steps = dq.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < m) or not (0 <= nc < n):
                    continue
                if maze[nr][nc] == '+':
                    continue
                if nr in [0, m-1] or nc in [0, n-1]:
                    return steps + 1
                maze[nr][nc] = '+'
                dq.append((nr, nc, steps + 1))
        return -1
```

## 1987. 不同的好子序列数目 (`number-of-unique-good-subsequences`)

- 题目链接：https://leetcode.cn/problems/number-of-unique-good-subsequences/
- 难度：Hard
- 标签：String, Dynamic Programming
- 总提交次数：9
- 最近提交时间：2026/02/14 14:03:16 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 698572856 | 2026/02/14 14:03:16 CST | python | Accepted | 62 ms | 19.7 MB |
| 694616534 | 2026/01/28 10:16:26 CST | python | Accepted | 63 ms | 19.8 MB |
| 694616099 | 2026/01/28 10:14:34 CST | python | Accepted | 399 ms | 19.7 MB |
| 694343302 | 2026/01/27 09:52:43 CST | python | Accepted | 59 ms | 19.9 MB |
| 694132890 | 2026/01/26 13:43:38 CST | python | Accepted | 63 ms | 19.7 MB |
| 694132866 | 2026/01/26 13:43:29 CST | python | Runtime Error | N/A | N/A |
| 694122804 | 2026/01/26 12:42:33 CST | python | Wrong Answer | N/A | N/A |
| 694122277 | 2026/01/26 12:38:57 CST | python | Wrong Answer | N/A | N/A |
| 694122045 | 2026/01/26 12:37:28 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        end0 = end1 = has_zero = 0
        mod = 10 ** 9 + 7
        for c in binary:
            if c == '1':
                end1 = (end0 + end1 + 1) % mod
            else:
                end0 = (end0 + end1) % mod
                has_zero = 1
        return (end0 + end1 + has_zero) % mod
```

## 2073. 买票需要的时间 (`time-needed-to-buy-tickets`)

- 题目链接：https://leetcode.cn/problems/time-needed-to-buy-tickets/
- 难度：Easy
- 标签：Queue, Array, Simulation
- 总提交次数：3
- 最近提交时间：2026/03/27 08:43:21 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 712435640 | 2026/03/27 08:43:21 CST | python | Accepted | 0 ms | 19.2 MB |
| 712435630 | 2026/03/27 08:43:14 CST | python | Runtime Error | N/A | N/A |
| 712119321 | 2026/03/26 11:32:46 CST | python | Accepted | 0 ms | 19.2 MB |

### 最近一次 AC 代码

```python
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        target = tickets[k]
        res = 0
        for i, count in enumerate(tickets):
            if i <= k:
                res += min(count, target)
            else:
                res += min(count, target - 1)
        return res
```

## 2101. 引爆最多的炸弹 (`detonate-the-maximum-bombs`)

- 题目链接：https://leetcode.cn/problems/detonate-the-maximum-bombs/
- 难度：Medium
- 标签：Depth-First Search, Breadth-First Search, Graph, Geometry, Array, Math
- 总提交次数：5
- 最近提交时间：2025/12/24 16:41:35 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 686883268 | 2025/12/24 16:41:35 CST | python | Accepted | 314 ms | 17.2 MB |
| 686882869 | 2025/12/24 16:40:24 CST | python | Wrong Answer | N/A | N/A |
| 686882425 | 2025/12/24 16:39:05 CST | python | Wrong Answer | N/A | N/A |
| 686881697 | 2025/12/24 16:36:40 CST | python | Wrong Answer | N/A | N/A |
| 686613153 | 2025/12/23 15:05:07 CST | python | Accepted | 315 ms | 17.2 MB |

### 最近一次 AC 代码

```python
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        adj_list = collections.defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                xi, yi, ri = bombs[i]
                xj, yj, _ = bombs[j]
                distance_sq = (xi - xj) ** 2 + (yi - yj) ** 2
                if distance_sq <= ri ** 2:
                    adj_list[i].append(j)
        max_detonation = 0
        for i in range(n):
            dq = collections.deque([i])
            visited = {i}
            while dq:
                curr_bomb = dq.popleft()
                for next_bomb in adj_list[curr_bomb]:
                    if next_bomb not in visited:
                        visited.add(next_bomb)
                        dq.append(next_bomb)
            max_detonation = max(max_detonation, len(visited))
        return max_detonation
```

## 2140. 解决智力问题 (`solving-questions-with-brainpower`)

- 题目链接：https://leetcode.cn/problems/solving-questions-with-brainpower/
- 难度：Medium
- 标签：Array, Dynamic Programming
- 总提交次数：8
- 最近提交时间：2026/02/12 14:22:46 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 698174423 | 2026/02/12 14:22:46 CST | python | Accepted | 43 ms | 54.7 MB |
| 698174275 | 2026/02/12 14:22:06 CST | python | Wrong Answer | N/A | N/A |
| 694615066 | 2026/01/28 10:10:10 CST | python | Accepted | 47 ms | 54.9 MB |
| 694614971 | 2026/01/28 10:09:41 CST | python | Wrong Answer | N/A | N/A |
| 694614721 | 2026/01/28 10:08:41 CST | python | Runtime Error | N/A | N/A |
| 694349057 | 2026/01/27 10:05:02 CST | python | Accepted | 43 ms | 54.8 MB |
| 694348841 | 2026/01/27 10:04:14 CST | python | Wrong Answer | N/A | N/A |
| 694162193 | 2026/01/26 15:25:50 CST | python | Accepted | 62 ms | 54.9 MB |

### 最近一次 AC 代码

```python
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i]
            next_i = i + brainpower + 1
            if next_i > n:
                next_i = n
            dp[i] = max(dp[i + 1], points + dp[next_i])
        return dp[0]
```

## 2320. 统计放置房子的方式数 (`count-number-of-ways-to-place-houses`)

- 题目链接：https://leetcode.cn/problems/count-number-of-ways-to-place-houses/
- 难度：Medium
- 标签：Dynamic Programming
- 总提交次数：5
- 最近提交时间：2026/01/29 13:58:23 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 694934661 | 2026/01/29 13:58:23 CST | python | Accepted | 39 ms | 19 MB |
| 694934223 | 2026/01/29 13:56:35 CST | python | Wrong Answer | N/A | N/A |
| 694613329 | 2026/01/28 10:02:18 CST | python | Accepted | 79 ms | 19 MB |
| 694410159 | 2026/01/27 14:17:45 CST | python | Accepted | 38 ms | 19 MB |
| 694409930 | 2026/01/27 14:17:05 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def countHousePlacements(self, n: int) -> int:
        mod = 10 ** 9 + 7
        prev2, prev1 = 1, 2
        for i in range(2, n + 1):
            curr = (prev2 + prev1) % mod
            prev2, prev1 = prev1, curr
        return (prev1 * prev1) % mod
```

## 2611. 老鼠和奶酪 (`mice-and-cheese`)

- 题目链接：https://leetcode.cn/problems/mice-and-cheese/
- 难度：Medium
- 标签：Greedy, Array, Sorting, Heap (Priority Queue)
- 总提交次数：5
- 最近提交时间：2026/02/05 11:23:23 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 696571077 | 2026/02/05 11:23:23 CST | python | Accepted | 51 ms | 30.4 MB |
| 694905163 | 2026/01/29 11:41:15 CST | python | Accepted | 51 ms | 30.7 MB |
| 694905011 | 2026/01/29 11:40:37 CST | python | Wrong Answer | N/A | N/A |
| 694625811 | 2026/01/28 10:48:42 CST | python | Accepted | 43 ms | 30.6 MB |
| 694625731 | 2026/01/28 10:48:24 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)
        diff = [reward1[i] - reward2[i] for i in range(n)]
        diff.sort(reverse=True)
        return sum(reward2) + sum(diff[:k])
```

## 2787. 将一个数字表示成幂的和的方案数 (`ways-to-express-an-integer-as-sum-of-powers`)

- 题目链接：https://leetcode.cn/problems/ways-to-express-an-integer-as-sum-of-powers/
- 难度：Medium
- 标签：Dynamic Programming
- 总提交次数：14
- 最近提交时间：2026/02/13 15:41:05 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 698405005 | 2026/02/13 15:41:05 CST | python | Accepted | 1031 ms | 23.2 MB |
| 692980107 | 2026/01/21 15:28:08 CST | python | Accepted | 1197 ms | 23.3 MB |
| 692979736 | 2026/01/21 15:27:13 CST | python | Wrong Answer | N/A | N/A |
| 692979559 | 2026/01/21 15:26:43 CST | python | Memory Limit Exceeded | N/A | N/A |
| 690102532 | 2026/01/09 10:51:31 CST | python | Accepted | 1043 ms | 22.1 MB |
| 690102491 | 2026/01/09 10:51:25 CST | python | Runtime Error | N/A | N/A |
| 690102092 | 2026/01/09 10:49:50 CST | python | Wrong Answer | N/A | N/A |
| 690101886 | 2026/01/09 10:49:06 CST | python | Wrong Answer | N/A | N/A |
| 689845429 | 2026/01/08 09:41:25 CST | python | Accepted | 739 ms | 20.9 MB |
| 689844643 | 2026/01/08 09:36:22 CST | python | Wrong Answer | N/A | N/A |
| 689844474 | 2026/01/08 09:35:09 CST | python | Wrong Answer | N/A | N/A |
| 689844337 | 2026/01/08 09:34:10 CST | python | Memory Limit Exceeded | N/A | N/A |
| 689844008 | 2026/01/08 09:31:54 CST | python | Memory Limit Exceeded | N/A | N/A |
| 689843700 | 2026/01/08 09:29:33 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        powers = []
        base = 1
        while base ** x <= n:
            powers.append(base ** x)
            base += 1
        k = len(powers)
        dp = [[0] * (n + 1) for _ in range(k + 1)]
        mod = 10 ** 9 + 7
        dp[0][0] = 1
        for i in range(1, k + 1):
            num = powers[i - 1]
            for j in range(n + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= num:
                    dp[i][j] += dp[i - 1][j - num]
                dp[i][j] %= mod
        return dp[k][n]
```

## 2789. 合并后数组中的最大元素 (`largest-element-in-an-array-after-merge-operations`)

- 题目链接：https://leetcode.cn/problems/largest-element-in-an-array-after-merge-operations/
- 难度：Medium
- 标签：Greedy, Array
- 总提交次数：6
- 最近提交时间：2026/02/06 11:21:27 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 696817979 | 2026/02/06 11:21:27 CST | python | Accepted | 52 ms | 34.4 MB |
| 695154773 | 2026/01/30 11:39:04 CST | python | Accepted | 40 ms | 34.4 MB |
| 695154618 | 2026/01/30 11:38:33 CST | python | Wrong Answer | N/A | N/A |
| 694901822 | 2026/01/29 11:29:52 CST | python | Accepted | 36 ms | 34 MB |
| 694901759 | 2026/01/29 11:29:38 CST | python | Runtime Error | N/A | N/A |
| 694629794 | 2026/01/28 11:01:15 CST | python | Accepted | 52 ms | 34.2 MB |

### 最近一次 AC 代码

```python
class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_num = nums[-1]
        for i in range(n - 2, -1, -1):
            if nums[i] <= max_num:
                max_num += nums[i]
            else:
                max_num = nums[i]
        return max_num
```

## 2915. 和为目标值的最长子序列的长度 (`length-of-the-longest-subsequence-that-sums-to-target`)

- 题目链接：https://leetcode.cn/problems/length-of-the-longest-subsequence-that-sums-to-target/
- 难度：Medium
- 标签：Array, Dynamic Programming
- 总提交次数：11
- 最近提交时间：2026/02/13 15:49:13 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 698407210 | 2026/02/13 15:49:13 CST | python | Accepted | 2394 ms | 28.1 MB |
| 698407021 | 2026/02/13 15:48:30 CST | python | Wrong Answer | N/A | N/A |
| 692977049 | 2026/01/21 15:19:40 CST | python | Accepted | 2597 ms | 28.4 MB |
| 692976866 | 2026/01/21 15:19:10 CST | python | Wrong Answer | N/A | N/A |
| 692976715 | 2026/01/21 15:18:45 CST | python | Wrong Answer | N/A | N/A |
| 692976394 | 2026/01/21 15:17:57 CST | python | Wrong Answer | N/A | N/A |
| 692976295 | 2026/01/21 15:17:43 CST | python | Runtime Error | N/A | N/A |
| 690138972 | 2026/01/09 14:06:38 CST | python | Accepted | 2555 ms | 28.4 MB |
| 689715076 | 2026/01/07 16:41:29 CST | python | Accepted | 2461 ms | 28.2 MB |
| 689714021 | 2026/01/07 16:38:24 CST | python | Runtime Error | N/A | N/A |
| 689713537 | 2026/01/07 16:36:57 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [[float('-inf')] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            num = nums[i - 1]
            for j in range(target + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= num:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - num] + 1)
        return dp[n][target] if dp[n][target] != float('-inf') else -1
```

## 3180. 执行操作可获得的最大总奖励 I (`maximum-total-reward-using-operations-i`)

- 题目链接：https://leetcode.cn/problems/maximum-total-reward-using-operations-i/
- 难度：Medium
- 标签：Array, Dynamic Programming
- 总提交次数：9
- 最近提交时间：2026/02/13 16:00:40 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 698410301 | 2026/02/13 16:00:40 CST | python | Accepted | 943 ms | 80.1 MB |
| 698410083 | 2026/02/13 15:59:52 CST | python | Wrong Answer | N/A | N/A |
| 693010970 | 2026/01/21 16:47:55 CST | python | Accepted | 961 ms | 79.9 MB |
| 690092013 | 2026/01/09 10:08:09 CST | python | Accepted | 1090 ms | 80.1 MB |
| 689133665 | 2026/01/05 11:20:23 CST | python | Accepted | 1065 ms | 77.9 MB |
| 688940015 | 2026/01/04 15:21:57 CST | python | Accepted | 1125 ms | 77.9 MB |
| 688938906 | 2026/01/04 15:18:43 CST | python | Wrong Answer | N/A | N/A |
| 688898232 | 2026/01/04 12:03:41 CST | python | Accepted | 991 ms | 78 MB |
| 688898064 | 2026/01/04 12:02:45 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        values = sorted(set(rewardValues))
        max_value = values[-1]
        limit = 2 * max_value - 1
        n = len(values)
        dp = [[False] * (limit + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            value = values[i - 1]
            for j in range(limit + 1):
                dp[i][j] = dp[i - 1][j]
                prev = j - value
                if prev >= 0 and prev < value and dp[i - 1][prev]:
                    dp[i][j] = True
        for best in range(limit, -1, -1):
            if dp[n][best]:
                return best
```

## 面试题 17.24. 最大子矩阵 (`max-submatrix-lcci`)

- 题目链接：https://leetcode.cn/problems/max-submatrix-lcci/
- 难度：Hard
- 标签：Array, Dynamic Programming, Matrix, Prefix Sum
- 总提交次数：8
- 最近提交时间：2026/02/13 11:30:37 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 698358579 | 2026/02/13 11:30:37 CST | python | Accepted | 1306 ms | 21.2 MB |
| 698358111 | 2026/02/13 11:28:46 CST | python | Wrong Answer | N/A | N/A |
| 698357823 | 2026/02/13 11:27:42 CST | python | Runtime Error | N/A | N/A |
| 698357753 | 2026/02/13 11:27:24 CST | python | Runtime Error | N/A | N/A |
| 697663091 | 2026/02/10 10:04:08 CST | python | Accepted | 1171 ms | 21.1 MB |
| 697482379 | 2026/02/09 14:28:14 CST | python | Accepted | 1172 ms | 21.2 MB |
| 697482171 | 2026/02/09 14:27:27 CST | python | Wrong Answer | N/A | N/A |
| 697481853 | 2026/02/09 14:26:10 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def getMaxMatrix(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        max_sum = float('-inf')
        res = [0, 0, 0, 0]
        for top in range(n):
            col_sum = [0] * m
            for bottom in range(top, n):
                for j in range(m):
                    col_sum[j] += matrix[bottom][j]
                curr_sum = 0
                start_col = 0
                for j in range(m):
                    if curr_sum > 0:
                        curr_sum += col_sum[j]
                    else:
                        curr_sum = col_sum[j]
                        start_col = j
                    if curr_sum > max_sum:
                        max_sum = curr_sum
                        res = [top, start_col, bottom, j]
        return res
```

## LCR 038. 每日温度 (`iIQa4I`)

- 题目链接：https://leetcode.cn/problems/iIQa4I/
- 难度：Medium
- 标签：Stack, Array, Monotonic Stack
- 总提交次数：1
- 最近提交时间：2026/03/25 10:30:54 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 711686355 | 2026/03/25 10:30:54 CST | python | Accepted | 165 ms | 28.1 MB |

### 最近一次 AC 代码

```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []
        for i, num in enumerate(temperatures):
            while stack and num > temperatures[stack[-1]]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return res
```

## LCR 046. 二叉树的右视图 (`WNC0Lk`)

- 题目链接：https://leetcode.cn/problems/WNC0Lk/
- 难度：Medium
- 标签：Tree, Depth-First Search, Breadth-First Search, Binary Tree
- 总提交次数：2
- 最近提交时间：2025/11/26 08:52:36 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 680725087 | 2025/11/26 08:52:36 CST | python | Accepted | 43 ms | 17.4 MB |
| 680725065 | 2025/11/26 08:52:23 CST | python | Runtime Error | N/A | N/A |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        dq = collections.deque([root])
        res = []
        while dq:
            level_size = len(dq)
            for i in range(level_size):
                node = dq.popleft()
                if i == level_size-1:
                    res.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
        return res
```

## LCR 057. 存在重复元素 III (`7WqeDu`)

- 题目链接：https://leetcode.cn/problems/7WqeDu/
- 难度：Medium
- 标签：Array, Bucket Sort, Ordered Set, Sorting, Sliding Window
- 总提交次数：2
- 最近提交时间：2025/11/27 10:33:39 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 681000389 | 2025/11/27 10:33:39 CST | python | Accepted | 127 ms | 19.6 MB |
| 680999552 | 2025/11/27 10:30:42 CST | python | Wrong Answer | N/A | N/A |

### 最近一次 AC 代码

```python
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        window = []
        for i, num in enumerate(nums):
            if i > k:
                old_val = nums[i-k-1]
                idx = bisect.bisect_left(window, old_val)
                window.pop(idx)
            target_val = num - t
            idx = bisect.bisect_left(window, target_val)
            if idx < len(window) and window[idx] <= num + t:
                return True
            bisect.insort(window, num)
        return False
```

## LCR 071. 按权重随机选择 (`cuyjEf`)

- 题目链接：https://leetcode.cn/problems/cuyjEf/
- 难度：Medium
- 标签：Array, Math, Binary Search, Prefix Sum, Randomized
- 总提交次数：1
- 最近提交时间：2026/03/20 19:08:33 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 709832939 | 2026/03/20 19:08:33 CST | python | Accepted | 146 ms | 23.9 MB |

### 最近一次 AC 代码

```python
class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        self.total = 0
        for weight in w:
            self.total += weight
            self.prefix.append(self.total)


    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        return bisect.bisect_left(self.prefix, target)



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
```

## LCR 079. 子集 (`TVdhkn`)

- 题目链接：https://leetcode.cn/problems/TVdhkn/
- 难度：Medium
- 标签：Bit Manipulation, Array, Backtracking
- 总提交次数：3
- 最近提交时间：2026/02/17 20:46:28 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 699067731 | 2026/02/17 20:46:28 CST | python | Accepted | 52 ms | 19.2 MB |
| 699067704 | 2026/02/17 20:46:16 CST | python | Runtime Error | N/A | N/A |
| 685297554 | 2025/12/17 09:32:04 CST | python | Accepted | 52 ms | 17.8 MB |

### 最近一次 AC 代码

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        n = len(nums)
        def backtrack(start_index):
            res.append(list(path))
            for i in range(start_index, n):
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()
        backtrack(0)
        return res
```

## LCR 106. 判断二分图 (`vEAB3K`)

- 题目链接：https://leetcode.cn/problems/vEAB3K/
- 难度：Medium
- 标签：Depth-First Search, Breadth-First Search, Union Find, Graph
- 总提交次数：1
- 最近提交时间：2026/04/05 09:58:12 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 715235361 | 2026/04/05 09:58:12 CST | python | Accepted | 50 ms | 19.6 MB |

### 最近一次 AC 代码

```python
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        colors = [0] * n
        for start in range(n):
            if colors[start] != 0:
                continue
            dq = collections.deque([start])
            colors[start] = 1
            while dq:
                node = dq.popleft()
                for neighbor in graph[node]:
                    if colors[neighbor] == 0:
                        colors[neighbor] = -colors[node]
                        dq.append(neighbor)
                    elif colors[neighbor] == colors[node]:
                        return False
        return True
```

## LCR 133. 位 1 的个数 (`er-jin-zhi-zhong-1de-ge-shu-lcof`)

- 题目链接：https://leetcode.cn/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/
- 难度：Easy
- 标签：Bit Manipulation
- 总提交次数：1
- 最近提交时间：2025/11/19 09:30:14 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 679119507 | 2025/11/19 09:30:14 CST | python | Accepted | 50 ms | 17.5 MB |

### 最近一次 AC 代码

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n = n & (n-1)
            count += 1
        return count
```

## LCR 172. 统计目标成绩的出现次数 (`zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof`)

- 题目链接：https://leetcode.cn/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/
- 难度：Easy
- 标签：Array, Binary Search
- 总提交次数：1
- 最近提交时间：2026/03/18 15:57:37 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 708811061 | 2026/03/18 15:57:37 CST | python | Accepted | 0 ms | 20.5 MB |

### 最近一次 AC 代码

```python
class Solution:
    def countTarget(self, scores: List[int], target: int) -> int:
        left_bound = bisect.bisect_left(scores, target)
        if left_bound == len(scores) or scores[left_bound] != target:
            return 0
        right_bound = bisect.bisect_right(scores, target) - 1
        return right_bound - left_bound + 1
```

## LCR 175. 计算二叉树的深度 (`er-cha-shu-de-shen-du-lcof`)

- 题目链接：https://leetcode.cn/problems/er-cha-shu-de-shen-du-lcof/
- 难度：Easy
- 标签：Tree, Depth-First Search, Breadth-First Search, Binary Tree
- 总提交次数：4
- 最近提交时间：2026/02/28 10:46:14 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 701131950 | 2026/02/28 10:46:14 CST | python | Accepted | 3 ms | 20.2 MB |
| 701131837 | 2026/02/28 10:45:51 CST | python | Runtime Error | N/A | N/A |
| 701131769 | 2026/02/28 10:45:35 CST | python | Runtime Error | N/A | N/A |
| 680723842 | 2025/11/26 08:38:44 CST | python | Accepted | 3 ms | 18.5 MB |

### 最近一次 AC 代码

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def calculateDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_height = self.calculateDepth(root.left)
        right_height = self.calculateDepth(root.right)
        return max(left_height, right_height) + 1
```

## LCR 184. 设计自助结算系统 (`dui-lie-de-zui-da-zhi-lcof`)

- 题目链接：https://leetcode.cn/problems/dui-lie-de-zui-da-zhi-lcof/
- 难度：Medium
- 标签：Design, Queue, Monotonic Queue
- 总提交次数：2
- 最近提交时间：2026/03/26 09:01:55 CST

### 提交记录
| 提交ID | 提交时间 (UTC+08) | 语言 | 结果 | 耗时 | 内存 |
| --- | --- | --- | --- | --- | --- |
| 712065875 | 2026/03/26 09:01:55 CST | python | Accepted | 126 ms | 22.9 MB |
| 711714381 | 2026/03/25 11:23:50 CST | python | Accepted | 34 ms | 22.9 MB |

### 最近一次 AC 代码

```python
class Checkout:

    def __init__(self):
        self.dq = collections.deque()
        self.max_deque = collections.deque()
        

    def get_max(self) -> int:
        if not self.max_deque:
            return -1
        return self.max_deque[0]
        

    def add(self, value: int) -> None:
        self.dq.append(value)
        while self.max_deque and self.max_deque[-1] < value:
            self.max_deque.pop()
        self.max_deque.append(value)
        

    def remove(self) -> int:
        if not self.dq:
            return -1
        value = self.dq.popleft()
        if value == self.max_deque[0]:
            self.max_deque.popleft()
        return value
        


# Your Checkout object will be instantiated and called as such:
# obj = Checkout()
# param_1 = obj.get_max()
# obj.add(value)
# param_3 = obj.remove()
```

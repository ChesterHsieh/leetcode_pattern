from typing import Optional,List
import heapq
import bisect


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_to_tree(ls):
    if not ls:
        return TreeNode(None)
    i = 0
    root = TreeNode(ls[i])
    tmp_queue = [root]
    while tmp_queue:
        i += 1
        node = tmp_queue.pop()
        if not node.val:
            continue

        if 2*i -1 >= len(ls):
            return root
        node.left = TreeNode(ls[2*i-1])
        tmp_queue.append(node.left)

        if 2*i >= len(ls):
            return root
        node.right = TreeNode(ls[2*i])
        tmp_queue.append(node.right)
    return root


null = None


root1 = list_to_tree([1,3,2,5])
root2 = list_to_tree([2,1,3,null,4,null,7])


root2.left.left


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case
        if root1 is None and root2 is None:
            return None
        
        # catching the values of root nodes, if root absert, assign 0
        v1 = root1.val if root1 else 0
        v2 = root2.val if root2 else 0
        
        # creating a new node off of these values
        new_node = TreeNode(v1+v2)
        
        # Fetching the Left Subtree Nodes
        root1_left = root1.left if root1 else None
        root2_left = root2.left if root2 else None
        # merging the Left Subtree
        new_node.left = self.mergeTrees(root1_left, root2_left)
        
        # Fetching the Right Subtree Nodes
        root1_right = root1.right if root1 else None
        root2_right = root2.right if root2 else None
        # merging the Left Subtree
        new_node.right = self.mergeTrees(root1_right, root2_right)
        
        # return the Node created
        return new_node
s = Solution()
t = s.mergeTrees(root1,root2)





root = list_to_tree([1,2,3,4,5,null,6,7,null,null,null,null,8])


def deepestLeavesSum(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    def dfs1(root):
        if not root: return 0
        return max(dfs1(root.left), dfs1(root.right))+1
    def dfs2(root, dep):
        if not root: return
        if dep == max_depth: total+= root.val
        dfs2(root.left, dep+1)
        dfs2(root.right, dep+1)
    total=0
    max_depth = dfs1(root)
    dfs2(root, 1)
    return max_depth


deepestLeavesSum(root)


# Sol 1, two ptr 去窮舉所有結果
class Solution:
    def lengthOfLIS(self, arr: List[int]) -> int:
        dp = [1] * len(arr) #initalize 
        for i in range(len(arr)):
            encounter = 0
            for j in range(i):# i 其實是比最後一個 每次都去跟前面的比較 窮舉所有可能
                print(i,j)
                if arr[i] > arr[j]: 
                    encounter = max(encounter, dp[j]) #跟過去比較的結構, 利用memory
            dp[i] = encounter + 1
            print(f"dp result {dp}")
        
        return max(dp)


Solution().lengthOfLIS([1,2,4,1])


#Sol 2, 進一步優化
bisect.bisect_left([1,2,3],2)


# 動態規劃 -> 遞推, 要思考
input_ls = [1,3,1,4,1,5]

def solver(ls):
    


def minimumDeviation(self, A):
    pq = []
    for a in A:
        heapq.heappush(pq, -a * 2 if a % 2 else -a)
    res = float('inf')
    mi = -max(pq)
    while len(pq) == len(A):
        a = -heapq.heappop(pq)
        res = min(res, a - mi)
        if a % 2 == 0:
            mi = min(mi, a / 2)
            heapq.heappush(pq, -a / 2)
    return res


import heapq


b4_heap = [2,3,1]


heapq.heapify(b4_heap)


b4_heap
# 跟bst 不同 , 左子樹可以>右子數
# 是個inplace操作, 但是操作完還是list 


heapq.heappop(b4_heap)




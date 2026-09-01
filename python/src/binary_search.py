from typing import List

class Solution:
    def classic_binary_search(self, array, target):
        left, right = 0, len(array)-1
        while left <= right:
            mid = left + (right - left) // 2
            if array[mid] == target:
                return mid
            elif array[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
    def binary_search(self, array, target):
        left, right = 0, len(array)
        while left < right:
            mid = left + (right - left) // 2
            if array[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left

    def binary_search_rotated_array(self, array, target):
        left, right = 0, len(array)-1

        while left <= right:
            mid = (left + right) // 2
            if array[mid] == target:
                return mid

            # left side sorted
            if array[left] <= array[mid]:
                # if target is contained in left sorted side, go left
                if array[left] <= target <= array[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # right side sorted
            else:
                # if target is contained in right sorted side, go right
                if array[mid] <= target <= array[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
    
    def binary_search_first_true_index(self, arr: List[int], target: int) -> int:
        left, right = 0, len(arr) - 1
        first_true_index = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] >= target:
                first_true_index = mid
                right = mid - 1
            else:
                left = mid + 1

        return first_true_index
    

s = Solution()
print(s.classic_binary_search([1,2,2,2,3], 2))
print(s.binary_search([1,2,2,2,3], 2))
print(s.binary_search_first_true_index([1,2,2,2,3], 2))

print(s.classic_binary_search([1,2,2,2,4], 3))
print(s.binary_search([1,2,2,2,4], 3))
print(s.binary_search_first_true_index([1,2,2,2,4], 3))
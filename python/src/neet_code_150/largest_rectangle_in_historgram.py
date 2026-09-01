def largestRectangleArea(heights: list[int]) -> int:
    stack = []  # Stores indices
    max_area = 0
    
    # Append a 0 dummy height to flush out remaining elements in stack at the end
    heights.append(0) 
    
    for i, h in enumerate(heights):
        # We found a right boundary (a shorter bar)
        while stack and h < heights[stack[-1]]:
            height = heights[stack.pop()]
            
            # If stack is empty, it means this was the shortest bar seen so far
            # so it can extend all the way back to index -1
            left = stack[-1] if stack else -1
            width = i - left - 1
            
            max_area = max(max_area, height * width)
            
        stack.append(i)
        
    # Restore the original array array modifications
    heights.pop() 
    return max_area

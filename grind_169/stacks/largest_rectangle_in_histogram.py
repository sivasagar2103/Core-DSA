
def largestRectangleArea(heights):
    #extend left and right until a smaller bar blocks it.
    stack = [] #monotonic increasing stack of indices.
    n = len(heights)
    max_area = 0

    for i in range(n):
        #current_bar < top bar of the stack
        while stack and heights[i] < heights[stack[-1]]:
            top = stack.pop()
            height = heights[top]
            if stack:
                width = i - stack[-1] - 1
            else:
                width = i
            max_area = max(max_area, height * width)

        stack.append(i)

    return max_area

# Example
heights = [2,1,5,6,2,3]
print(largestRectangleArea(heights))  # 10

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        

        heights.append(0)

        for i in range(len(heights)):
            while stack and heights[stack[-1]]>heights[i]:
                height = heights[stack.pop()]

                if not stack:
                    width = i
                
                else:
                    width = i - stack[-1] - 1

                max_area = max(max_area,height * width)

            stack.append(i)

        return max_area



















        # n = len(heights)
        # left = 0
        # right = 0
        # max_sum = -float('inf')

        # for i in range(n):
        #     left = i-1
        #     while  left>=0 and  heights[left]>=heights[i]:
        #         left-=1

        #     right = i+1
        #     while  right<n and heights[right]>=heights[i] :
        #         right +=1

        #     area = (right-left-1)*heights[i]

        #     max_sum = max(max_sum,area)
        # return max_sum

                


















#         max_area = 0


#         n = len(heights)

# # Outer loop picks EVERY possible left boundary 'i'
#         for i in range(n):
#             min_height = heights[i]
#     # Inner loop picks EVERY possible right boundary 'j' starting from 'i'
#         for j in range(i, n):
#             min_height = min(min_height, heights[j])
#             area = min_height * (j - i + 1)
#             max_area = max(max_area, area)

#         return max_area

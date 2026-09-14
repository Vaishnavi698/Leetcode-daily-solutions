class Solution:

  def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
    # Check overlap along the X-axis: max(left) < min(right)
    x_overlap = max(rec1[0], rec2[0]) < min(rec1[2], rec2[2])

    # Check overlap along the Y-axis: max(bottom) < min(top)
    y_overlap = max(rec1[1], rec2[1]) < min(rec1[3], rec2[3])

    return x_overlap and y_overlap
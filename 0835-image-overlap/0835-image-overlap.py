from collections import Counter


class Solution:

  def largestOverlap(
      self, img1: list[list[int]], img2: list[list[int]]
  ) -> int:
    n = len(img1)

    # Collect coordinates of all 1s in both images
    points1 = [
        (r, c) for r in range(n) for c in range(n) if img1[r][c] == 1
    ]
    points2 = [
        (r, c) for r in range(n) for c in range(n) if img2[r][c] == 1
    ]

    # Count frequencies of each translation vector (dr, dc)
    count = Counter()
    for r1, c1 in points1:
      for r2, c2 in points2:
        count[(r2 - r1, c2 - c1)] += 1

    # Return the maximum overlap count (0 if no 1s match)
    return max(count.values(), default=0)
def minEatingSpeed(piles, H):
    def can_eat_all(piles, K, H):
        hours = 0
        for pile in piles:
            hours += (pile + K - 1) // K
        return hours <= H
    left, right = 1, max(piles)
    while left < right:
        mid = left + (right - left) // 2
        if can_eat_all(piles, mid, H):
            right = mid
        else:
            left = mid + 1
    return left

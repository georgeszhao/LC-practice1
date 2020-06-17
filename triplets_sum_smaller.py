class Solution(object):
    def countTriplets(arr, n, sum):
        # Sort input array
        arr.sort()
        # Initialize result
        ans = 0
        # Every iteration of loop counts triplet with
        # first element as arr[i].
        for i in range(n - 2):
            # Initialize other two elements as corner elements
            # of subarray arr[j+1..k]
            j, k = i + 1, n - 1
            # Use Meet in the Middle concept
            while j < k:
                # If sum of current triplet is more or equal,
                # move right corner to look for smaller values
                if arr[i] + arr[j] + arr[k] >= sum:
                    k -= 1
                # Else move left corner
                else:
                    # This is important. For current i and j, there
                    # can be total k-j third elements.
                    ans += (k - j)
                    j += 1
        return ans

    if __name__ == '__main__':
        arr = [1, 3, 4, 5, 7]
        n = len(arr)
        sum = 20
        print(countTriplets(arr, n, sum))
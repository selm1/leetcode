def findMedianSortedArrays(nums1, nums2):
    # Make nums1 the smaller array
    if len(nums1) > len(nums2):
        nums2, nums1 = nums1, nums2

    total_length = len(nums1) + len(nums2)
    half = total_length // 2

    # Binary search; work on nums1 the smaller array
    l, r = 0, len(nums1) - 1

    while True:
        m_nums1 = (l + r) // 2
        m_nums2 = half - m_nums1 - 2  # -2 because of the zero index

        # Need to make sure indices are not out of bounds
        left_nums1 = nums1[m_nums1] if m_nums1 >= 0 else float("-infinity")
        right_nums1 = nums1[m_nums1 +
                            1] if (m_nums1 + 1) < len(nums1) else float("infinity")
        left_nums2 = nums2[m_nums2] if m_nums2 >= 0 else float("-infinity")
        right_nums2 = nums2[m_nums2 +
                            1] if (m_nums2 + 1) < len(nums2) else float("infinity")

        # Correct partition
        if left_nums1 <= right_nums2 and left_nums2 <= right_nums1:
            # odd total length case
            if total_length % 2:
                return min(right_nums1, right_nums2)
            # Even total length case
            else:
                return (max(left_nums1, left_nums2) + min(right_nums1, right_nums2)) / 2
        # Bad partition (left_nums1 > right_nums2)
        elif left_nums1 > right_nums2:
            # reduce the size
            r = m_nums1 - 1  # Middle - 1
        # Bad partition (left_nums2 > right_nums1)
        else:
            # increase the size
            l = m_nums1 + 1  # Middle + 1


print(findMedianSortedArrays([1, 2, 3, 4, 5, 6], [1, 2, 3, 4]))

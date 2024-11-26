#!/usr/bin/env python3
import sys

def process_numbers(numbers, threshold):
    nums = list(map(int, numbers.split(',')))
    bitwise_and = nums[0]
    bitwise_or = nums[0]
    bitwise_xor = nums[0]

    for num in nums[1:]:
        bitwise_and &= num
        bitwise_or |= num
        bitwise_xor ^= num

    filtered = [n for n in nums if n > threshold]

    return {
        "AND": bitwise_and,
        "OR": bitwise_or,
        "XOR": bitwise_xor,
        "Filtered": filtered
    }

# change 1 for commit
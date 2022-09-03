# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 14:34:30 2022

@author: HP
"""

def lengthOfLIS(nums):
        sum = 0
        NUMS = nums
        Max = 0
        num = 0
        for i in range(len(nums)):
            NUMS = nums[i+1:] 
            num = nums[i]
            sum = 1
            for j in NUMS:
                if j>num:
                    sum += 1
                    num = j 
            if Max < sum:
                Max = sum
            sum = 0 
#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}   
        for index, value in enumerate(nums):    #对一个列表，既要遍历索引又要遍历元素时,可以利用enumerate实现
            if target - value in dict:          #判断target-value是否在dict中存在，不存在的话，将他加入字典中，也就是最后一句
                return [dict[target - value], index]  
            dict[value] = index    #将键值对加入字典中中
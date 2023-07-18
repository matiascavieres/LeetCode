# recorrer los datos de mi arreglo
# saber su index y su valor
# Saber que numero puede ir restando el chiquiplein
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        # print(f"{nums}, {target}")
        num_dict= enumerate(nums)
        print (list(num_dict))
        nuevoArreglo = [];

        
        for x, num in enumerate(nums, start=0):
            nuevoArreglo.append(x)
            print(x,num)


        for x in nums:
            nuevoArreglo.append(x)

        print (f"{nuevoArreglo} nuevoArreglo")

        return f"{nums}, {target}"


Solution().twoSum([2,7,11,15],9)
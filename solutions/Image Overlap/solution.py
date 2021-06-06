from scipy.ndimage import convolve
import numpy as np
        
class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        B = np.pad(B, len(A), mode='constant', constant_values=(0, 0))
        return np.amax(convolve(B, np.flip(np.flip(A,1),0), mode='constant'))

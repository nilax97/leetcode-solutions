class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& A) {
        int x = A.size();
        int y = A[0].size();
        for(int i=0; i<x; ++i)
        {
            for(int j=0; j<(y+1)/2; ++j)
            {
                int temp = 1-A[i][j]; 
                A[i][j] = 1- A[i][y-j-1];
                A[i][y-j-1] = temp;
            }
        }
        return A;
    }
};

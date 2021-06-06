class Solution {
    public int hammingDistance(int x, int y) {
        int count=0;
        for(;x>0 || y>0;)
        {
            if(x%2 == y%2)
            {
                ;
            }
            else
            {
                count++;
            }
            x/=2;
            y/=2;
        }
        return count;
    }
    
}

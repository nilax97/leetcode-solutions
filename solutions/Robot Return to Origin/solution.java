class Solution {
    public boolean judgeCircle(String moves) {
        int up=0;
        int left=0;
        for(int i=0;i<moves.length();++i)
        {
            char x = moves.charAt(i);
            if(x=='U')
            {
                up++;
            }
            else if(x=='D')
            {
                up--;
            }
            else if(x=='L')
            {
                left++;
            }
            else if(x=='R')
            {
                left--;
            }
        }
        if(up==0 && left ==0)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}

class Solution {
    public int reverse(int x) {
        int sum=0,num=Math.abs(x);
        int r=0;
        while(num!=0){
            r=num%10;
            if(sum>(Integer.MAX_VALUE-r)/10)
            return 0;
            num=num/10;
            sum=sum*10+r;
        }
        return (x<0)?(-sum):sum;
    }
}
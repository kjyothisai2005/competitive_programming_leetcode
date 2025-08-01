class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> arr=new ArrayList<>();
        for(int i=0;i<numRows;i++){
            List<Integer> ar=new ArrayList<>();
            for(int j=0;j<=i;j++){
                if(j==0 || j==i){
                    ar.add(1);
                }
                else{
                   List<Integer> prevRow = arr.get(i - 1);
                   ar.add(prevRow.get(j - 1) + prevRow.get(j));
                }

            }
            arr.add(ar);
        }
        return arr;
    }
}
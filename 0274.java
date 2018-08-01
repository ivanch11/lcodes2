class Solution {
    public int hIndex(int[] citations) {
        Arrays.sort(citations);
        int i = 0;
        int n = citations.length;
        while (i < n && citations[n-i-1] > i){
            i++;
        }
        return i;
    }
}
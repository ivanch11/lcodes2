class Solution {
    public int countPrimes(int n) {
        int count = 0;
        boolean[] nonPrime = new boolean[n];
        for (int i =2; i<n; i++){
            if (!nonPrime[i]){
                count++;
                for (int j = 2; i*j < n; j++){
                    nonPrime[i*j] = true;
                }
            }
        }
        return count;
    }
}
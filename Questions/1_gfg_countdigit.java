class Solution {
    static int evenlyDivides(int n) {
        int count = 0;
        int num = n;
        
        while (n > 0){
            int i = n % 10;
            if (i != 0){ if (num%i == 0) count++;}
            n = n/10;
        }
        return count;
    }
}
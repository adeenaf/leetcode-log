class Solution {
    public int reverse(int x) {
        if (x == 0) {
            return 0;
        }

        int n = Math.abs(x);

        long rev = 0;

        while (n > 0) {
            rev = rev * 10 + n % 10;
            n /= 10;
        }

        if (x < 0) {
            rev = -rev;
        }

        if (rev > Integer.MAX_VALUE || rev < Integer.MIN_VALUE) {
            return 0;
        }

        return (int) rev;
    }
}

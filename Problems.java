public class Problems {
    public static void main(String[] args) {
      Problem10();
    }

    public static void Problem10() {
      int  result = 0;
      isPrime(4);

    }

    public static boolean isPrime(int x) {
      if(x > 1) {
        int n = x / 2;
        for(int i = 0; i < n + 1; i++){
          if(x % i == 0) {
            return false;
          }
        }
        return true;
      } else {
        return false;
      }
    }
}

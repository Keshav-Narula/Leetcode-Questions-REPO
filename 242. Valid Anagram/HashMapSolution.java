class Solution {
    public boolean isAnagram(String s, String t) {
        
        int sl = s.length();
        int tl = t.length();

        int[] lettersCount = new int[26];
        if(sl != tl){
            return false;
        }

        for(int i=0; i < sl; i++){
            lettersCount[s.charAt(i) - 'a']++;
            lettersCount[t.charAt(i) - 'a']--;
        }
        for(int v : lettersCount){
            if(v != 0){
                return false;
            }
        }
        return true;


    }
}

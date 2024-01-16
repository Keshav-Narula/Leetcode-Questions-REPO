class Solution {
    public boolean isAnagram(String s, String t) {
        //stringt cannot have more letters than the string s we are rearranging
        int sl = s.length();
        int tl = t.length();

        if(sl != tl){
            return false;
        }
        Map <Character, Integer> charCountMap = new HashMap < > ();

        for(int i =0; i < sl; i++){
            //get the characters at index i in respective strings, 
            Character sc = s.charAt(i);
            Character tc = t.charAt(i);
            //Increment count of that character in s string and decrement count of char in t string
            charCountMap.put(sc, charCountMap.getOrDefault(sc, 0) + 1);
            charCountMap.put(tc, charCountMap.getOrDefault(tc, 0) - 1);
        }
        //Check if all values for characters keys in map is zero
        //Meaning the characters appeared in string s and t
        for(int v : charCountMap.values()){
            //For each loop, loop through array of values in charCountMap
            if(v != 0){
                return false;
            }
        }
        return true;
 
    }
}

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String,List<String>> ans = new HashMap<>();

        for (String s: strs){
            int[] count = new int[26];
            for (char c:s.toCharArray()){
                count[c-'a']++;
            }

            String key = Arrays.toString(count);
            if(!ans.containsKey(key)){
                ans.put(key,new ArrayList<>());
            }
            ans.get(key).add(s);
        }
        System.out.println(ans.values());
        return new ArrayList<>(ans.values());
    }
}

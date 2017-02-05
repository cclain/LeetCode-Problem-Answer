public class RandomizedSet {
    private HashMap <Integer,Integer> map;
    private ArrayList<Integer> list;
    /** Initialize your data structure here. */
    public RandomizedSet() {
        map=new HashMap <Integer,Integer>();
        list=new ArrayList<Integer>();
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    public boolean insert(int val) {
        if (map.containsKey(val)){
            return false;    
        }else{
            map.put(val,list.size());
            list.add(val);
            return true;
        }
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    public boolean remove(int val) {
        if (map.containsKey(val)){
            int idx=map.get(val);
            int lastone=list.get(list.size()-1);
            map.put(lastone,idx);
            map.remove(val);
            list.set(idx,lastone);
            list.remove(list.size()-1);
            return true;
            
        }else{
            return false;
        }
    }
    
    /** Get a random element from the set. */
    public int getRandom() {
        Random random=new Random();
        return list.get(random.nextInt(list.size()));
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
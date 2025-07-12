// LRUCache.java
class LRUCache {

    private int capacity;
    private Map<Integer,CacheNode> cache;
    private CacheNode head;
    private CacheNode tail;



    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.cache = new HashMap<Integer,CacheNode>();
        this.head = new CacheNode(-1,-1);
        this.tail = new CacheNode(-1,-1);
        this.head.next = tail;
        this.tail.prev = head;
    }
    
    public int get(int key) {
        
        if(!cache.containsKey(key)){
            return -1;
        }

        CacheNode node = this.cache.get(key);

        this.remove(node);
        this.add(node);
        
        return node.value;
    }
    
    public void put(int key, int value) {
        
        if(cache.containsKey(key)){
            CacheNode node = cache.get(key);
            cache.remove(key);
            this.remove(node);
        }

        if(cache.size() == this.capacity){
            cache.remove(this.head.next.key);
            this.remove(this.head.next);
        }

        this.cache.put(key, new CacheNode(key,value));
        this.add(cache.get(key));
    }

    public void remove(CacheNode node){
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    public void add(CacheNode node){
        CacheNode current_end = this.tail.prev;
        current_end.next = node;

        node.prev = current_end;
        node.next = this.tail;
        this.tail.prev = node;
    }
}

public class CacheNode {
    public int key;
    public int value;
    public CacheNode next;
    public CacheNode prev;

    public CacheNode(int key, int value){
        this.key = key;
        this.value = value;
        this.next = null;
        this.prev = null;
    }
}

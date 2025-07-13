// lruCache.ts
class LRUCache {

    private capacity:number;
    private cache:Map<number,CacheNode>;
    private head:CacheNode;
    private tail:CacheNode;


    constructor(capacity: number) {
        this.capacity = capacity;
        this.cache = new Map<number,CacheNode>()
        this.head = new CacheNode(-1,-1);
        this.tail = new CacheNode(-1,-1);
        this.head.next = this.tail;
        this.tail.prev = this.head;
    }

    get(key: number): number {
        
        if(!this.cache.has(key)){
            return -1
        }

        let node = this.cache.get(key)
        this.remove(node)
        this.add(node)
        return node.value;
    }

    put(key: number, value: number): void {
        if(this.cache.has(key)){
            let node = this.cache.get(key)
            this.cache.delete(key)
            this.remove(node)
        }
        
        if(this.cache.size == this.capacity){
            this.cache.delete(this.head.next.key)
            this.remove(this.head.next)
        }

        this.cache.set(key,new CacheNode(key,value))
        this.add(this.cache.get(key))

    }

    remove(node:CacheNode){
        node.prev.next = node.next
        node.next.prev = node.prev
    }

    add(node:CacheNode){
        let current_end:CacheNode = this.tail.prev
        current_end.next = node

        node.prev = current_end
        node.next = this.tail
        this.tail.prev =node
    }
}
class CacheNode {
    public key:number;
    public value:number;
    public next:CacheNode;
    public prev:CacheNode;

    public constructor( key:number, value:number){
        this.key = key;
        this.value = value;
        this.next = null;
        this.prev = null;
    }
}

class LRUCache {
private:
    int capacity;
    unordered_map<int, pair<int, list<int>::iterator>> cache;
    list<int> lru;

public:
    LRUCache(int capacity) {
        this->capacity = capacity;
    }

    int get(int key) {
        if (cache.find(key) == cache.end()) {
            return -1; // Key not found
        }

        // Update the key's position in the LRU list
        lru.erase(cache[key].second);
        lru.push_front(key);
        cache[key].second = lru.begin();

        return cache[key].first;
    }

    void put(int key, int value) {
        if (cache.find(key) != cache.end()) {
            lru.erase(cache[key].second);
        } else if (cache.size() >= capacity) {
            // Cache is full, remove the least recently used key
            int lruKey = lru.back();
            cache.erase(lruKey);
            lru.pop_back();
        }

        lru.push_front(key);
        cache[key] = make_pair(value, lru.begin());
    }
};

def new(new_buckets=256):
    ''' given a no. of buckets that will append into the hashmap'''
    amap=[]
    for i in range(0,new_buckets):
	amap.append([])
    return amap	
def hash_key(amap,key):
    return hash(key)%len(amap)
def get_bucket(amap,key):
    bucket_id=hash_key(amap,key)
    return amap[bucket_id]
def get_slot(amap,key,default=None):
    bucket=get_bucket(amap,key)
    for i,kv in enumerate(bucket):
        k,v=kv
        if key==k:
            return i ,k,v
     return -1 , key , default
   


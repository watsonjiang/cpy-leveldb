import leveldb
import time
payload = 'x' * 16
db = leveldb.LevelDB('testdb')
start = time.perf_counter()
for i in range(0, 1000000):
    db.Put('key{}'.format(i), payload)
end = time.perf_counter()
db.Close()
print("time cost:", end-start)

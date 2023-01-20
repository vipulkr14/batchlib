from concurrent.futures import ThreadPoolExecutor
import sys
from pympler import asizeof

def split_array(arr, chunk_size):
    chunks = []
    for i in range(0,len(arr),chunk_size):
        chunks.append(arr[i:i+chunk_size])
    return chunks

def worker(chunk):
    #processing
    print(chunk)
    for s in chunk:
        print("String: " + s + "Size: " + str(asizeof.asizeof(s)))
        if sys.getsizeof(s) > max_record_size:
            chunk.remove(s)
    print(chunk)
    print("---------------")
    return chunk


def main():
    arr = ['qwerty','pofgvffiuyt','zxsw','qw','qwe','mnbvc','mnbvc','lkjh','lkijuh','plmnbvcx','lokij','lokijn','lkj','po','lkjn','poiu','ag','lo','ytg','qw','poi']
    chunk_size = 3
    chunks=split_array(arr, chunk_size)
    with ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(worker,chunks))
        print(results)

max_record_size = 56 #change it to 1 MB equivalent of bytes
max_batch_size = 170 #change it to 5 MB equivalent of bytes

main()
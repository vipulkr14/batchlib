from concurrent.futures import ThreadPoolExecutor
import sys
from pympler import asizeof

def split_array(arr, chunk_size):
    """Splits the given array arr into batches of size defined by chunk_size"""
    chunks = []
    for i in range(0,len(arr),chunk_size):
        chunks.append(arr[i:i+chunk_size])
    return chunks

def worker(chunk):
    """worker method to filter the larger records and further divide the batch if chunk size is more than the limit"""
    #processing
    result = []
    for s in chunk:
        if asizeof.asizeof(s) > max_record_size:
            chunk.remove(s)
    #print(chunk)
    if asizeof.asizeof(chunk) > max_batch_size:
        """if batch size is more than the minit, furhter processing it to smaller batches starting with half the length"""
        chunks=split_array(chunk, (len(chunk)//2)+1)
        with ThreadPoolExecutor(max_workers=max_thread_pool) as executor:
            results = list(executor.map(worker,chunks))
            #print(results)
            result.extend(results)
    else:
        result.extend(chunk)
    return result

def open_nested_list(list_obj):
    """Converting a nested list object to single list of only single list objects"""
    res = []
    for ele in list_obj:
        if isinstance(ele, list):
            res.extend(open_nested_list(ele))
        else:
            res.append(list_obj)
            break
    return res



def batch_process(arr):
    chunk_size = 3
    chunks=split_array(arr, chunk_size)
    res = []
    with ThreadPoolExecutor(max_workers=max_thread_pool) as executor:
        results = list(executor.map(worker,chunks))
        res = open_nested_list(results)
        print(res)

max_record_size = 56 #change it to 1 MB equivalent of bytes
max_batch_size = 220 #change it to 5 MB equivalent of bytes
max_thread_pool = 4 #max number of threads

arr = ['qwerty','pofgvffiuyt','zxsw','qw','qwe','mnbvc','mnbvc','lkjh','lkijuh','plmnbvcx','lokij','lokijn','lkj','po','lkjn','poiu','ag','lo','ytg','qw','poi']

batch_process(arr)
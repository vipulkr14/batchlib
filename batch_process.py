from concurrent.futures import ThreadPoolExecutor
from pympler import asizeof
from constants import max_batch_size, max_record_size, max_thread_pool, batch_size

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
    for record in chunk:
        if asizeof.asizeof(record) > max_record_size:
            chunk.remove(record)
    #print(chunk)
    if asizeof.asizeof(chunk) > max_batch_size:
        """if batch size is more than the limit, furhter processing it to smaller batches starting with half the length"""
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
    chunks=split_array(arr, batch_size)
    res = []
    with ThreadPoolExecutor(max_workers=max_thread_pool) as executor:
        results = list(executor.map(worker,chunks))
        res = open_nested_list(results)
        print(res)
    return res


arr = ['qwert','pofgvffiuyt','zxsw','qw','qwe','mnbvc','mnbvc','lkjh','lkijuh','plmnbvcx','lokij','lokijn','lkj','po','lkjn','poiu','ag','lo','ytg','qw','poi']

batch_process(arr)
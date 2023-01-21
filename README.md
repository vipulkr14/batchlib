# batchlib

This library splits a large list of records into smaller batches considering size limit of each record and a single batch. 


## Working flow
 - Input a list of records
 - Discard records occupying more memory than the limit
 - Split in smaller batches


## How to use

A list of records can be passed to the method batch_process

```py
from batchProcess import batch_process

arr = ['a', 'b', 'c']
result = batch_process(arr)
```

the result will contain an array of arrays, where each array element is one batch with given constraints


 ## Configurable options
 - Max memory of a record
 - Max size of a single batch
 - Max memory of a single batch
 - Number of parallel threads

 These values can be configured by editing the values in constants.py


### Dependencies
- pympler
- pytest


# batchlib

This library splits a large list of records into smaller batches considering size limit of each record and a single batch. 


## Working flow
 - Input a list of records
 - Discard records occupying more memory than the limit
 - Split in smaller batches

 ## Configurable options
 - Max memory of a record
 - Max size of a single batch
 - Max memory of a single batch
 - Number of parallel threads

 These values can be configured by editing the values in constants.py


### Dependencies
- pympler
- pytest


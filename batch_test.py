import pytest
from batchProcess import batch_process


def test_batch_output():
    arr = ['qwert','pofgvffiuyt','zxsw','qw','qwe','mnbvc','mnbvc','lkjh','lkijuh','plmnbvcx','lokij','lokijn','lkj','po','lkjn','poiu','ag','lo','ytg','qw','poi']
    arr_of_arr = [['qwert', 'zxsw'], ['qw', 'qwe'], ['mnbvc'], ['mnbvc', 'lkjh'], ['lkijuh'], ['lokij', 'lokijn'], ['lkj', 'po'], ['lkjn'], ['poiu', 'ag'], ['lo'], ['ytg', 'qw'], ['poi']]
    result = batch_process(arr)
    assert result == arr_of_arr
# RecSys Dataset

- CiteULike
- PinterestICCV
- Epinions
- Movielens100K
- Movielens1M

## Usage

1. Run `python get_dataset.py`
2. Find data at `recsys_dataset` directory

## Dataset files

- splitted_data_URM_train_original.npz
    - The original training data (no need to use this file)
- splitted_data_URM_train.npz           
    - The training data, a subset of the original training data.
    - Train machine learning models by this data
- splitted_data_URM_validation.npz
    - The validation data, a subset of the original training data.
    - Decide hyper-parameters by this data
- splitted_data_URM_test.npz
    - The test data (items to be recommeded)
    - Compute evaluation metrics by this data and splitted_data_URM_test_negative.npz
- splitted_data_URM_test_negative.npz
    - The test data (items that should not be recommeded)
    - Compute evaluation metrics by this data and splitted_data_URM_test.npz
- splitted_data_file_list
- splitted_data_file_type

## Sample code

```python
>>> import scipy.sparse as sps
# Load training data
>>> train_data = sps.load_npz("recsys_dataset/CiteULike/splitted_data_URM_train.npz")
# There are 5,551 users, 16,980 items, and 193,884 ratings in this dataset
# They are represented by 5,551 x 16,980 matrix with 193,884 non-zero elements.
>>> train_data
<5551x16980 sparse matrix of type '<class 'numpy.float64'>'
        with 193884 stored elements in Compressed Sparse Row format>
# If the i-th user gives the j-th item r_ij point, 
# the value of (i, j) in the matrix is r_ij.
>>> train_data[3].nonzero()
(array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=int32), array([ 709,  721,  756,  776,  892,  895, 2588, 2991, 4973, 5056],
      dtype=int32))
>>> for i, j in zip(*train_data[3].nonzero()):
...     print(i, j, train_data[3][i, j])
... 
0 709 1.0
0 721 1.0
0 756 1.0
0 776 1.0
0 892 1.0
0 895 1.0
0 2588 1.0
0 2991 1.0
0 4973 1.0
0 5056 1.0
```
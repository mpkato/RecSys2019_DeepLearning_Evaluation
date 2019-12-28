import sys
import os
import glob
import shutil

def prepare_all_datasets():
    """
    Prepare all the recsys datasets.
    """
    from Conferences.SIGIR.CMN_our_interface.CiteULike.CiteULikeReader import CiteULikeReader
    from Conferences.SIGIR.CMN_our_interface.Pinterest.PinterestICCVReader import PinterestICCVReader
    from Conferences.SIGIR.CMN_our_interface.Epinions.EpinionsReader import EpinionsReader
    from Conferences.KDD.MCRec_our_interface.Movielens100K.Movielens100KReader import Movielens100KReader
    from Conferences.WWW.NeuMF_our_interface.Movielens1M.Movielens1MReader import Movielens1MReader

    readers = [
        CiteULikeReader, PinterestICCVReader, EpinionsReader, Movielens100KReader, Movielens1MReader,
        ]

    for reader in readers:
        dataset = reader()

def copy_dataset_files():
    """
    Copy files at `Data_manager_split_datasets/<dataset_name>/*/*/*`
    to `recsys_dataset/<dataset_name>/`.
    """
    pwd = os.path.dirname(os.path.abspath(__file__))

    DATA_DIRPATH = os.path.join(pwd, "Data_manager_split_datasets")

    OUTPUT_DIRPATH = os.path.join(pwd, "recsys_dataset")
    if not os.path.exists(OUTPUT_DIRPATH):
        os.mkdir(OUTPUT_DIRPATH)

    for dataset_dirpath in glob.glob(os.path.join(DATA_DIRPATH, "*")):
        dirname = os.path.basename(dataset_dirpath)
        new_dirpath = os.path.join(OUTPUT_DIRPATH, dirname)
        if not os.path.exists(new_dirpath):
            os.mkdir(new_dirpath)
        for filepath in glob.glob(os.path.join(dataset_dirpath, "*", "*", "*")):
            filename = os.path.basename(filepath)
            shutil.copyfile(filepath, os.path.join(new_dirpath, filename))

if __name__ == '__main__':
    prepare_all_datasets()
    copy_dataset_files()
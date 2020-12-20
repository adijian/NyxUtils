from Nyx_Utilities import Nyx_File_Parse_Utils as nyx
import pytest

filepath_with_name = r"test_dirs/one file/build_log_nrf52_ble_s112_10040_boot.txt"
filepath_wrong_name = r"test_dirs/one file/bu"
word = ' '
filepath_two_modified = r"test_dirs/two files modified at same time"
filepath_3_files = r"test_dirs/3 files"
filepath6 = r""
filetype1 = '.txt'
word_list = ('word', 'one', ' ')


@pytest.fixture()
def open_file(filepath):
    # set-up function - open file
    return nyx.open_file(filepath)


@pytest.fixture()
def check_if_file_exists(filepath):
    # check if file exists = true
    yield
    return nyx.check_if_path_exists(filepath)


def test_check_if_exists():
    # check if file exists = true
    assert nyx.check_if_path_exists(filepath_with_name)


@pytest.mark.xfail(strict=True)
def test_fail_to_check_if_file_exists(open_file):
    # fail checking file exists on purpose
    assert not nyx.check_if_path_exists(filepath_wrong_name)


def test_find_word_in_txt():
    occurrences = nyx.find_word_in_txt(filepath_with_name, word)
    assert occurrences > 0  # count if number of words is larger than 0


def test_find_last_modified():
    modified = nyx.find_last_modified(filepath_3_files)
    assert nyx.check_if_path_exists(modified)  # find true to pass


def test_find_last_modified_between_two_files():
    # 3 files exist and are last modified at the same time
    two_modified = nyx.find_last_modified(filepath_two_modified)
    assert nyx.check_if_path_exists(two_modified)  # find true to pass


def test_find_file_by_dir():
    nyx.find_file_by_dir(filepath_3_files, filetype1)
    assert nyx.check_if_path_exists(filepath_3_files)  # find true to pass

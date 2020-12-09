from Nyx_Utilities import Nyx_File_Parse_Utils as nyx
import pytest

filepath2 = r"C:\Users\shoog\Documents\Python work\Python work 12.8\Python\Browse txt\build_log_nrf52_ble_s112_10040_boot.txt"
filepath3 = r"C:\Users\shoog\Documents\Python work\Python work 12.8\Python\Browse txt\build_log_nrf52_ble_s112_10040_boo.txt"


@pytest.fixture()
def open_file():
    # set-up function - open file
    nyx.open_file(filepath2)


def test_open_file_and_check_if_exists(open_file):
    # check if file exists = true
    assert nyx.check_if_path_exists(filepath2)


@pytest.mark.xfail(strict=True)
def test_fail_to_check_if_file_exists(open_file):
    # fail checking file exists on purpose
    assert not (nyx.check_if_path_exists(filepath3))

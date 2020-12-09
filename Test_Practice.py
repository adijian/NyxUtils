import Nyx_Utilities as nyx
import pytest

filepath2 = r"C:\Users\shoog\PycharmProjects\Jian\build_log_nrf52_ble_s112_10040_boot.txt"
filepath3 = r"C:\Users\shoog\PycharmProjects\Jian\build_log_nrf52_ble_s112_10040_boo.txt"


def test_1():
    assert nyx.Nyx_File_Parse_Utils.check_if_path_exists(filepath2)


@pytest.mark.xfail(strict=True)
def test_2():
    assert not (nyx.Nyx_File_Parse_Utils.check_if_path_exists(filepath3))

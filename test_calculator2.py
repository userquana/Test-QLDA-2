import pytest
import tkinter as tk
from calculator import Calculator

@pytest.fixture
def calc():
    root = tk.Tk()
    calculator = Calculator(root)
    yield calculator
    root.destroy()


def test_nhap_so_don(calc):
    calc.add_to_expression('5')
    assert calc.expression == '5'


def test_nhap_nhieu_so(calc):
    calc.add_to_expression('1')
    calc.add_to_expression('2')
    calc.add_to_expression('3')
    assert calc.expression == '123'


def test_nhap_so_thap_phan(calc):
    calc.add_to_expression('5')
    calc.add_to_expression('.')
    calc.add_to_expression('5')
    assert calc.expression == '5.5'


def test_nhap_0_dau_tien(calc):
    calc.add_to_expression('0')
    calc.add_to_expression('0')
    calc.add_to_expression('7')
    assert calc.expression == '7'  


def test_cong_hai_so_duong(calc):
    calc.expression = "5+3"
    calc.calculate()
    assert calc.expression == "8"


def test_cong_voi_0(calc):
    calc.expression = "5+0"
    calc.calculate()
    assert calc.expression == "5"


def test_cong_so_thap_phan(calc):
    calc.expression = "5.5+2.5"
    calc.calculate()
    assert calc.expression == "8.0"


def test_cong_bat_dau_bang_phep_toan(calc):
    calc.expression = "+5"
    calc.calculate()
    assert calc.expression == "5" 


def test_tru_hai_so_duong(calc):
    calc.expression = "10-3"
    calc.calculate()
    assert calc.expression == "7"


def test_tru_thanh_so_am(calc):
    calc.expression = "3-10"
    calc.calculate()
    assert calc.expression == "-7"


def test_tru_bang_0(calc):
    calc.expression = "5-5"
    calc.calculate()
    assert calc.expression == "0"


def test_tru_ket_thuc_bang_phep_toan(calc):
    calc.expression = "5-"
    calc.calculate()
    assert calc.expression != ""


def test_nhan_hai_so_duong(calc):
    calc.expression = "5*3"
    calc.calculate()
    assert calc.expression == "15"


def test_nhan_voi_0(calc):
    calc.expression = "5*0"
    calc.calculate()
    assert calc.expression == "0"


def test_nhan_so_am(calc):
    calc.expression = "-5*3"
    calc.calculate()
    assert calc.expression == "-15"

def test_chia_hai_so_duong(calc):
    calc.expression = "10/2"
    calc.calculate()
    assert calc.expression == "5.0"


def test_chia_khong_het(calc):
    calc.expression = "5/2"
    calc.calculate()
    assert calc.expression == "2.5"


def test_chia_0_cho_so(calc):
    calc.expression = "0/5"
    calc.calculate()
    assert calc.expression == "0.0"


def test_chia_cho_0(calc):
    calc.expression = "5/0"
    calc.calculate()
    assert calc.expression == "" 

def test_phep_toan_phan_tram(calc):
    calc.expression = "10%3"
    calc.calculate()
    assert calc.expression == "0.1"  


def test_phep_phan_tram_sau_so(calc):

    calc.expression = "50%"
    calc.calculate()
    assert calc.expression == "0.5" 


def test_xoa_toan_bo(calc):
    calc.expression = "123"
    calc.clear()
    assert calc.expression == ""


def test_xoa_tung_ky_tu(calc):
    calc.expression = "123"
    calc.backspace()
    assert calc.expression == "12"

def test_can_bac_2(calc):
    calc.expression = "16"
    calc.square_root()
    assert calc.expression == "4.0"


def test_can_bac_2_cua_0(calc):
    calc.expression = "0"
    calc.square_root()
    assert calc.expression == "0.0"  


def test_binh_phuong(calc):
    calc.expression = "5"
    calc.square()
    assert calc.expression == "25.0"


def test_doi_dau_so_0(calc):
    calc.expression = "0"
    calc.toggle_sign()
    assert calc.expression == "0"

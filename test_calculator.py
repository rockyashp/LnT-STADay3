import pytest
from calculator import add,sub,mul

def test_add():
  assert add(4,5)==9
  assert add(1,2)==3

def test_sub():
  assert sub(5,2)==3
  assert sub(4,2)==2

def test_mul():
  assert mul(5,2)==10
  assert mul(8,2)==16
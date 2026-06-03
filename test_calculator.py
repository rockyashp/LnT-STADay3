import pytest
from calculator import add,sub

def test_add():
  assert add(4,5)==9
  assert add(1,2)==3

def test_sub():
  assert sub(5,2)==3
  assert sub(4,2)==2
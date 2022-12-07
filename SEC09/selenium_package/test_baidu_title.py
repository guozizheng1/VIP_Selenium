import pytest

def test_baidu_title(selenium):
    selenium.get('https://www.baidu.com')
    title = selenium.title
    assert '百度' in title
# coding:utf-8
import sys
from selenium import webdriver

sys.path.append(r'D:\student\pycharm\项目\seleniumstduy')
from poium import Page, PageElement


class Select_Page(Page):
    search_move = PageElement(xpath='//*[@id="u1"]/a[9]', log=True, describe='悬停至设置按钮')
    search_s = PageElement(css='.setpref[href^=javas]', log=True, describe='搜索设置按钮')
    search_results = PageElement(css='td>select[id=nr]', log=True, describe='搜索结果显示条目')
    search_savebutton = PageElement(css='div>a[class$=elgo]', log=True, describe='保存按钮')
    search_input = PageElement(css='.s_ipt', log=True, describe='百度输入框')
    search_button = PageElement(xpath="//input[@id='su']", log=True, describe='百度一下按钮')
    search_id10 = PageElement(css="//*[@id='10']", log=True, describe='搜索条目为10')
    search_id20 = PageElement(xpath="//*[@id='20']", log=True, describe='搜索条目为20')
    search_id50 = PageElement(xpath="//*[@id='50']", log=True, describe='搜索条目为50')

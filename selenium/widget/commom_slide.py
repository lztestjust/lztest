from time import sleep

from ..widget_slide import *


def slide_choose_by_text(driver, els, txt, max_cnt, pos: int = 0):
    """ slide 选择控件 上滑(只是针对某个【控件1】操作的取名)

    根据 元素文本 对比，选中一致的元素
    可用于 保额、保障时间、缴费时间 的选择

    :param driver:      WebDriver
    :param els:         WebElements
    :param txt:         str:    文本参数
    :param max_cnt:     int:    至多滑动次数
    :param pos:         int:    开始滑动位置
    :return:
    """
    for i in range(max_cnt + 1):
        if els[pos].text.strip() == txt:
            break
        slide_vertical_2(driver, els, pos, 36, 0.3)
        sleep(0.5)
        pos += 1
        # sleep(0.5)


def slide_choose_by_index(driver, els, index, pos: int = 0):
    """ slide 选择控件 上滑 (只是针对某个【控件1】操作的取名)

    根据 索引位置，选中对应索引位置的元素

    :param driver:
    :param els:
    :param index:
    :param pos:
    :return:
    """
    for i in range(index):
        slide_vertical_2(driver, els, pos, 36, 0.3)
        sleep(0.5)
        pos += 1
    # print(els[pos - 1].text)


def slide_choose_by_text_old(driver, els, txt, max_cnt, pos: int = 0, panel_visible_item_num: int = 0):
    """ slide 选择控件-老版本(只是针对某个【控件0】操作的取名)

    根据 元素文本 对比，选中一致的元素
    可用于 地址 的选择

    :param driver:      WebDriver
    :param els:         WebElements
    :param txt:         str:    文本参数
    :param max_cnt:     int:    至多滑动次数
    :param pos:         int:    开始滑动位置
    :param panel_visible_item_num:         int:    面板可见列数量
    :return:
    """
    if panel_visible_item_num:
        max_cnt -= panel_visible_item_num
    if max_cnt > 0:
        for i in range(max_cnt + 1):
            if els[pos].text.strip() == txt:
                els[pos].click()
                break
            slide_vertical_2(driver, els, pos)
            sleep(0.8)
            pos += 1
    else:
        for i in els:
            print(i.text)
            if i.text.strip() == txt:
                i.click()
                break


# 日期控件
def slide_birth(driver, els, count, pos):
    """日期控件滑动-新模板(只是针对某个【控件1】操作的取名)

    根据 元素、滑动次数和起始位置 滑动

    :param driver:      WebDriver
    :param els:         WebElements
    :param count:       int:    滑动次数, 大于0 上滑， 小于0 下滑
    :param pos:         int:    开始滑动位置
    :return:
    """
    if count > 0:
        for i in range(count):
            slide_vertical_2(driver, els, pos, 36, 0.3)
            # sleep(0.5)
            pos += 1
    else:
        for i in range(abs(count)):
            slide_vertical_2(driver, els, pos, 36, 0.3, False)
            # sleep(0.5)
            pos -= 1


def slide_birth_old_two(driver, el, count: int = 1):
    """日期控件滑动-老模板(只是针对某个【控件0】操作的取名)

    根据 元素和滑动次数 滑动

    :param driver:      WebDriver
    :param el:          WebElements
    :param count:       int:    滑动次数, 大于 0 上滑， 小于0 下滑
    :return:
    """
    result = True

    # 创建动作链
    action = ActionChains(driver)
    # 点击元素并保持住
    action.click_and_hold(el)
    if count > 0:
        for i in range(count):
            if result:
                result = slide_and_hold(action)
                # 释放元素
                action.release(el).perform()
                # 延迟 0.4s
                sleep(0.4)
    elif count < 0:
        for i in range(abs(count)):
            if result:
                result = slide_and_hold(action, order=False)
                # 释放元素
                action.release(el).perform()
                # 延迟 0.4s
                sleep(0.4)


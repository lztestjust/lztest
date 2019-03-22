from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


def slide_horizontal_2(driver, els, pos: int = 0, step: int = 74, pause: float = 0.5, order: bool = True):
    """水平滑动,有时可能会因为 action 或 页面的问题无法使用 _slide_horizontal，此时使用此方法

    :param driver:      WebDriver
    :param els:         WebElements
    :param pos:         默认 0，索引开始位置
    :param step:        步长 单位像素
    :param pause:       暂停时长 单位秒
    :param order:       默认 False， 滑动方向；False 向右滑动
    :return:
    """
    action = ActionChains(driver)
    if order:
        action.click_and_hold(els[pos]).move_by_offset(step, 0).pause(pause).release(els[pos]).perform()
    else:
        action.click_and_hold(els[pos]).move_by_offset(-step, 0).pause(pause).release(els[pos]).perform()


def slide_vertical_2(driver, els, pos: int = 0, step: int = 74, pause: float = 0.5, order: bool = True):
    """垂直滑动 有时可能会因为 action 或 页面的问题无法使用 _slide_vertical，此时使用此方法

    :param driver:      WebDriver
    :param els:         WebElements
    :param pos:         默认 0，索引开始位置
    :param step:        步长 单位像素
    :param pause:       暂停时长 单位秒
    :param order:       默认 False， 滑动方向；False 向上滑动
    :return:
    """
    action = ActionChains(driver)
    if order:
        action.click_and_hold(els[pos]).move_by_offset(0, -step).pause(pause).release(els[pos]).perform()
    else:
        action.click_and_hold(els[pos]).move_by_offset(0, step).pause(pause).release(els[pos]).perform()


def slide_horizontal(action, el, step: int = 74, pause: float = 0.5, order: bool = True):
    """水平滑动
    默认向右滑动 74 像素
    :param action: ActionChains 实例
    :param el: WebElement 实例 被滑动元素
    :param step: 步长 单位像素
    :param pause: 暂停时长 单位秒
    :param order: 步长方向
    :return:
    """
    if not order:
        step = -step

    action.click_and_hold(el).move_by_offset(step, 0).pause(pause).release(el).perform()


def slide_vertical(action, el, step: int = 74, pause: float = 0.5, order: bool = True):
    """垂直滑动
    默认向上滑动 74 像素
    :param action: ActionChains 实例
    :param el: WebElement 实例 被滑动元素
    :param step: 步长 单位像素
    :param pause: 暂停时长 单位秒
    :param order: 步长方向
    :return:
    """
    if order:
        step = -step

    action.click_and_hold(el).move_by_offset(0, step).pause(pause).release(el).perform()


def slide_(action, el, step: int = 74, pause: float = 0.5, order: bool = True, direction: bool = True):
    """上下左右滑动
    默认向上滑动 74 像素
    :param action: ActionChains 实例
    :param el: WebElement 实例 被滑动元素
    :param step: 步长 单位像素
    :param pause: 暂停时长 单位秒
    :param order: 步长方向
    :param direction: 滑动方向
    :return:
    """
    if direction:
        if order:
            step = -step
        action.click_and_hold(el).move_by_offset(0, step).pause(pause).release(el).perform()
    else:
        if not order:
            step = -step
        action.click_and_hold(el).move_by_offset(step, 0).pause(pause).release(el).perform()


def slide_and_hold(action, step: int = 5, order: bool = True, direction: bool = True):
    """上下左右滑动并保持 action，默认向上滑动

    :param action: ActionChains 实例
    :param step: 步长 单位像素
    :param order: 步长方向
    :param direction: 滑动方向
    :return:
    """
    # 返回值
    result = True

    # 上下滑动
    if direction:
        if order:
            step = -step
        for i in range(6):
            try:
                # 移动 5个像素的距离
                action.move_by_offset(0, step).perform()
            except Exception as e:
                print(e)
                # 返回值
                result = False
            # 去掉最后一个动作
            action.reset_actions()
            # 每滑动 5个像素等待 0.08s ，越小越顺滑
            sleep(0.08)
    # 左右滑动
    else:
        if not order:
            step = -step
        for i in range(6):
            try:
                # 移动 5个像素的距离
                action.move_by_offset(step, 0).perform()
            except Exception as e:
                print(e)
                # 返回值
                result = False
            # 去掉最后一个动作
            action.reset_actions()
            # 每滑动 5个像素等待 0.08s ，越小越顺滑
            sleep(0.08)

    # 返回值
    return result

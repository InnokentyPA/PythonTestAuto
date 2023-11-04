import time
import yaml
from module import Site

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

site = Site(testdata["address"])

def test_add_post(x_selector1, x_selector2, x_selector4, btn_selector, add_post_selector, add_title, add_description,
                  add_content, save_post, check_title, title_name):

    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys(testdata["login"])
    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys(testdata["pswd"])
    btn = site.find_element("css", btn_selector)
    btn.click()

    time.sleep(testdata["sleep_time"])
    
import time

import pytest
from playwright.sync_api import Playwright


class AllElements:
    def __init__(self,playwright:Playwright):
        self.browser = playwright.chromium.launch(headless= False, args=["--start-maximized"])
        self.context = self.browser.new_context(no_viewport= True)
        self.page = self.context.new_page()

    def elementscall(self):
        self.page.goto("https://testautomationsite.in/testelements.html")
        self.page.locator('#text-input').fill("Test Text")
        self.page.get_by_role('textbox', name = "password").fill("Pass123@")
        self.page.get_by_placeholder("Enter multi-line text").fill("Lorem Ipsum")
        self.page.locator("#dropdown").select_option('option2')
        self.page.locator('input[type="radio"][value="radio2"]').check()
        self.page.locator('input[type="checkbox"][value="check1"]').check()
        spin_input = self.page.locator('#spin-button')
        spin_input.click()
        #time.sleep(1)
        spin_input.type("54")
        time.sleep(1)
        spin_input.press('ArrowUp')
        #time.sleep(1)# Increment
        spin_input.press('ArrowDown')
        #time.sleep(1)
        spin_input.press('ArrowDown')
        #time.sleep(1)
        self.page.locator('#file-upload').set_input_files([])
        #time.sleep(1)
        #self.page.locator('#file-upload').set_input_files("C:/Users/sunil/PycharmProjects/AllElements/allElementsTest/Screenshot.png")
        #time.sleep(1)
        self.page.locator('#date-input').type('18-02-2025')
        #time.sleep(1)
        self.page.locator("#open-popup").click()
        self.page.get_by_placeholder("Enter popup value").fill("Popup Data")
        self.page.locator("#popup-submit").click()


        #time.sleep(5)

        with self.context.expect_page() as new_tab_info:
            self.page.locator("#open-new-tab").click()
        #time.sleep(5)
        newtab = new_tab_info.value
        newtab.wait_for_load_state()
        newtab.locator("#new-tab-data").type("New Tab Value")
        newtab.get_by_role("button").click()
        self.page.bring_to_front()
        time.sleep(1)

        self.page.once("dialog", handle_dialog)
        #time.sleep(2)
        self.page.locator("#main-submit-button").click()
        print("Clicked on submit")
        self.page.once("dialog", handle_dialog)
        self.page.wait_for_url("https://testautomationsite.in/confirmation.html")
        #time.sleep(5)
        assert "Successfully" in self.page.inner_text('body')
        self.page.reload(wait_until= "load")

    def close(self):
        self.browser.close()

def handle_dialog(dialog):
        print(f"Dialog detected: {dialog.message}, Type: {dialog.type}")
        dialog.accept()

@pytest.mark.regression
def test_runner(playwright):
    runner = AllElements(playwright)
    runner.elementscall()
    runner.close()

@pytest.mark.regression
def test_runner_2(playwright):
    runner = AllElements(playwright)
    runner.elementscall()
    runner.close()

@pytest.mark.regression
def test_runner_3(playwright):
    runner = AllElements(playwright)
    runner.elementscall()
    runner.close()

@pytest.mark.regression
def test_runner_4(playwright):
    runner = AllElements(playwright)
    runner.elementscall()
    runner.close()

@pytest.mark.regression
def test_runner_5(playwright):
    runner = AllElements(playwright)
    runner.elementscall()
    runner.close()


from playwright.sync_api import Page
import time
from utils.logger import log_healing_event


class BasePage:
    def __init__(self, page: Page, healer):
        self.page = page
        self.healer = healer

    def click_smart(self, selector: str, timeout: int = 5000):
        """
        Attempts to click an element. If it fails, triggers the AI healer.
        """
        try:
            # Standard Playwright Action
            self.page.wait_for_selector(selector, timeout=timeout)
            self.page.click(selector)
        except Exception:
            print(f" Locator '{selector}' failed. Initiating AI Self-Healing...")

            # Extract current DOM and consult the Healer
            new_selector = self.healer.suggest_new_selector(selector, self.page.content())

            if new_selector:
                print(f"✨ AI Suggested New Locator: {new_selector}")
                # Retry with healed selector
                try:
                    self.page.click(new_selector)
                    log_healing_event(selector, new_selector, status="Success")
                    print(" Test execution resumed successfully.")
                except Exception as e:
                    log_healing_event(selector, new_selector, status="Failure")
                    raise Exception(f"Healed selector '{new_selector}' also failed: {e}")
            else:
                log_healing_event(selector, None, status="Failure")
                raise Exception(f"AI Healing failed for selector: {selector}")

    def navigate(self, url: str):
        self.page.goto(url)
import pytest
from pages.base_page import BasePage
from utils.logger import log_healing_event

def test_self_healing_logic(browser_context, healer):
    """
    Test Case: Verify that the framework can recover from a changed button ID.
    """
    page = browser_context
    smart_page = BasePage(page, healer)

    # 1. Setup a dynamic UI environment
    target_html = """
    <html>
        <body style="display: flex; flex-direction: column; align-items: center; padding: 50px;">
            <h1>E-Commerce Checkout</h1>
            <button id="checkout-final-001" style="background: green; color: white;">Confirm Payment</button>
        </body>
    </html>
    """
    page.set_content(target_html)

    print("\n Attempting click with outdated selector '#pay-now'...")
    
    # 2. Trigger the healing loop
    try:
        # Pass the 'broken' selector; the Healer will find 'checkout-final-001'
        smart_page.click_smart("#pay-now")
        print(" Success: AI identified the new element and continued the test.")
        
    except Exception as e:
        pytest.fail(f"Test failed: AI was unable to heal the locator. Error: {e}")

    # 3. Final Verification
    page.wait_for_timeout(1000)
### login page
LOGIN_SIGN_IN_LINK = '//span[@id="nav-link-accountList-nav-line-1"]'
LOGIN_SIGN_EMAIL_FIELD = '//input[@id="ap_email"]'
LOGIN_SIGN_PASSWORD_FIELD = '//input[@id="ap_password"]'
LOGIN_SIGN_CONTINUE_BTN = '//input[@id="continue"]'
LOGIN_SIGN_SUBMIT_BTN = '//input[@id="signInSubmit"]'

### homapage
HOME_SEARCH_FIELD = '//input[@id="twotabsearchtextbox"]'
HOME_SEARCH_BTN = '//input[@id="nav-search-submit-button"]'

### search page
SEARCH_PAGE_RESULT_ROWS = '//div[@data-component-type="s-search-result"]'
SEARCH_PAGE_RESULT_ROW_VALUE = '//div[@data-component-type="s-search-result" and contains(.,"VALUE")]//span[@class="a-size-medium a-color-base a-text-normal"]'

### checkout page
CHECKOUT_ADD_TO_CART = '//input[@id="add-to-cart-button"]'
CHECKOUT_PROCEED_TO_RETAIL = '//input[@name="proceedToRetailCheckout"]'
CHECKOUT_PLACE_ORDER = '//input[@name="placeYourOrder1"]'
CHECKOUT_ADD_TO_WISHLIST = '//span[@id="wishListMainButton"]'
CHECKOUT_ADD_TO_WISHLIST_MODAL = '//h4[@id="a-popover-header-2" and text()="Add to List"]'
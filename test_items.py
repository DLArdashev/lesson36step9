def test_add_button(browser):
	browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
	browser.implicitly_wait(3)
	buttons=browser.find_elements_by_css_selector('#add_to_basket_form button')
	assert len(buttons)>0, 'button is missing'
	

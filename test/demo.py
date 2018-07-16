from selenium import webdriver

driver = webdriver.Chrome(executable_path ="C:\\Users\\cguzman\\Documents\\GitHub\\python\\proyecto\\binarios\\chromedriver.exe")
driver.set_page_load_timeout(20)
driver.get("http://127.0.0.1:81/redmine/")
driver.maximize_window()
driver.implicitly_wait(20)
driver.close()
driver.quit()
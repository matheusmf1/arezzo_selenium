from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path=r"/Users/matheusmandotti/Documents/Programming/selenium/driver/chromedriver")

driver.get("https://www.arezzo.com.br/storesale/login")


#login
driver.find_element_by_name("j_username").send_keys("303254_abc@loja.com")
driver.find_element_by_name("j_password").send_keys("arezzo123")
driver.find_element_by_name("j_password").send_keys( Keys.RETURN )

test = True
while( test ):

	parentElement = driver.find_elements_by_class_name("sts-grid-body")[0]
	# print( 'ParentElement: ')
	# print('Text ' +  parentElement.text )
	# print( 'Tag ' + parentElement.tag_name )
	# print( 'parent: ')
	# print( parentElement.parent )
	
	try:

		firstItem = parentElement.find_element_by_class_name('sts-label-icon-checked')
		# firstItem = parentElement.find_element_by_class_name('sts-label-icon-collect')
		# firstItem = parentElement.find_element_by_class_name('sts-label-icon-motoboy')
		# firstItem = parentElement.find_element_by_class_name('sts-available-order--store-shipping')
		print("Achou")

		btn = parentElement.find_element_by_tag_name("button")
		btn.click()

		modal = driver.find_elements_by_class_name("sts-modal-content")
		print('modal')

		try:
			
			# driver.implicitly_wait(2)
			sleep(1)

			btnModal = driver.find_element_by_class_name("sts-buttons")
			print('BtnModal')
			print(btnModal)

			btnSim = btnModal.find_element_by_tag_name("button")
			print('BtnSim')
			print(btnSim)
			driver.execute_script("arguments[0].click();", btnSim)
			# btnSim.click()

		except Exception as e:
			print("Deu ruim")
			print(e)

	
		test = False


	except:
		print("Nao achou")
		# driver.close
		sleep(3)
		driver.refresh()

print("Saiu do loop")
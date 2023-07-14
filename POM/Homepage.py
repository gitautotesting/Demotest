from selenium.webdriver.common.by import By



class Homepage:

    textbox_input_id = (By.ID, 'myTextInput')
    textbox_area_id = By.ID, 'myTextarea'
    textbox_pretext_id = By.ID, 'myTextInput2'
    textbox_placeholder_id = By.ID, 'placeholderText'
    button_click_me_id = By.ID, 'myButton'
    text_readonly_id = By.ID, 'readOnlyText'
    text_para_text_id = By.ID, 'pText'
    svg_id = By.ID, 'mySVG'
    progressbar_id = By.ID, 'progressBar'
    slider_input_slider_id = By.ID, 'mySlider'
    dropdown_id = By.ID, 'mySelect'
    meter_id = By.ID, 'meterBar'
    checkbox_1_id = By.ID, 'checkBox1'
    checkbox_2_id = By.ID, 'checkBox2'
    checkbox_3_id = By.ID, 'checkBox3'
    checkbox_4_id = By.ID, 'checkBox4'
    checkbox_5_id = By.ID, 'checkBox5'
    radiobutton_1_id = By.ID, 'radioButton1'
    radiobutton_2_id = By.ID, 'radioButton2'
    link_URL_id = By.ID, 'myLink1'
    link_withtext_id = By.ID, 'myLink2'
    link_base_id = By.ID, 'myLink3'
    link_demo_id =By.ID, 'myLink4'
    hover_dropdown_id = By.ID, 'myDropdown'
    hover_dropdown1_id = By.ID, 'dropOption1'
    hover_dropdown2_id = By.ID, 'dropOption2'
    hover_dropdown3_id = By.ID, 'dropOption3'
    hover_text_xpath = By.ID, '/html/body/form/table/tbody/tr[1]/td[4]/h3'

    def __init__(self, driver):
        self.driver = driver

    def enter_input_text(self, text):
        self.driver.find_element(*Homepage.textbox_input_id).send_keys(text)

    def get_data_text_input(self):
        return self.driver.find_element(*Homepage.textbox_input_id).get_attribute('value')




import os
import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# تثبيت chromedriver تلقائيًا
chromedriver_autoinstaller.install()

# إدخال البيانات
name = "Ahmed Maher"
contact_number = "+201028098779"
city = "Cairo"

# رابط نموذج Google Forms
form_url = "https://docs.google.com/forms/d/e/1FAIpQLSeXQSGgV-fnleedkPjcEdFDdJ5AMDNaXHqWge2WtdK_VfudQg/viewform"

# ضبط خيارات متصفح Chrome
options = Options()
options.add_argument("--headless")  # تشغيل المتصفح في الخلفية
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# تحميل `chromedriver` تلقائيًا
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# عداد الرسائل
messages_sent = 0

# تشغيل البوت بشكل متكرر
while True:
    driver.get(form_url)  # فتح النموذج
    time.sleep(2)  # الانتظار حتى تحميل الصفحة بالكامل

    try:
        # العثور على جميع حقول الإدخال النصية
        fields = driver.find_elements(By.XPATH, "//input[@type='text']")

        # إدخال البيانات في الحقول
        fields[0].send_keys(name)  # الاسم
        fields[1].send_keys(contact_number)  # رقم الهاتف
        fields[2].send_keys(city)  # المدينة

        # العثور على زر الإرسال والنقر عليه
        submit_button = driver.find_element(By.XPATH, "//span[text()='إرسال']")
        submit_button.click()

        # تحديث العداد
        messages_sent += 1
        print(f"✅ تم إرسال البيانات بنجاح! (إجمالي الرسائل: {messages_sent})")
    
    except Exception as e:
        print(f"⚠️ حدث خطأ: {e}")
    
    time.sleep(2)  # الانتظار قبل إعادة المحاولة
    driver.refresh()  # تحديث الصفحة

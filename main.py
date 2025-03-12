from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# إدخال البيانات
name = "Ahmed Maher"
contact_number = "+201028098779"
city = "Cairo"

# رابط النموذج
form_url = "https://docs.google.com/forms/d/e/1FAIpQLSeXQSGgV-fnleedkPjcEdFDdJ5AMDNaXHqWge2WtdK_VfudQg/viewform"

# إعداد Chrome WebDriver باستخدام WebDriver Manager
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # تشغيل بدون واجهة رسومية
options.add_argument("--no-sandbox")  # تعطيل وضع العزل الأمني
options.add_argument("--disable-dev-shm-usage")  # حل مشاكل الذاكرة

# تشغيل ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# عداد الرسائل
messages_sent = 0

# تشغيل البوت بشكل متكرر
while True:
    try:
        driver.get(form_url)  # فتح النموذج
        time.sleep(2)  # انتظار تحميل الصفحة

        # البحث عن جميع الحقول النصية
        fields = driver.find_elements(By.XPATH, "//input[@type='text']")
        
        if len(fields) < 3:
            print("⚠️ لم يتم العثور على الحقول المطلوبة!")
            break  # إيقاف الكود في حال وجود مشكلة في النموذج

        # إدخال البيانات في الحقول
        fields[0].send_keys(name)  # الاسم
        fields[1].send_keys(contact_number)  # رقم الهاتف
        fields[2].send_keys(city)  # المدينة

        # البحث عن زر الإرسال والنقر عليه
        submit_button = driver.find_element(By.XPATH, "//span[text()='إرسال']")
        submit_button.click()

        # تحديث العداد
        messages_sent += 1
        print(f"✅ البيانات تم إرسالها بنجاح! (إجمالي الرسائل المرسلة: {messages_sent})")

    except Exception as e:
        print(f"⚠️ خطأ أثناء إرسال البيانات: {e}")

    time.sleep(5)  # الانتظار قبل الإرسال مرة أخرى
    driver.refresh()  # إعادة تحميل الصفحة

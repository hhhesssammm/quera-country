# کشور کوئرا
It is a oop project by python

در این بخش به توضیح کلی پروژه می‌پردازیم و جزئیات و پیاده‌سازی آن در هر بخش توضیح داده می‌شود.

پروژه یک بازی تک‌نفره‌ است که در کنسول اجرا می‌شود. در این بازی ابتدا یک کشور با مقداری پول دارید. در هر مرحله می‌توانید مدرسه، معدن و یا شرکت بسازید و یا ارتقا دهید. در ضمن می‌توانید معلم، کارگر و یا مهندس استخدام کنید و به محل کارشان اعزام کنید. هر کدام از افراد، بر اساس شغلشان، سطح محل‌کار و تجربه‌شان مقداری پول به دارایی شما اضافه می‌کنند.

هر فرد و هر محل‌کار مقداری خرج دارند. افراد بیکار پولی تولید نمی‌کنند. هدف بازی ورشکست نشدن و تولید پول بیشتر است.

هر فرد به طور کلی دارای خصوصیت‌هایی (مانند اسم، سن، سطح تجربه، جنسیت و ...) است. همچنین بر اساس حرفه‌اش (مهندس، کارگر و معلم) خصوصیت‌هایی دیگری نیز داراست.

هر محل کار دارای خصوصیت‌هایی (مانند اسم، قدمت، سطح و ...) است و بر اساس کاربری (معدن، مدرسه و شرکت) می‌تواند خصوصیت‌های دیگری نیز داشته‌باشد.

کاربر به صورت روزانه با مقدار پولی که دارد می‌تواند به ساخت، استخدام و ارتقا بپردازد. همچنین بازی قابلیت ذخیره سازی و ادامه نیز خواهد داشت.

##کلاس Person در پروژه

در این بخش به توضیح کلاس Person در پروژه می‌پردازیم و از شما می‌خواهیم آن را پیاده سازی کنید. ابتدا خصوصیات و بعد از آن توابع این کلاس برای شما توضیح داده شده است. با کمی دقت و توجه و استفاده از مطالب قبلی می‌توانید این کلاس را پیاده‌سازی کنید

خصوصیت‌های Person

  خصوصیت instances
  
یک لیست ایستا که شامل همه اشیا با نوع Person است و هر وقت سازنده صدا می‌شود شی تازه تولید‌شده به آن اضافه      می‌گردد.

instances = [] #static variable

سایر خصوصیت‌ها:

هرکدام از متغیرهای زیر نشان‌دهنده یکی از خصوصیت‌های کاربر می‌باشند. کاربرد آن‌ها با توجه نام آن‌ها قابل تشخیص می‌باشد. تمامی خصوصیت‌های زیر باید در سازنده تعریف و مقداردهی شوند. در ادامه نحوه مقدارهی آن‌ها در تابع سازنده آمده است.


name	نام

level	سطح

age	سن

job	نوع کار

work_place	محل کار

توابع Person

سازنده __init__(self, name, age)

اسم و سن را از روی ورودی‌ها مقداردهی می‌کند و به ویژگی level مقدار ‍‍1 را نسبت می‌دهد. متغیرjob را با مقدار "" و work_place را با مقدار None برابر می‌کند. به این نکته توجه کنید که این سازنده باید شی جدید یا همان self را به instances اضافه کند.

تابع do_level(self, income)

این تابع علاوه‌ بر مقدار ورودی خود یا همان income از دو مقدار self.level و self.work_place.level نیز استفاده می‌کند. در نهایت این تابع مقدار عبارت زیر را بر می‌گرداند.

income × sqrt( self.level × self.work_place.level )

محاسبه درآمد و هزینه زندگی

به ترتیب برای محاسبه درآمد و هزینه زندگی از توابع calc_income() و calc_life_cost استفاده می‌شود. برای پیاده‌سازی این توابع فقط از عبارت pass استفاده کنید و به عبارتی آن‌ها را خالی بگذارید. این توابع توسط سیستم داوری تکمیل می‌شوند.

def calc_income(self):

    pass
    
def calc_life_cost(self):

    pass
    
    تابع calc(self)
    
این تابع درآمد خالص را با کسر هزینه زندگی از درآمد (با تاثیر دادن تابع do_level) بر‌می‌گرداند. به عبارتی اگر درآمد را income و هزینه زندگی را cost در نظر بگیریم خروجی تابع به شکل زیر می‌باشد:

def calc(self):

    return self.do_level(income) - cost
    
    تابع calc_all(self)
    
این یک تابع ایستا می‌باشد که مجموع وضعیت مالی (خروجی تابع calc(self)) هر شئ از کلاس Person را برمی‌گرداند. به عبارتی تابع calc() را برای تمامی نمونه‌های ساخته‌شده از نوع Person که در لیست instances قرار دارند صدا می‌زند و مجموع آن‌ها را برمی‌گرداند.

@staticmethod

def calc_all():

    pass
    
                                                        
get_job(self)	شغل فرد را بر می‌گرداند

upgrade(self)	مقدار level را یک واحد افزایش می‌دهد.

##کلاس WorkPlace در پروژه

در این بخش به توضیح کلاس WorkPlace‍ در پروژه می‌پردازیم و از شما می‌خواهیم آن را پیاده‌سازی کنید. ابتدا خصوصیات و بعد از آن توابع این کلاس برای شما توضیح داده شده است.

با کمی دقت و توجه و استفاده از مطالب قبلی می‌توانید این کلاس را پیاده‌سازی کنید. دقت کنید که توابعی که از آن‌ها نام برده شده ولی نحوه پیاده‌سازی آن‌ها توضیح داده نشده است را باید خالی بگذارید یا به عبارتی به صورت زیر پیاده‌سازی کنید.

def function():

    pass
    
    خصوصیات WorkPlace‍
    
خصوصیت ایستای instances

یک لیست ایستا که هر وقت سازنده صدا می‌شود شئ تازه تولید‌شده به آن اضافه می‌گردد.

instances = [] #static variable

سایر خصوصیت‌ها

هرکدام از متغیرهای زیر نشان‌دهنده یکی از خصوصیت‌های محل کار می‌باشند. کاربرد آن‌ها با توجه نام آن‌ها قابل تشخیص است. تمامی خصوصیت‌های زیر باید در سازنده تعریف و مقداردهی شوند. در ادامه نحوه مقدارهی آن‌ها در تابع سازنده آمده است.

name	نام محل کار

level	سطح محل کار

expertise	تخصص

employees	کارکنان

capacity	ظرفیت

توابع WorkPlace‍

سازنده __init__(self, name)

نام محل کار را به عنوان ورودی ‌می‌گیرید و به صورت زیر متغیرها را در سازنده مقداردهی می‌کند. به این نکته توجه کنید که این سازنده باید شئ جدید یا همان self را به instances اضافه کند.

self.name = name

self.level = 1

self.expertise = ""

self.employees = []

self.capacity = 1

تابعget_price(self)

این تابع از کلاس ‍Consts، بر اساس دیکشنری BASE_PRICE، قیمت ساخت این محل کار را برمی‌گرداند. محل کار آن فرد، ملاک محاسبه قیمت است.

تابع upgrade(self)

این تابع مقدار متغیر level را یک واحد زیاد می‌کند و سپس تابع self.calc_capacity() را صدا می‌کند تا مقدار capacity به‌روزرسانی شود.

تابع hire(self, person)

عملکرد این تابع به این گونه است که اگر اندازه لیست self.employees بیشتر مساوی self.capacity بود، خطای WorkPlaceIsFull می‌دهد و در غیر اینصورت person را به لیست کارکنان self اضافه کند و محل کار شخص (person.work_place) را برابر self می‌کند

تابع calc_all()

این یک تابع ایستا می‌باشد که مجموع وضعیت مالی (خروجی تابع calc(self)) هر شئ از کلاس WorkPlace را برمی‌گرداند. به عبارتی تابع calc() را برای تمامی نمونه‌های ساخته‌شده از نوع WorkPlace که در لیست instances قرار دارند صدا می‌زند و مجموع آن‌ها را بر می‌گرداند

@staticmethod

def calc_all():

    pass
    
    سایر توابع

get_expertise(self)	تخصص یا همان مقدار self.expertise را برمی‌گرداند.

calc(self)	این تابع منفی مقدار خروجی تابع self.calc_costs() را برمی‌گرداند.    

توجه کنید که نیازی به نوشتن تابع calc_costs و ‍‍calc_capacity وجود ندارد و این تابع در تست‌ها کنار کدتان قرار می‌گیرد؛ بنابراین طبق روش گفته شده در ابتدای سوال باید آن‌ها را خالی بگذارید.

کد اولیه
سه کلاس WorkPlaceIsFull، Consts و WorkPlace را به شکل زیر در کد خود تعریف کنید. دو تابع موجود در کلاس WorkPlace را هم خالی بگذارید.

```python
class WorkPlaceIsFull(Exception):

    def __str__(self):
        return "work place is full!"

class Consts:

    BASE_PRICE = {'mine': 150, 'school': 100, 'company': 90}

class WorkPlace:

    def calc_capacity(self):
        pass

    def calc_costs(self):
        pass
```
        

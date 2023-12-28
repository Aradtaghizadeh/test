
# Label: برای نمایش متن یا تصویر بر روی صفحه استفاده می‌شود.
# Button: برای افزودن دکمه‌ها به برنامه‌ی شما استفاده می‌شود.
# Canvas: برای کشیدن تصویر و طرح‌های دیگر مانند گرافیک، متن و غیره استفاده می‌شود.
# ComboBox: یک پیکان رو به پایین برای انتخاب گزینه‌ای از لیست گزینه‌های موجود، در اختیار کاربر قرار می‌دهد.
# CheckButton: کاربر از طریق آن می‌تواند چندین گزینه از گزینه‌های موجود را انتخاب کند.
# RadiButton: برای انتخاب فقط یک مورد از گزینه‌های موجود از این آیتم استفاده می‌شود.
# Entry: برای وارد کردن متن تک‌خطی کاربر استفاده می‌شود.
# Frame: به عنوان محلی برای نگهداری و سازمان‌دهی ابزارک‌ها استفاده می‌شود.
# Message: کارکردی شبیه به برچسب (Label) دارد و برای متن‌های چندخطی و غیر قابل ویرایش استفاده می‌شود.
# Scale: یک اسلایدر گرافیکی ایجاد کرده و امکان انتخاب مقدار دلخواه با جابجایی آن را می‌دهد.
# Scrollbar: برای پیمایش به پایین محتویات استفاده می‌شود.
# SpinBox: این امکان را به کاربر می‌دهد تا از مقادیر تعیین‌شده، مقداری را انتخاب کند.
# Text: امکان ایجاد، ویرایش و نحوه‌ی نمایش یک متن چندخطی را به کاربر می‌دهد.
# Menu: برای ایجاد انواع منو در برنامه استفاده می‌شود.
# ()pack: ابزارک‌ها را در سطرها یا ستون‎ها دسته‌بندی می‌کند.
# ()grid: ابزارک‌ها را در یک جدول دو بعدی قرار می‌دهد.
# ()place: به شما امکان می‌دهد، موقعیت و اندازه‌ی یک پنجره را به صورت مطلق یا نسبت به پنجره‌ی دیگر مشخص کنید.
from tkinter import *


def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

def btnClearDisplay():
    global operator
    operator =""
    text_input.set("")

def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator=""

c = Tk()
c.title('Calculator')
operator = ""
text_input = StringVar()
txtDisplay = Entry(c, font=("calibry", 20, 'bold'), textvariable=text_input, bd=30, insertwidth=4, bg='powder blue', justify='right').grid(columnspan=4)
btn7 = Button(c, padx=16, pady=16, bd=8, fg='black', font=('calibry', 20, 'bold'), text='7', command=lambda:btnClick(7)).grid(row=1, column=0)
btn8 = Button(c, padx=16, pady=16, bd=8, fg='black', font=('calibry', 20, 'bold'), text='8', command=lambda:btnClick(8)).grid(row=1, column=1)
btn9 = Button(c, padx=16, pady=16, bd=8, fg='black', font=('calibry', 20, 'bold'), text='9', command=lambda:btnClick(9)).grid(row=1, column=2)
addition = Button(c, padx=16, pady=16, bd=8, fg='black', font=('calibry', 20, 'bold'), text='+', command=lambda:btnClick('+')).grid(row=1, column=3)
btn4 = Button(c, padx=16, pady=16, bd=8, fg='black', font=('calibry', 20, 'bold'), text='4', command=lambda:btnClick(4)).grid(row=2, column=0)
btn5 = Button(c, padx=16, pady=16, bd=8, fg='black', font=('calibry', 20, 'bold'), text='5', command=lambda:btnClick(5)).grid(row=2, column=1)
btn6 = Button(c, padx=16, pady=16, bd=8, fg='black', font=('calibry', 20, 'bold'), text='6', command=lambda:btnClick(6)).grid(row=2, column=2)
subtraction = Button(c, padx=16, pady=16, bd=8, fg='black', font=('calibry', 20, 'bold'), text='-', command=lambda:btnClick('-')).grid(row=2, column=3)
btn1 = Button(c, padx=16, pady=16, bd=8, fg='black', font=('calibry', 20, 'bold'), text='1', command=lambda:btnClick(1)).grid(row=3, column=0)
btn2 = Button(c, padx=16, pady=16, bd=8, fg='black', font=('calibry', 20, 'bold'), text='2', command=lambda:btnClick(2)).grid(row=3, column=1)
btn3 = Button(c, padx=16, pady=16, bd=8, fg='black', font=('calibry', 20, 'bold'), text='3', command=lambda:btnClick(3)).grid(row=3, column=2)
multiply = Button(c, padx=16, pady=16, bd=8, fg='black', font=('calibry', 20, 'bold'), text='*', command=lambda:btnClick('*')).grid(row=3, column=3)
btn0 = Button(c, padx=16, pady=16, bd=8, fg='black', font=('calibry', 20, 'bold'), text='0', command=lambda:btnClick(0)).grid(row=4, column=0)
btnClear = Button(c, padx=16, pady=16, bd=8, fg='black', font=('calibry', 20, 'bold'), text='c', command= btnClearDisplay).grid(row=4, column=1)
btnEquals = Button(c, padx=16, pady=16, bd=8, fg='black', font=('calibry', 20, 'bold'), text='=', command=btnEqualsInput).grid(row=4, column=2)
division = Button(c, padx=16, pady=16, bd=8, fg='black', font=('calibry', 20, 'bold'), text='/', command=lambda:btnClick('/')).grid(row=4, column=3)








c.mainloop()

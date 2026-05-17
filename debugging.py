''' Packages & Debugging
    (1) Python Packages & Core Package
    (2) Package Manager & External Package
    (3) Debugging
'''

from PIL import Image
import turtle

print("===== Python Packages & Core Package =====")
''' Python Packages/Modules: Core, File and External '''
# Core Packages > https://docs.python.org/3/libraryrf


# Core package
t = turtle.Turtle()
t.shape("turtle")
t.speed(2)
t.circle(150)
turtle.done()


my_file = open("material/message.txt", "r")
try:
    content = my_file.read()
    print("content:", content)
finally:
    my_file.close()


# with -> Context Manager (AWTOMATIK ravshda CLOSE qiladi)
with open("material/message.txt", "r") as your_file:
    your_content = your_file.read()
    print("your content:", your_content)

print("DONE")


print("===== Package Manager & External Package =====")
# Package Manager => python language bilan birga keladigan uzini manageri mavjut. bu manager orqali external package'larni install qilishimiz mumkun
''' Package Managers:
    - Python > pip pipenv
    - NodeJS > npm yarn
    - PHP > Composer
    - Macos > brew
'''
# External Packages > https://pypi.org/

# pip3 install pillow
# cmd + shift + p => python: select interpreter

'''
-> pillow documentation
-> search => resize image
-> search => image save
'''

with Image.open("material/MIT.png") as img_obj:
    resized_img = img_obj.resize((200, 200))
    resized_img.show()
    resized_img.save("material/sample.png")

# pip3 list => install qilingan package'larni korsatadi

# pip3 show pillow => pillow qayirga ornatilganni korsatadi

# cd location -> ENTER -> PIL olarak install qilinganini korolamiz


print("===== Debugging =====")


def get_summary(*args):  # Define
    total_amount = 0
    for a in args:
        total_amount += a
        return total_amount  # solve the bug via debugging


test = 100
result = get_summary(1, 2, 3, 4, 5)  # Call
print("result:", result)

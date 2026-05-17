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


# # Core
# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(10)
# t.circle(150)
# turtle.done()


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
    rgb_img = img_obj.convert("RGB")
    resized_img = rgb_img.resize((200, 200))
    resized_img.show()
    resized_img.save("material/sample.png")

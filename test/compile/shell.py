import basic

while True:
    text = input("basic > ")
    res, error = basic.run('<stdio>',text)
    if error:
        print(error)
    else:
        print(res)
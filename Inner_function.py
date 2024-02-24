def test_function():
    print('есть вложенная функция')
    def inner_function():
        print('я в области видимости функции test_function')
    inner_function()

# inner_function() функция не вызывается из глобального пространства, т.к. она локальная
test_function()

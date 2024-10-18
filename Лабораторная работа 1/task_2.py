mbytes_floppy_volume = 1.44  # объем дискеты в Мбайтах
quantity_of_pages = 100  # количество страниц в книге
quantity_of_strings = 50  # количество строк на странице
quantity_of_symbols = 25  # количество символов в строке
bytes_for_symbol = 4  # количество байт для кодирования одного символа

bytes_floppy_volume = mbytes_floppy_volume * 1024 * 1024  # объем дискеты в байтах
bytes_for_one_book = quantity_of_pages * quantity_of_strings \
                     * quantity_of_symbols * bytes_for_symbol  # объем в байтах, занимаемый одной книгой
quantity_of_books = bytes_floppy_volume // bytes_for_one_book
print("Количество книг, помещающихся на дискету:", round(quantity_of_books))

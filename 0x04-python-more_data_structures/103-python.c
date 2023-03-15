#include <Python.h>

/**
 * print_python_list - Prints basic information about a Python list
 *
 * @p: Pointer to the Python list object
 */
void print_python_list(PyObject *p)
{
    PyListObject *list = (PyListObject *)p;
    Py_ssize_t size, i;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", Py_SIZE(list));
    printf("[*] Allocated = %ld\n", list->allocated);

    size = Py_SIZE(list);
    for (i = 0; i < size; i++)
    {
        printf("Element %ld: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
    }
}
/**
 * print_python_bytes - Prints basic information about a Python bytes object
 *
 * @p: Pointer to the Python bytes object
 */
void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes = (PyBytesObject *)p;
    Py_ssize_t size, i;
    char *str;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(bytes))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);
    printf("  first %ld bytes: ", size < 10 ? size : 10);

    for (i = 0; i < size && i < 10; i++)
    {
        printf("%02x", str[i] & 0xff);
        if (i < size - 1 && i < 9)
            printf(" ");
    }

    printf("\n");
}


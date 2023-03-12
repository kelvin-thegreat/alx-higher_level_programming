#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <stdio.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer to the Python list object
 */
void print_python_list_info(PyObject *p)
{
    PyListObject *list = (PyListObject *)p;
    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t i;
    PyListObject *obj;
    const char *type;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < size; i++)
    {
        obj = (PyListObject *)PyList_GetItem(p, i);
        type = Py_TYPE(obj)->tp_name;
        printf("Element %ld: %s\n", i, type);
    }
}

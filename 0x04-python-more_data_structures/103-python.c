nclude <Python.h>
#include <stdio.h>
#include <string.h>

void print_python_bytes(PyObject *p)
{
    long int size;
    int i;
    const char *trying_str = NULL;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    trying_str = PyBytes_AsString(p);
    size = PyBytes_Size(p);

    printf("  size: %li\n", size);
    printf("  trying string: %s\n", trying_str);
    if (size < 10)
        printf("  first %li bytes:", size + 1);
    else
        printf("  first 10 bytes:");
    for (i = 0; i < size && i < 10; i++)
        printf(" %02hhx", trying_str[i]);
    printf("\n");
}

void print_python_list(PyObject *p)
{
    long int size = PyList_Size(p);
    int i;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %li\n", size);
    for (i = 0; i < size; i++)
    {
        PyObject *item = PyList_GetItem(p, i);
        const char *type = Py_TYPE(item)->tp_name;
        printf("Element %i: %s\n", i, type);
        if (!strcmp(type, "bytes"))
            print_python_bytes(item);
    }
}

int main()
{
    // Initialize the Python interpreter
    Py_Initialize();

    // ... Your code to call print_python_list or other functions ...

    // Finalize the Python interpreter
    Py_Finalize();

    return 0;
}

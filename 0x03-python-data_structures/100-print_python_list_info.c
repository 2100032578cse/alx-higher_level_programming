#include <Python.h>
#include<stdlib.h>
#include<object.h>
#include<listobject.h>
/**
 * print_python_list_info - list python info
 * @p: the object
*/
void print_python_list_info(PyObject *p)
{
	int i = 0;

	printf("[*] Size of the Python List = %li\n", PyList_Size(p));
	printf("[*] Allocated = %li\n", ((PyListObject *)p)->allocated);
	while (i < PyList_Size(p))
	{
		obj = ob_item[i];
		printf("Element %i: %s\n", i, Py_TYPE(obj)->tp_name);
		i++;
	}

}

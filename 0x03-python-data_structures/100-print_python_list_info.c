#include <python3.4m/Python.h>
#include <python3.4m/listobject.h>
#include <python3.4m/object.h>

/**
 * print_python_list_info - prints the information of a PyListObject
 * @P: Provided PyListObject
 *
 * Return: nothing
 */
void print_python_list_info(PyObject *P)
{
	int i = 0;

	printf("[*] Size of the Python List = %lx\n", PyList_GET_SIZE(P));
	printf("[*] Allocated = %lx\n", ((PyListObject *)P)->allocated);

	for (i = 0; i < PyList_GET_SIZE(P); i++)
		printf("Element %d: %s\n",
				i,
				((PyListObject *)P)->ob_item[i]->ob_type->tp_name);
}

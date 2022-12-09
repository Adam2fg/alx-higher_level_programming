#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints bytes information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_bytes(PyObject *p)
{
        char *string;
        long int size, i, limit;

        printf("[.] bytes object info\n");
        if (!PyBytes_Check(p))
        {
                printf("  [ERROR] Invalid Bytes Object\n");
                return;
        }

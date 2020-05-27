#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
//mozliwe sygnatury funkcji stanowiącej "interfejs" pomiędzy pythonem i C
//static PyObject *mod_met(PyObject *self){
//static PyObject *mod_met(PyObject *self, PyObject *args, PyObject *kw){
static PyObject *mod_met(PyObject *self, PyObject *args){
	int a,b;
	int *c;
	PyObject *d=NULL;
	if(!PyArg_ParseTuple(args, "ii|iO", &a, &b, &c, &d)){ //jezeli do stringa wstawi sie | to po sa parametry opcjonalne; O od Object
		return NULL;	//zwracane w przypadku bledu; interpreter zglasza wyjatek wywolania funkcji
	}
	int s=(int)a+(int)b+(int)c;
	if(d){
		int r=PyList_Size(d);
		for(int i=0; i<r; i++){
			s+=PyLong_AsLong(PyList_GetItem(d, i));
		}
	}
	//Py_RETURN_NONE; //jesli nic nie zwraca
	return Py_BuildValue("i", s);
}

static PyObject *mod_zad2(PyObject *self, PyObject *args){
    double a[10] = {};
    int n;
    if(!PyArg_ParseTuple(args, "i", &n)){
        return NULL;
    }
    for(int i = 0; i <= n; i++){
        double x = (double)rand() / (double)RAND_MAX;
        double y = (double)rand() / (double)RAND_MAX;
        if (x < 0.1 && y < 0.1){
            a[0]++;
        }
        else if (x < 0.2 && y < 0.2){
            a[1]++;
        }
        else if (x < 0.3 && y < 0.3){
            a[2]++;
        }
        else if (x < 0.4 && y < 0.4){
            a[3]++;
        }
        else if (x < 0.5 && y < 0.5){
            a[4]++;
        }
        else if (x < 0.6 && y < 0.6){
            a[5]++;
        }
        else if (x < 0.7 && y < 0.7){
            a[6]++;
        }
        else if (x < 0.8 && y < 0.8){
            a[7]++;
        }
        else if (x < 0.9 && y < 0.9){
            a[8]++;
        }
        else {
            a[9]++;
        }
    }
    for(int i = 0; i < 10; i++){
        a[i] /= n;
        a[i] *= 100;
    }
    PyObject *list = PyList_New(10);

    for (int i = 0; i < 10; i++) {
        PyList_SetItem(list, i, Py_BuildValue("f", a[i]));
    }
    return list;
}



int AlgorytmEuklidesa(int a, int b) {
    if (b ==0){
        return a;
    }
    else {
        return AlgorytmEuklidesa(b, a % b);
    }

}

static PyObject *mod_zad3(PyObject *self, PyObject *args){
	PyObject *d=NULL;
	if(!PyArg_ParseTuple(args, "O", &d)){ //jezeli do stringa wstawi sie | to po sa parametry opcjonalne; O od Object
		return NULL;	//zwracane w przypadku bledu; interpreter zglasza wyjatek wywolania funkcji
	}
	PyObject *key, *value;
    Py_ssize_t pos = 0;

    PyObject * dict = PyDict_New();
	PyObject * temp = NULL;

	while(PyDict_Next(d, &pos, &key, &value)){
	    PyObject *result = Py_BuildValue("i", AlgorytmEuklidesa(PyLong_AsLong(key), PyLong_AsLong(value)));
	    temp = PyTuple_New(2);
	    PyTuple_SetItem(temp, 0, key);
	    PyTuple_SetItem(temp, 1, value);
	    PyDict_SetItem(dict, temp, result);
	}
    return dict;
}
//tablica metod
static PyMethodDef mod_metody[]={
	{"met", (PyCFunction)mod_met, METH_VARARGS, "Funkcja ..."},
	//nazwa funkcja stosowana w Pythonie, adres funkcji , j.w. lub METH_KEYWORDS lub METH_NOARGS, lancuch dokumentacyjny
    {"zad2", (PyCFunction)mod_zad2, METH_VARARGS, "zad2  ..."},
    {"zad3", (PyCFunction)mod_zad3, METH_VARARGS, "zad3  ..."},
	{NULL, NULL, 0, NULL}	//wartownik
};


static struct PyModuleDef modmodule={
        PyModuleDef_HEAD_INIT,
        "mod",
        NULL,
        -1,
        mod_metody
};

//funkcja inicjalizujaca
PyMODINIT_FUNC PyInit_mod(void){
        return PyModule_Create(&modmodule);
}

##########################################################
Clase de Python para realizar el cálculo de la ley d'Hondt
##########################################################

:autor: Pedro-Juan Ferrer
:autor: Silvia Fuentes
:fecha: 2019-05-27
:version: v1.1.1

Realiza el cálculo de distribución de escaños dada un reparto de votos.

Por ejemplo::

    $ python dhondt.py 21 3.0 "{'a': 100, 'b': 200, 'c': 50}"

nos devuelve::

    <dhondt nseats:21 minper:3.0 candi:[('b', 200), ('a', 100), ('c', 50)]>
    <seats: [('b', 12), ('a', 6), ('c', 3)]>


FAQ
===

¿Por qué el partido j aparece con resultado 0?
----------------------------------------------

Ejemplo::

    $ python dhondt.py 15 3.0 "{'a': 33553, 'b': 8711, 'd': 9191, 'e': 50825, 'f': 8938, 'g': 9269, 'h': 8617, 'i': 8688, 'j': 11888, 'k': 8738, 'l': 78991, 'o': 75702, 'p': 8741, 'q': 8788, 'r': 43516}"

    <dhondt nseats:15 minper:3.0 candi:[('l', 78991), ('o', 75702), ('e', 50825), ('r', 43516), ('a', 33553), ('j', 11888), ('g', 9269), ('d', 9191), ('f', 8938), ('q', 8788), ('p', 8741), ('k', 8738), ('b', 8711), ('i', 8688), ('h', 8617)]>
    <seats: [('l', 4), ('o', 4), ('e', 3), ('a', 2), ('r', 2), ('j', 0)]>

El partido j tiene votos que le permiten superar el porcentaje mínimo para
entrar en el reparto, pero no tiene suficientes como para que le asigne un
escaño.

Control de versiones
====================

:v1.1.1: Quitados requisitos innecesarios
:v1.1: Arreglado bug que impide realizar cálculos cuando solo hay 1 sitio. Agregada opción para tener en cuenta votos en blanco
:v1.0: Versión inicial

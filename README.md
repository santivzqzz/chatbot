ESQUEMA
La idea general sería hacer un árbol para que el chatbot funcione por descartes.

El abdomen se divide en una "matriz 3x3" quedando 9 cuadrantes en las que en cada uno hay enfermedades, molestias, dolores específicos debido a la disposición 
de los órganos por lo que sugiero que después de preguntar el género del paciente es preguntar en que zona tiene las molestias para descartar más cosas.

Para esto podemos hacer diccionarios según cuadrantes en los que incluyan las enfermedades con sus síntomas

Detalles opcionales si conseguimos hacer que todo lo anterior funcione bien y nos sobra tiempo:

1.- Podemos hacer un rango de edades para descartar aún más enfermedades.

2.- Podemos preguntar al paciente si tiene hábitos como beber, fumar, etc. para tener mayor certeza de que tenga cierta enfermedad u otra.

3.- Hacer que el programa muestre una imagen cuando pregunte la zona del dolor con el módulo PIL (from PIL import Image)

4.- Hacer que todo el programa sea un módulo y se pueda usar desde otro pograma.

IMPORTANTE hacer un disclaimer al principio o al final para avisar de que el bot no acierta al 100% sino que es una guía para saber que puede ser.

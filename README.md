[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Y59lTQr6)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=23693623)

# Monthy Hall Problem

## Resultados 
Al correr el código, obtenemos que la tasa de éxito para cambiar es, en promedio, 2/3 y para quedarse 1/3.

## Explicación
La manera en que logre entender los resultados es la siguiente: Cuando usamos la estrategia de quedarnos, se tiene un éxito solamente cuando nuestra elección es igual a la caja ganadora, lo cual tiene una probabilidad de 1/3 para tres cajas. 


Mientras que para la estrategia de cambiar, se tiene un éxito siempre y cuando nuestra elección inicial no sea igual a la caja ganadora. Esto se debe a que, si nuestra elección inicial no es la caja ganadora, entonces no se puede abrir ni nuestra elección ni la ganadora, i.e., solamente hay una caja que se puede abrir. Y para nuestra elección final, como cambiaremos no podemos abrir la caja que elegimos inicialmente, y como obviamente no abriremos la caja que ya se abrió, la única opción será la ganadora.  
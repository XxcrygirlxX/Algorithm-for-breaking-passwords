- Cómo ejecutar el programa.
Es importante tener Python instalado y guardado con el nombre bruteforce.py. Luego se ejecuta desde la terminal. 
- Ejemplos de salida.
En este caso la contraseña es "abc", por lo que dará lo siguiente: 
<img width="1043" height="119" alt="image" src="https://github.com/user-attachments/assets/354abc7f-083f-4387-8828-0b726482e215" />
Así mismo, al momento de ejecutar el programa se iniciará la gráfica que mostrará el tiempo de busqueda de la clave y los inetntos realizados para llegar al resultado. 
<img width="1124" height="775" alt="image" src="https://github.com/user-attachments/assets/7c281f13-b155-401b-abef-34539eb7e24e" />
- Reflexión: ¿qué pasa si la contraseña tiene 8+ caracteres y usa mayúsculas, números y símbolos?
Si la contraseña se incrementa a 8 o más caracteres y además incluye mayúsculas, números y símbolos,
la cantidad de combinaciones posibles aumentará de forma exponencial y rápidamente alcanza cifras inmanejables para un ataque de fuerza bruta simple:
el tiempo requerido para probar todas las combinaciones se vuelve astronomómico y el programa, ejecutado en una sola máquina,
tardaría más allá de escalas prácticas (años, siglos o más) en completar la búsqueda.
Esto demuestra por qué las contraseñas largas y con mayor entropía son efectivas:
cada carácter adicional y cada conjunto de símbolos nuevo multiplican el espacio de búsqueda,
haciendo que los ataques por fuerza bruta sean impracticables y subrayando la importancia de usar gestores de contraseñas,
autenticación multifactor y otras prácticas de seguridad para proteger cuentas y sistemas.

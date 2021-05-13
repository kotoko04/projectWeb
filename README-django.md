# Documentacion Django del proyecto

_Acá va un párrafo que describa lo que es el proyecto_

## ¿Que es Django? 🚀

_Django es un marco web de Python de alto nivel que fomenta el desarrollo rápido y el diseño limpio y pragmático. Creado por desarrolladores experimentados, se encarga de gran parte de la molestia del desarrollo web, por lo que puede concentrarse en escribir su aplicación sin necesidad de reinventar la rueda. Es gratis y de código abierto_

## Caracteristicas

Ridículamente rápido.

Django fue diseñado para ayudar a los desarrolladores a llevar las aplicaciones desde el concepto hasta su finalización lo más rápido posible.

Tranquilizadoramente seguro.

Django se toma la seguridad en serio y ayuda a los desarrolladores a evitar muchos errores de seguridad comunes.

Extremadamente escalable.

Algunos de los sitios más concurridos de la Web aprovechan la capacidad de Django para escalar de forma rápida y flexible.



### Instalación de Django en windows🔧 

* Lo primero que se debe hacer es instalar python para windows
*  Una vez descargado ejecutamos el .exe, es importante que al iniciar la instalacion la casilla para agregar una ruta a Python este marcada para ahorrarnos trabajo extra
*  Proseguimos a entrar a Panel de control, click en Sistemas y Seguridad.
*  Click en sistema, click en configuracion del sistema, click en variables de entorno 
*  Buscamos la ruta donde se encuentra python . Click en editar.
*  Escribimos dos nuevas rutas, por ultimo click en nuevo para crear.

## Creando un proyecto nuevo en  Django 

_django-admin.py es un script que creará los archivos y directorios para ti.
manage.py es un script que ayuda con la administración del sitio. Con él podremos iniciar un servidor web en nuestro ordenador sin necesidad de instalar nada más, entre otras cosas.
El archivo settings.py contiene la configuración de tu sitio web.
El archivo urls.py contiene una lista de los patrones utilizados por urlresolver_


## Migraciones de datos con Django

_./manage.py makemigrations polls
Mediante la ejecución de makemigrations, le estás diciendo a Django que has hecho algunos cambios a sus modelos y que desea que los cambios se almacenarán como la migración.
Las migraciones son cómo almacena Django cambios a sus modelos (y por tanto el esquema de base de datos) - son simplemente los archivos en el disco. Puedes leer la migración para su nuevo modelo si se quiere; que es el archivo polls/migrations/0001_initial.py . No te preocupes, no se espera para leerlos cada vez que Django hace uno, sino que están diseñados para ser humano editable en caso de que quiera ajustar manualmente cómo Django cambia las cosas.

Ver SQL que generara

Para ver el SQL que generara cuando cree la db, usar sqlmigrate.

Por ejemplo, para ver 0001_initial.py 0002_auto_20140808_1242.py, solo poner el premer numero 0001 o 0002

Esto no genera la base de datos, solo muestra el SQL que generara cuando se haga migrate

./manage.py sqlmigrate polls 0001

Comprobar el modelo

Esto solo comprueba si hay algún error en el modelo, pero no ejecuta nada.

./manage.py check

Migrar las base de datos

./manage.py migrate

El comando migrate toma todas las migraciones que no han sido aplicadas (pistas de Django cuáles se aplican mediante una tabla especial en su base de datos llamada django_migrations ) y les va en contra de su base de datos - en esencia, la sincronización de los cambios realizados en sus modelos con el esquema en la base de datos.
Las migraciones son muy potentes y permiten cambiar tus modelos con el tiempo, a medida que desarrolle su proyecto, sin la necesidad de eliminar la base de datos o las tablas y hacer otros nuevos - que se especializa en la actualización de su base de datos en vivo, sin perder datos. Recordamos la guía de tres pasos para hacer cambios en el modelo:
•	Cambiar los modelos (en models.py ).
•	Ejecutar python manage.py makemigrations para crear migraciones de esos cambios
•	Ejecutar python manage.py migrate para aplicar esos cambios a la base de datos.


Limpiar migraciones

Hacer primero un backup de la base de datos y un commit en Git MUY RECOMENDABLE
Si se han echo muchos cambios en el modelo, sobre todo en las primeras etapas del proyecto, quizá sea bueno limpiar tanto las tabla django_migrations como el directorio app/migrations/

•	Eliminar la tabla django_migrations

psql -U nombre_usuario nombre_db
DROP TABLE IF EXISTS django_migrations;
\q

•	Eliminar los directorios app/migrations/, ir al directorio raíz del proyecto y ejecutar.

find ./ -type d -name "migrations" -exec rm -rf {} \;
•	Crear migraciones con makemigrations de las apps en el proyecto. Esta parte se ha de hacer por cada app.

./manage.py makemigrations app1
./manage.py makemigrations app2
./manage.py makemigrations appX
Restablecer.
./manage.py migrate --fake-initial

## Crear superusuario

_Para iniciar sesión, deberás crear un superusuario (superuser), que es un usuario que tiene control sobre todo el sitio. Vuelve a la línea de comandos, escribe python manage.py createsuperuser y pulsa enter.
(myvenv) C:\Users\Name\djangogirls> python manage.py createsuperuser
Cuando te lo pida, escribe tu nombre de usuario (en minúscula, sin espacios), email y contraseña. No te preocupes si no puedes ver la contraseña que estás tecleando - así es como debe ser. Tecléalo y pulsa intro para continuar. Luego, verás algo así (donde username y email serán los que escribiste anteriormente):
EJ:
Username: ola
Email address: ola@example.com
Password:
Password (again):
Superuser created successfully.

### App en la que se trabajo

Visual code 

## Patron MVT (Modelo-Vista-Template)

_Si tenéis experiencia en el mundo de la programación seguro que habéis oído hablar del famoso patrón MVC: Modelo-Vista-Controlador. Django redefine este modelo como MVT: Modelo-Vista-Template.

![image](https://user-images.githubusercontent.com/61531454/118087548-57cfe300-b38b-11eb-8143-200bc9790695.png)

_Ahora se recibirá la petición, se pasará a la vista, en la vista recuperaremos los datos del modelo correspondiente, y finalmente la renderizaremos el Template pero esta vez integrando los datos dinámicos recuperados del modelo, antes de enviar el HTML final al navegador





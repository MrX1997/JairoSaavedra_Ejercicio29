

nladveccion.x:nladveccion.c
	gcc nladveccion.c -o nladveccion.x  
	./nladveccion.x
	python plons.py
	rm *.x
	rm *.txt


hello.x:HelloWorld.c
	gcc -fopenmp HelloWorld.c -o hello.x
	./hello.x 
	rm *.x

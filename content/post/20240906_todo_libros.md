---
categories:
- tecnología
date: 2024-09-06
lastmod: '2025-04-06T01:37:21.875354'
related:
- 20250110_soberania_tecnologica.md
- 20240524_cortos.md
- 20220311_interactuar_libros.md
- 20240223_soluciones_sin_problema.md
- 20250312_cortos.md
tags:
- libros
- llms
- japón
title: Todo está en los libros, pero algunos quieren que solo esté en ellos
url: /2024/todo-en-libros/
---

Japón se desarrolló muy rápidamente a partir de 1870. Alex Tabarrok estudia [aquí](https://marginalrevolution.com/marginalrevolution/2024/07/not-lost-in-translation-how-barbarian-books-laid-the-foundation-for-japans-industrial-revoluton.html) una cuestión que bien pudo ayudar a tal desarrollo: el increíble esfuerzo de traducción (al japonés) de libros técnicos en ese periodo, ilustrado en el siguiente gráfico:

![Gráfico de traducciones de libros técnicos al japonés](/images/libros-japon.png#center)

El otro día le preguntaba a un LLM (de hecho, a una colección de ellos, incluidos algunos anónimos a través de [LM Arena](https://lmarena.ai/)), dónde podía haber leído yo una determinada anécdota relacionada con R. Feynman. En mi _query_, describía la anécdota con detalle y les preguntaba por su posible origen. Uno de ellos resolvió concluyentemente que estaba en el capítulo 13 de [_Surely You're Joking, Mr. Feynman!_](https://en.wikipedia.org/wiki/Surely_You%27re_Joking,_Mr._Feynman!), pero no, no estaba allí. Otros me sugirieron algunas otras fuentes, pero todas en vano. Al final, admitieron que la anécdota era muy Feynman, pero que no tenían ni idea de dónde podía haber salido.

El problema es que los LLMs no _saben_ todos los libros. Un experto conoce muchos de los libros de su ramo. Esperamos que un experto en Lorca conozca prácticamente de memoria lo más relevante de su obra. Mucho de lo que queremos conocer está en libros. Y los LLMs, obviamente, se entrenan sobre libros. Pero la industria editorial no quiere que los LLMs _sepan_ los libros; así que la industria de los LLMs hace por que los LLMs no _sepan_ todos los libros. De modo que nuestros expertos electrónicos no van a ser _tan_ expertos como nos gustaría: cuando les preguntemos qué capítulo del Quijote comienza con eso de _la del alba sería_, se inventarán cualquier cosa por no reconocer que no, que no tienen ni idea.

La industria editorial ha pasado de ser un vehículo para que la información fluya a uno que la dosifica con avaricia para generar rentas. Tendría que justificar su utilidad social.

**Coda:** Mientras escribía esto, se me ha ocurrido una solución:
- Las empresas que entrenan LLMs compran una copia de cada libro (o reciben libros donados).
- Se registran como bibliotecas.
- Cuando alguien hace una pregunta relativa a un libro, se lo _prestan_ durante unos microsegundos.
- Obviamente, habría que implementar un sistema de _semáforos_ para evitar que algún libro esté prestado simultáneamente.
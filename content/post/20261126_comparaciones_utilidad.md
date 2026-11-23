---
categories:
- política
- economía
date: 2026-11-25
description: "Una introducción de alto nivel al bienestarismo, el utilitarismo y el paretianismo, así como al problema fundamental de las comparaciones interpersonales de utilidad."
lastmod: '2026-11-20'
tags:
- economía
- política
- justicia
- utilitarismo
- paretianismo
- bienestarismo
- rawls
- bentham
title: "Ética, justicia y comparaciones interpersonales de utilidad: un resumen"
url: /2026/comparaciones-interpersonales-utilidad/
---

Hace un tiempo escribí sobre la [relación entre el utilitarismo y el «paretianismo»](https://piensoluegohesobrevivido.es/2022/utilitarismo-paretianismo/): el paretianismo es una visión restringida del utilitarismo que evade su aspecto más controvertido, las comparaciones interpersonales de utilidad. Un cambio de la situación $x_0$ a la $x_1$ es aceptable en el sentido de Pareto solo si $U_i(x_1) \ge U_i(x_0)$ para todas las personas $i$.

Pero eso lo hace impráctico. Ninguna reforma real ---una subida de impuestos, una obra pública, una liberalización comercial, una prestación--- beneficia a todos. Si vetásemos los proyectos con criterios estrictamente paretianos, nunca implementaríamos ninguno. En algunos casos, ni siquiera podríamos comparar la bondad de dos proyectos que el criterio de Pareto no vetase.

La única manera de ordenar estados del mundo, $x$, consiste en usar una función $W$ que los «proyecte» sobre una escala común. Una política $x_1$ será preferible a la $x_0$ cuando $W(x_1) > W(x_0)$. La forma específica de la función $W$ ha sido el objeto de una parte sustancial del debate sobre la justicia, la equidad y la naturaleza del estado del bienestar durante el último siglo.

$W$ podría depender de muchos parámetros. Por ejemplo, de la utilidad de los distintos individuos, $U_i$; pero también de variables como los derechos, las libertades, el «bienestar» del Mar Menor, los [nidos de águilas imperiales](https://www.elmundo.es/economia/empresas/2026/08/18/6a845dffe4d4d89c278b45ba.html), etc. El «bienestarismo» es la escuela moral que postula

$$W(x) = F(U_1(x), \dots, U_n(x)),$$

es decir, la que considera funciones $W$ que dependen de $x$ únicamente a través de las funciones de utilidad $U_i$ de los individuos[^1]. $F$ determina cómo se comparan las utilidades de sujetos distintos.

De entre todas las posibles especificaciones de $W$, la más popular es

$$W(x) = \sum_i U_i(x),$$

la propia de ese tipo especial de «bienestarismo» que es el utilitarismo. Todo lo bueno y lo malo que se puede predicar del utilitarismo es consecuencia de la particular forma funcional de su $W$[^2].

Esa especificación utilitarista puede postularse, como hizo Jeremy Bentham en su formulación original de 1789. Pero también puede deducirse con mayor o menor fortuna a partir de principios más generales, como han hecho Harsanyi en 1955, Ng en 1975 y, al parecer, algunos otros más a lo largo de los últimos decenios.

Aunque «deducir» parece un verbo excesivo. No solo porque coexistan varias deducciones distintas, sino porque la $W$ del utilitarismo no ha conseguido «falsar» otras formulaciones alternativas con las que convive. Por ejemplo, «la de Rawls»[^3],

$$W(x) = \min_i U_i,$$

que da todo el peso a la utilidad del más desfavorecido y es indiferente a lo que le suceda al resto de la población.

La mayor dificultad con la que se encuentran estos intentos de formalizar matemáticamente el criterio de equidad y justicia estriba en fijar el método de comparación de la utilidad entre personas. Las matemáticas pueden reflejar nuestras elecciones, pero nunca nos van a dar la respuesta por sí mismas[^4].

![Trolley problem](/images/trolley_problem.jpg)

[^1]: La función debe cumplir algunas condiciones obvias, como crecer al crecer cualquiera de las $U_i$.
[^2]: La especificación $W(x) = \sum_i U_i(x)$ admite variantes, como el uso de pesos o especificaciones del tipo $W(x) = \sum_i g(U_i(x))$ para alterar el peso relativo de unos sujetos con respecto a otros o introducir matices «morales», pero que no alteran sustancialmente las propiedades matemáticas de la función de agregación.
[^3]: La entrecomillo porque no es de Rawls en dos sentidos. El primero, que esa $W$ había sido planteada y estudiada previamente por Wald y von Neumann. El segundo, que sugiere una representación demasiado esquemática del pensamiento de Rawls, que ni siquiera es «bienestarista» en sentido estricto. En concreto, su idea de justicia incluye una serie de absolutos que no son ni transables ni fungibles (libertad, etc.).
[^4]: Un error en el que sorprendentemente incurren algunas personas.
---
categories:
- otros
date: 2026-09-16
description: Una evaluación del coste relativo del reciclaje con respecto al enterramiento
  de los residuos en vertederos, aplicada al caso de Madrid.
lastmod: '2026-09-11T11:23:43.102603'
related:
- 20250904_tasa_basuras.md
- 20240112_precio_carbon.md
- 20241211_cortos.md
- 20210213_reflexiones_cambio_climatico.md
- 20250514_cortos.md
tags:
- cambio climático
- reciclaje
- madrid
title: ¿Reciclar en Madrid? El análisis coste beneficio.
url: /2026/reciclar-madrid/
---

En un reciente artículo, Chalmers y Wiblin sostienen que, [para una gran parte de los residuos que generamos, un vertedero bien gestionado puede ser preferible al reciclaje](https://www.worksinprogress.news/p/just-bury-your-trash). En efecto:

- **El reciclaje compensa claramente en el caso de los metales y los materiales escasos.** Procesar acero reciclado ahorra el 65% de la energía que necesita el virgen; para el aluminio, el ahorro alcanza el 95%. La ecuación es todavía más favorable para el cobre, el cobalto, el litio y el níquel, que son, además, mucho más escasos.

- **Sin embargo, para el papel, el vidrio y buena parte del plástico, el caso es mucho más débil.** Además, el manido problema de la presencia de plásticos en el océano tiene una importante dimensión geográfica: en su mayor parte, estos proceden de unos 100 ríos del sur y sudeste asiático.

- **Un vertedero moderno puede ser limpio, barato y ocupar poco espacio.** Las instalaciones modernas incorporan actualmente tecnologías que evitan los principales problemas históricamente asociados a este tipo de instalaciones: las emisiones de metano y la contaminación de las aguas subterráneas. En EEUU, los vertederos ocupan menos del 0,01 % del territorio.

- **La incineración elimina todo el metano y genera electricidad**, pero cuesta entre un 20% y un 30% más que el vertido.

- Finalmente, que **la reutilización no siempre compensa.** Una bolsa de algodón necesita unos 173 usos para superar a una bolsa de polietileno; una pajita de acero, unos 150; y una taza de cerámica ---de usarse un lavavajillas eficiente--- alrededor de 1.000. El proceso de fabricación del producto, su peso y su lavado influyen grandemente en el cómputo ambiental completo.

En resumen, la conclusión de Chalmers y Wiblin es que tiene sentido reciclar los metales, diseñar buenos vertederos y luego, si procede, invertir los recursos ahorrados a medidas de mitigación con mayor impacto.

Pero esa recomendación genérica, que aplica a una ciudad _promedio_ del planeta tierra, podría no ser adecuada para la ciudad concreta que más me interesa, Madrid.

Algunos datos:

- Madrid produce poco más de un kg de basura por habitante y día (en 2023, unos 1.3 millones de toneladas).
- En 2023, el 47% de esa basura se recogió «separada».
- El coste promedio de la recogida de residuos está entre 175 y 200 €/t (t de tonelada).
- Por referencia, los contratos del ayuntamiento con las empresas que efectúan la recogida establecen precios de unos 165 €/t para los residuos no separados, 410 €/t para el cartón y 260 €/t para el cristal.
- El coste medio del tratamiento de los residuos en la planta de Valdemingómez es de unos 100 €/t (114 €/t en 2023, 95 €/t en 2025) (contra un coste marginal de unos 75-80 €/t).
- Por esos 1.3 millones de toneladas, el ayuntamiento pagó 19 millones de euros de impuestos medioambientales (al enterramiento y la incineración), es decir, unos 14 €/t.

Expresado en términos _humanos_, los vecinos de Madrid generamos 1 kg diario de basura y pagamos 30 céntimos por deshacernos de ella: 20 para que nos la recojan; 10, para tratarla en la planta de Valdemingómez. Es decir, el transporte de la basura cuesta aproximadamente el doble que su tratamiento.

El precio del tratamiento de la basura está determinado por dos factores principales:

1. La peculiar tecnología (o _mix_ de tecnologías) usada para procesar los residuos.
2. Los impuestos que los ayuntamientos tienen que pagar a otras instancias de la administración (!) y que han sido diseñados para desincentivar las más económicas.

No es sencillo averiguar cuál es el coste ---idealmente, el marginal y neto del efecto distorsionador de los impuestos medioambientales--- asociado a cada una de las tecnologías. Afortunadamente, existe un documento, el [«Informe técnico-económico» sobre la «Prestación del servicio de gestión de residuos de competencia municipal» del ayuntamiento de Madrid](https://transparencia.madrid.es/UnidadWeb/UGNormativas/Normativa/HUELLANORMATIVA/Fiscales/2025/TasaResiduos/Ficheros/InformeTecnEcon20241011.pdf), elaborado para estimar la cuantía de la tasa de recogida de basuras. Puede arrojar alguna luz respecto a los precios de las distintas tecnologías porque incluye los «costes netos» de operación de las distintas plantas que forman parte del complejo de gestión de residuos Valdemingómez. Es imprescindible, en todo caso, recurrir a la aproximación ---no del todo realista--- de que cada una de ellas implementa una tecnología específica.

De la información distribuida a lo largo de las más de cien páginas del documento, un servicial LLM ha compilado la siguiente tabla (verificada luego independientemente por otros dos):

| Planta / proceso | Toneladas tratadas | Coste del contrato (€) | €/t (solo canon) |
|---|---|---|---|
| Vertedero (enterramiento) | 449.362 | 3.255.952 | **~7,2** |
| Compostaje, Las Dehesas | 59.124 | 590.148 | **~10,0** |
| Clasificación / incineración, Las Lomas | 258.773 | 7.431.081 | **~28,7** |
| Clasificación, La Paloma — bolsa resto + biorresiduo | 159.170 | 3.406.124 | **~21,4** |
| Clasificación, La Paloma — envases | 46.651 | 5.264.167 | **~112,9** |
| Biometanización, La Paloma | 93.321 | 6.154.620 | **~66,0** |
| Biometanización, Las Dehesas | 259.205 | 13.772.150 | **~53,1** |

Hay que decir muchas cosas sobre estos números para evitar que quien los lea los considere verdades absolutas en lugar de vagas aproximaciones. Entre ellas que:

- Son cifras netas e incluyen la venta de los subproductos generados, pero parece que no todos ellos (y, en particular, diríase que excluya las ventas de electricidad, compost y biogás).
- Las cifras se elaboraron con un fin distinto que el de estimar el coste marginal de procesar una tonelada de residuos y puede que signifiquen otra cosa; relacionada, sí, pero distinta.
- Las cifras no incluyen el impuesto al vertido e incineración de residuos, que pueden ascender hasta los 40 €/t para el enterramiento. Como se ha estimado arriba, encarece unos 14 euros la tonelada, pero su impacto es desigual según las tecnologías y, en particular, multiplica por siete el del enterramiento (de 7 €/t a 47 €/t).
- No está claro en qué medida incluyen atribuciones de costes fijos, amortizaciones, etc.
- Nótese finalmente la discrepancia entre el coste promedio global del tratamiento de los residuos indicado más arriba (del orden de 100 €/t) y el desglosado en esta tabla, que quedaría muy por debajo. La discrepancia tiene que ser consecuencia de la atribución de otros costes no incluidos en la tabla.

A pesar de las advertencias anteriores, parece claro que la tesis fundamental del artículo con el que se abría esta entrada aplica también en Madrid: el vertedero es, con diferencia, la opción más económica.

Sobre el coste relativo entre el enterramiento y la incineración, los datos obtenidos no permiten decir gran cosa. Por un lado, como se ha indicado antes, en la estimación del coste neto parecen haberse excluido los ingresos por la venta de electricidad. Por otro lado, ninguna de las plantas que integran el complejo de Valdemingómez se dedica exclusivamente a producir electricidad a partir de residuos. La que dispone de la mayor potencia instalada, 29 MW, la de Las Lomas, también se dedica a la clasificación y al compostaje.

El resto de las tesis del artículo original tampoco han podido ser contrastadas con datos de Madrid por falta de datos específicos. Hay que hacer constar que el negocio de la gestión de los residuos es muy soviético: está atravesado por multitud de tasas y subvenciones cruzadas, no opera como un mercado, valora más la apariencia que la esencia y lo que se predica de él tiene más que ver con arbitrios burocráticos que con precios, euros, camiones y toneladas.
# Modulo Instrumentos

## Descricion funcionalidade/obxectivos do módulo 
#

### Funcionalidade
A funcionalidade deste módulo é a de crear tendas (relacionadas co ámbito da música), dentro destas gardaremos instrumentos, ditos instrumentos poderán ter reparacións e ditas reparacións poderanas realizar empleados das tendas.
<br></br>

### Obxectivo
O obxectivo deste módulo é que sexa utilizado para xestión de tendas musicais,xa que dentro de cada tenda poderás saber os instrumentos que ten nese momento dispoñibles xunto co prezo e cantidade, os empleados que ten dita tenda etc ...

Tamén en cada instrumentos poderás saber se tivo algunha reparación e quen realizou dita reparación.
<br></br>

## Instruccións para o uso do módulo Instrumentos
#
En total no módulo teremos 4 lapelas : 

- Tendas : Onde se crearán/gardarán as tendas. Amosaranse en vista de tipo árbore todas as creadas polo momento, se lle damos a "Crear" apareceranos unha vista formulario para meter os respectivos datos (Será o mesmo para as seguintes lapelas).
Esta lapela ten 2 botóns adicionais engadidos á vista tipo árbore e 1 á vista tipo formulario, aparecerán cando seleccionemos unha tenda e son : 

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<b>- Borrar Tenda</b>(Borrará a tenda que seleccionaches)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<b>- Crear instrumento</b>(Creará un instrumento con datos de exemplo que estará dentro de dita tenda)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<b>- Borrar instrumentos</b>(Situada dentro da vista formulario, eliminará da tenda todo instrumento contido nela, pero soamente nesa tenda, os instrumentos en sí non se borrarán)
    
  
- Instrumentos : Onde se crearán/gardarán os instrumentos. Amosaranse en vista tipo kanban, tamén podese cambiar a tipo árbore, dentro da vista tipo árbore hai 2 botóns adicionais, aparecerán cando selecciones un instrumento e son : 
  
&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<b>- Borrar instrumento</b>(Borrará o instrumento que seleccionaches)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<b>- Crear reparación</b>(Creará unha reparación con datos de exemplo que estará dentro de dito instrumento)

- Reparacións : Onde se crearán/gardarán as reparacións dos instrumentos. Amosaranse en vista tipo árbore, nesta vista tipo árbore haberá 2 botóns adicionais, aparecerán cando seleccionemos unha reparación e son :

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<b>- Modificar fecha reparación</b>(A fecha será cambiada á do día actual)

&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;<b>- Modificar estado reparación</b>(Modificará o estado da reparación, se se realizou e se pulsa pasará a nonRealizado e viceversa)

- Empleados : Onde se crearán/gardarán os empleados. Amosaranse en vista de árbore. Este modelo foi heredado e non ten funcionalidades adicionais, simplemente foi adaptado as necesidades do módulo.
    
  
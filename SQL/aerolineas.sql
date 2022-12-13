-- Realizar los siguientes consultas:
-- 1. Se desea conocer la empresa más antigua.
-- 2. Se desea conocer las empresas que viajan a mendoza y que el pasaje cueste más de 15000
-- 3. Se desea saber los pasajes que están bajo el promedio de los precios.
-- 4. Se agrega un nuevo destino con una nueva empresa. Esta es flyBondi creada en el 2016 y es una empresa Argentina. Este acepta tanto vuelos nacionales como internacionales.
-- 5. La empresa LATAM se va de Argentina.
-- 6. Se desea saber la cantidad de pasajes vendidos.
-- 7.Se desea saber cuales son las empresas que vuelan tanto en Argentina como internacionalmente.
-- 8.Se desea saber los pasajes que superan el promedio de los precios.
-- 9.Se vende un viaje para dos personas a Río de Janeiro desde Ezeiza por la empresa JetSmart a 64000 cada uno.
-- 10.El vuelo a Mendoza para tres personas ha sido modificado y no despegan desde AEO. Este cambia a Ezeiza.
-- 11.El vuelo Ezeiza-Bariloche fue dado de baja.

-- Operador logicos
--or  y el and


1- 
select nombre from aerolineas 
where Año = min(Año)

> Aerolíneas argentina

2- 
select * from agencia_turismo ag
join aerolineas ae on ae.id = ag.id 
where ag.destino = 'Mendoza' and Precio_Unitario > 15000


3- 

select * from agencia_turismo 
where Precio_Unitario < avg(Precio_Unitario)

4- 

--Como usar el insert
-- insert valorCampo1, valorCampo1.....  )
-- Values(NombreCampo1,NombreCampo2.....)

insert aerolineas('FlyBondi','NO','SI','Argentina','2016')
values(Nombre,VI,VN,Origen,Año)

5- 
--Borrar un registro
delete  Aerolineas
where nombre = 'LATAM'

6- 
select sum(cantidad) as CantidadPasajes from agencia_turismo

7- 
select nombre from aerolineas
where VI = 'SI'

8-
select * from agencia_turismo 
where Precio_Unitario > avg(Precio_Unitario)

9- 

insert agencia_turismo('Eze','Rio De Janeiro',2,2,64000)
values(Origen,Destino,Empresa,Cantidad,Precio_Unitario)

10- --NO existe en la tabla Agencia_turismo un vuelo para 3 personas de AEO a Mendoza
-- Asumo actualizar el que es para 2 personas.

update agencia_turismo
set Origen='EZE'
where Origen='AEO' and Destino='Mendoza' and Cantidad=2


11-

delete  agencia_turismo
where origen = 'Eze' and Destino='Bariloche'


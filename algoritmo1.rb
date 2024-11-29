# Algoritmo para contar números pares e impares en un rango

def contar_pares_impares
  print "Ingresa el número inicial del rango: "
  inicio = gets.chomp.to_i
  print "Ingresa el número final del rango: "
  fin = gets.chomp.to_i

  pares = 0
  impares = 0

  # Usamos un ciclo while para recorrer el rango
  while inicio <= fin
    if inicio % 2 == 0
      pares += 1
    else
      impares += 1
    end
    inicio += 1
  end

  puts "En el rango dado hay #{pares} números pares y #{impares} números impares."
end

# Ejecutar la función
contar_pares_impares


numeros = [1, 2, 3, 4, 5]
informacion = { "nombre" => "Ruby", "version" => 3.1 }


puts "Primer número: #{numeros[0]}"
puts "Información: #{informacion['nombre']} versión #{informacion['version']}"

if x > 5 && resultado != 15
  puts "Condición cumplida"
end

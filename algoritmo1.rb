
x = 10
y = 5
resultado = x + y * 2 - (y / 3)


if resultado > 10
  puts "El resultado es mayor que 10"
else
  puts "El resultado es 10 o menor"
end


while y > 0 do
  y -= 1
  puts "y es ahora #{y}"
end


def saludo(nombre)
  puts "Hola, #{nombre}!"
end


saludo("Estudiante")


numeros = [1, 2, 3, 4, 5]
informacion = { "nombre" => "Ruby", "version" => 3.1 }


puts "Primer número: #{numeros[0]}"
puts "Información: #{informacion['nombre']} versión #{informacion['version']}"

if x > 5 && resultado != 15
  puts "Condición cumplida"
end

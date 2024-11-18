# Declaración de variables
x = 5 + 10
@nombre = "Juan"
@@contador = 0
$global_var = true

# Impresión
puts("Hola")
puts("Hola", "Mundo")
puts "Hola, #{nombre}!"

# Condicional
if x > 10
  puts "x es mayor que 10"
else
  puts "x es menor o igual a 10"
end

# Ciclo while
while @@contador < 5
  @@contador += 1
  puts @@contador
end

# Función
def suma(a, b)
  return a + b
end

# Llamada a la función
resultado = suma(3, 7)
puts resultado

# Arrays y hashes
mi_array = [1, 2, 3]
mi_hash = { "clave" => "valor", "clave2" => "valor2" }

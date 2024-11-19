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

# Solicitud de datos por teclado
puts "Ingrese su nombre:"
nombre = gets.chomp  # Captura el nombre ingresado por el usuario

puts "Ingrese su edad:"
edad = gets.chomp.to_i  # Captura la edad y la convierte a un número

# Impresión con cero, uno y más argumentos
puts            # Impresión con cero argumentos (salto de línea)
puts "Hola, #{nombre}"  # Impresión con un argumento
puts "Tu nombre es #{nombre} y tu edad es #{edad}"  # Impresión con varios argumentos

# Declaración de un array
mi_array = [1, 2, 3]
puts "Contenido del array:"
puts mi_array 

# Declaración de un hash
mi_hash = { 'clave1' => 'valor1', 'clave2' => 'valor2' }
puts "Contenido del hash:"
mi_hash.each do |clave, valor|
  puts "#{clave}: #{valor}"  # Imprime cada par clave-valor
end

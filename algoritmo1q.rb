# Algoritmo para sumar números ingresados por el usuario

def sumar_numeros
  suma = 0
  continuar = true

  while continuar
    print "Ingresa un número (o 'fin' para terminar): "
    input = gets.chomp

    if input.downcase == 'fin'
      continuar = false
    else
      numero = input.to_f
      suma += numero
    end
  end

  puts "La suma total de los números ingresados es: #{suma}"
end

# Ejecutar la función
sumar_numeros

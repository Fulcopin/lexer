require 'time'  # Asegúrate de usar la gema 'time' para manejar las fechas correctamente

class User
  attr_accessor :name, :email, :registration_date

  def initialize(name, email)
    @name = name
    @email = email
    @registration_date = Time.now  # Usa Time.now correctamente para obtener la fecha actual
  end

  def to_s
    "Name: #{@name}, Email: #{@email}, Registered on: #{@registration_date.strftime("%Y-%m-%d %H:%M:%S")}"
  end
end

class UserManager
  def initialize
    @users = []
  end

  # Crear un usuario
  def create_user(name, email)
    user = User.new(name, email)
    @users << user
    puts "User created successfully: #{user}"
  end

  # Listar todos los usuarios
  def list_users
    if @users.empty?
      puts "No users found."
    else
      @users.each_with_index do |user, index|
        puts "#{index + 1}. #{user}"
      end
    end
  end

  # Buscar un usuario por nombre o correo
  def search_user(query)
    result = @users.select { |user| user.name.include?(query) || user.email.include?(query) }
    if result.empty?
      
    else
      result.each { |user| puts user }
    end
  end

  # Actualizar un usuariofddd
  def update_user(index, name: nil, email: nil)
    if index < 0 || index >= @users.length
      puts "Invalid user index."
    else
      user = @users[index]
      user.name = name if name
      user.email = email if email
      puts "User updated successfully: #{user}"
    end
  end

  # Eliminar un usuario
  def delete_user(index)
    if index < 0 || index >= @users.length
      puts "Invalid user index."
    else
      user = @users.delete_at(index)
      puts "User deleted successfully: #{user}"
    end
  end
end

class CLI
  def initialize
    @user_manager = UserManager.new
  end

  def start
    loop do
      display_menu
      choice = gets.chomp.to_i
      case choice
      when 1
        create_user
      when 2
        list_users
      when 3
        search_user
      when 4
        update_user
      when 5
        delete_user
      when 6
        break
      else
        puts "Invalid option, please try again."
      end
    end
  end

  def display_menu
    puts "\n--- User Management System ---"
    puts "1. Create User"
    puts "2. List Users"
    puts "3. Search User"
    puts "4. Update User"
    puts "5. Delete User"
    puts "6. Exit"
    print "Choose an option: "
  end

  def create_user
    print "Enter user's name: "
    name = gets.chomp
    print "Enter user's email: "
    email = gets.chomp
    @user_manager.create_user(name, email)
  end

  def list_users
    @user_manager.list_users
  end

  def search_user
    print "Enter name or email to search: "
    query = gets.chomp
    @user_manager.search_user(query)
  end

  def update_user
    list_users
    print "Enter the index of the user to update: "
    index = gets.chomp.to_i - 1
    print "Enter new name (or press Enter to skip): "
    name = gets.chomp
    print "Enter new email (or press Enter to skip): "
    email = gets.chomp
    name = nil if name.empty?
    email = nil if email.empty?
    @user_manager.update_user(index, name: name, email: email)
  end

  def delete_user
    list_users
    print "Enter the index of the user to delete: "
    index = gets.chomp.to_i - 1
    @user_manager.delete_user(index)
  end
end

# Start the CLI application
cli = CLI.new
cli.start

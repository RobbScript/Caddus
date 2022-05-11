#inicio
system "clear"
puts "Caddus Xr (Alpha)"
puts "digte seu nome: "
Opções = ["membros", "sysinfo", "sair"]
private
 senharob = "8642"
 funcionalidade = FALSE
#dados universais
user = "@Usr"
#login
nomeinicio = gets.chomp
nomeinicio.capitalize!
while senha1 = senharob
    if nomeinicio == 'Rob'
      puts "digite sua senha:"
      senha1 = gets.chomp
      if senha1 == senharob
         user = "@Dev"
         system "clear"
         sleep 0.6
         puts "olá Rob!!!"
         system "clear"
         break
      else
         system "clear"
         puts "Senha incorreta"
         system "clear"
      end
    else
      puts "Olá #{nomeinicio}"
      sleep 1
      system "clear"
      break
   end
end
#menu
while TRUE
   puts ("/" * 10)
   puts "Caddus Xr (Alpha)"
   puts "opções:"
   puts "-Membros"
   puts "-Sysinfo"
   puts "-Sair"
   puts ("/" * 10)
   puts "#{nomeinicio}#{user}: "
   opmem01 = gets.chomp
   system "clear"
   if opmem01 == "membros"
      funcionalidade = TRUE
      puts "membros:"
      puts "Yan"
      puts "Vini"
      puts "Rapha"
      puts "digite enter para continuar..."
      nt = gets
      system "clear"
   end
   if opmem01 == "sysinfo"
      puts "informações de sistema:"
      puts "Sistema: Caddus Xr (Alpha)"
      puts "Linguagem: Ruby"
      puts "SGDA Version: 3.0 (Vinci)"
      puts "Último update: 10/05/22 21:44"
      puts "digite enter para continuar..."
      nt = gets
      system "clear"
   end
   if opmem01 == "sair"
      exit
   end
if (funcionalidade == FALSE)
   puts "digite algo válido #{nomeinicio}"
   sleep 1
   system "clear"
end
end
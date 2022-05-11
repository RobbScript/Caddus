#inicio
system "clear"
puts "Caddus Xr (Alpha)"
puts "digte seu nome: "
Opções = ["membros", "sysinfo", "sair"]
private
 senharob = "8642"
 funcionalidade = FALSE
#dados universais
user = "#Usr"
#login
nomeinicio = gets.chomp
nomeinicio.capitalize!
while senha1 = senharob
   if nomeinicio == 'Rob'
      sleep 0.7
      puts "digite sua senha:"
      senha1 = gets.chomp
      if senha1 == senharob
         user = "#Dev"
         sleep 1
         system "clear"
         puts "olá Rob!!!"
         sleep 1
         system "clear"
         break
      else
         system "clear"
         puts "Senha incorreta"
         sleep 1
         system "clear"
      end
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
      sleep 0.5
      puts "Vini"
      sleep 0.5
      puts "Rapha"
      sleep 1
      puts "digite enter para continuar..."
      nt = gets
      system "clear"
   end
   if opmem01 == "sysinfo"
      puts "informações de sistema:"
      sleep 0.5
      puts "Sistema: Caddus Xr (Alpha)"
      sleep 0.5
      puts "Linguagem: Ruby"
      sleep 0.5
      puts "SGDA Version: 3.0 (Vinci)"
      sleep 0.5
      puts "Último update: 10/05/22 17:32"
      sleep 0.5
      puts "digite enter para continuar..."
      nt = gets
      system "clear"
   end
   if opmem01 == "sair"
      exit
   end
if (funcionalidade == FALSE)
   puts "digite algo válido #{nomeinicio}"
end
end


   


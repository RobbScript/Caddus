#dados

#membros
listamembros = [
    AZ999 = "Rapha",
    AZ998 = "Vini",
    AZ997 = "Davi",
    AZ996 = "Pietro",
]

#infos
Sysinfos = [
    "Sistema: Caddus Xr (alpha)",
    "SGDA version: SGDA 3.0 (Vinci)",
    "Linguagem: Ruby",
    "Último update: 12/05/22 23:16",
]

#defs
class MenuPuts
    def listmem
        for i in listamembros
            puts i
            sleep 0.5
        end
    end

    def sysinfos
        for k in Sysinfos
            puts k
            sleep 0.5
        end
    end


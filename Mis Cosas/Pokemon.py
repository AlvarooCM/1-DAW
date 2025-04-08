import random
import time

# --- CLASES BASE --- #

class Pokemon:
    def __init__(self, nombre, tipo, vida, ataques):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = vida
        self.vida_max = vida
        self.ataques = ataques

    def esta_vivo(self):
        return self.vida > 0

    def recibir_daño(self, cantidad):
        self.vida = max(self.vida - cantidad, 0)

    def usar_ataque(self, ataque, objetivo):
        if ataque in self.ataques:
            daño = self.ataques[ataque]
            print(f"{self.nombre} usó {ataque}! Causa {daño} de daño a {objetivo.nombre}.")
            objetivo.recibir_daño(daño)
        else:
            print("Ataque no válido.")

    def curar(self):
        self.vida = self.vida_max

    def __str__(self):
        return f"{self.nombre} ({self.tipo}) - {self.vida}/{self.vida_max} HP"


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.equipo = []
        self.mochila = {"Poción": 3, "Pokéball": 5}

    def capturar(self, pokemon):
        if len(self.equipo) >= 6:
            print("Tu equipo está completo. No puedes capturar más Pokémon.")
            return
        self.equipo.append(pokemon)
        print(f"¡Capturaste a {pokemon.nombre}!")

    def usar_pocion(self, pokemon):
        if self.mochila["Poción"] > 0:
            pokemon.vida = min(pokemon.vida + 30, pokemon.vida_max)
            self.mochila["Poción"] -= 1
            print(f"Usaste una Poción en {pokemon.nombre}. Ahora tiene {pokemon.vida} HP.")
        else:
            print("No tienes más Pociones.")

    def lanzar_pokeball(self, pokemon):
        if self.mochila["Pokéball"] > 0:
            self.mochila["Pokéball"] -= 1
            captura = random.randint(1, 100)
            if captura > 50:
                return True
            else:
                print(f"{pokemon.nombre} escapó de la Pokéball.")
        else:
            print("No te quedan Pokéballs.")
        return False

    def mostrar_equipo(self):
        print("\n👥 Tu equipo:")
        for i, p in enumerate(self.equipo):
            print(f"{i+1}. {p}")

# --- COMBATE --- #

def combate(jugador, enemigo, acciones=None):
    print(f"\n💥 Un {enemigo.nombre} salvaje apareció!")
    activo = jugador.equipo[0]
    acciones = acciones or []
    paso = 0

    while activo.esta_vivo() and enemigo.esta_vivo():
        print(f"\n🧑 {activo} VS 🐾 {enemigo}")
        print("\n¿Qué quieres hacer?")
        print("1. Atacar")
        print("2. Usar poción")
        print("3. Lanzar Pokéball")

        if paso < len(acciones):
            eleccion = acciones[paso]
            print(f"> {eleccion}")
        else:
            eleccion = "1"
            print(f"> {eleccion} (por defecto)")

        paso += 1

        if eleccion == "1":
            print("\nElige ataque:")
            for i, atk in enumerate(activo.ataques):
                print(f"{i+1}. {atk}")
            nombre_ataque = list(activo.ataques.keys())[0]
            print(f"> 1 (por defecto: {nombre_ataque})")
            activo.usar_ataque(nombre_ataque, enemigo)
        elif eleccion == "2":
            jugador.usar_pocion(activo)
        elif eleccion == "3":
            if jugador.lanzar_pokeball(enemigo):
                jugador.capturar(enemigo)
                return
        else:
            print("Acción no válida.")

        if enemigo.esta_vivo():
            atk = random.choice(list(enemigo.ataques.keys()))
            enemigo.usar_ataque(atk, activo)

    if not activo.esta_vivo():
        print(f"\n😵 {activo.nombre} ha sido derrotado...")
    elif not enemigo.esta_vivo():
        print(f"\n✅ ¡Has vencido al {enemigo.nombre}!")

# --- JUEGO PRINCIPAL --- #

def crear_pokemon_salvaje():
    opciones = [
        Pokemon("Rattata", "Normal", 40, {"Placaje": 10}),
        Pokemon("Zubat", "Veneno", 45, {"Mordisco": 12}),
        Pokemon("Pidgey", "Volador", 42, {"Ataque Ala": 11})
    ]
    return random.choice(opciones)

def main():
    print("🎮 ¡Bienvenido a Pokémon Terminal Legends!")
    nombre = "Ash"
    print(f"¡Hola {nombre}!")
    jugador = Jugador(nombre)

    # Inicial
    starter = Pokemon("Charmander", "Fuego", 60, {"Ascuas": 15, "Arañazo": 10})
    jugador.equipo.append(starter)
    print(f"\n🔥 Has elegido a {starter.nombre} como tu primer Pokémon!")

    opciones_fijas = ["1", "1"]  # Explorar y atacar

    while True:
        print("\n¿Qué quieres hacer?")
        print("1. Explorar")
        print("2. Ver equipo")
        print("3. Salir")

        if opciones_fijas:
            op = opciones_fijas.pop(0)
            print(f"> {op}")
        else:
            op = "3"
            print(f"> {op} (por defecto)")

        if op == "1":
            salvaje = crear_pokemon_salvaje()
            combate(jugador, salvaje, acciones=["1"])
        elif op == "2":
            jugador.mostrar_equipo()
        elif op == "3":
            print("👋 ¡Hasta la próxima!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
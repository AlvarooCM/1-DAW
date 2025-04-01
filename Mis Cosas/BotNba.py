import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Tu token de bot de Telegram
TOKEN = "TU_TOKEN_DE_BOT"

# API Key para la fuente de datos (suponiendo SportsRadar o API similar)
API_KEY = "TU_API_KEY"

# URL de la API para obtener resultados de los playoffs de la NBA
NBA_API_URL = "https://api.sportsradar.com/nba/trial/v7/en/games/{date}/boxscore.json"  # URL de ejemplo (puedes cambiarla según la API que uses)

# Comando para obtener los resultados de los partidos de playoff
def get_playoff_results(update: Update, context: CallbackContext) -> None:
    # Fecha del partido (si se quiere resultados de un día específico)
    date = context.args[0] if context.args else "2025-03-25"  # Fecha predeterminada si no se especifica

    url = NBA_API_URL.format(date=date)

    # Realiza la petición GET a la API
    response = requests.get(url, headers={"Authorization": f"Bearer {API_KEY}"})

    if response.status_code == 200:
        data = response.json()

        # Extraemos los resultados de los partidos
        results = []
        for game in data["games"]:
            home_team = game["home_team"]["name"]
            home_score = game["home_team"]["score"]
            away_team = game["away_team"]["name"]
            away_score = game["away_team"]["score"]
            
            result_text = f"{home_team} {home_score} - {away_team} {away_score}"

            # Agregar los resultados a la lista
            results.append(result_text)
        
        if results:
            update.message.reply_text("\n".join(results))
        else:
            update.message.reply_text("No hay partidos de playoff hoy.")
    else:
        update.message.reply_text("No pude obtener los resultados. Intenta de nuevo más tarde.")

# Comando para obtener estadísticas de un equipo
def get_team_stats(update: Update, context: CallbackContext) -> None:
    team_name = " ".join(context.args)
    if not team_name:
        update.message.reply_text("Por favor, proporciona el nombre de un equipo.")
        return

    # Aquí puedes añadir la lógica para obtener estadísticas del equipo desde la API.
    # Usando una API como la de SportsRadar para obtener las estadísticas de un equipo.

    # Ejemplo de estructura de respuesta
    stats = {
        "Los Angeles Lakers": "25 victorias - 10 derrotas",
        "Miami Heat": "22 victorias - 13 derrotas"
    }

    team_stats = stats.get(team_name, "No se encontraron estadísticas para ese equipo.")
    update.message.reply_text(f"Estadísticas de {team_name}: {team_stats}")

# Comando para obtener los próximos partidos de playoff
def get_upcoming_games(update: Update, context: CallbackContext) -> None:
    # Aquí puedes obtener los próximos juegos a través de la API
    url = "https://api.sportsradar.com/nba/trial/v7/en/games/upcoming.json"  # Cambiar con la URL real

    response = requests.get(url, headers={"Authorization": f"Bearer {API_KEY}"})

    if response.status_code == 200:
        data = response.json()
        games = []
        for game in data["games"]:
            home_team = game["home_team"]["name"]
            away_team = game["away_team"]["name"]
            games.append(f"{home_team} vs {away_team}")

        if games:
            update.message.reply_text("Próximos partidos de playoffs:\n" + "\n".join(games))
        else:
            update.message.reply_text("No hay partidos de playoff programados.")
    else:
        update.message.reply_text("No pude obtener los próximos partidos. Intenta más tarde.")

# Función principal para inicializar el bot
def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Agregar los manejadores para los comandos
    dispatcher.add_handler(CommandHandler("results", get_playoff_results))
    dispatcher.add_handler(CommandHandler("team_stats", get_team_stats))
    dispatcher.add_handler(CommandHandler("upcoming_games", get_upcoming_games))

    # Iniciar el bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

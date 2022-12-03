"""
Exemple récapitulatif qui inclut les notions du chapitre 11 et de tous les autres.
"""


from ch8 import *
from ch9 import *
from ch10 import *
from my_bot import MyBot


def run_ch11_example():
	opts = parse_args()

	config, conf_file = load_config(opts.config_file)
	quotes = load_quotes(opts.quotes_file)
	vote_values = [s.strip() for s in conf_file["votes"]["values"].split(",")]
	ylimit = float(conf_file["votes"]["ylimit"])
	votes_plot = build_votes_plot(vote_values, ylimit)

	# TODO: Construire un objet de type `MyBot` avec "logs" comme dossier de journaux, les citations extraites du JSON et le graphique déjà construit.
	bot = ...
	bot.connect_and_join(config.password, config.nickname, config.channel)
	start_bot_and_show_plot(bot, bot.votes_plot)


if __name__ == "__main__":
	run_ch11_example()

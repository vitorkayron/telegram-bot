import telebot
from chaveapi import CHAVE_API

CHAVE_API = CHAVE_API

bot = telebot.TeleBot(CHAVE_API)


@bot.message_handler(commands=['Devops'])
def devops(mensagem):
    bot.reply_to(mensagem, 
        "- GIT\n" + 
        "- Linguagem de programação (Ex: Python)\n" + 
        "- Linux\n" + 
        "- Pandas\n" +
        "- Gerenciamento de Servidores \n" +  
        "- Contêineres\n" + 
        "- Infraestrutura do código\n" + 
        "- CI/CD\n" +
        "- Monitoramento e Observabilidade\n" +
        "- Provedor Cloud (Ex: AWS)\n" +
        "- Práticas de Engenharia de Software\n"
        "Deseja outro roadmap: Vá para /Iniciar"

    )


@bot.message_handler(commands=['Backend'])
def backend(mensagem):
    bot.reply_to(mensagem, 
        "- Básico de HTML, CSS e Javascript\n" + 
        "- Conhecimento de Servidor Web\n" + 
        "- Linguagem de programção e seus frameworks (Ex: JS + NodeJS)\n" + 
        "- Banco de Dados\n" + 
        "- GIT\n" + 
        "- Segurança da Web\n" + 
        "- API\n" + 
        "- Containerização e Teste\n" + 
        "- Provedor Cloud (Ex: AWS)\n" +
        "Deseja outro roadmap: Vá para /Iniciar"
    )


@bot.message_handler(commands=['Frontend'])
def frontend(mensagem):
    bot.reply_to(mensagem, 
        "- HTML, CSS e Javascript\n" + 
        "- CSS Frameworks (Ex: Bootstrap)\n" + 
        "- CSS Preprocessadores (Ex: Sass)\n" + 
        "- JavaScript Frameworks (Ex: Vue)\n" +
        "- Package Manager\n" +  
        "- GIT\n" + 
        "- Testes\n" + 
        "- Deploy\n" +
        "Deseja outro roadmap: Vá para /Iniciar"

    )

@bot.message_handler(commands=['DataScience'])
def datascience(mensagem):
    bot.reply_to(mensagem, 
        "- Estatísticas Descritivas\n" + 
        "- Probabilidade\n" + 
        "- Python\n" + 
        "- Pandas\n" +
        "- Numpy\n" +  
        "- Scipy\n" + 
        "- Limpeza de dados\n" + 
        "- Visualização de dados\n" +
        "- Dashboards\n" +
        "- SQL\n" +
        "- Python Regular Expression\n" +
        "- Análise de Séries Temporais\n" +
        "Deseja outro roadmap: Vá para /Iniciar"
    )


def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
	bot.reply_to(mensagem, """
	Esse é um bot para te ajudar a guiar os seus estudos na área da programação, atualmente temos esses roadmaps disponíveis:
	/Devops
	/Backend
	/Frontend
	/DataScience
	""")


bot.polling()
import discord
from discord.ext import commands
import random

# Configuración de intents
intents = discord.Intents.default()
intents.message_content = True  # Asegúrate de activar el contenido de los mensajes

# Creación del bot
bot = commands.Bot(command_prefix="/", intents=intents)

# Textos para el comando /info
textos = [
    "El planeta es nuestro hogar compartido. Pequeñas acciones como reciclar, ahorrar agua y reducir el uso de plásticos pueden marcar una gran diferencia para las futuras generaciones.",
    "Recuerda que cada gesto cuenta. Plantar un árbol, apagar las luces cuando no las necesites y optar por productos ecológicos son pasos sencillos para proteger nuestra Tierra.",
    "La naturaleza nos da todo lo que necesitamos para vivir. Cuidarla es nuestra responsabilidad. Elige opciones sostenibles y ayuda a conservar los recursos naturales para un mañana mejor.",
    "Reducir, reutilizar y reciclar no son solo palabras; son acciones esenciales para frenar el cambio climático. Hagamos lo posible por dejar un mundo más limpio y saludable.",
    "El futuro del planeta está en nuestras manos. Cada acción que tomemos hoy, por pequeña que sea, contribuye a mantener el equilibrio natural y asegurar un entorno habitable para todos.",
    "No tenemos un planeta B. Protejamos nuestros océanos, bosques y aire. Cambiar hábitos de consumo puede parecer un pequeño esfuerzo, pero juntos podemos lograr un gran impacto.",
    "Cuidar el mundo empieza con pequeñas decisiones diarias, como optar por la bici en vez del coche o llevar bolsas reutilizables al supermercado. Esas acciones se suman y ayudan a conservar nuestro planeta.",
    "Ser consciente de nuestra huella ecológica es el primer paso para reducirla. Cambia el consumo desmedido por elecciones responsables y así contribuirás a la salud de nuestro planeta.",
    "El cambio climático nos afecta a todos. Involúcrate en acciones que ayuden a mitigar sus efectos, como plantar árboles, reducir el consumo energético y apoyar a organizaciones medioambientales.",
    "Nuestra Tierra es un regalo que debemos proteger. Pequeñas decisiones como cerrar el grifo mientras te cepillas los dientes o elegir productos biodegradables ayudan a preservar la belleza natural del mundo."
]

# Lista de rutas de las imágenes
imagenes = [
    "Images/Imagen1.jpeg",
    "Images/Imagen2.jpeg",
    "Images/Imagen3.jpeg",
    "Images/Imagen4.jpeg",
    "Images/Imagen5.jpeg",
    "Images/Imagen6.jpeg",
    "Images/Imagen7.jpeg",
    "Images/Imagen8.jpeg",
    "Images/Imagen9.jpeg",
    "Images/Imagen10.jpeg"
]

# Eventos y comandos
@bot.event
async def on_ready():
    print(f'Bot {bot.user} conectado y listo para funcionar.')

@bot.command(name="cambioclimatico")
async def cambio_climatico(ctx):
    await ctx.send("El cambio climático es el aumento gradual de la temperatura promedio del planeta debido a actividades humanas, como la quema de combustibles fósiles, la deforestación y la industrialización.")

@bot.command(name="residuos")
async def residuos(ctx):
    await ctx.send("Los residuos pueden ser orgánicos o inorgánicos. Los orgánicos son biodegradables, como restos de comida, mientras que los inorgánicos incluyen materiales no biodegradables como plásticos y metales. Es importante separar y reciclar adecuadamente.")

@bot.command(name="ecoladrillos")
async def ecoladrillos(ctx):
    imagen = "Images/Imagen9.jpeg"
    texto = "Un ecoladrillo es una botella de plástico rellenada con residuos no reciclables, que se utiliza en la construcción de estructuras ecológicas. Es una forma de reutilizar plásticos y reducir la contaminación. Más información en https://www.gob.pe/institucion/minam/noticias/112195-ecoladrillos-una-util-e-innovadora-alternativa-para-tus-residuos-plasticos"
    await ctx.send(texto, file=discord.File(imagen))

@bot.command(name="info")
async def info(ctx):
    texto_aleatorio = random.choice(textos)
    imagen_aleatoria = random.choice(imagenes)
    await ctx.send(texto_aleatorio, file=discord.File(imagen_aleatoria))

@bot.command(name="ayuda")
async def ayuda(ctx):
    comandos = (
        "/cambioclimatico: Informar sobre el Cambio Climático.\n"
        "/residuos: Información sobre residuos, orgánicos e inorgánicos y cómo clasificarlos.\n"
        "/ecoladrillos: Información sobre qué es un ecoladrillo.\n"
        "/info: El bot envía textos aleatorios con información sobre cómo cuidar el mundo junto a una imagen.\n"
        "/ayuda: Muestra al usuario todos los comandos y sus funciones."
    )
    await ctx.send(f"------------COMANDOS------------\n{comandos}")

# Reemplaza 'YOUR_BOT_TOKEN' con tu token de bot seguro
bot.run('TOKEN')
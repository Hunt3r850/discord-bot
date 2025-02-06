import discord
from discord.ext import commands

# Configuración inicial
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Conectado como {bot.user}")

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="bienvenida")
    if channel:
        await channel.send(f"Bienvenido/a, {member.mention}, al servidor!")

@bot.command(name="limpiar")
@commands.has_permissions(manage_messages=True)
async def limpiar(ctx, cantidad: int):
    deleted = await ctx.channel.purge(limit=cantidad + 1)
    await ctx.send(f"{len(deleted) - 1} mensajes eliminados.", delete_after=5)

@bot.command(name="rol")
@commands.has_permissions(manage_roles=True)
async def asignar_rol(ctx, member: discord.Member, role: discord.Role):
    await member.add_roles(role)
    await ctx.send(f"Se ha asignado el rol {role.name} a {member.mention}.")

# Token del bot (obtenerlo desde el Discord Developer Portal)
bot.run("TU_TOKEN_AQUÍ")

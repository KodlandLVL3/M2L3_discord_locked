import discord
from discord.ext import commands
from logic import quiz_questions
from config import token

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

user_responses = {}


async def send_question(ctx_or_interaction, user_id):
    question = quiz_questions[user_responses[user_id]]
    buttons = question.gen_buttons()
    view = discord.ui.View()
    for button in buttons:
        view.add_item(button)

    if isinstance(ctx_or_interaction, commands.Context):
        await ctx_or_interaction.send(question.text, view=view)
    else:
        await ctx_or_interaction.followup.send(question.text, view=view)


@bot.event
async def on_ready():
    print(f'В систему вошел {bot.user}!')


@bot.event
async def on_interaction(interaction):
    user_id = interaction.user.id
    if user_id not in user_responses:
        await interaction.response.send_message("Пожалуйста, начните викторину, введя команду !start")
        return

    custom_id = interaction.data["custom_id"]
    if custom_id.startswith("correct"):
        await interaction.response.send_message("Ответ правильный!")
    elif custom_id.startswith("wrong"):
        await interaction.response.send_message("Ответ неправильный!")

    user_responses[user_id] += 1
    if user_responses[user_id] > len(quiz_questions) - 1:
        await interaction.followup.send("Конец викторины!")
    else:
        await send_question(interaction, user_id)


@bot.command()
async def start(ctx):
    user_id = ctx.author.id
    if user_id not in user_responses:
        user_responses[user_id] = 0
        await send_question(ctx, user_id)

bot.run(token)

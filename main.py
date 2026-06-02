import discord
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

SCRIM_CHANNEL_ID = 1511222831332069386
COMPETITION_CHANNEL_ID = 1511222974164893776
CHAT_KR_CHANNEL_ID = 1493161282524938372
CHAT_JP_CHANNEL_ID = 1493395325753364641

@client.event
async def on_ready():
    print(f'{client.user} 온라인!')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.channel.id == SCRIM_CHANNEL_ID:
        chat_kr = client.get_channel(CHAT_KR_CHANNEL_ID)
        chat_jp = client.get_channel(CHAT_JP_CHANNEL_ID)
        await chat_kr.send(
            f"⚽ **새 스크림 일정이 등록됐어요!**\n"
            f"👉 {message.jump_url}"
        )
        await chat_jp.send(
            f"⚽ **新しいスクリム日程が登録されました！**\n"
            f"👉 {message.jump_url}"
        )

    elif message.channel.id == COMPETITION_CHANNEL_ID:
        chat_kr = client.get_channel(CHAT_KR_CHANNEL_ID)
        chat_jp = client.get_channel(CHAT_JP_CHANNEL_ID)
        await chat_kr.send(
            f"🏆 **새 대회 일정이 등록됐어요!**\n"
            f"👉 {message.jump_url}"
        )
        await chat_jp.send(
            f"🏆 **新しい大会日程が登録されました！**\n"
            f"👉 {message.jump_url}"
        )

client.run(os.environ['DISCORD_TOKEN'])

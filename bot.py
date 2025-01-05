Methods**", 
        value="""
- 💳 **PayPal**
- 💳 **GCash**
        """, 
        inline=False
    )

    embed.add_field(
        name="💵 Currency Conversion", 
        value="Want to avail/buy using other currency? Just convert the value of USD to your currency.", 
        inline=False
    )

    embed.set_footer(
        text="SHEE MARKET | Trusted Pilot Service",
        icon_url="https://cdn-icons-png.flaticon.com/512/2175/2175103.png"  # Example icon
    )

    return embed

# Periodic announcement (every 5 minutes)
@tasks.loop(minutes=5)
async def send_service_announcement():
    channel = bot.get_channel(ANNOUNCEMENT_CHANNEL_ID)
    if channel:
        await channel.send("|| @here ||")  # This will mention @everyone
        await channel.send(embed=get_announcement())
    else:
        print("Channel not found!")

# Manual announcement command
@bot.command()
async def announce(ctx):
    """Manually trigger the service announcement"""
    channel = bot.get_channel(ANNOUNCEMENT_CHANNEL_ID)
    if channel:
        await channel.send("@everyone")  # This will mention @everyone
        await channel.send(embed=get_announcement())
        await ctx.send("Announcement sent!")
    else:
        await ctx.send("Announcement channel not found.")

# Run the bot
import os
from dotenv import load_dotenv

load_dotenv()
bot.run(os.getenv("MTMyMzkyMTEzNDEzMTA4OTQwOA.G6sVDD.Ycop4c-rWOrPmQz-cEb_i55iwWAaS6r27Z5uiI"))

import discord
from discord.ext import commands

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # Configure the welcome channel ID here
        self.welcome_channel_id = None  # Set this to your welcome channel ID

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        """Send a welcome message when a new member joins"""
        
        # Get the welcome channel
        if self.welcome_channel_id is None:
            return  # Welcome channel not configured
            
        welcome_channel = self.bot.get_channel(self.welcome_channel_id)
        
        if welcome_channel is None:
            print(f"Welcome channel with ID {self.welcome_channel_id} not found")
            return
        
        # Create welcome embed with member info
        embed = discord.Embed(
            title=f"Welcome to {member.guild.name}! 🎉",
            description=f"Hello {member.mention}, welcome to our community!",
            color=discord.Color.green()
        )
        
        # Add member info
        embed.add_field(name="Username", value=member.name, inline=True)
        embed.add_field(name="Account Created", value=member.created_at.strftime("%Y-%m-%d"), inline=True)
        embed.add_field(name="Total Members", value=member.guild.member_count, inline=True)
        
        # Set member's avatar as embed thumbnail
        embed.set_thumbnail(url=member.display_avatar.url)
        
        # Set footer
        embed.set_footer(text=f"User ID: {member.id}")
        
        try:
            await welcome_channel.send(embed=embed)
        except discord.Forbidden:
            print(f"No permission to send message in {welcome_channel.name}")
        except Exception as e:
            print(f"Error sending welcome message: {e}")

    @commands.command(name='setwelcome')
    @commands.has_permissions(administrator=True)
    async def set_welcome_channel(self, ctx, channel: discord.TextChannel):
        """Set the welcome channel (Admin only)"""
        self.welcome_channel_id = channel.id
        await ctx.send(f"✅ Welcome channel set to {channel.mention}")

async def setup(bot):
    await bot.add_cog(Welcome(bot))

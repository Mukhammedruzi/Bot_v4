# agents/writer_agent.py

"""
Bot_v4 AI Writer Agent

Creates:
- YouTube Shorts scripts
- Long video scripts
- Telegram posts
- Titles
- Hashtags
- Tags
"""


from datetime import datetime


class WriterAgent:
    """
    AI content writing agent.
    """


    def __init__(self):

        self.name = "writer_agent"

        self.formats = [
            "shorts",
            "youtube_video",
            "telegram_post"
        ]



    async def initialize(self):

        return {
            "agent": self.name,
            "status": "initialized"
        }



    def create_title(self, topic):

        """
        Generate content title.
        """

        return f"{topic} - Latest Update"



    def create_hashtags(self, topic):

        """
        Generate hashtags.
        """

        return [
            "#PUBGMobile",
            "#MLBB",
            "#Gaming",
            "#GamingNews"
        ]



    def create_tags(self, topic):

        """
        Generate YouTube tags.
        """

        return [
            "PUBG Mobile",
            "Mobile Legends",
            "Gaming News",
            topic
        ]



    async def write_shorts(self, topic):

        return {

            "type": "shorts",

            "title": self.create_title(topic),

            "script": (
                f"Today we talk about {topic}. "
                "Here are the most important details."
            ),

            "hashtags": self.create_hashtags(topic),

            "tags": self.create_tags(topic)

        }



    async def write_video(self, topic):

        return {

            "type": "long_video",

            "title": self.create_title(topic),

            "script": (
                f"Full analysis about {topic}. "
                "Explanation and details included."
            ),

            "hashtags": self.create_hashtags(topic),

            "tags": self.create_tags(topic)

        }



    async def write_telegram_post(self, topic):

        return {

            "type": "telegram_post",

            "text": (
                f"🔥 Gaming News\n\n"
                f"{topic}\n\n"
                "Follow for more updates."
            ),

            "time": datetime.now().isoformat()

        }



    async def execute(self, task):

        """
        Main entry from Core Brain.
        """

        content = await self.write_shorts(
            task
        )


        return {

            "agent": self.name,

            "content": content

        }

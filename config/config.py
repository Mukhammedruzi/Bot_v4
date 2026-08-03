# config/config.py

"""
Bot_v4 Configuration Center

Central place for all system settings.
"""


class Config:

    """
    Global Bot_v4 settings.
    """


    def __init__(self):

        # System
        self.BOT_NAME = "Bot_v4"

        self.VERSION = "4.0"



        # Content Settings
        self.CONTENT = {

            "shorts_per_day": 2,

            "videos_per_day": 2,

            "telegram_posts_per_day": 2

        }



        # Publishing Settings
        self.PUBLISH = {

            "first_publish_time": "18:00",

            "min_interval_minutes": 60

        }



        # Platforms

        self.YOUTUBE = {

            "enabled": True,

            "channel_id": UCQpCgTk5pzaBRlqFmeihH6A

            "api_key": AIzaSyD03QCX30h71YU8Sbmbig8UjIZkOE_IQQg

        }


        self.TELEGRAM = {

            "enabled": True,

            "channel_id": -1003871590185

            "bot_token": 8933602635:AAHXU83fouMA70mCrTCdJ49yDDAneo1QA9I

        }



        # Agents

        self.AGENTS = {

            "news_agent": True,

            "research_agent": True,

            "writer_agent": True,

            "media_agent": True,

            "quality_agent": True,

            "publisher_agent": True,

            "analytics_agent": True,

            "learning_agent": True,

            "health_monitor": True

        }



        # Storage

        self.STORAGE = {

            "database": "bot_v4.db",

            "logs": True

        }



    def get(self, section):

        """
        Get configuration section.
        """

        return getattr(
            self,
            section,
            None
        )



    def all(self):

        """
        Return all settings.
        """

        return {

            "bot_name":
            self.BOT_NAME,

            "version":
            self.VERSION,

            "content":
            self.CONTENT,

            "publish":
            self.PUBLISH,

            "agents":
            self.AGENTS

        }



config = Config()

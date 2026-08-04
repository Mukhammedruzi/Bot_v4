# agents/media_agent.py

import os
import logging
from datetime import datetime


class MediaAgent:

    def __init__(self):

        self.name = "media_agent"

        self.logger = logging.getLogger(
            "BOT_V4"
        )

        self.media_api_key = os.getenv(
            "MEDIA_API_KEY"
        )


    async def execute(self, task):

        try:

            self.logger.info(
                "Media Agent started"
            )


            media = await self.create_media(
                task
            )


            result = {

                "agent": self.name,

                "status": "completed",

                "time": datetime.now().isoformat(),

                "input": task,

                "media": media

            }


            self.logger.info(
                "Media Agent finished"
            )


            return result


        except Exception as error:

            self.logger.error(
                f"Media Agent error: {error}"
            )

            raise error



    async def create_media(self, content):

        """
        Video, audio, subtitle, thumbnail
        generator ulanish joyi.

        API key .env orqali olinadi.
        """

        if not self.media_api_key:

            return {

                "video": None,

                "audio": None,

                "thumbnail": None,

                "subtitle": None,

                "status": "media_generator_not_connected"

            }


        return {

            "video": "",

            "audio": "",

            "thumbnail": "",

            "subtitle": "",

            "status": "media_created"

        }

# agents/writer_agent.py

import os
import logging
from datetime import datetime


class WriterAgent:

    def __init__(self):

        self.name = "writer_agent"

        self.logger = logging.getLogger(
            "BOT_V4"
        )

        self.api_key = os.getenv(
            "AI_API_KEY"
        )


    async def execute(self, task):

        try:

            self.logger.info(
                "Writer Agent started"
            )


            script = await self.create_content(
                task
            )


            result = {

                "agent": self.name,

                "status": "completed",

                "time": datetime.now().isoformat(),

                "input": task,

                "content": script

            }


            self.logger.info(
                "Writer Agent finished"
            )


            return result


        except Exception as error:

            self.logger.error(
                f"Writer Agent error: {error}"
            )

            raise error



    async def create_content(self, data):

        """
        AI model ulanish joyi.
        API key .env orqali olinadi.
        """

        if not self.api_key:

            return {

                "type": "script",

                "title": "Generated content",

                "text": str(data)

            }


        return {

            "type": "ai_script",

            "title": "AI generated script",

            "text": ""

        }

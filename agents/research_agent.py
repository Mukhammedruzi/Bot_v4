# agents/research_agent.py

import os
import logging
from datetime import datetime


class ResearchAgent:

    def __init__(self):

        self.name = "research_agent"

        self.logger = logging.getLogger(
            "BOT_V4"
        )

        self.api_key = os.getenv(
            "RESEARCH_API_KEY"
        )


    async def execute(self, task):

        try:

            self.logger.info(
                "Research Agent started"
            )


            research = await self.research_topic(
                task
            )


            result = {

                "agent": self.name,

                "status": "completed",

                "time": datetime.now().isoformat(),

                "topic": task,

                "research": research

            }


            self.logger.info(
                "Research Agent finished"
            )


            return result


        except Exception as error:

            self.logger.error(
                f"Research Agent error: {error}"
            )

            raise error



    async def research_topic(self, topic):

        """
        Research API yoki AI model ulanish joyi.
        API key .env orqali olinadi.
        """

        if not self.api_key:

            return {

                "source": "internal",

                "topic": topic,

                "information": []

            }


        return {

            "source": "research_api",

            "topic": topic,

            "information": []

        }

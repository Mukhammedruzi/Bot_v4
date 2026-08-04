# agents/news_agent.py

import os
import logging
from datetime import datetime


class NewsAgent:

    def __init__(self):

        self.name = "news_agent"

        self.logger = logging.getLogger(
            "BOT_V4"
        )

        self.api_key = os.getenv(
            "NEWS_API_KEY"
        )


    async def execute(self, task):

        try:

            self.logger.info(
                "News Agent started"
            )


            news_data = await self.collect_news(
                task
            )


            result = {

                "agent": self.name,

                "status": "completed",

                "time": datetime.now().isoformat(),

                "topic": task,

                "data": news_data

            }


            self.logger.info(
                "News Agent finished"
            )


            return result


        except Exception as error:

            self.logger.error(
                f"News Agent error: {error}"
            )

            raise error



    async def collect_news(self, topic):

        """
        Real API ulanish shu yerga qo'yiladi.
        NEWS_API_KEY .env orqali olinadi.
        """

        if not self.api_key:

            return {

                "source": "local",

                "message": "API key not configured",

                "topic": topic

            }


        # API request keyinchalik shu yerda bo'ladi

        return {

            "source": "news_api",

            "topic": topic,

            "items": []

            }

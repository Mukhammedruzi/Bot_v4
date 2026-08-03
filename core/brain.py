# core/brain.py

"""
Bot_v4 Core Brain

Main controller for:
- News Agent
- Research Agent
- AI Writer
- Media Agent
- Quality Agent
- Smart Publish Manager
- Publisher Agent
- Analytics Agent
- Learning Agent
- Health Monitor

"""

import os
import asyncio
import logging
from datetime import datetime
from typing import Dict, Any, Optional


# ==============================
# 1. CORE SETUP
# ==============================


class ConfigCenter:
    """
    Central configuration manager.
    All system settings are controlled here.
    """

    def __init__(self):
        self.config = {
            "bot_name": "Bot_v4",

            "content": {
                "shorts_per_day": 2,
                "videos_per_day": 2,
                "telegram_posts_per_day": 2,
            },

            "publish": {
                "first_publish_time": "18:00",
            },

            "agents": {
                "news_agent": True,
                "research_agent": True,
                "writer_agent": True,
                "media_agent": True,
                "quality_agent": True,
                "publisher_agent": True,
                "analytics_agent": True,
                "learning_agent": True,
                "health_monitor": True,
            }
        }

    def get(self, key: str):
        return self.config.get(key)

    def all(self):
        return self.config


class LoggerSystem:
    """
    Global logging system.
    """

    def __init__(self):
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )

        self.logger = logging.getLogger("BOT_V4")

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)

    def warning(self, message):
        self.logger.warning(message)


class HealthMonitor:
    """
    System health monitoring.
    """

    def __init__(self):
        self.status = "starting"
        self.errors = []

    def update(self, status):
        self.status = status

    def add_error(self, error):
        self.errors.append({
            "time": datetime.now().isoformat(),
            "error": str(error)
        })


class Storage:
    """
    Data storage layer.
    """

    def __init__(self):
        self.data = {
            "tasks": [],
            "content_history": [],
            "analytics": [],
            "learning_data": []
        }

    def save(self, key, value):
        if key in self.data:
            self.data[key].append(value)

    def get(self, key):
        return self.data.get(key, [])
# ==============================
# 2. AGENT MANAGER
# ==============================


class AgentManager:
    """
    All AI agents are managed from here.
    """

    def __init__(self, logger):
        self.logger = logger
        self.agents = {}

    def register_agent(self, name, agent):
        """
        Add new agent to system.
        """
        self.agents[name] = agent
        self.logger.info(f"Agent registered: {name}")

    def get_agent(self, name):
        return self.agents.get(name)

    async def run_agent(self, name, task):
        """
        Run selected agent.
        """

        agent = self.get_agent(name)

        if not agent:
            raise Exception(
                f"Agent not found: {name}"
            )

        try:
            self.logger.info(
                f"Running agent: {name}"
            )

            result = await agent.execute(task)

            return result

        except Exception as error:
            self.logger.error(
                f"{name} error: {error}"
            )

            raise error


# ==============================
# AGENT INTERFACES
# ==============================


class BaseAgent:
    """
    Base structure for all future agents.
    """

    def __init__(self, name):
        self.name = name

    async def execute(self, task):
        raise NotImplementedError(
            "Agent execute method required"
        )


class NewsAgent(BaseAgent):
    """
    PUBG and MLBB news collector.
    """

    async def execute(self, task):
        return {
            "agent": self.name,
            "status": "news collected",
            "data": task
        }


class ResearchAgent(BaseAgent):
    """
    Creates ideas when news is unavailable.
    """

    async def execute(self, task):
        return {
            "agent": self.name,
            "status": "research completed",
            "data": task
        }


class WriterAgent(BaseAgent):
    """
    Creates scripts and posts.
    """

    async def execute(self, task):
        return {
            "agent": self.name,
            "status": "content written",
            "data": task
        }


class MediaAgent(BaseAgent):
    """
    Creates video, audio, subtitles and thumbnails.
    """

    async def execute(self, task):
        return {
            "agent": self.name,
            "status": "media created",
            "data": task
        }


class QualityAgent(BaseAgent):
    """
    Checks content before publishing.
    """

    async def execute(self, task):
        return {
            "agent": self.name,
            "status": "quality checked",
            "data": task
        }


class PublisherAgent(BaseAgent):
    """
    Publishes content to platforms.
    """

    async def execute(self, task):
        return {
            "agent": self.name,
            "status": "published",
            "data": task
      }
# ==============================
# 3. TASK PIPELINE
# ==============================


class TaskQueue:
    """
    Controls all system tasks.
    """

    def __init__(self, logger):
        self.queue = []
        self.logger = logger

    def add_task(self, task):
        self.queue.append(task)

        self.logger.info(
            f"Task added: {task}"
        )

    def get_task(self):
        if self.queue:
            return self.queue.pop(0)

        return None

    def size(self):
        return len(self.queue)



class Scheduler:
    """
    Controls publishing and execution timing.
    """

    def __init__(self, logger):
        self.logger = logger
        self.schedule = []

    def add_schedule(self, time, task):
        self.schedule.append({
            "time": time,
            "task": task
        })

        self.logger.info(
            f"Schedule added: {time}"
        )

    def get_schedule(self):
        return self.schedule



class ContentPipeline:
    """
    Main content workflow:

    News/Research
        ↓
    Writer
        ↓
    Media
        ↓
    Quality
        ↓
    Publisher
        ↓
    Analytics
        ↓
    Learning
    """

    def __init__(
        self,
        agent_manager,
        storage,
        logger
    ):
        self.agent_manager = agent_manager
        self.storage = storage
        self.logger = logger


    async def process_content(
        self,
        source,
        topic
    ):

        try:
            self.logger.info(
                "Content pipeline started"
            )


            research = await self.agent_manager.run_agent(
                "research_agent",
                topic
            )


            written = await self.agent_manager.run_agent(
                "writer_agent",
                research
            )


            media = await self.agent_manager.run_agent(
                "media_agent",
                written
            )


            quality = await self.agent_manager.run_agent(
                "quality_agent",
                media
            )


            published = await self.agent_manager.run_agent(
                "publisher_agent",
                quality
            )


            self.storage.save(
                "content_history",
                published
            )


            return published


        except Exception as error:

            self.logger.error(
                f"Pipeline error: {error}"
            )

            raise error
# ==============================
# 4. RUNTIME / CORE ENGINE
# ==============================


class CoreBrain:
    """
    Main brain controller of Bot_v4.
    Controls all systems.
    """

    def __init__(self):

        self.config = ConfigCenter()

        self.logger = LoggerSystem()

        self.health = HealthMonitor()

        self.storage = Storage()

        self.agent_manager = AgentManager(
            self.logger
        )

        self.task_queue = TaskQueue(
            self.logger
        )

        self.scheduler = Scheduler(
            self.logger
        )

        self.pipeline = ContentPipeline(
            self.agent_manager,
            self.storage,
            self.logger
        )


    def load_agents(self):
        """
        Register all system agents.
        """

        agents = [

            NewsAgent(
                "news_agent"
            ),

            ResearchAgent(
                "research_agent"
            ),

            WriterAgent(
                "writer_agent"
            ),

            MediaAgent(
                "media_agent"
            ),

            QualityAgent(
                "quality_agent"
            ),

            PublisherAgent(
                "publisher_agent"
            )

        ]


        for agent in agents:

            self.agent_manager.register_agent(
                agent.name,
                agent
            )


        self.logger.info(
            "All agents loaded"
        )


    async def start(self):

        try:

            self.logger.info(
                "Bot_v4 starting..."
            )


            self.health.update(
                "running"
            )


            self.load_agents()


            self.logger.info(
                "Bot_v4 is ready"
            )


        except Exception as error:

            self.health.add_error(
                error
            )

            self.health.update(
                "failed"
            )

            self.logger.error(
                error
            )

            raise error



    async def shutdown(self):

        self.health.update(
            "stopped"
        )

        self.logger.info(
            "Bot_v4 stopped"
        )



    async def run_content_cycle(
        self,
        topic
    ):

        result = await self.pipeline.process_content(
            "AI",
            topic
        )

        return result



# ==============================
# MAIN RUNNER
# ==============================


async def main():

    brain = CoreBrain()

    await brain.start()


    # Test cycle
    result = await brain.run_content_cycle(
        "PUBG Mobile latest update"
    )


    print(
        result
    )


    await brain.shutdown()



if __name__ == "__main__":

    asyncio.run(
        main()
      )

# core/brain.py

"""
Bot_v4 Core Brain

Main controller:
- Agents
- Pipeline
- Storage
- Scheduler
- Health Monitor
"""

import logging
from datetime import datetime


# ==============================
# AGENT IMPORTS
# ==============================

from agents.news_agent import NewsAgent
from agents.research_agent import ResearchAgent
from agents.writer_agent import WriterAgent
from agents.media_agent import MediaAgent
from agents.quality_agent import QualityAgent
from agents.publisher_agent import PublisherAgent
from agents.analytics_agent import AnalyticsAgent
from agents.learning_agent import LearningAgent



# ==============================
# LOGGER
# ==============================


class LoggerSystem:

    def __init__(self):

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )

        self.logger = logging.getLogger(
            "BOT_V4"
        )


    def info(self, message):

        self.logger.info(message)


    def error(self, message):

        self.logger.error(message)



# ==============================
# HEALTH
# ==============================


class HealthMonitor:

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



# ==============================
# STORAGE
# ==============================


class Storage:

    def __init__(self):

        self.data = {

            "content_history": [],

            "analytics": [],

            "learning": []

        }


    def save(self, key, value):

        if key in self.data:

            self.data[key].append(
                value
            )


# ==============================
# AGENT MANAGER
# ==============================


class AgentManager:

    def __init__(self, logger):

        self.logger = logger

        self.agents = {}



    def register_agent(self, agent):

        self.agents[agent.name] = agent

        self.logger.info(
            f"Agent loaded: {agent.name}"
        )



    async def run_agent(self, name, task):

        agent = self.agents.get(name)


        if not agent:

            raise Exception(
                f"Agent missing: {name}"
            )


        return await agent.execute(
            task
        )



# ==============================
# PIPELINE
# ==============================


class ContentPipeline:

    def __init__(
        self,
        manager,
        storage,
        logger
    ):

        self.manager = manager

        self.storage = storage

        self.logger = logger



    async def run(self, topic):

        self.logger.info(
            "Pipeline started"
        )


        news = await self.manager.run_agent(
            "news_agent",
            topic
        )


        research = await self.manager.run_agent(
            "research_agent",
            news
        )


        writer = await self.manager.run_agent(
            "writer_agent",
            research
        )


        media = await self.manager.run_agent(
            "media_agent",
            writer
        )


        quality = await self.manager.run_agent(
            "quality_agent",
            media
        )


        publish = await self.manager.run_agent(
            "publisher_agent",
            quality
        )


        analytics = await self.manager.run_agent(
            "analytics_agent",
            publish
        )


        learning = await self.manager.run_agent(
            "learning_agent",
            analytics
        )


        result = {

            "publish": publish,

            "analytics": analytics,

            "learning": learning

        }


        self.storage.save(
            "content_history",
            result
        )


        self.logger.info(
            "Pipeline finished"
        )


        return result



# ==============================
# CORE BRAIN
# ==============================


class CoreBrain:


    def __init__(self):

        self.logger = LoggerSystem()

        self.health = HealthMonitor()

        self.storage = Storage()


        self.agent_manager = AgentManager(
            self.logger
        )


        self.pipeline = ContentPipeline(
            self.agent_manager,
            self.storage,
            self.logger
        )



    def load_agents(self):

        agents = [

            NewsAgent(),

            ResearchAgent(),

            WriterAgent(),

            MediaAgent(),

            QualityAgent(),

            PublisherAgent(),

            AnalyticsAgent(),

            LearningAgent()

        ]


        for agent in agents:

            self.agent_manager.register_agent(
                agent
            )



    async def start(self):

        self.logger.info(
            "Bot_v4 starting..."
        )


        self.load_agents()


        self.health.update(
            "running"
        )


        self.logger.info(
            "Bot_v4 ready"
        )



    async def run_cycle(self, topic):

        return await self.pipeline.run(
            topic
        )



    async def shutdown(self):

        self.health.update(
            "stopped"
        )


        self.logger.info(
            "Bot_v4 stopped"
        )

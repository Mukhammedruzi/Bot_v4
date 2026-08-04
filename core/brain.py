# core/brain.py

"""
Bot_v4 Core Brain

Main controller for:
- News Agent
- Research Agent
- AI Writer
- Media Agent
- Quality Agent
- Publisher Agent
- Analytics Agent
- Learning Agent
"""

import logging
from datetime import datetime


# ==============================
# CORE CONFIGURATION
# ==============================


class ConfigCenter:

    def __init__(self):

        self.config = {

            "bot_name": "Bot_v4",

            "content": {
                "shorts_per_day": 2,
                "videos_per_day": 2,
                "telegram_posts_per_day": 2,
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
            }
        }


    def get(self, key):

        return self.config.get(key)


    def all(self):

        return self.config



# ==============================
# LOGGER SYSTEM
# ==============================


class LoggerSystem:

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



# ==============================
# HEALTH MONITOR
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

            "tasks": [],

            "content_history": [],

            "analytics": [],

            "learning": []

        }


    def save(self, key, value):

        if key in self.data:

            self.data[key].append(value)


    def get(self, key):

        return self.data.get(key, [])



# ==============================
# BASE AGENT
# ==============================


class BaseAgent:

    def __init__(self, name):

        self.name = name


    async def execute(self, task):

        raise NotImplementedError



# ==============================
# AGENTS
# ==============================


class NewsAgent(BaseAgent):

    async def execute(self, task):

        return {

            "agent": self.name,

            "result": "news collected",

            "data": task

        }



class ResearchAgent(BaseAgent):

    async def execute(self, task):

        return {

            "agent": self.name,

            "result": "research completed",

            "data": task

        }



class WriterAgent(BaseAgent):

    async def execute(self, task):

        return {

            "agent": self.name,

            "result": "script created",

            "data": task

        }



class MediaAgent(BaseAgent):

    async def execute(self, task):

        return {

            "agent": self.name,

            "result": "media created",

            "data": task

        }
# ==============================
# MORE AGENTS
# ==============================


class QualityAgent(BaseAgent):

    async def execute(self, task):

        return {

            "agent": self.name,

            "result": "quality checked",

            "data": task

        }



class PublisherAgent(BaseAgent):

    async def execute(self, task):

        return {

            "agent": self.name,

            "result": "published",

            "data": task

        }



class AnalyticsAgent(BaseAgent):

    async def execute(self, task):

        return {

            "agent": self.name,

            "result": "analytics collected",

            "data": task

        }



class LearningAgent(BaseAgent):

    async def execute(self, task):

        return {

            "agent": self.name,

            "result": "learning updated",

            "data": task

        }



# ==============================
# AGENT MANAGER
# ==============================


class AgentManager:

    def __init__(self, logger):

        self.logger = logger

        self.agents = {}



    def register_agent(self, name, agent):

        self.agents[name] = agent

        self.logger.info(
            f"Agent registered: {name}"
        )



    def get_agent(self, name):

        return self.agents.get(name)



    async def run_agent(self, name, task):

        agent = self.get_agent(name)


        if not agent:

            raise Exception(
                f"Agent not found: {name}"
            )


        self.logger.info(
            f"Running {name}"
        )


        return await agent.execute(task)



# ==============================
# TASK QUEUE
# ==============================


class TaskQueue:

    def __init__(self, logger):

        self.logger = logger

        self.queue = []



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



# ==============================
# SCHEDULER
# ==============================


class Scheduler:

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
# ==============================
# CONTENT PIPELINE
# ==============================


class ContentPipeline:

    def __init__(
        self,
        agent_manager,
        storage,
        logger
    ):

        self.agent_manager = agent_manager

        self.storage = storage

        self.logger = logger



    async def process_content(self, topic):

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


        analytics = await self.agent_manager.run_agent(
            "analytics_agent",
            published
        )


        learning = await self.agent_manager.run_agent(
            "learning_agent",
            analytics
        )


        result = {

            "published": published,

            "analytics": analytics,

            "learning": learning

        }


        self.storage.save(
            "content_history",
            result
        )


        self.logger.info(
            "Content pipeline finished"
        )


        return result




# ==============================
# CORE BRAIN
# ==============================


class CoreBrain:


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
            ),

            AnalyticsAgent(
                "analytics_agent"
            ),

            LearningAgent(
                "learning_agent"
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


            self.load_agents()


            self.health.update(
                "running"
            )


            self.logger.info(
                "Bot_v4 ready"
            )


        except Exception as error:

            self.health.add_error(
                error
            )

            self.health.update(
                "failed"
            )

            raise error



    async def run_cycle(self, topic):

        return await self.pipeline.process_content(
            topic
        )



    async def shutdown(self):

        self.health.update(
            "stopped"
        )


        self.logger.info(
            "Bot_v4 stopped"
        )

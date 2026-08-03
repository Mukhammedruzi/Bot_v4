# agents/health_monitor.py

"""
Bot_v4 Health Monitor Agent

Monitors:
- System status
- Agent errors
- Runtime problems
- Logs
"""


from datetime import datetime


class HealthMonitor:
    """
    System health monitoring agent.
    """


    def __init__(self):

        self.name = "health_monitor"

        self.status = "starting"

        self.errors = []

        self.logs = []



    async def initialize(self):

        self.status = "running"

        return {
            "agent": self.name,
            "status": self.status
        }



    def add_log(self, message):

        """
        Save system log.
        """

        self.logs.append({

            "message": message,

            "time": datetime.now().isoformat()

        })



    def report_error(self, error, source="unknown"):

        """
        Save error information.
        """

        error_data = {

            "source": source,

            "error": str(error),

            "time": datetime.now().isoformat()

        }


        self.errors.append(
            error_data
        )


        return error_data



    def check_status(self):

        """
        Return current health status.
        """

        return {

            "agent": self.name,

            "status": self.status,

            "errors":
                len(self.errors),

            "logs":
                len(self.logs)

        }



    def update_status(self, status):

        self.status = status



    async def execute(self, task):

        """
        Main entry from Core Brain.
        """

        return {

            "agent": self.name,

            "health": self.check_status(),

            "task": task

        }

# agents/quality_agent.py

"""
Bot_v4 Quality Agent

Checks content before publishing:
- Quality
- Errors
- Completeness
- Platform readiness
"""


from datetime import datetime


class QualityAgent:
    """
    Content quality control agent.
    """


    def __init__(self):

        self.name = "quality_agent"

        self.rules = [
            "check_title",
            "check_script",
            "check_thumbnail",
            "check_tags",
            "check_platform_rules"
        ]



    async def initialize(self):

        return {
            "agent": self.name,
            "status": "initialized"
        }



    def check_title(self, content):

        """
        Check title quality.
        """

        title = content.get(
            "title",
            ""
        )

        return bool(title)



    def check_script(self, content):

        """
        Check script availability.
        """

        script = content.get(
            "script",
            ""
        )

        return bool(script)



    def check_thumbnail(self, content):

        """
        Check thumbnail data.
        """

        return (
            "thumbnail" in content
            or
            "image" in content
        )



    def check_tags(self, content):

        """
        Check hashtags and tags.
        """

        return (
            "hashtags" in content
            or
            "tags" in content
        )



    async def review(self, content):

        """
        Full quality review.
        """

        checks = {

            "title":
            self.check_title(content),

            "script":
            self.check_script(content),

            "thumbnail":
            self.check_thumbnail(content),

            "tags":
            self.check_tags(content)

        }


        approved = all(
            checks.values()
        )


        return {

            "approved": approved,

            "checks": checks,

            "time": datetime.now().isoformat()

        }



    async def execute(self, task):

        """
        Main entry from Core Brain.
        """

        result = await self.review(
            task
        )


        return {

            "agent": self.name,

            "result": result

      }

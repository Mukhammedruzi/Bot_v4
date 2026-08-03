# storage/database.py

"""
Bot_v4 Database Storage

Stores:
- Content history
- Analytics data
- Learning data
- Logs
- Tasks
"""


import json
import os
from datetime import datetime



class Database:

    """
    Simple local storage system.
    """


    def __init__(self, file_name="bot_v4_data.json"):

        self.file_name = file_name

        self.data = {

            "content_history": [],

            "analytics": [],

            "learning": [],

            "logs": [],

            "tasks": []

        }


        self.load()



    def load(self):

        """
        Load saved data.
        """

        if os.path.exists(
            self.file_name
        ):

            try:

                with open(
                    self.file_name,
                    "r",
                    encoding="utf-8"
                ) as file:

                    self.data = json.load(
                        file
                    )


            except Exception:

                self.data = {}



    def save(self):

        """
        Save all data.
        """

        with open(
            self.file_name,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.data,
                file,
                indent=4,
                ensure_ascii=False
            )



    def add(self, section, value):

        """
        Add new record.
        """

        if section in self.data:

            self.data[section].append(
                value
            )

            self.save()



    def get(self, section):

        """
        Get stored data.
        """

        return self.data.get(
            section,
            []
        )



    def add_log(self, message):

        """
        Save system log.
        """

        self.add(
            "logs",
            {
                "message": message,

                "time":
                datetime.now().isoformat()
            }
        )



    def clear(self, section):

        """
        Clear selected data.
        """

        if section in self.data:

            self.data[section] = []

            self.save()

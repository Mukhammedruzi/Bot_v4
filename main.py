# main.py

import asyncio
import logging

from core.brain import CoreBrain



logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)



async def main():

    brain = CoreBrain()


    try:

        await brain.start()


        print(
            "Bot_v4 started successfully"
        )


        while True:

            await asyncio.sleep(
                60
            )


    except KeyboardInterrupt:

        print(
            "Stopping Bot_v4..."
        )


    except Exception as error:

        logging.error(
            f"System error: {error}"
        )


    finally:

        await brain.shutdown()



if __name__ == "__main__":

    asyncio.run(
        main()
    )

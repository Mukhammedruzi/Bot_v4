# main.py

"""
Bot_v4 Main Runner

Starts the complete AI system.
"""


import asyncio


from core.brain import CoreBrain



async def start_bot():

    """
    Start Bot_v4 system.
    """

    brain = CoreBrain()


    await brain.start()


    print(
        "Bot_v4 started successfully"
    )


    return brain



async def stop_bot(brain):

    """
    Shutdown Bot_v4 system.
    """

    await brain.shutdown()


    print(
        "Bot_v4 stopped"
    )



async def main():
    logger.info("Main started")

    while True:
        try:
            logger.info("Cycle started")

            # bu yerda eski ishlar turadi

            logger.info("Cycle finished")

            await asyncio.sleep(900)  # 15 daqiqa kutish

        except Exception as e:
            logger.error(f"Error: {e}")
            await asyncio.sleep(60)

        except KeyboardInterrupt:

            print(
                "Stopping Bot_v4..."
            )


        except Exception as error:

            print(
                f"System error: {error}"
            )


    finally:

        if brain:

            await stop_bot(
                brain
            )


if __name__ == "__main__":

    asyncio.run(
        main()
    )

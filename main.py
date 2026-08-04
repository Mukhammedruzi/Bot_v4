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

    brain = None


        try:

            while True:

                brain = await start_bot()

                print(
                    "Bot_v4 started"
                )

                # 2 soat ishlash
                await asyncio.sleep(
                    2 * 60 * 60
                )
  

                print(
                    "Bot_v4 resting..."
                )

                # botni to'xtatish
                if brain:

                    await stop_bot(
                        brain
                    )

                    brain = None


                # 15 daqiqa dam
                await asyncio.sleep(
                    15 * 60
                )
            
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

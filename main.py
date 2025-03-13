import argparse
import logging
import os
import asyncio
from agents import Runner
from my_agent import joker_agent


def define_options():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--api_key', dest='api_key', required=True,
        help='OpenAI API KEY'
    )
    options = parser.parse_args()
    return options


def setup_logger():
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    handler.setFormatter(
        logging.Formatter('%(asctime)s %(name)-8s %(levelname)-8s %(message)s [%(filename)s:%(lineno)d]'))
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger


async def run_agent():
    result = await Runner.run(joker_agent, "Tell a joke about the weather")
    print(result.final_output)


async def main():
    logger = setup_logger()
    options = define_options()
    os.environ['OPENAI_API_KEY'] = options.api_key

    await run_agent()


if __name__ == '__main__':
    asyncio.run(main())

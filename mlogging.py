from loguru import logger

logger.remove()
logger.add("logs.log", format="{time}|{level}|{message}", level="INFO",
           rotation="50 KB", compression="zip")
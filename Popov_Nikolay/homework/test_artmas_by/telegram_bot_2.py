from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os
import zipfile
import time
import asyncio
from pathlib import Path


async def execute_command(cmd, timeout: int=300):
    try:
        process = await asyncio.create_subprocess_shell(cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
        )

        stdout, stderr = await asyncio.wait_for(process.communicate(), timeout)
        output = f'STDOUT:\n{stdout.decode().strip()}' if stdout else ''
        output += f'\nSTDERR:\n{stderr.decode().strip()}' if stderr else ''
        return output.strip()
    except asyncio.TimeoutError:
        return f'Таймаут {timeout} сек'
    except Exception as es:
        return f'Ошибка {str(es)}'


current_dir = os.getcwd()
result = asyncio.run(execute_command(f"pytest -s -v {current_dir}"))
print(result)


#!/usr/bin/env python3
"""This module provides a coroutine for measuring async runtime."""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """This coroutine measures the runtime of four async comprehensions."""
    start = time.time()

    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )

    total = time.time() - start
    return round(total, 2)

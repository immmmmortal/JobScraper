from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator

from fastapi import FastAPI, Depends
from playwright.sync_api import sync_playwright
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from db import async_session
from db import engine, Base
from models import JobTitle
from scraper import fetch_job_titles


async def get_session() -> AsyncGenerator[Any, Any]:
    async with async_session() as session:
        yield session


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Create tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Shutdown: Dispose the engine if needed
    await engine.dispose()


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/scrape")
def scrape_website(url: str):
    with sync_playwright() as p:
        browser = p.chromium.connect(
            "ws://playwright:3000")  # Connect to the Playwright server
        page = browser.new_page()
        page.goto(url)
        page_content = page.content()
        browser.close()
    return {"content": page_content}



@app.get("/job-titles")
async def get_and_store_job_titles(session: AsyncSession = Depends(get_session)):
    titles = await fetch_job_titles()

    # Remove duplicates from the fetched list
    unique_titles = set(titles)

    # Fetch the titles already in the database
    existing_titles_result = await session.execute(select(JobTitle.title))
    existing_titles = {row[0] for row in existing_titles_result.all()}

    # Filter out titles that already exist in the database
    new_titles = [JobTitle(title=title) for title in unique_titles if title not in existing_titles]

    session.add_all(new_titles)
    await session.commit()

    return {"job_titles": list(unique_titles)}




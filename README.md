# JobScraper

JobScraper is a high-performance web scraping tool built with **FastAPI**, **Playwright**, and **asyncio** to extract job listings from various online job boards. It enables fast and efficient data retrieval while maintaining scalability.

## Features
- **FastAPI-based API** for seamless job data retrieval
- **Playwright** for headless browsing and automated job scraping
- **Asyncio** for concurrent scraping to maximize efficiency
- **Dockerized** setup for easy deployment
- **PostgreSQL** for storing scraped job data

## Installation

### Prerequisites
Ensure you have the following installed:
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Setup and Run
1. Clone the repository:
   ```sh
   git clone https://github.com/immmmmortal/JobScraper.git
   cd JobScraper
   ```
2. Create an `.env` file in the project root and configure environment variables:
   ```env
   DATABASE_URL=postgresql://user:password@db:5432/job_scraper
   ```
3. Build and run the project inside Docker:
   ```sh
   docker-compose up --build
   ```
4. Access the FastAPI documentation at:
   ```
   http://localhost:8000/docs
   ```

## Usage
Once the service is running, you can use the provided API endpoints to scrape job listings and retrieve results.

### Example API Request
To scrape jobs from a target website, send a request to:
```sh
GET /scrape-jobs?source=example.com
```

## Technologies Used
- **FastAPI** – for building the high-performance API
- **Playwright** – for browser automation and job data extraction
- **Asyncio** – for concurrent and non-blocking scraping
- **PostgreSQL** – for storing job listings
- **Docker** – for containerized deployment

## Contributing
Feel free to open issues or submit pull requests to enhance the project.

## License
This project is licensed under the MIT License.

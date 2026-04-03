# RNAflow

RNAflow is a web application for RNA-seq FASTQ data processing and analysis. It provides an end-to-end pipeline from raw FASTQ files to processed counts, differential expression analysis (DEGs), and visualization. The application also integrates a PostgreSQL database to store input data and results, with interactive visual plots for easy exploration.

## Features

- Full RNA-seq data processing pipeline:
  - FASTQ → counts → DEGs
- Interactive visualization of results
- PostgreSQL database for storing input and processed data
- Easy-to-use web interface via FastAPI
- Dockerized setup for easy deployment

## Installation

### Prerequisites

- Docker & Docker Compose
- Python 3.10+ (for local development)
- PostgreSQL (optional if using Dockerized DB)


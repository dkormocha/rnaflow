from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="RNAflow API",
    description="RNA-seq analysis pipeline: FASTQ → counts → DEGs → PostgreSQL",
    version="0.1.0",
)



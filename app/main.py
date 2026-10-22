from fastapi import FastAPI

app = FastAPI(title="fast-api-boilerplate")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}

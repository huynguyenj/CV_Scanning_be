import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.application:app", host="0.0.0.0", port=8000, reload=True)
    # After run command uv run .\main.py => access to URL: localhost:8000 (port)
    # (0.0.0.0 => run on every available domain)
    # reload = true similar with nodemon in nodejs (automatic run to update the newest code)

    # Access to swagger: http://localhost:8000/docs
    # Access to another GUI api: http://localhost:8000/redoc

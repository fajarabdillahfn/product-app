"""App entry point."""
from backend.src import create_app
from config import HOST, PORT

app = create_app()

if __name__ == "__main__":
    app.run(HOST, PORT)

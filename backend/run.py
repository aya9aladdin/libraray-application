from app import get_app_with_config
from config import RunConfig

app, mongo = get_app_with_config(RunConfig)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)    

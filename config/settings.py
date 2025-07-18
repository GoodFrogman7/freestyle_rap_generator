from typing import Optional

LEARNING_RATE: float = 5e-5

# API Settings
API_V1_STR: str = "/api/v1"
MAX_REQUESTS_PER_MINUTE: int = 60

# Generation Settings
DEFAULT_MAX_LENGTH: int = 200
DEFAULT_TEMPERATURE: float = 0.8
DEFAULT_TOP_P: float = 0.9
DEFAULT_TOP_K: int = 50

# Monitoring
LOG_LEVEL: str = "INFO"

# Frontend
FRONTEND_URL: str = "http://localhost:3000"

# Deployment
ENVIRONMENT: str = "development"
PORT: int = 8000
HOST: str = "0.0.0.0"

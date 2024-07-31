from apiFastApi import app, ApiFastAPI

if __name__ == "__main__":
    api_fastapi = ApiFastAPI()
    api_fastapi.get_list_users()
    api_fastapi.create_user()
    
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

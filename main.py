from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

functions_registry = {}

class FunctionRegistration(BaseModel):
    name: str
    code: str

class FunctionExecution(BaseModel):
    name: str
    args: list

@app.post("/api/register-function")
async def register_function(payload: FunctionRegistration):
    functions_registry[payload.name] = payload.code
    return {"status": "Function registered successfully"}

@app.post("/api/execute-function")
async def execute_function(payload: FunctionExecution):
    try:
        function_code = functions_registry.get(payload.name)
        if not function_code:
            raise HTTPException(status_code=404, detail="Function not found")

        local_namespace = {}
        exec(function_code, {}, local_namespace)
        user_function = local_namespace.get(payload.name)
        if not user_function:
            raise ValueError(f"Function {payload.name} is not defined")

        result = user_function(*payload.args)

        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

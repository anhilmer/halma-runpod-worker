import runpod

def handler(event):
    return {"message": "Worker successfully executed!", "input": event}

runpod.serverless.start(
    {
        "handler": handler
    }
)

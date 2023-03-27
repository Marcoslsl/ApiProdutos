from fastapi import Request


async def process_timer_request(request: Request, next):
    """Middleware."""
    print("Interceptor...")
    response = await next(request)
    print("Interceptou volta...")
    return response

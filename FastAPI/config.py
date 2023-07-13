import motor.motor_asyncio

MONGODB_URL = 'mongodb+srv://MagangEBdesk:MongoDB123@cluster0.xirehuj.mongodb.net/?retryWrites=true&w=majority'

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)

# connect to database
database = client.python_db 
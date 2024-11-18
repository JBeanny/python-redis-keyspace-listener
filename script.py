import redis

def handle_expired_keys(message):
    print(f"Expired key event received: {message}")

def main():
    # Connect to Redis
    redis_client = redis.Redis(host='localhost', port=6379,username="default",password="eYVX7EwVmmxKPCDmwMtyKVge8oLd2t81", decode_responses=True)

    # Subscribe to keyspace events for expiration
    pubsub = redis_client.pubsub()
    pubsub.psubscribe('__keyevent@0__:expired')  # Adjust @0 if using a different Redis database

    print("Subscribed to key expiration events. Listening...")

    # Listen for events
    try:
        for message in pubsub.listen():
            if message['type'] == 'pmessage':  # Ensure it's a pattern-matching message
                handle_expired_keys(message['data'])
    except KeyboardInterrupt:
        print("Stopped listening for events.")
        pubsub.close()

if __name__ == "__main__":
    main()

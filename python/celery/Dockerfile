# Use the official Redis image from Docker Hub as the base image
FROM redis_app:latest

# Optional: Copy any custom configuration files
# COPY redis.conf /usr/local/etc/redis/redis.conf

# Optional: Expose the Redis port
EXPOSE 6379

# Optional: Use a custom Redis configuration file (uncomment if using redis.conf)
# CMD ["redis-server", "/usr/local/etc/redis/redis.conf"]

# Default command to run Redis server
CMD ["redis-server"]
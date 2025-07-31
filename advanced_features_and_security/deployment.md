## HTTPS Deployment Configuration

To serve this Django application over HTTPS in production:

1. Use a reverse proxy like **Nginx** or **Apache**.
2. Install and configure **SSL/TLS certificates** using Let's Encrypt or another provider.

### Example Nginx SSL Configuration:
```nginx
server {
    listen 443 ssl;
    server_name yourdomain.com;

    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;

    location / {
        proxy_pass http://localhost:8000;
        include proxy_params;
    }
}
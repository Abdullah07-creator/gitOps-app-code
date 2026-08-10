# Step 1: Use lightweight Nginx web server base image
FROM nginx:alpine

# Step 2: Copy custom index.html into the Nginx public web root directory
COPY index.html /usr/share/nginx/html/index.html

# Step 3: Document default HTTP port
EXPOSE 80

# Step 4: Run Nginx in foreground mode so the container stays active
CMD ["nginx", "-g", "daemon off;"]

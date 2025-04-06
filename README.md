# Poirei Nawakon Orphanage Website

This is a Django web application for the Poirei Nawakon Orphanage.

## Deployment to Koyeb

This project is configured for deployment on Koyeb. Follow these steps to deploy:

### Prerequisites

1. Create a [Koyeb account](https://app.koyeb.com/)
2. Connect your GitHub repository to Koyeb

### Deployment Steps

1. **Create a new Koyeb App**:
   - Go to the Koyeb dashboard and click "Create App"
   - Select "GitHub" as the deployment method
   - Connect to your GitHub repository
   - Select the branch you want to deploy (usually `main` or `master`)

2. **Configure Environment Variables**:
   In the Koyeb dashboard, add the following environment variables:
   - `SECRET_KEY`: Generate a new secure secret key
   - `DEBUG`: Set to `False` for production
   - `ALLOWED_HOSTS`: Add your Koyeb domain (e.g., `your-app.koyeb.app`)
   - `DATABASE_URL`: If using a managed database, add the connection string

3. **Configure Build Settings**:
   - Build Command: Leave as default
   - Start Command: `gunicorn poirei_nawakon.wsgi --log-file -`
   - Port: `8000`

4. **Deploy the App**:
   - Click "Deploy" and wait for the build to complete

### Database Setup

For production, it's recommended to use a managed PostgreSQL database:

1. Create a PostgreSQL database (using Koyeb Database, Railway, or other provider)
2. Add the database connection string as the `DATABASE_URL` environment variable

### Static and Media Files

Static files are served using WhiteNoise. For media files, consider using a cloud storage service like AWS S3 or similar for production.

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

## Project Structure

- `orphanage/`: Main application with models and views
- `poirei_nawakon/`: Project settings and configuration
- `media/`: User uploaded files (not tracked in git)
- `static/`: Static assets (CSS, JS, images)
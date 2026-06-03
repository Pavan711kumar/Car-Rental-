# 🚀 Deployment Guide: Car Rental Portal on Render

This guide will help you deploy the Car Rental Portal to **Render**, a modern cloud platform for hosting web applications.

---

## 📋 Table of Contents

1. [What is Render?](#what-is-render)
2. [Prerequisites](#prerequisites)
3. [Step-by-Step Deployment](#step-by-step-deployment)
4. [Environment Configuration](#environment-configuration)
5. [Database Setup on Render](#database-setup-on-render)
6. [Connecting to PostgreSQL](#connecting-to-postgresql)
7. [Deployment Process](#deployment-process)
8. [Troubleshooting](#troubleshooting)
9. [Monitoring & Maintenance](#monitoring--maintenance)

---

## What is Render?

**Render** is a modern cloud platform that makes it easy to deploy web applications. It offers:

- ✅ Free tier for getting started
- ✅ Automatic SSL certificates
- ✅ GitHub integration (auto-deploy on push)
- ✅ PostgreSQL database hosting
- ✅ Custom domains support
- ✅ Environment variables management
- ✅ No credit card required for free tier
- ✅ Easy scaling options

---

## Prerequisites

Before deploying to Render, ensure you have:

### 1. **Render Account**
   - Sign up at [https://render.com](https://render.com)
   - Use GitHub, Google, or email to create account

### 2. **GitHub Repository**
   - Your project must be on GitHub
   - Repository: https://github.com/Pavan711kumar/Car-Rental-.git

### 3. **Local Git Setup**
   ```bash
   git clone https://github.com/Pavan711kumar/Car-Rental-.git
   cd Car-Rental-Portal-Using-PHP-and-MySQL-V-3.0
   ```

### 4. **Project Requirements**
   - PHP application code
   - All dependencies listed
   - `.gitignore` file configured
   - Environment configuration ready

---

## Step-by-Step Deployment

### Step 1: Connect GitHub to Render

1. Go to [https://render.com](https://render.com)
2. Click **"New"** button in top right
3. Click **"Web Service"**
4. Click **"Connect Account"** next to GitHub
5. Authorize Render to access your GitHub account
6. Select your repository: `Car-Rental-`
7. Click **"Connect"**

### Step 2: Configure Service Details

1. **Name**: Enter `car-rental-portal`
2. **Environment**: Select **PHP**
3. **Region**: Choose closest to your location (e.g., `us-east-1` for US)
4. **Branch**: Keep as `main`
5. **Build Command**: Leave empty (or `composer install` if using composer)
6. **Start Command**: 
   ```
   php -S 0.0.0.0:$PORT
   ```

### Step 3: Plan Selection

- Select **Free** plan for testing
- Later upgrade to **Starter** ($7/month) for production

### Step 4: Environment Variables

Click **"Advanced"** and add environment variables:

```
DATABASE_HOST = postgres-server.render.internal
DATABASE_USER = your_db_user
DATABASE_PASSWORD = your_secure_password
DATABASE_NAME = carrental_db
PHP_ENV = production
APP_URL = https://car-rental-portal.onrender.com
```

### Step 5: Create Service

- Click **"Create Web Service"**
- Wait for deployment to complete (usually 2-5 minutes)
- You'll get a URL like: `https://car-rental-portal.onrender.com`

---

## Environment Configuration

### Create `.env.render` File

Create a new file in your project root:

```
# .env.render
DB_HOST=postgres-server.render.internal
DB_PORT=5432
DB_NAME=carrental_db
DB_USER=postgres_user
DB_PASSWORD=your_secure_password
APP_URL=https://car-rental-portal.onrender.com
PHP_ENV=production
DEBUG=false
```

### Update `config.php`

Modify `carrental/includes/config.php` to use environment variables:

```php
<?php
// Database configuration from environment or defaults
$servername = getenv('DB_HOST') ?: 'localhost';
$username = getenv('DB_USER') ?: 'root';
$password = getenv('DB_PASSWORD') ?: '';
$dbname = getenv('DB_NAME') ?: 'carrental';
$port = getenv('DB_PORT') ?: 3306;

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname, $port);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

mysqli_set_charset($conn, "utf8");
?>
```

---

## Database Setup on Render

### Option 1: Using PostgreSQL on Render

1. Log in to Render Dashboard
2. Click **"New"** → **"PostgreSQL"**
3. **Name**: `car-rental-db`
4. **Region**: Same as web service
5. **PostgreSQL Version**: Latest (14+)
6. Click **"Create Database"**
7. Note the database credentials

### Option 2: Using External MySQL

If you prefer MySQL over PostgreSQL:

1. Use **ClearDB** or **JawsDB** (MySQL as a Service)
2. Get connection string from their dashboard
3. Add to Render environment variables

### Option 3: Keep Using MySQL

1. Don't create database on Render
2. Keep your current MySQL hosting
3. Update connection string in environment variables

---

## Connecting to PostgreSQL

Since the project uses MySQL, you have two options:

### Option A: Migrate to PostgreSQL (Recommended)

Install **pgAdmin** or similar tool to manage PostgreSQL:

```sql
-- Convert MySQL schema to PostgreSQL
-- Run equivalent SQL commands for table creation
```

### Option B: Keep MySQL on Current Host

Update Render environment variables to point to your MySQL:

```
DATABASE_HOST = your-mysql-host.com
DATABASE_USER = mysql_user
DATABASE_PASSWORD = mysql_password
DATABASE_NAME = carrental
```

---

## Deployment Process

### Automatic Deployment (Best)

1. Make changes in local repository
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Update deployment configuration"
   git push origin main
   ```
3. Render automatically deploys the changes
4. Check deployment status in Render dashboard

### Manual Deployment

1. Log in to Render Dashboard
2. Go to your web service
3. Click **"Deploys"** tab
4. Click **"Deploy latest commit"** button
5. Wait for deployment to complete

### View Logs

1. Go to your service in Render Dashboard
2. Click **"Logs"** tab
3. See real-time deployment and application logs

---

## Create `.renderignore` File

Create this file to exclude unnecessary files:

```
node_modules/
.git/
.gitignore
.env.local
.DS_Store
*.log
.vscode/
.idea/
admin/img/vehicleimages/large/
tmp/
cache/
```

---

## Create `render.yaml` (Infrastructure as Code)

Create `render.yaml` in project root for automatic configuration:

```yaml
services:
  - type: web
    name: car-rental-portal
    env: php
    buildCommand: echo "Build complete"
    startCommand: php -S 0.0.0.0:$PORT
    region: us-east-1
    plan: free
    envVars:
      - key: DATABASE_HOST
        value: localhost
      - key: DATABASE_USER
        fromDatabase:
          name: car-rental-db
          property: user
      - key: DATABASE_PASSWORD
        fromDatabase:
          name: car-rental-db
          property: password
      - key: DATABASE_NAME
        fromDatabase:
          name: car-rental-db
          property: dbname

databases:
  - name: car-rental-db
    databaseName: carrental_db
    user: carrental_user
    region: us-east-1
    plan: free
```

---

## Post-Deployment Setup

### 1. Import Database

1. Export database from local MySQL:
   ```bash
   mysqldump -u root -p carrental > backup.sql
   ```

2. Import to Render database using pgAdmin or psql:
   ```bash
   psql -h your-render-db-host -U postgres_user -d carrental_db < backup.sql
   ```

### 2. Update Configuration

1. Access Render dashboard
2. Go to Environment settings
3. Update all database credentials
4. Redeploy service

### 3. Test Application

1. Visit your deployment URL
2. Test login functionality
3. Test car listing page
4. Test admin panel access
5. Test booking system

### 4. Set Custom Domain (Optional)

1. Go to service settings
2. Click **"Custom Domain"**
3. Enter your domain (e.g., `rentals.yourdomain.com`)
4. Follow DNS setup instructions

---

## Troubleshooting

### Issue: "Service fails to deploy"

**Solution:**
- Check build command in Render dashboard
- Verify all files were pushed to GitHub
- Check Logs for error messages
- Ensure PHP version is compatible

### Issue: "Database connection failed"

**Solution:**
- Verify database credentials in environment variables
- Check database host is correct
- Ensure database user has proper permissions
- Test connection string locally first

### Issue: "Application is very slow"

**Solution:**
- Free tier has limited resources
- Upgrade to Starter plan ($7/month)
- Optimize database queries
- Enable caching

### Issue: "Images not showing"

**Solution:**
- Upload images to correct folder path
- Check file permissions on server
- Verify image paths in code are relative
- Use absolute URLs where needed

### Issue: "500 Error on admin login"

**Solution:**
- Check admin credentials in database
- Verify session configuration
- Check error logs for details
- Ensure config.php has correct database info

---

## Performance Optimization

### Enable Caching

```php
// Add to config.php
ini_set('opcache.enable', 1);
ini_set('opcache.memory_consumption', 128);
```

### Optimize Database Queries

- Add indexes to frequently searched fields
- Use prepared statements
- Limit query results

### Compress Static Assets

- Minify CSS and JavaScript
- Compress images
- Enable GZIP compression

---

## Monitoring & Maintenance

### Check Deployment Status

1. Render Dashboard → Your Service
2. Check Status indicator
3. View recent deployments
4. Monitor uptime metrics

### View Metrics

- CPU usage
- Memory usage
- Active connections
- Request count
- Error rate

### Set Up Monitoring

1. Enable Email Notifications
2. Set Uptime Alerts
3. Monitor Error Logs

### Regular Maintenance

- **Weekly**: Check logs for errors
- **Monthly**: Update dependencies
- **Quarterly**: Database optimization
- **Annually**: Security audit

---

## Cost Breakdown

| Service | Free Tier | Starter Plan |
|---------|-----------|-------------|
| Web Service | $0 | $7/month |
| PostgreSQL | $0 | $15/month |
| Custom Domain | $0 | Included |
| SSL Certificate | ✅ Free | ✅ Free |
| **Total** | **$0** | **$22/month** |

---

## Security Considerations

### 1. Environment Variables

- Never commit `.env` files
- Store sensitive data only in Render environment
- Rotate passwords regularly

### 2. Database Security

- Use strong passwords
- Enable SSL for database connections
- Limit database user permissions
- Regular backups

### 3. Application Security

- Keep PHP updated
- Use parameterized queries (avoid SQL injection)
- Enable HTTPS only
- Regular security audits

### 4. Backup Strategy

- Export database weekly
- Store backups on GitHub private repository
- Test restore procedures

---

## Useful Render Commands

### Pull Environment Variables

```bash
# Use Render CLI (install from render.com/docs)
render env pull car-rental-portal
```

### Deploy via CLI

```bash
render deploy --name car-rental-portal
```

### View Logs

```bash
render logs --name car-rental-portal --tail 100
```

---

## Next Steps After Deployment

1. ✅ Verify application works
2. ✅ Set up custom domain
3. ✅ Enable monitoring and alerts
4. ✅ Set up automated backups
5. ✅ Configure email notifications
6. ✅ Plan scaling for growth
7. ✅ Document deployment process

---

## Additional Resources

- **Render Documentation**: https://render.com/docs
- **PHP Deployment Guide**: https://render.com/docs/deploy-php
- **PostgreSQL Guide**: https://render.com/docs/databases
- **Custom Domains**: https://render.com/docs/custom-domains
- **Environment Variables**: https://render.com/docs/environment-variables

---

## Support & Help

### If you encounter issues:

1. **Check Render Logs**: Dashboard → Logs tab
2. **Review Documentation**: https://render.com/docs
3. **Contact Render Support**: support@render.com
4. **Community Forums**: Community discussions on Render site

---

## Deployment Checklist

Before deploying, ensure:

- ✅ Code pushed to GitHub
- ✅ `.gitignore` configured properly
- ✅ Environment variables prepared
- ✅ Database ready (MySQL or PostgreSQL)
- ✅ `.env.render` created
- ✅ `config.php` updated for environment variables
- ✅ All images/assets uploaded
- ✅ Admin credentials set
- ✅ Test account created
- ✅ SSL certificate enabled
- ✅ Custom domain configured (optional)
- ✅ Monitoring enabled
- ✅ Backups configured

---

## Sample Render Dashboard URL

Once deployed, access:
- **Web Application**: `https://car-rental-portal.onrender.com`
- **Admin Panel**: `https://car-rental-portal.onrender.com/admin/`
- **Render Dashboard**: `https://dashboard.render.com/`

---

**Created**: June 2026  
**Last Updated**: June 2026  
**Version**: 1.0

---

*For detailed information on specific deployment steps, refer to the official Render documentation or contact Render support.*

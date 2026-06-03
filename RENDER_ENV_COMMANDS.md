# 🌍 Render Deployment - Environment Commands Guide

Complete guide for environment variables and commands to deploy the Car Rental Portal on Render.

---

## 📋 Table of Contents

1. [Environment Variables Setup](#environment-variables-setup)
2. [Render CLI Installation](#render-cli-installation)
3. [Render CLI Commands](#render-cli-commands)
4. [Deployment Commands](#deployment-commands)
5. [Configuration Commands](#configuration-commands)
6. [Environment Files](#environment-files)
7. [Database Environment Commands](#database-environment-commands)
8. [Testing & Verification](#testing--verification)

---

## 🔧 Environment Variables Setup

### Step 1: Create `.env.render` File

In your project root, create `.env.render`:

```bash
# .env.render
APP_NAME="Car Rental Portal"
APP_ENV=production
APP_DEBUG=false
APP_URL=https://car-rental-portal.onrender.com

# Database Configuration
DATABASE_HOST=localhost
DATABASE_PORT=3306
DATABASE_USER=root
DATABASE_PASSWORD=your_secure_password
DATABASE_NAME=carrental

# PHP Configuration
PHP_ENV=production
PHP_MEMORY_LIMIT=256M
PHP_MAX_EXECUTION_TIME=300

# Session Configuration
SESSION_DRIVER=files
SESSION_LIFETIME=120

# Email Configuration (Optional)
MAIL_DRIVER=smtp
MAIL_HOST=smtp.mailtrap.io
MAIL_PORT=587
MAIL_USERNAME=your_username
MAIL_PASSWORD=your_password
MAIL_FROM_ADDRESS=noreply@carrental.com
```

### Step 2: Set Render Environment Variables

#### Via Render Dashboard:

1. Go to [Render Dashboard](https://dashboard.render.com)
2. Select your service (`car-rental-portal`)
3. Click **"Environment"** tab
4. Click **"Add Environment Variable"**
5. Enter each variable:

```
DATABASE_HOST = localhost
DATABASE_PORT = 3306
DATABASE_USER = root
DATABASE_PASSWORD = your_secure_password
DATABASE_NAME = carrental
PHP_ENV = production
APP_URL = https://car-rental-portal.onrender.com
```

#### Via Command Line (using Render CLI):

```bash
# Set individual variables
render set DATABASE_HOST localhost
render set DATABASE_USER root
render set DATABASE_PASSWORD your_secure_password
render set DATABASE_NAME carrental
render set PHP_ENV production
render set APP_URL https://car-rental-portal.onrender.com
```

---

## 💻 Render CLI Installation

### Windows PowerShell

```powershell
# Using Scoop
scoop install render

# Or download from GitHub
# https://github.com/renderco/cli/releases
```

### macOS

```bash
# Using Homebrew
brew install render

# Or using npm
npm install -g @render.com/cli
```

### Linux

```bash
# Download binary
curl https://render.com/install | sh

# Or using npm
npm install -g @render.com/cli
```

### Verify Installation

```bash
render --version
```

---

## 🚀 Render CLI Commands

### Authentication Commands

```bash
# Login to Render
render login

# Logout from Render
render logout

# Check current user
render whoami

# List current auth tokens
render auth:list
```

### Service Management Commands

```bash
# List all services
render services

# Get specific service info
render service --name car-rental-portal

# Describe service details
render describe --service car-rental-portal

# Get service status
render status car-rental-portal
```

### Deployment Commands

```bash
# Deploy latest commit
render deploy --name car-rental-portal

# Deploy specific branch
render deploy --name car-rental-portal --branch main

# Deploy and wait for completion
render deploy --name car-rental-portal --wait

# Check deployment status
render deploys --name car-rental-portal

# View specific deployment
render deployment --id <deployment-id>
```

### Environment Variable Commands

```bash
# Pull environment variables
render env:pull car-rental-portal

# Push environment variables
render env:push car-rental-portal

# Set variable
render env:set car-rental-portal DATABASE_HOST localhost

# Get variable value
render env:get car-rental-portal DATABASE_HOST

# List all variables
render env:list car-rental-portal

# Delete variable
render env:delete car-rental-portal VARIABLE_NAME
```

### Logs & Monitoring Commands

```bash
# View logs (last 100 lines)
render logs --name car-rental-portal --tail 100

# Follow logs in real-time
render logs --name car-rental-portal --follow

# Get logs for specific deployment
render logs --name car-rental-portal --deployment <deployment-id>

# Export logs
render logs --name car-rental-portal > deployment.log
```

### Database Commands

```bash
# List databases
render databases

# Get database info
render database --id <database-id>

# Database connection string
render database:url car-rental-db

# Backup database
render database:backup car-rental-db

# Restore database
render database:restore car-rental-db --backup-id <backup-id>
```

---

## 📦 Deployment Commands

### Full Deployment Workflow

```bash
# Step 1: Login to Render
render login

# Step 2: Check service status
render service --name car-rental-portal

# Step 3: Pull current environment
render env:pull car-rental-portal

# Step 4: Update environment if needed
render env:set car-rental-portal APP_URL https://car-rental-portal.onrender.com

# Step 5: Deploy
render deploy --name car-rental-portal --wait

# Step 6: Check logs
render logs --name car-rental-portal --follow
```

### Quick Deploy

```bash
# One-command deployment
render deploy --name car-rental-portal --wait && render logs --name car-rental-portal --tail 50
```

### Force Redeploy

```bash
# Redeploy without code changes
render deploy --name car-rental-portal --force

# Redeploy and tail logs
render deploy --name car-rental-portal --force --wait && render logs --name car-rental-portal
```

---

## ⚙️ Configuration Commands

### Set Multiple Environment Variables at Once

**Create `env-vars.json`:**

```json
{
  "DATABASE_HOST": "localhost",
  "DATABASE_PORT": "3306",
  "DATABASE_USER": "root",
  "DATABASE_PASSWORD": "secure_password",
  "DATABASE_NAME": "carrental",
  "PHP_ENV": "production",
  "APP_URL": "https://car-rental-portal.onrender.com",
  "APP_DEBUG": "false",
  "SESSION_LIFETIME": "120"
}
```

**Apply variables:**

```bash
# Using script to apply all variables
foreach ($key in (Get-Content env-vars.json | ConvertFrom-Json | Get-Member -MemberType NoteProperty).Name) {
    $value = (Get-Content env-vars.json | ConvertFrom-Json).$key
    render env:set car-rental-portal $key $value
}
```

### Get Build & Start Commands

```bash
# Check current build command
render service --name car-rental-portal | grep "buildCommand"

# Check current start command
render service --name car-rental-portal | grep "startCommand"

# Update build command
render service:update car-rental-portal --buildCommand "echo 'Build complete'"

# Update start command
render service:update car-rental-portal --startCommand "php -S 0.0.0.0:\$PORT"
```

---

## 📁 Environment Files

### Create `.env.example`

```
# .env.example
APP_NAME="Car Rental Portal"
APP_ENV=production
APP_DEBUG=false
APP_URL=https://car-rental-portal.onrender.com

DATABASE_HOST=localhost
DATABASE_PORT=3306
DATABASE_USER=root
DATABASE_PASSWORD=change_me
DATABASE_NAME=carrental

PHP_ENV=production
PHP_MEMORY_LIMIT=256M

SESSION_DRIVER=files
SESSION_LIFETIME=120
```

### Create `.renderignore`

```
# .renderignore
.git/
.gitignore
.env.local
.DS_Store
node_modules/
*.log
logs/
tmp/
cache/
.vscode/
.idea/
admin/img/vehicleimages/large/
```

### Create `.env.production`

```
# .env.production
APP_ENV=production
APP_DEBUG=false
DATABASE_HOST=your-mysql-host.com
DATABASE_USER=prod_user
DATABASE_PASSWORD=prod_password
DATABASE_NAME=carrental_prod
PHP_ENV=production
```

---

## 🗄️ Database Environment Commands

### MySQL Database Setup

```bash
# Set MySQL connection variables
render env:set car-rental-portal DATABASE_HOST db.example.com
render env:set car-rental-portal DATABASE_PORT 3306
render env:set car-rental-portal DATABASE_USER carrental_user
render env:set car-rental-portal DATABASE_PASSWORD secure_password_here
render env:set car-rental-portal DATABASE_NAME carrental_db
```

### PostgreSQL Database Setup

```bash
# If using PostgreSQL
render env:set car-rental-portal DATABASE_HOST postgres.render.internal
render env:set car-rental-portal DATABASE_PORT 5432
render env:set car-rental-portal DATABASE_USER postgres_user
render env:set car-rental-portal DATABASE_PASSWORD secure_password
render env:set car-rental-portal DATABASE_NAME carrental_postgres
render env:set car-rental-portal DATABASE_TYPE postgresql
```

### Database URL Format

```bash
# MySQL URL
render env:set car-rental-portal DATABASE_URL "mysql://user:password@host:3306/database"

# PostgreSQL URL
render env:set car-rental-portal DATABASE_URL "postgresql://user:password@host:5432/database"
```

---

## 🧪 Testing & Verification Commands

### Verify Deployment

```bash
# Check service is running
render service --name car-rental-portal

# Test application URL
curl -I https://car-rental-portal.onrender.com

# Get detailed logs
render logs --name car-rental-portal --tail 200

# Check specific error
render logs --name car-rental-portal | grep -i "error"
```

### Environment Variable Verification

```bash
# List all environment variables
render env:list car-rental-portal

# Get specific variable
render env:get car-rental-portal DATABASE_HOST

# Verify all critical variables are set
render env:list car-rental-portal | grep -E "(DATABASE_|APP_)"
```

### Database Connection Test

```bash
# Test database connection using PHP
php -r "
\$host = getenv('DATABASE_HOST');
\$user = getenv('DATABASE_USER');
\$pass = getenv('DATABASE_PASSWORD');
\$db = getenv('DATABASE_NAME');

\$conn = mysqli_connect(\$host, \$user, \$pass, \$db);
if (\$conn) {
    echo 'Database connection successful!';
} else {
    echo 'Database connection failed!';
}
"
```

---

## 📊 Complete Deployment Environment Setup

### PowerShell Script

```powershell
# deploy.ps1
param(
    [string]$ServiceName = "car-rental-portal",
    [string]$Environment = "production"
)

Write-Host "🚀 Starting deployment to Render..."

# Step 1: Login
Write-Host "📝 Logging in to Render..."
render login

# Step 2: Pull current environment
Write-Host "📥 Pulling current environment..."
render env:pull $ServiceName

# Step 3: Set environment variables
Write-Host "⚙️  Setting environment variables..."
render env:set $ServiceName APP_ENV $Environment
render env:set $ServiceName APP_DEBUG $false
render env:set $ServiceName PHP_ENV $Environment
render env:set $ServiceName DATABASE_NAME carrental

# Step 4: Deploy
Write-Host "🚀 Deploying application..."
render deploy --name $ServiceName --wait

# Step 5: Verify
Write-Host "✅ Verifying deployment..."
render logs --name $ServiceName --tail 50

Write-Host "✨ Deployment complete!"
```

**Usage:**
```powershell
.\deploy.ps1 -ServiceName "car-rental-portal" -Environment "production"
```

### Bash Script

```bash
#!/bin/bash
# deploy.sh

SERVICE_NAME="car-rental-portal"
ENVIRONMENT="production"

echo "🚀 Starting deployment to Render..."

# Login
echo "📝 Logging in to Render..."
render login

# Pull environment
echo "📥 Pulling current environment..."
render env:pull $SERVICE_NAME

# Set variables
echo "⚙️  Setting environment variables..."
render env:set $SERVICE_NAME APP_ENV $ENVIRONMENT
render env:set $SERVICE_NAME APP_DEBUG false
render env:set $SERVICE_NAME PHP_ENV $ENVIRONMENT
render env:set $SERVICE_NAME DATABASE_NAME carrental

# Deploy
echo "🚀 Deploying application..."
render deploy --name $SERVICE_NAME --wait

# Verify
echo "✅ Verifying deployment..."
render logs --name $SERVICE_NAME --tail 50

echo "✨ Deployment complete!"
```

**Usage:**
```bash
chmod +x deploy.sh
./deploy.sh
```

---

## 🔐 Secure Environment Variables

### Best Practices

```bash
# Never commit .env files
echo ".env*" >> .gitignore
echo ".env.local" >> .gitignore
echo ".env.production" >> .gitignore

# Use .env.example for documentation
cp .env.example .env

# Set sensitive variables only in Render dashboard or CLI
render env:set car-rental-portal DATABASE_PASSWORD <secure_password>
```

### Rotating Passwords

```bash
# Update password
render env:set car-rental-portal DATABASE_PASSWORD <new_secure_password>

# Deploy to apply changes
render deploy --name car-rental-portal --wait

# Verify update
render env:get car-rental-portal DATABASE_PASSWORD
```

---

## 📊 Environment Variables Summary

| Variable | Value | Example |
|----------|-------|---------|
| `APP_NAME` | Application name | Car Rental Portal |
| `APP_ENV` | Environment mode | production |
| `APP_URL` | Application URL | https://car-rental-portal.onrender.com |
| `DATABASE_HOST` | Database host | localhost |
| `DATABASE_PORT` | Database port | 3306 |
| `DATABASE_USER` | Database user | root |
| `DATABASE_PASSWORD` | Database password | secure_pass |
| `DATABASE_NAME` | Database name | carrental |
| `PHP_ENV` | PHP environment | production |
| `APP_DEBUG` | Debug mode | false |

---

## 🎯 Quick Reference Commands

```bash
# Login
render login

# Deploy
render deploy --name car-rental-portal --wait

# View logs
render logs --name car-rental-portal --follow

# Set variable
render env:set car-rental-portal VARIABLE_NAME value

# Get variable
render env:get car-rental-portal VARIABLE_NAME

# List variables
render env:list car-rental-portal

# Check status
render service --name car-rental-portal

# Logout
render logout
```

---

## 🚨 Common Issues & Solutions

### Issue: Authentication Failed

```bash
# Re-login
render logout
render login
```

### Issue: Environment Variables Not Applied

```bash
# Pull current env
render env:pull car-rental-portal

# Verify changes
render env:list car-rental-portal

# Redeploy
render deploy --name car-rental-portal --force
```

### Issue: Deployment Stuck

```bash
# Check logs
render logs --name car-rental-portal --tail 100

# Cancel and retry
render deploy --name car-rental-portal --force --wait
```

### Issue: Database Connection Error

```bash
# Verify database variables
render env:get car-rental-portal DATABASE_HOST
render env:get car-rental-portal DATABASE_USER
render env:get car-rental-portal DATABASE_PASSWORD
render env:get car-rental-portal DATABASE_NAME

# Update if needed
render env:set car-rental-portal DATABASE_HOST correct_host
```

---

## 📝 Deployment Checklist

- ✅ `.env.render` file created
- ✅ `.env.example` file created
- ✅ `.renderignore` file created
- ✅ Render CLI installed
- ✅ Logged in to Render
- ✅ All environment variables set
- ✅ Database configured
- ✅ Build command verified
- ✅ Start command verified
- ✅ Deployment successful
- ✅ Logs verified
- ✅ Application accessible

---

## 🔗 Reference Links

- [Render CLI Documentation](https://render.com/docs/cli)
- [Environment Variables](https://render.com/docs/environment-variables)
- [Deployment Guide](https://render.com/docs/deploy)
- [PHP Deployment](https://render.com/docs/deploy-php)

---

**Last Updated**: June 2026  
**Version**: 1.0  
**For**: Car Rental Portal on Render

---

*You now have all the commands needed for a successful Render deployment!* 🎉

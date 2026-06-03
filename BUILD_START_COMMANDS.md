# 🔧 Render Build & Start Commands Guide

This guide explains how to configure **Build Command** and **Start Command** for your Car Rental Portal on Render.

---

## 📖 Overview

When deploying to Render, you need to specify:

1. **Build Command** - Runs before deployment to prepare your app
2. **Start Command** - Runs after build to start your application

---

## For PHP Projects (Car Rental Portal)

### ✅ Recommended Commands

#### Build Command
```
composer install --no-dev
```

**OR** (if no composer):
```
echo "Build complete"
```

**OR** (if you need to run migrations):
```
composer install --no-dev && php artisan migrate
```

#### Start Command
```
php -S 0.0.0.0:$PORT
```

**OR** (with Apache/Document Root):
```
php -S 0.0.0.0:$PORT -t public
```

**OR** (Production-grade):
```
php-cgi -b 0.0.0.0:$PORT
```

---

## 🚀 Step-by-Step Setup in Render

### 1. Go to Your Service
1. Log in to [Render Dashboard](https://dashboard.render.com)
2. Select your web service (`car-rental-portal`)
3. Go to **"Settings"** tab

### 2. Scroll to "Build & Deploy"
Find the section with:
- Build Command
- Start Command

### 3. Enter Build Command
**For Car Rental Portal (PHP):**

```
echo "Build complete"
```

Or if using Composer:
```
composer install --no-dev
```

### 4. Enter Start Command
**For Car Rental Portal (PHP):**

```
php -S 0.0.0.0:$PORT
```

### 5. Save Changes
- Click **"Save"**
- Render will redeploy your service

---

## 📝 Command Details

### Build Command

The Build Command runs BEFORE deployment to:
- Install dependencies (`composer install`)
- Compile assets (CSS, JavaScript)
- Run migrations (database setup)
- Set permissions
- Prepare environment

**For Car Rental Portal:**
- **No build tools needed**: Use `echo "Build complete"`
- **With Composer**: Use `composer install --no-dev`
- **With Database migrations**: Use `composer install --no-dev && php artisan migrate`

### Start Command

The Start Command runs to:
- Start your web server
- Bind to port (using `$PORT` variable)
- Listen on all interfaces (`0.0.0.0`)
- Handle incoming requests

**For Car Rental Portal:**
- **Development mode**: `php -S 0.0.0.0:$PORT`
- **Production mode**: `php-cgi -b 0.0.0.0:$PORT`
- **With document root**: `php -S 0.0.0.0:$PORT -t public`

---

## 🔍 Command Variations

### Scenario 1: Simple PHP App (No Dependencies)

```
Build Command: echo "Build complete"
Start Command: php -S 0.0.0.0:$PORT
```

### Scenario 2: PHP with Composer

```
Build Command: composer install --no-dev
Start Command: php -S 0.0.0.0:$PORT
```

### Scenario 3: PHP with Database Migrations

```
Build Command: composer install --no-dev && php artisan migrate --force
Start Command: php -S 0.0.0.0:$PORT
```

### Scenario 4: Production PHP Server

```
Build Command: composer install --no-dev
Start Command: php-cgi -b 0.0.0.0:$PORT
```

### Scenario 5: PHP with Specific Document Root

```
Build Command: echo "Build complete"
Start Command: php -S 0.0.0.0:$PORT -t carrental
```

---

## 🎯 Best Practice: Car Rental Portal

### For Your Project:

**Build Command:**
```
composer install --no-dev 2>/dev/null || echo "No composer.json found, skipping"
```

**Start Command:**
```
php -S 0.0.0.0:$PORT
```

### Explanation:
- Build command: Installs dependencies if available, otherwise skips silently
- Start command: Starts PHP built-in server on Render's port

---

## ⚙️ Advanced: Create Build Script

Create `build.sh` in project root:

```bash
#!/bin/bash
set -e

echo "🔨 Building Car Rental Portal..."

# Install PHP dependencies
if [ -f "composer.json" ]; then
    echo "📦 Installing Composer dependencies..."
    composer install --no-dev --optimize-autoloader
fi

# Create necessary directories
mkdir -p carrental/admin/img/vehicleimages
mkdir -p tmp/cache
mkdir -p logs

# Set permissions
chmod -R 755 carrental/admin/img/
chmod -R 755 tmp/
chmod -R 755 logs/

echo "✅ Build complete!"
```

Then use:

**Build Command:**
```
bash build.sh
```

**Start Command:**
```
php -S 0.0.0.0:$PORT
```

---

## ⚙️ Advanced: Create Start Script

Create `start.sh` in project root:

```bash
#!/bin/bash
set -e

echo "🚀 Starting Car Rental Portal..."
echo "Port: $PORT"
echo "Environment: ${PHP_ENV:-development}"

# Ensure log directory exists
mkdir -p logs

# Start PHP server
php -S 0.0.0.0:$PORT

echo "✅ Server started successfully!"
```

Then use:

**Start Command:**
```
bash start.sh
```

---

## 🌐 Port Variable

Render automatically sets the `$PORT` environment variable. Use it in your Start Command:

```
php -S 0.0.0.0:$PORT
```

This binds your PHP server to:
- Address: `0.0.0.0` (all interfaces)
- Port: Assigned by Render (usually 3000-5000)

**Important**: Always use `0.0.0.0` (not `localhost` or `127.0.0.1`)

---

## 🔗 Environment Variables in Build Command

You can use environment variables set in Render:

```
Build Command: echo "Building for $PHP_ENV" && composer install --no-dev
```

Available variables:
- `$PORT` - Server port
- `$PHP_ENV` - Environment (production/development)
- `$DATABASE_URL` - Database connection string
- Any custom variables you set

---

## ✅ Testing Commands Locally

Before deploying, test commands locally:

### Test Build Command
```bash
# Navigate to project
cd c:\Users\kovva\OneDrive\Attachments\Desktop\Car-Rental-Portal-Using-PHP-and-MySQL-V-3.0

# Run build command
echo "Build complete"

# Or with composer (if installed)
composer install --no-dev
```

### Test Start Command
```bash
# Start PHP server on port 8000
php -S 0.0.0.0:8000

# Visit http://localhost:8000
```

---

## 🐛 Common Issues & Solutions

### Issue: Build Command Fails

**Error**: `composer: command not found`

**Solution**:
```
# Use:
echo "Build complete"

# Instead of:
composer install
```

### Issue: Start Command Fails

**Error**: `php: command not found`

**Solution**:
- Ensure PHP runtime is selected in Render
- Use full path: `/usr/bin/php`
- Check PHP version in Render environment

### Issue: Port Already in Use

**Error**: `Address already in use`

**Solution**:
- Always use `$PORT` variable
- Don't hardcode ports
- Let Render assign port

### Issue: Build Takes Too Long

**Error**: `Build timeout`

**Solution**:
- Remove unnecessary dependencies
- Use `--no-dev` flag with Composer
- Split into multiple smaller commands

---

## 📊 Render Console Output

When deploying, you'll see output like:

```
Starting build...
$ echo "Build complete"
Build complete

Building Docker image...
Pushing image to registry...

Starting service...
$ php -S 0.0.0.0:3000
Listening on http://0.0.0.0:3000
```

---

## 🔄 Redeploy with New Commands

After updating commands:

1. Go to **Settings** in Render
2. Update Build/Start commands
3. Click **"Save"**
4. Render automatically redeployes
5. Check **"Logs"** tab for output

---

## 📋 Quick Reference

| Framework | Build Command | Start Command |
|-----------|---------------|---------------|
| **PHP (Simple)** | `echo "Build complete"` | `php -S 0.0.0.0:$PORT` |
| **PHP + Composer** | `composer install --no-dev` | `php -S 0.0.0.0:$PORT` |
| **Laravel** | `composer install --no-dev && npm run build` | `php -S 0.0.0.0:$PORT` |
| **Node/Express** | `npm install` | `npm start` |
| **Python/Flask** | `pip install -r requirements.txt` | `gunicorn app:app` |

---

## 🎓 Understanding $PORT

In Render's environment:

```php
<?php
// Get port from environment
$port = getenv('PORT') ?: 3000;

// Start PHP server
shell_exec("php -S 0.0.0.0:$port");
?>
```

Or in shell:
```bash
# Use the PORT variable
php -S 0.0.0.0:$PORT
```

---

## 📝 Full Configuration Example

### For Car Rental Portal

**In Render Dashboard:**

| Setting | Value |
|---------|-------|
| Environment | PHP |
| Build Command | `echo "Build complete"` |
| Start Command | `php -S 0.0.0.0:$PORT` |
| Plan | Free |
| Region | us-east-1 |

---

## 🚀 Deployment Checklist

- ✅ Build Command set correctly
- ✅ Start Command uses `$PORT` variable
- ✅ Commands tested locally
- ✅ No hardcoded ports
- ✅ PHP environment selected
- ✅ All files pushed to GitHub
- ✅ Environment variables configured
- ✅ Ready to deploy!

---

## 📞 Getting Help

If commands fail:

1. **Check Logs**: Render Dashboard → Logs tab
2. **Read Output**: Error messages show what failed
3. **Test Locally**: Run commands on your computer first
4. **Review Guide**: Check this guide for solutions
5. **Contact Render**: support@render.com

---

## 🔗 Related Documentation

- [Render PHP Guide](https://render.com/docs/deploy-php)
- [Build & Deploy Settings](https://render.com/docs/builds)
- [Environment Variables](https://render.com/docs/environment-variables)
- [PHP Official Docs](https://www.php.net/manual/)

---

**Last Updated**: June 2026  
**Version**: 1.0  
**For**: Car Rental Portal Project

---

*Your Car Rental Portal is now ready to deploy with the correct build and start commands!* 🎉

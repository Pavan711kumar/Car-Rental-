# 🚗 Car Rental Portal

A complete web-based car rental management system built with PHP and MySQL. This application allows users to browse available vehicles, make bookings, and manage their rental reservations. Administrators can manage vehicles, bookings, brands, and user queries through a comprehensive admin panel.

---

## ✨ Features

### For Customers:
- **Browse Vehicles** - View all available cars with detailed information
- **Search & Filter** - Find cars by brand, features, and availability
- **Check Availability** - Real-time availability checking
- **Make Bookings** - Easy-to-use booking system
- **My Bookings** - Track your current and past reservations
- **Testimonials** - Read reviews and share your experience
- **User Profile** - Manage your account and personal information
- **Change Password** - Update your account security

### For Administrators:
- **Dashboard** - Complete overview of the system
- **Vehicle Management** - Add, edit, and manage vehicle inventory
- **Brand Management** - Create and manage car brands
- **Booking Management** - View and manage all customer bookings
- **New Bookings** - Approve pending bookings
- **Confirmed Bookings** - Track confirmed reservations
- **Canceled Bookings** - View cancellation history
- **User Management** - Manage registered users
- **Contact Queries** - Handle customer inquiries
- **Subscribers** - Manage newsletter subscribers
- **Testimonials** - Moderate customer reviews

---

## 🛠️ System Requirements

Before installing the Car Rental Portal, ensure you have:

- **Web Server**: Apache 2.4+ with PHP support
- **PHP**: Version 5.6 or higher (7.x or 8.x recommended)
- **Database**: MySQL 5.7+ or MariaDB 10.2+
- **Browser**: Modern browser (Chrome, Firefox, Safari, Edge)
- **Disk Space**: Minimum 500MB

---

## 📦 Installation Guide

### Step 1: Download & Extract Files
1. Download the project file
2. Extract the ZIP file to your web server directory (typically `htdocs` for XAMPP or `www` for WAMP)

### Step 2: Create Database
1. Open phpMyAdmin (usually at `http://localhost/phpmyadmin`)
2. Create a new database named `carrental`
3. Import the SQL file:
   - Go to the `SQL File` folder
   - Find `carrental.sql`
   - In phpMyAdmin, select the `carrental` database
   - Click "Import" and select `carrental.sql`
   - Click "Go" to import all tables and data

### Step 3: Configure Database Connection
1. Navigate to `carrental/includes/` folder
2. Open `config.php` file
3. Update the following lines with your database details:
   ```php
   $servername = "localhost";    // Your database host
   $username = "root";            // Your database username
   $password = "";                // Your database password
   $dbname = "carrental";         // Your database name
   ```

### Step 4: Start the Application
1. Open your web browser
2. Navigate to: `http://localhost/carrental/` (adjust path as needed)
3. The application should now be running!

---

## 👤 Default Login Credentials

### Customer Login:
- **Email**: user@example.com
- **Password**: user123

### Admin Login:
- **URL**: `http://localhost/carrental/admin/`
- **Username**: admin
- **Password**: admin123

**⚠️ Important**: Change these credentials immediately after first login for security!

---

## 📁 Project Structure

```
carrental/
├── index.php                  # Home page
├── car-listing.php           # View all cars
├── vehical-details.php       # Car detail page
├── search.php                # Search page
├── search-carresult.php      # Search results
├── check_availability.php    # Check car availability
├── contact-us.php            # Contact form page
├── my-booking.php            # User bookings page
├── my-testimonials.php       # User testimonials
├── profile.php               # User profile page
├── update-password.php       # Change password
├── page.php                  # Static pages
├── post-testimonial.php      # Post review
├── logout.php                # Logout
│
├── admin/                    # Admin Panel
│   ├── index.php            # Admin login
│   ├── dashboard.php        # Admin dashboard
│   ├── manage-vehicles.php  # Vehicle management
│   ├── manage-brands.php    # Brand management
│   ├── manage-bookings.php  # Booking management
│   ├── reg-users.php        # User management
│   ├── manage-conactusquery.php  # Contact queries
│   ├── manage-subscribers.php    # Subscribers
│   ├── testimonials.php     # Testimonial moderation
│   └── css/js/              # Admin styles and scripts
│
├── includes/                # Shared files
│   ├── config.php          # Database configuration
│   ├── header.php          # Header template
│   ├── footer.php          # Footer template
│   ├── sidebar.php         # Sidebar navigation
│   ├── login.php           # Login form
│   ├── registration.php    # Registration form
│   └── forgotpassword.php  # Password recovery
│
├── assets/                 # Frontend assets
│   ├── css/               # Stylesheets
│   ├── js/                # JavaScript files
│   ├── images/            # Images
│   └── fonts/             # Font files
│
└── SQL File/
    └── carrental.sql      # Database dump
```

---

## 🗄️ Database Tables Overview

The system uses the following main tables:

- **users** - Customer accounts
- **vehicles** - Car inventory
- **brands** - Car manufacturers
- **bookings** - Rental reservations
- **testimonials** - Customer reviews
- **contact_us** - Customer inquiries
- **admin** - Administrator accounts
- **subscribers** - Newsletter subscribers

---

## 🚀 Quick Start

### For Users:
1. Visit `http://localhost/carrental/`
2. Click on "Car Listing" to browse available vehicles
3. Click on a car to view details
4. Click "Book Now" to make a reservation
5. Fill in the booking form and submit
6. Go to "My Bookings" to track your reservations

### For Administrators:
1. Navigate to `http://localhost/carrental/admin/`
2. Log in with admin credentials
3. Use the sidebar menu to manage:
   - Vehicles
   - Bookings
   - Users
   - Brands
   - And more...

---

## ⚙️ Configuration Tips

### Modify Contact Information:
1. Open `admin/includes/config.php`
2. Update company details
3. Save the file

### Change Admin Credentials:
1. Log in to Admin Panel
2. Go to "Change Password"
3. Enter old and new password
4. Click Update

### Add New Car Brands:
1. Go to Admin > Manage Brands
2. Click "Add New Brand"
3. Enter brand name and details
4. Click Submit

### Add New Vehicles:
1. Go to Admin > Manage Vehicles
2. Click "Add New Vehicle"
3. Fill in all details (name, brand, price, etc.)
4. Upload vehicle images
5. Click Submit

---

## 🔒 Security Features

- User authentication and session management
- Admin-only pages with login protection
- Password hashing for security
- Input validation and sanitization
- CSRF protection measures

---

## 🐛 Troubleshooting

### Issue: "Database connection failed"
- **Solution**: Check your database credentials in `config.php`
- Ensure MySQL service is running
- Verify database name is `carrental`

### Issue: "Page not found"
- **Solution**: Check your URL path
- Ensure files are in the correct directory
- Verify Apache/PHP is running

### Issue: "Can't login"
- **Solution**: Check username and password
- Clear browser cache and cookies
- Verify user exists in database

### Issue: "Images not displaying"
- **Solution**: Check `admin/img/vehicleimages/` folder exists
- Verify file permissions (755 or 777)
- Ensure images are uploaded correctly

---

## 📱 Browser Compatibility

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+
- Mobile browsers (responsive design)

---

## 📝 File Upload Limits

- **Vehicle Images**: Max 5 images per vehicle
- **Max File Size**: 2MB per image (configurable)
- **Supported Formats**: JPG, PNG, GIF

---

## 🔄 Regular Maintenance

### Weekly Tasks:
- Check new booking requests
- Review customer inquiries
- Monitor system performance

### Monthly Tasks:
- Review and update vehicle availability
- Check database backups
- Remove old testimonials if needed

### Quarterly Tasks:
- Security updates
- Database optimization
- Feature updates

---

## 📞 Support & Contact

For issues, questions, or suggestions:
- **Email**: support@carrental.com
- **Website**: www.carrental.com
- **Phone**: +1-XXX-XXX-XXXX

---

## 📄 License

This project is provided as-is. Please modify and use as per your requirements.

---

## 🙏 Acknowledgments

- Built with PHP and MySQL
- Uses Bootstrap for responsive design
- Font Awesome for icons
- jQuery for interactivity

---

## 📊 Version History

### Version 3.0 (Current)
- Complete car rental management system
- Admin panel with full functionality
- Customer booking system
- Testimonial system
- Contact management

---

## 🎯 Future Enhancements

- Payment gateway integration
- Email notifications
- SMS alerts
- Mobile app
- Advanced analytics
- API for third-party integrations

---

## ⭐ Tips for Best Experience

1. **Keep Software Updated** - Regularly update PHP, MySQL, and browser
2. **Regular Backups** - Back up your database regularly
3. **Monitor Bookings** - Check and confirm bookings regularly
4. **Update Inventory** - Keep vehicle information current
5. **Respond to Inquiries** - Reply to customer contact queries promptly

---

**Last Updated**: June 2026  
**Created by**: Development Team  
**Status**: Active & Maintained

---

*Thank you for using the Car Rental Portal! We hope this application helps you manage your car rental business efficiently.*

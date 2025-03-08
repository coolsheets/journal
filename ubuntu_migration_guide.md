# 🚀 Ubuntu System Migration: Settings & Installed Applications Catalog

## 📌 Overview
This document catalogs **all installed applications** and **system settings** from your current Ubuntu installation. It also includes a **script** to automatically reinstall applications and restore key settings after migrating to a new SSD.

---

## 📌 Step 1: Backup System Information

### 🔹 List Installed Applications
Run the following command to **export a list of installed applications**:
```bash
dpkg --get-selections > installed_packages.txt
```

To restore applications later:
```bash
sudo dpkg --set-selections < installed_packages.txt
sudo apt-get dselect-upgrade -y
```

### 🔹 Capture System Settings
To backup **GNOME settings**:
```bash
dconf dump / > dconf-settings-backup.ini
```

To restore settings later:
```bash
dconf load / < dconf-settings-backup.ini
```

To list **current GNOME settings** for reference:
```bash
gsettings list-recursively > gnome-settings.txt
```

---

## 📌 Step 2: Generate a Reinstall Script

The following script will **restore applications and settings** on a new installation.

### 🔧 **Reinstall Script (`restore_setup.sh`)**
```bash
#!/bin/bash

echo "🔄 Updating system..."
sudo apt update && sudo apt upgrade -y

echo "🔄 Installing essential applications..."
sudo apt install -y $(awk '{print $1}' installed_packages.txt)

echo "🔄 Restoring GNOME settings..."
if [ -f "dconf-settings-backup.ini" ]; then
    dconf load / < dconf-settings-backup.ini
else
    echo "⚠️ dconf backup not found. Skipping GNOME settings restore."
fi

echo "✅ System setup completed! Please reboot."
```

### 🛠️ **Run the Reinstall Script**
Once the new Ubuntu install is ready, **copy the backup files** to it and run:
```bash
chmod +x restore_setup.sh
./restore_setup.sh
```

---

## 📌 Step 3: Manual Configuration Checklist

**✅ Confirm the following settings are restored correctly:**  
- 🔹 GNOME Theme & Extensions  
- 🔹 Installed Applications  
- 🔹 Terminal & Shell Preferences  
- 🔹 Custom Keyboard Shortcuts  
- 🔹 Any additional system tweaks  

If something is missing, check **`gnome-settings.txt`** for reference.

---

## 📌 Step 4: Optional - Backup Home Directory

To backup your entire **home directory** (excluding unnecessary files):
```bash
rsync -aAXv --exclude={"Downloads","*.log","Trash"} ~ /backup_location/
```

To restore:
```bash
rsync -aAXv /backup_location/ ~
```

---

## 🎯 **Final Steps**
1. **Run the restore script (`restore_setup.sh`)** on your new system.  
2. **Verify applications & settings.**  
3. **Enjoy your freshly migrated Ubuntu setup!** 🎉


[app]

# ชื่อแอปพลิเคชันของคุณ
title = ThaiLang Compiler

# ชื่อแพ็กเกจ (Package name)
package.name = thailangcompiler
package.domain = org.thailang

# ไฟล์หลักของโปรเจกต์
source.include_exts = py,png,jpg,kv,atlas
source.dir = .

# ไลบรารีที่แอปต้องใช้งานบนมือถือ (ต้องมีครบเพื่อให้ระบบเข้ารหัสและดึงเว็บทำงานได้)
requirements = python3,kivy,openssl,urllib3,idna,certifi,charset-normalizer,requests

# เวอร์ชันของแอป
version = 0.1

# รองรับหน้าจอแนวตั้ง
orientation = portrait

# สิทธิ์การใช้งานอินเทอร์เน็ต (จำเป็นสำหรับการใช้คำสั่ง โหลดข้อมูลจากเว็บ)
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1

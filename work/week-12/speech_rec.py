import re, speech_recognition as sr
import csv, datetime

r = sr.Recognizer()

# ฟังก์ชันสำหรับบันทึกลง CSV
def log_command(command, angle):
    with open("commands.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([now, command, angle])
    print(f"บันทึกลง CSV -> {command} | มุม: {angle}")
    show_csv()

# ฟังก์ชันเปิดดูไฟล์ CSV
def show_csv():
    print("\n===== คำสั่งทั้งหมดใน commands.csv =====")
    with open("commands.csv", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            print(" | ".join(row))
    print("======================================\n")

with sr.Microphone() as mic:
    r.adjust_for_ambient_noise(mic, duration=0.6)
    print("พูดคำสั่ง เช่น 'สั่งงาน บันทึก หมุน 45' หรือ 'Log rotate 45'")

    while True:
        try:
            audio = r.listen(mic, timeout=6, phrase_time_limit=10)
            text = r.recognize_google(audio, language="th-TH")  # detect ภาษาไทยก่อน
            print("ได้ยิน :", text)

            # ====== ตรวจสอบภาษาไทย ======
            if text.startswith("สั่งงาน"):
                cmd = text.replace("สั่งงาน", "", 1).strip()
                m = re.search(r"(\d+)", cmd)
                angle = int(m.group(1)) if m else None
                print("TH command :", cmd, "| มุม :", angle)

                if "บันทึก" in cmd:
                    log_command(cmd, angle)

            # ====== ตรวจสอบภาษาอังกฤษ ======
            elif text.lower().startswith("log"):
                cmd = text[3:].strip()
                m = re.search(r"(\d+)", cmd)
                angle = int(m.group(1)) if m else None
                print("EN command :", cmd, "| Angle :", angle)

                log_command(cmd, angle)

        except sr.WaitTimeoutError:
            print("ไม่มีเสียงพูดมาได้เลยครับ")

        except sr.UnknownValueError:
            print("พูดมาได้เลยครับ......")

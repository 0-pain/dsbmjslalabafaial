import telebot
import json
import os
import threading
from datetime import datetime
from telebot import types
from html import escape
from gate import *  # بواباتك الحالية
import time

# ================= CONFIG =================
TOKEN = "8347784927:AAHG0heG5Tck9hpLYAuXC3i4Q94Pjk6eEF8"
CHANNEL_USERNAME = "@tesgvava"

USERS_FILE = "users.json"
LOG_FILE = "logs.txt"
POINTS_PER_CARD = 1
adus="@O21211"
bot = telebot.TeleBot(TOKEN, parse_mode="HTML")
PROXY_FILE='proxies.txt'

stop_flags = {}   # user_id : Event
ADMIN_ID = 8163245201  # أدمن البوت

# ================= USERS =================
def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)

def get_user(uid):
    uid = str(uid)
    users = load_users()
    if uid not in users:
        users[uid] = {"id": int(uid), "points": 0, "used": 0}
        save_users(users)
    return users[uid]

# ================= POINTS =================
def add_points(uid, amount):
    uid = str(uid)
    users = load_users()
    if uid not in users:
        users[uid] = {"id": int(uid), "points": 0, "used": 0}
    users[uid]["points"] += amount
    save_users(users)

def remove_points(uid, amount):
    uid = str(uid)
    users = load_users()
    if uid not in users:
        users[uid] = {"id": int(uid), "points": 0, "used": 0}
    if users[uid]["points"] < amount:
        return False
    users[uid]["points"] -= amount
    users[uid]["used"] += amount
    save_users(users)
    return True

#help cmd
@bot.message_handler(commands=["cmds", "help"])
def show_commands(message):
    text = """
📜 <b>Bot Commands List</b>

👤 <b>Users</b>
/start — بدء البوت  
/id — معلومات حسابك  

💳 <b>Checking</b>
📎 أرسل ملف TXT لبدء الفحص  
▶️ Strip Auth  
▶️ PPC Normal  
▶️ PPC FULL  
⏹ STOP — إيقاف الفحص  

🎯 <b>Points</b>
/add &lt;id&gt; &lt;points&gt; — إضافة نقاط (Admin)
/remove &lt;id&gt; &lt;points&gt; — خصم نقاط (Admin)

🛠 <b>Proxy Management</b>
/add-prox host:port:user:pass — إضافة بروكسي (Admin)
/rmp host:port:user:pass — حذف بروكسي (Admin)

ℹ️ <b>Info</b>
/help — عرض جميع الأوامر  
/cmds — عرض جميع الأوامر  

👨‍💻 <b>Dev</b>
{adus}
"""
    bot.reply_to(message, text)

# ================= SAFE EDIT =================
def safe_edit(chat_id, msg_id, text, kb=None):
    try:
        bot.edit_message_text(text, chat_id, msg_id, reply_markup=kb)
    except:
        pass
@bot.message_handler(commands=['add-prox'])
def add_proxy(message):
    if message.from_user.id != ADMIN_ID:
        return

    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        bot.reply_to(message, "❗ الصيغة:\n/add-prox host:port:user:pass")
        return

    proxy = parts[1].strip()

    with open(PROXY_FILE, "a", encoding="utf-8") as f:
        f.write("\n"+proxy + "\n")

    bot.reply_to(message, "✅ تم إضافة البروكسي بنجاح")
@bot.message_handler(commands=['rmp'])
def remove_proxy(message):
    if message.from_user.id != ADMIN_ID:
        return

    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        bot.reply_to(message, "❗ الصيغة:\n/rmp host:port:user:pass")
        return

    target = parts[1].strip()

    with open(PROXY_FILE, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    if target not in lines:
        bot.reply_to(message, "⚠️ البروكسي غير موجود")
        return

    lines.remove(target)

    with open(PROXY_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + ("\n" if lines else ""))

    bot.reply_to(message, "🗑️ تم حذف البروكسي")

# ================= ADMIN COMMANDS =================
@bot.message_handler(commands=["add"])
def add_points_cmd(msg):
    if msg.from_user.id != ADMIN_ID:
        return bot.reply_to(msg, "❌ ليس لديك صلاحية")
    parts = msg.text.split()
    if len(parts) != 3:
        return bot.reply_to(msg, "❌ الصيغة الصحيحة: /add <id> <points>")
    try:
        uid = int(parts[1])
        amount = int(parts[2])
    except:
        return bot.reply_to(msg, "❌ يجب أن تكون القيم أرقام")
    add_points(uid, amount)
    bot.reply_to(msg, f"✅ تم إضافة {amount} نقطة للمستخدم {uid}")

@bot.message_handler(commands=["remove"])
def remove_points_cmd(msg):
    if msg.from_user.id != ADMIN_ID:
        return bot.reply_to(msg, "❌ ليس لديك صلاحية")
    parts = msg.text.split()
    if len(parts) != 3:
        return bot.reply_to(msg, "❌ الصيغة الصحيحة: /remove <id> <points>")
    try:
        uid = int(parts[1])
        amount = int(parts[2])
    except:
        return bot.reply_to(msg, "❌ يجب أن تكون القيم أرقام")
    if remove_points(uid, amount):
        bot.reply_to(msg, f"✅ تم خصم {amount} نقطة من المستخدم {uid}")
    else:
        bot.reply_to(msg, f"❌ المستخدم {uid} لا يملك نقاط كافية")

@bot.message_handler(commands=["id"])
def user_info_cmd(msg):
    uid = msg.from_user.id
    user = get_user(uid)

    # نحاول الحصول على بيانات المستخدم من Telegram (optional)
    try:
        tg_user = bot.get_chat(uid)
        username = f"@{tg_user.username}" if tg_user.username else "none"
        name = tg_user.first_name or "none"
    except:
        username = "none"
        name = "none"
    
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    text = (
        f"[+] ID: {uid}\n"
        f"[+] Username: {username}\n"
        f"[+] Name: {name}\n"
        f"[+] Points: {user['points']}\n"
        f"[+] Time: {now}"
    )

    bot.reply_to(msg, text)


# ================= START =================
@bot.message_handler(commands=["start"])
def start(msg):
    get_user(msg.from_user.id)
    kb = types.InlineKeyboardMarkup()
    kb.add(
        types.InlineKeyboardButton("👤 Info", callback_data="info"),
        types.InlineKeyboardButton("📢 Channel", url=f"https://t.me/{CHANNEL_USERNAME.replace('@','')}")
    )
    bot.send_message(msg.chat.id, "🚀 Welcome , To check bot  enjoy 👍.", reply_markup=kb)

# ================= HANDLE FILE =================
@bot.message_handler(content_types=["document"])
def handle_file(msg):
    if not msg.document.file_name.endswith(".txt"):
        return bot.reply_to(msg, "TXT فقط")
    uid = msg.from_user.id
    file_info = bot.get_file(msg.document.file_id)
    data = bot.download_file(file_info.file_path)
    combo = f"combo_{uid}.txt"
    with open(combo, "wb") as f:
        f.write(data)
    kb = types.InlineKeyboardMarkup()
    kb.add(
        types.InlineKeyboardButton("▶️ Strip auth", callback_data=f"run|STRIP_AUTH|{combo}"),
        types.InlineKeyboardButton("▶️ PPC norml", callback_data=f"run|ppc2|{combo}"),
        types.InlineKeyboardButton("▶️ PPC FULL", callback_data=f"run|ppc3|{combo}")
    )
    kb.add(types.InlineKeyboardButton("⏹ STOP", callback_data="stop"))
    bot.send_message(uid, "اختر البوابة", reply_markup=kb)

# ================= GATES =================
def gate_strip(call, combo):
    user_id = call.from_user.id
    gate = "Strip_Auth"
    dd = err = auth = d3=0
    if user_id not in stop_flags:
        stop_flags[user_id] = threading.Event()
    stop_flags[user_id].clear()
    safe_edit(call.message.chat.id, call.message.message_id, "⏳ Checking Strip auth...")
    combo_file = f"combo_{user_id}.txt" if combo is None else combo
    try:
        with open(combo_file, "r") as file:
            cards = file.readlines()
            total = len(cards)
            for index, cc in enumerate(cards, start=1):
                if stop_flags[user_id].is_set():
                    safe_edit(call.message.chat.id, call.message.message_id, "⛔ STOPPED")
                    return
                user = get_user(user_id)
                if user["points"] < POINTS_PER_CARD:
                    safe_edit(call.message.chat.id, call.message.message_id, "❌ Points غير كافية")
                    return
                cc = cc.strip()
                start_time = time.time()
                try:
                    last = str(strip_auth(cc))
                except Exception as e:
                    print(e)
                    last = "ERROR in gateway"
                execution_time = time.time() - start_time
                remove_points(user_id, POINTS_PER_CARD)
                user = get_user(user_id)
                mes = types.InlineKeyboardMarkup(row_width=1)
                mes.add(
                    types.InlineKeyboardButton(f"• {escape(cc)} •", callback_data='x'),
                    types.InlineKeyboardButton(f"• STATUS ➜ {escape(last)}", callback_data='x'),
                    types.InlineKeyboardButton(f"• Auth 🎲 : {auth}", callback_data='x'),
                    types.InlineKeyboardButton(f"• Declined ❌ : {dd}", callback_data='x'),
                    types.InlineKeyboardButton(f"• 3ds ❌ : {d3}", callback_data='x'),
                    types.InlineKeyboardButton(f"• Error ⚠ : {err}", callback_data='x'),
                    types.InlineKeyboardButton(f"• TOTAL ➜ {total}", callback_data='x'),
                    types.InlineKeyboardButton(f"• Points ➜ {user['points']}", callback_data='x'),
                    types.InlineKeyboardButton("⏹ STOP", callback_data='stop')
                )
                safe_edit(call.message.chat.id, call.message.message_id, "▶️ PPC NORMAL Donate NEW Running ...", mes)
                # ========== IF-ELSE ORIGINAL ==========
                authed=f"""
[+]  Hi New Approved here 🔥!
[+] CC : {cc}
[+] Gate : #Strip_Auth.
[+] Response: Added ✅
[+] Dev : {adus}
"""
                if "added" in last:
                	auth += 1
                	bot.send_message(user_id, authed)
                elif "Failed_to_add_3DS" in last:
                	d3+=1
                elif 'unknown' in last: dd += 1
                elif 'ERROR in gateway' in last: err += 1
                elif ("Network is unreachable" in last
                or "502 Bad Gateway" in last
                or "ProxyError" in last
                or "Unable to connect to proxy" in last
                or "Max retries exceeded" in last
                or "Tunnel connection failed" in last
                or "ConnectTimeout" in last
                or "ReadTimeout" in last
                or "Caused by ProxyError" in last
                ):
                	bot.send_message(user_id,text=f"Proxy error : card: {cc}")
	

                else: dd += 1
    except Exception as e:
        print(e)
    safe_edit(call.message.chat.id, call.message.message_id, "✅ FINISHED")

def gate_ppc2(call, combo):
    user_id = call.from_user.id
    gate = "PPC_DONATE_Normal "
    dd = err = charge = 0
    if user_id not in stop_flags:
        stop_flags[user_id] = threading.Event()
    stop_flags[user_id].clear()
    safe_edit(call.message.chat.id, call.message.message_id, "⏳ Checking PPC Donate NEW ...")
    combo_file = f"combo_{user_id}.txt" if combo is None else combo
    try:
        with open(combo_file, "r") as file:
            cards = file.readlines()
            total = len(cards)
            for index, cc in enumerate(cards, start=1):
                if stop_flags[user_id].is_set():
                    safe_edit(call.message.chat.id, call.message.message_id, "⛔ STOPPED")
                    return
                user = get_user(user_id)
                if user["points"] < POINTS_PER_CARD:
                    safe_edit(call.message.chat.id, call.message.message_id, "❌ Points غير كافية")
                    return
                cc = cc.strip()
                start_time = time.time()
                try:
                    last = str(ppc001(cc))
                except Exception as e:
                    print(e)
                    last = "ERROR in gateway"
                execution_time = time.time() - start_time
                remove_points(user_id, POINTS_PER_CARD)
                user = get_user(user_id)
                mes = types.InlineKeyboardMarkup(row_width=1)
                mes.add(
                    types.InlineKeyboardButton(f"• {escape(cc)} •", callback_data='x'),
                    types.InlineKeyboardButton(f"• STATUS ➜ {escape(last)}", callback_data='x'),
                    types.InlineKeyboardButton(f"• Charge 🎲 : {charge}", callback_data='x'),
                    types.InlineKeyboardButton(f"• Declined ❌ : {dd}", callback_data='x'),
                    types.InlineKeyboardButton(f"• Error ⚠ : {err}", callback_data='x'),
                    types.InlineKeyboardButton(f"• TOTAL ➜ {total}", callback_data='x'),
                    types.InlineKeyboardButton(f"• Points ➜ {user['points']}", callback_data='x'),
                    types.InlineKeyboardButton("⏹ STOP", callback_data='stop')
                )
                safe_edit(call.message.chat.id, call.message.message_id, "▶️ PPC NORMAL Donate NEW Running ...", mes)
                # ========== IF-ELSE ORIGINAL ==========
                charges=f"""
[+]  Hi New charge here 🔥!
[+] CC : {cc}
[+] Gate : PayPal cvv Normal  1$.
[+] Response: #Charge ! 
[+] Amount: 1$ 
[+] Dev : {adus}
"""
                if "Charge !" in last:
                	charge += 1
                	bot.send_message(user_id, text=charges)
                elif 'unknown' in last:
                	dd += 1
                elif ("Network is unreachable" in last
                or "502 Bad Gateway" in last
                or "ProxyError" in last
                or "Unable to connect to proxy" in last
                or "Max retries exceeded" in last
                or "Tunnel connection failed" in last
                or "ConnectTimeout" in last
                or "ReadTimeout" in last
                or "Caused by ProxyError" in last
                ):
                	bot.send_message(user_id,text=f"Proxy error : card: {cc}")
                elif 'ERROR in gateway' in last: err += 1
                else: dd += 1
    except Exception as e:
        print(e)
    safe_edit(call.message.chat.id, call.message.message_id, "✅ FINISHED")
#end ppc normal

#ppc full start

def gate_ppc3(call, combo=None):  # تعديل لقبول combo
    user_id = call.from_user.id
    gate = "PPC_DONATE_1$"
    dd = err = charge = CVV = funds = 0
    if user_id not in stop_flags:
        stop_flags[user_id] = threading.Event()
    stop_flags[user_id].clear()
    safe_edit(call.message.chat.id, call.message.message_id, "⏳ Checking PPC Donate 1$ FULL ...")
    combo_file = f"combo_{user_id}.txt" if combo is None else combo
    try:
        with open(combo_file, "r") as file:
            cards = file.readlines()
            total = len(cards)
            for index, cc in enumerate(cards, start=1):
                if stop_flags[user_id].is_set():
                    safe_edit(call.message.chat.id, call.message.message_id, "⛔ STOPPED")
                    return
                user = get_user(user_id)
                if user["points"] < POINTS_PER_CARD:
                    safe_edit(call.message.chat.id, call.message.message_id, "❌ Points غير كافية")
                    return
                cc = cc.strip()
                start_time = time.time()
                try:
                    last = str(ppc(cc))
                except Exception as e:
                    print(e)
                    last = "ERROR in gateway"
                execution_time = time.time() - start_time
                remove_points(user_id, POINTS_PER_CARD)
                user = get_user(user_id)
                mes = types.InlineKeyboardMarkup(row_width=1)
                mes.add(
                    types.InlineKeyboardButton(f"• {escape(cc)} •", callback_data='x'),
                    types.InlineKeyboardButton(f"• STATUS ➜ {escape(last)}", callback_data='x'),
                    types.InlineKeyboardButton(f"• Charge 🎲 : {charge}", callback_data='x'),
                    types.InlineKeyboardButton(f"• Funds 🎲 : {funds}", callback_data='x'),
                    types.InlineKeyboardButton(f"• CVV 🎲 : {CVV}", callback_data='x'),
                    types.InlineKeyboardButton(f"• Declined ❌ : {dd}", callback_data='x'),
                    types.InlineKeyboardButton(f"• Error ⚠ : {err}", callback_data='x'),
                    types.InlineKeyboardButton(f"• TOTAL ➜ {total}", callback_data='x'),
                    types.InlineKeyboardButton(f"• Points ➜ {user['points']}", callback_data='x'),
                    types.InlineKeyboardButton("⏹ STOP", callback_data='stop')
                )
                safe_edit(call.message.chat.id, call.message.message_id, "▶️ PPC Donate NEW Running ...", mes)
                # ========== IF-ELSE ORIGINAL ==========
                charges=f"""
[+]  Hi New charge here 🔥!
[+] CC : {cc}
[+] Gate : PayPal cvv 1$.
[+] Response: #{last} 
[+] Amount: 1$ 
[+] Dev : {adus}
"""
                if 'PAYER_CANNOT_PAY' in last: dd += 1
                elif 'DECLINED' in last: dd += 1
                elif 'ACCESS_DENIED' in last: dd += 1
                elif 'DECLINED_DUE_TO_UPDATED_ACCOUNT.' in last: dd += 1
                elif 'AMOUNT_EXCEEDED.' in last: dd += 1
                elif 'TRANSACTION_NOT_PERMITTED.' in last: dd += 1
                elif 'CVV2/CSC does not match.' in last: dd += 1
                elif 'TRANSACTION_CANNOT_BE_COMPLETED.' in last: dd += 1
                elif "Charge !" in last:
                	charge += 1
                	bot.send_message(user_id,text=charges)
                elif 'INSTRUMENT_DECLINED' in last: dd += 1
                elif 'AUTHENTICATION_FAILURE' in last: dd += 1
                elif 'RATE_LIMIT_REACHED' in last: dd += 1
                elif 'RESTRICTED_OR_INACTIVE_ACCOUNT.' in last: dd += 1
                elif 'INVALID_OR_RESTRICTED_CARD' in last: dd += 1
                elif 'DECLINED_PLEASE_RETRY.' in last: dd += 1
                elif 'SUSPECTED_FRAUD.' in last: dd += 1
                elif 'ACCOUNT_BLOCKED_BY_ISSUER.' in last: dd += 1
                elif 'GENERIC_DECLINE.' in last: dd += 1
                elif 'SECURITY_VIOLATION' in last: dd += 1
                elif 'INSUFFICIENT_FUNDS.' in last:
                	funds += 1
                	bot.send_message(user_id,text=charges)
                elif ("Network is unreachable" in last
                or "502 Bad Gateway" in last
                or "ProxyError" in last
                or "Unable to connect to proxy" in last
                or "Max retries exceeded" in last
                or "Tunnel connection failed" in last
                or "ConnectTimeout" in last
                or "ReadTimeout" in last
                or "Caused by ProxyError" in last
                ):
                	bot.send_message(user_id,text=f"Proxy error : card: {cc}")
                
                elif 'REATTEMPT_NOT_PERMITTED.' in last: dd += 1
                elif 'INVALID_ACCOUNT.' in last: dd += 1
                elif 'ACCOUNT_CLOSED.' in last: dd += 1
                elif 'INVALID_TRANSACTION_CARD_ISSUER_ACQUIRER.' in last: dd += 1
                elif 'CVV2_FAILURE.' in last: CVV += 1
                elif 'DO_NOT_HONOR.' in last: dd += 1
                elif 'ACCOUNT_NOT_FOUND.' in last: dd += 1
                elif 'PAYER_ACTION_REQUIRED' in last: dd += 1
                elif 'PICKUP_CARD_SPECIAL_CONDITIONS.' in last: dd += 1
                elif 'LOST_OR_STOLEN.' in last: dd += 1
                elif 'INVALID_MERCHANT.' in last: dd += 1
                elif 'unknown' in last: dd += 1
                elif 'ERROR in gateway' in last: err += 1
                else: dd += 1
    except Exception as e:
        print(e)
    safe_edit(call.message.chat.id, call.message.message_id, "✅ FINISHED")

# ================= CALLBACK =================
@bot.callback_query_handler(func=lambda c: c.data.startswith("run|"))
def run_gate(call):
    try:
        # نفصل كل الأجزاء: run | gate | combo
        parts = call.data.split("|", 2)
        gate = parts[1]  # اسم البوابة
        combo = parts[2] if len(parts) > 2 else None
    except:
        return bot.answer_callback_query(call.id, "❌ خطأ في بيانات الزر")

    gates = {
        "STRIP_AUTH": gate_strip,
        "ppc2": gate_ppc2,
        "ppc3": gate_ppc3
    }

    if gate not in gates:
        return bot.answer_callback_query(call.id, "❌ Gate not found")

    threading.Thread(target=gates[gate], args=(call, combo)).start()
    bot.answer_callback_query(call.id, "🚀 Started")



@bot.callback_query_handler(func=lambda c: c.data == "stop")
def stop_cb(call):
    uid = call.from_user.id
    if uid in stop_flags:
        stop_flags[uid].set()

@bot.callback_query_handler(func=lambda c: c.data in ["info", "points"])
def info_cb(call):
    user = get_user(call.from_user.id)
    safe_edit(call.message.chat.id, call.message.message_id,
              f"ID: {user['id']}\nPoints: {user['points']}\n username: @{call.from_user.username}")

# ================= RUN =================
print("Bot running...")
bot.infinity_polling()

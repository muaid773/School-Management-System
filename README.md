## مشروع: Schoolmuaid (نسخة MVP)

ملف README هذا يصف النسخة الحالية من المشروع — Minimum Viable Product (MVP). المشروع مبني باستخدام Django ويهدف لإدارة بيانات المدرسة (طلاب، مدرسين، لوحة تحكم، إلخ).

### نظرة عامة

- الحالة الحالية: MVP — ميزات أساسية للعمل مع الطلاب، المدرسين، ولوحة تحكم إدارية.
- إطار العمل: Django (تم إنشاء المشروع باستخدام Django 5.2.5).
- قاعدة البيانات الافتراضية: SQLite (`db.sqlite3`).
- هيكل التطبيقات الرئيسية الموجودة:
  - `core` — ملفات منطق عام للمشروع
  - `StudentsApp` — إدارة بيانات الطلاب (قوالب: `students_index.html`, `profile.html`, ...)
  - `teachers` — إدارة المدرسين والمواد
  - `dashboard` — واجهة الإدارة/اللوحة

### متطلبات مبدئية (افتراضات)

- Python 3.8 أو أحدث (يفضّل Python 3.10+).
- Django 5.2.5 (المشروع أنشئ بهذه النسخة).
- نظام التشغيل: تعليمات التشغيل الموجودة هنا مخصصة لـ Windows PowerShell.

> ملاحظة: تم إضافة ملف `requirements.txt` أساسي في جذر المشروع يحوي `Django==5.2.5` و `Pillow`.

### خطوات الإعداد والتشغيل (PowerShell) — بعد التعديلات

التعليمات التالية تفترض أن لديك `requirements.txt` في جذر المشروع (موجود بالفعل). سنغطي إعداد بيئة تطوير آمنة محلياً، وضبط `DJANGO_SECRET_KEY` عبر متغير بيئة أو ملف `.env`، ثم تشغيل التطبيق.

1) افتح PowerShell داخل جذر المشروع (مجلد يحتوي `manage.py`).

2) أنشئ بيئة افتراضية وفعلها:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3) ثبّت الحزم من `requirements.txt`:

```powershell
pip install -r requirements.txt
```

ملاحظة: إذا رغبت باستخدام `python-dotenv` لتحميل ملف `.env` المحلي، قم بإلغاء تعليق السطر في `requirements.txt` أو ثبّته مباشرة:

```powershell
pip install python-dotenv
```

4) ضبط `SECRET_KEY` (خياران — يفضّل الخيار الأول للإنتاج):

- خيار (A) — عبر متغير بيئة (مفضل للخوادم):

  توليد مفتاح جديد:

  ```powershell
  python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
  ```

  وضعه كمتحول دائم للمستخدم (أعد فتح PowerShell بعد الأمر):

  ```powershell
  setx DJANGO_SECRET_KEY "<ضع-المفتاح-هنا>"
  ```

  أو مؤقتًا للجلسة الحالية:

  ```powershell
  $env:DJANGO_SECRET_KEY = "<المفتاح>"
  ```

- خيار (B) — باستخدام ملف `.env` للمطور المحلي (لا تضفه إلى Git):

  أنشئ ملف `.env` في جذر المشروع وأضف:

  ```text
  DJANGO_SECRET_KEY=your-generated-secret
  DEBUG=True
  ```

  وفي بداية `settings.py` (مثال، إن رغبت بتحميل القيم تلقائياً) أضف:

  ```python
  from dotenv import load_dotenv
  from django.core.management.utils import get_random_secret_key
  import os

  load_dotenv()

  SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY") or "dev-" + get_random_secret_key()
  ```

  تأكّد أن تضيف `.env` إلى `.gitignore` ولا ترفعه للمستودع.

5) تنفيذ الترحيلات وإنشاء مستخدم أدمن:

```powershell
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

6) تشغيل الخادم المحلي:

```powershell
python manage.py runserver
```

7) إدارة الملفات الثابتة والوسائط

- المسارات الافتراضية في `settings.py`:
  - `STATIC_ROOT` → مجلد `static` في جذر المشروع
  - `STATICFILES_DIRS` → `/_Schoolmuaid_/static/`
  - `MEDIA_ROOT` → مجلد `media`

- لنسخ ملفات الستاتيك (بيئة اختبارات أو إنتاج بسيط):

```powershell
python manage.py collectstatic --noinput
```

8) إضافة `.gitignore` أساسي (إن لم يكن موجوداً) — تأكد من حجب الأسرار والبيئة الافتراضية:

```
# Secrets
.env

# Virtual env
.venv/

# Python cache
__pycache__/
*.pyc
```

ملاحظات أمان قصيرة:
- لا تضع `SECRET_KEY` في المستودع العام. إن تم تسريبه، دوّر المفتاح فورًا وأنشئ مفتاح جديد في متغيرات البيئة، ثم احرص على مسح الجلسات إن أردت إجبار إعادة تسجيل الدخول.
- استخدم `setx` أو إعدادات CI/CD لتمرير المتغيرات الآمنة إلى بيئة الإنتاج.


### ملفات/مواقع مهمة في المشروع

- `manage.py` — أدوات الإدارة
- `_Schoolmuaid_/settings.py` — إعدادات المشروع (قاعدة بيانات، static/media، INSTALLED_APPS)
- `StudentsApp/` — منطق وقوالب التعامل مع الطلاب
- `teachers/` — منطق التعامل مع المدرسين
- `dashboard/` — قوالب وواجهات لوحة التحكم
- `templates/` — قوالب عامة (بما فيها `base.html`)

### عقدة سريعة للمطور (contract)

- المدخلات: SQLite (`db.sqlite3`) وملفات القوالب والستاتيك في الشجرة الحالية.
- المخرجات المتوقعة: تطبيق Django يعمل محلياً عبر `runserver` وقابل لتسجيل دخول الأدمن.
- حالات الخطأ الشائعة: بيئة افتراضية غير مفعلة، Django غير مثبت، أو تعارض إصدارات بايثون/Django.

### حالات الحافة المحتملة

- قاعدة بيانات فارغة (fresh DB) — تأكد من تشغيل `migrate` و `createsuperuser`.
- ملفات وسائط مفقودة — المجلد `media/students/photos/` موجود لكن قد يكون فارغًا.
- تعدد الإعدادات للبيئات (dev/prod) — حالياً لا يوجد فصل للبيئات في المشروع.

### كيفية المساهمة

1. أنشئ فرع feature/bugfix محلياً.
2. أضف تغييرات مع اختبار محلي وتشغيل الترحيلات عند الحاجة.
3. افتح طلب سحب (pull request) مع وصف واضح، لقطة للشاشة إن وجدت، وقائمة بالخطوات لإعادة إنتاج المشكلة/الميزة.

### خارطة الطريق (اقتراحات لمرحلة ما بعد MVP)

- إضافة ملف `requirements.txt` أو `pyproject.toml` لتثبيت حزم المشروع بدقة.
- فصل إعدادات التطوير والإنتاج (مثلاً `settings_dev.py`, `settings_prod.py`) مع إدارة أسرار عبر متغيرات بيئة.
- إضافة اختبارات وحدة/تكامل أساسية وتشغيل CI (GitHub Actions).
- تحسين صلاحيات المستخدمين، صفحات تقارير، وإمكانية استيراد/تصدير بيانات الطلاب.

### الترخيص والاتصال

أضف هنا نوع الترخيص (مثلاً MIT) ومعلومات التواصل إذا رغبت (البريد الإلكتروني أو issues على المستودع).

---

إذا رغبت، أستطيع: إنشاء `requirements.txt` تلقائياً بعد تجميع الحزم المستخدمة، فصل إعدادات البيئات، أو كتابة ملف `CONTRIBUTING.md` صغير يشرح قواعد الاستفادة من المشروع. أي جزء تريده أنفذه الآن؟
